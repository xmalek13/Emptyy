#!/bin/bash
# Run desk.py until MEMEDESK_CHUNK_UNTIL (a chunk handoff) or MEMEDESK_END_AT (mark to market).
# If the process exits early or state.json goes stale, restart it so one hung loop does not
# sit until the chunk deadline. Paper trading only: no wallets, keys, signing, or orders.
# The script directory is the working directory (state.json and logs/ live beside desk.py).
set -u
cd "$(dirname "$0")"
mkdir -p logs

logical_epoch() {
  python3 - << 'PY'
import os, datetime as dt
def parse(raw):
    if not raw:
        return None
    s = raw.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    d = dt.datetime.fromisoformat(s)
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d
end = parse(os.environ.get("MEMEDESK_END_AT", "2026-11-20T14:00:00Z"))
chunk = parse(os.environ.get("MEMEDESK_CHUNK_UNTIL", ""))
stop = end if chunk is None or chunk >= end else chunk
print(int(stop.timestamp()))
PY
}

last_event() {
  python3 - << 'PY'
import json
path = "logs/events.jsonl"
last = ""
try:
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                last = json.loads(line).get("event") or ""
            except Exception:
                pass
except Exception:
    last = ""
print(last)
PY
}

LOGICAL="$(logical_epoch)"
GRACE_UNTIL=$((LOGICAL + 480))
PID=""
FAST=0

on_stop() {
  echo "$(date -Is) run.sh received stop signal" >> logs/supervisor.log
  if [ -n "${PID:-}" ] && kill -0 "$PID" 2>/dev/null; then
    kill -TERM "$PID" 2>/dev/null || true
    sleep 2
    kill -KILL "$PID" 2>/dev/null || true
    wait "$PID" 2>/dev/null || true
  fi
  exit 0
}
trap on_stop TERM INT

while :; do
  python3 -u desk.py >> logs/stdout.log 2>&1 &
  PID=$!
  STARTED="$(date +%s)"
  echo "$(date -Is) started desk.py pid $PID" >> logs/supervisor.log
  LAST="$(date +%s)"
  while kill -0 "$PID" 2>/dev/null; do
    NOW="$(date +%s)"
    if [ $((NOW - LAST)) -gt 30 ]; then
      echo "$(date -Is) watchdog clock jump $((NOW - LAST))s; grace 30s" >> logs/supervisor.log
      sleep 30
      LAST="$(date +%s)"
      continue
    fi
    # Past the grace window, kill a process that did not exit on its own.
    # A deadline that is already past still gets a few seconds to record chunk_end / end.
    if [ "$NOW" -ge "$GRACE_UNTIL" ] && [ "$NOW" -ge $((STARTED + 20)) ]; then
      echo "$(date -Is) past grace; killing desk.py pid $PID" >> logs/supervisor.log
      kill -TERM "$PID" 2>/dev/null || true
      sleep 2
      kill -KILL "$PID" 2>/dev/null || true
      break
    fi
    if [ "$NOW" -ge $((STARTED + 45)) ]; then
      if [ -f state.json ]; then
        AGE=$((NOW - $(stat -c %Y state.json)))
      else
        AGE=$((NOW - STARTED))
      fi
      if [ "$AGE" -gt 90 ]; then
        echo "$(date -Is) state.json stale ${AGE}s; dumping stacks and restarting $PID" >> logs/supervisor.log
        kill -USR1 "$PID" 2>/dev/null || true
        sleep 2
        kill -KILL "$PID" 2>/dev/null || true
        break
      fi
    fi
    LAST="$NOW"
    sleep 10
  done
  wait "$PID" 2>/dev/null || true
  echo "$(date -Is) desk.py pid $PID exited" >> logs/supervisor.log
  PID=""
  EV="$(last_event)"
  if [ "$EV" = "chunk_end" ] || [ "$EV" = "end" ]; then
    echo "$(date -Is) clean stop ($EV)" >> logs/supervisor.log
    exit 0
  fi
  NOW="$(date +%s)"
  if [ "$NOW" -ge "$LOGICAL" ]; then
    echo "$(date -Is) past chunk deadline after exit ($EV); not restarting" >> logs/supervisor.log
    exit 0
  fi
  LIVED=$((NOW - STARTED))
  if [ "$LIVED" -lt 20 ]; then
    FAST=$((FAST + 1))
    echo "$(date -Is) fast exit ${LIVED}s ($FAST/5)" >> logs/supervisor.log
    if [ "$FAST" -ge 5 ]; then
      echo "$(date -Is) desk.py failed five times quickly; giving up this chunk" >> logs/supervisor.log
      exit 1
    fi
  else
    FAST=0
  fi
  sleep 5
done
