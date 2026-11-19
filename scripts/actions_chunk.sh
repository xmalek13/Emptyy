#!/bin/bash
# One GitHub Actions chunk of the MemeDesk paper-trading simulator.
# Restores state.json + logs from the `data` branch, runs until the chunk deadline
# or the strategy end, pushes snapshots back to `data`, then dispatches the next
# chunk. Paper trading only: no wallets, keys, signing, or orders.
set -u
set -o pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
mkdir -p logs

END_AT="${END_AT:-2026-11-20T14:00:00Z}"
CHUNK_MINUTES="${CHUNK_MINUTES:-340}"
DATA_DIR="${MEMEDESK_DATA_DIR:-/tmp/memedesk-data}"
PERSIST_EVERY="${MEMEDESK_PERSIST_EVERY:-600}"
EARLY_PERSIST="${MEMEDESK_EARLY_PERSIST:-90}"
RUN_URL="${GITHUB_SERVER_URL:-https://github.com}/${GITHUB_REPOSITORY:-local}/actions/runs/${GITHUB_RUN_ID:-0}"
PERSIST_OK=0

log() { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $*"; }

if [ -n "${GITHUB_TOKEN:-}" ]; then
  echo "::add-mask::$GITHUB_TOKEN"
fi

# Cap the chunk so this job can still commit and dispatch before the 6h kill.
if ! [[ "$CHUNK_MINUTES" =~ ^[0-9]+$ ]]; then
  log "chunk_minutes '$CHUNK_MINUTES' is not an integer; using 340"
  CHUNK_MINUTES=340
fi
if [ "$CHUNK_MINUTES" -gt 340 ]; then CHUNK_MINUTES=340; fi
if [ "$CHUNK_MINUTES" -lt 1 ]; then CHUNK_MINUTES=1; fi
if [ -z "$END_AT" ]; then END_AT="2026-11-20T14:00:00Z"; fi

configure_auth() {
  if [ -z "${GITHUB_TOKEN:-}" ] || [ -z "${GITHUB_REPOSITORY:-}" ]; then
    return 0
  fi
  local basic
  basic="$(printf 'x-access-token:%s' "$GITHUB_TOKEN" | base64 -w0)"
  git -C "$DATA_DIR" config http.https://github.com/.extraheader "AUTHORIZATION: basic ${basic}"
}

prepare_data_repo() {
  rm -rf "$DATA_DIR"
  if [ -n "${GITHUB_REPOSITORY:-}" ]; then
    git clone --quiet --no-tags "https://github.com/${GITHUB_REPOSITORY}.git" "$DATA_DIR" || return 1
  else
    local remote
    remote="$(git remote get-url origin)"
    git clone --quiet --no-tags "$remote" "$DATA_DIR" || return 1
  fi
  git -C "$DATA_DIR" config user.email "41898282+github-actions[bot]@users.noreply.github.com"
  git -C "$DATA_DIR" config user.name "github-actions[bot]"
  git -C "$DATA_DIR" config commit.gpgsign false
  configure_auth
  if git -C "$DATA_DIR" ls-remote --exit-code --heads origin data >/dev/null 2>&1; then
    git -C "$DATA_DIR" fetch --quiet origin data || return 1
    git -C "$DATA_DIR" checkout --quiet -B data origin/data || return 1
    log "restored data branch at $(git -C "$DATA_DIR" rev-parse --short HEAD)"
  else
    git -C "$DATA_DIR" checkout --quiet --orphan data || return 1
    git -C "$DATA_DIR" rm -rf . >/dev/null 2>&1 || true
    log "data branch does not exist yet; it will be created on the first snapshot"
  fi
}

restore_state() {
  if [ -f "$DATA_DIR/state.json" ]; then
    cp -a "$DATA_DIR/state.json" "$ROOT/state.json"
    log "resumed state.json"
  fi
  if [ -d "$DATA_DIR/logs" ]; then
    mkdir -p "$ROOT/logs"
    if command -v rsync >/dev/null 2>&1; then
      rsync -a "$DATA_DIR/logs/" "$ROOT/logs/"
    else
      cp -a "$DATA_DIR/logs/." "$ROOT/logs/"
    fi
    log "resumed logs"
  fi
  if [ "${GITHUB_EVENT_NAME:-}" != "workflow_dispatch" ] && [ -f "$DATA_DIR/chunk.json" ]; then
    local saved
    saved="$(python3 - "$DATA_DIR/chunk.json" << 'PY'
import json, sys
try:
    print(json.load(open(sys.argv[1])).get("end_at") or "")
except Exception:
    print("")
PY
)"
    if [ -n "$saved" ]; then
      log "keeping saved end_at $saved (this run is ${GITHUB_EVENT_NAME:-local}, not a manual dispatch)"
      END_AT="$saved"
    fi
  fi
}

open_positions() {
  python3 - "$1" << 'PY'
import json, sys
path = sys.argv[1]
try:
    state = json.load(open(path))
except Exception:
    print(0)
    raise SystemExit
n = 0
for book in (state.get("books") or {}).values():
    n += len(book.get("open") or {})
print(n)
PY
}

scan_loops() {
  python3 - "$ROOT/state.json" << 'PY'
import json, sys
try:
    print(json.load(open(sys.argv[1])).get("scan_loops") or 0)
except Exception:
    print(0)
PY
}

write_report() {
  local body="$ROOT/report.txt"
  if [ -f "$ROOT/state.json" ] && python3 "$ROOT/report.py" > "$body" 2>"$ROOT/logs/report.err"; then
    :
  else
    {
      echo "report.py could not render a full report yet."
      [ -f "$ROOT/logs/report.err" ] && tail -n 20 "$ROOT/logs/report.err"
    } > "$body"
  fi
  {
    echo "# MemeDesk paper-trading report"
    echo
    echo "Simulation only. No wallets, private keys, signing, or real orders."
    echo
    echo '```'
    cat "$body"
    echo '```'
  } > "$ROOT/REPORT.md"
}

write_chunk_json() {
  python3 - "$ROOT/state.json" "$ROOT/chunk.json" << PY
import json, os, sys
state_path, out_path = sys.argv[1], sys.argv[2]
state = {}
try:
    state = json.load(open(state_path))
except Exception:
    state = {}
books = state.get("books") or {}
def book(name):
    b = books.get(name) or {}
    return {
        "equity": b.get("equity"),
        "cash": b.get("cash"),
        "open": len(b.get("open") or {}),
    }
doc = {
    "end_at": os.environ.get("END_AT"),
    "chunk_until": os.environ.get("MEMEDESK_CHUNK_UNTIL") or None,
    "chunk_minutes": os.environ.get("CHUNK_MINUTES"),
    "run_id": os.environ.get("GITHUB_RUN_ID"),
    "run_url": os.environ.get("RUN_URL"),
    "event": os.environ.get("GITHUB_EVENT_NAME"),
    "persisted_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    "reason": os.environ.get("PERSIST_REASON"),
    "scan_loops": state.get("scan_loops"),
    "evaluations": state.get("evaluations"),
    "risk_ticks": state.get("risk_ticks"),
    "api_errors": state.get("api_errors"),
    "last_loop": state.get("last_loop"),
    "last_scan_secs": state.get("last_scan_secs"),
    "last_risk_tick": state.get("last_risk_tick"),
    "unique_tokens": state.get("unique_tokens"),
    "books": {"original": book("original"), "adjusted": book("adjusted")},
}
json.dump(doc, open(out_path, "w"), indent=2)
print("scans=%s evals=%s ticks=%s api_errors=%s orig_open=%s adj_open=%s" % (
    doc["scan_loops"], doc["evaluations"], doc["risk_ticks"], doc["api_errors"],
    doc["books"]["original"]["open"], doc["books"]["adjusted"]["open"]))
PY
}

persist() {
  local reason="$1"
  if [ ! -f "$ROOT/state.json" ]; then
    log "persist($reason): no state.json yet"
    return 1
  fi
  export PERSIST_REASON="$reason" RUN_URL CHUNK_MINUTES END_AT
  local summary
  if ! summary="$(write_chunk_json)"; then
    log "persist($reason): chunk.json failed"
    return 1
  fi
  write_report || true
  mkdir -p "$DATA_DIR/logs" || return 1
  cp -a "$ROOT/state.json" "$DATA_DIR/state.json" || return 1
  cp -a "$ROOT/REPORT.md" "$DATA_DIR/REPORT.md" || return 1
  cp -a "$ROOT/chunk.json" "$DATA_DIR/chunk.json" || return 1
  if command -v rsync >/dev/null 2>&1; then
    rsync -a "$ROOT/logs/" "$DATA_DIR/logs/" || return 1
  else
    cp -a "$ROOT/logs/." "$DATA_DIR/logs/" || return 1
  fi
  cat > "$DATA_DIR/README.md" << 'EOF'
# MemeDesk paper-trading data

This branch is written by the `memedesk` GitHub Actions workflow. It is the live state of a **simulation**. There are no wallets, keys, or orders here.

- [`REPORT.md`](REPORT.md) — both variants side by side
- `state.json` — equity, open positions, and scan counters (the resume file)
- `logs/` — trades, skips, latency, supervisor
- `chunk.json` — which Actions run last wrote this commit

Do not edit this branch by hand. The next snapshot overwrites these files from the runner.
EOF
  git -C "$DATA_DIR" add -f state.json REPORT.md chunk.json README.md logs || return 1
  if git -C "$DATA_DIR" diff --cached --quiet; then
    log "persist($reason): no file changes ($summary)"
    PERSIST_OK=$((PERSIST_OK + 1))
    return 0
  fi
  local msg
  msg="paper: $summary ($reason run ${GITHUB_RUN_ID:-local})"
  if ! git -C "$DATA_DIR" -c commit.gpgsign=false commit -q -m "$msg" -m "Run: $RUN_URL"; then
    log "persist($reason): commit failed"
    return 1
  fi
  local i
  for i in 1 2 3 4 5; do
    if git -C "$DATA_DIR" push origin HEAD:data; then
      log "persist($reason): pushed $(git -C "$DATA_DIR" rev-parse --short HEAD) $summary"
      if [ -n "${GITHUB_STEP_SUMMARY:-}" ]; then
        echo "- $(date -u +%H:%M:%S) $reason $summary" >> "$GITHUB_STEP_SUMMARY"
      fi
      PERSIST_OK=$((PERSIST_OK + 1))
      return 0
    fi
    log "persist($reason): push failed (try $i); fetching and rebasing"
    git -C "$DATA_DIR" fetch origin data || true
    git -C "$DATA_DIR" rebase origin/data || git -C "$DATA_DIR" rebase --abort || true
    sleep $((i * 3))
  done
  log "persist($reason): push failed after retries"
  return 1
}

dispatch_next() {
  if [ -z "${GITHUB_TOKEN:-}" ] || [ -z "${GITHUB_REPOSITORY:-}" ]; then
    log "not on Actions; skipping workflow_dispatch handoff"
    return 0
  fi
  local api="${GITHUB_API_URL:-https://api.github.com}"
  local code body i
  for i in 1 2 3 4 5; do
    body="$(mktemp)"
    code="$(curl -sS -o "$body" -w "%{http_code}" -X POST \
      -H "Authorization: Bearer ${GITHUB_TOKEN}" \
      -H "Accept: application/vnd.github+json" \
      "$api/repos/${GITHUB_REPOSITORY}/actions/workflows/memedesk.yml/dispatches" \
      -d "{\"ref\":\"main\",\"inputs\":{\"end_at\":\"${END_AT}\",\"chunk_minutes\":\"${CHUNK_MINUTES}\"}}")" || code="000"
    if [ "$code" = "204" ]; then
      log "dispatched next chunk (end_at=$END_AT chunk_minutes=$CHUNK_MINUTES)"
      rm -f "$body"
      return 0
    fi
    log "dispatch failed HTTP $code (try $i): $(head -c 300 "$body")"
    rm -f "$body"
    sleep $((i * 3))
  done
  return 1
}

log "MemeDesk chunk starting"
log "run=$RUN_URL event=${GITHUB_EVENT_NAME:-local} requested_end=$END_AT chunk_minutes=$CHUNK_MINUTES"

prepare_data_repo || { log "could not prepare the data branch checkout"; exit 1; }
restore_state
export END_AT CHUNK_MINUTES

PLAN="$(python3 - "$END_AT" "$CHUNK_MINUTES" "$ROOT/state.json" << 'PY'
import datetime as dt, json, os, sys
end_raw, minutes, state_path = sys.argv[1], int(sys.argv[2]), sys.argv[3]
def parse(raw):
    s = raw.strip()
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    d = dt.datetime.fromisoformat(s)
    if d.tzinfo is None:
        d = d.replace(tzinfo=dt.timezone.utc)
    return d.astimezone(dt.timezone.utc)
end = parse(end_raw)
now = dt.datetime.now(dt.timezone.utc)
opens = 0
if os.path.exists(state_path):
    try:
        state = json.load(open(state_path))
        for book in (state.get("books") or {}).values():
            opens += len(book.get("open") or {})
    except Exception:
        opens = 0
remain = (end - now).total_seconds()
if remain <= 0:
    mode = "mark" if opens else "stop"
    chunk_until = ""
    trade_limit = 900
else:
    mode = "trade"
    chunk_secs = minutes * 60
    if remain <= chunk_secs:
        # Final partial chunk: desk.py runs through END_AT and marks to market.
        chunk_until = ""
        trade_limit = int(remain) + 600
    else:
        until = now + dt.timedelta(seconds=chunk_secs)
        chunk_until = until.strftime("%Y-%m-%dT%H:%M:%SZ")
        trade_limit = chunk_secs + 600
print("\n".join([
    f"MODE={mode}",
    f"CHUNK_UNTIL={chunk_until}",
    f"TRADE_LIMIT={max(120, trade_limit)}",
    f"OPENS={opens}",
    f"REMAIN={int(remain)}",
]))
PY
)"
# shellcheck disable=SC1090
eval "$PLAN"
log "plan mode=$MODE opens=$OPENS remain_s=$REMAIN chunk_until=${CHUNK_UNTIL:-<end>} trade_limit_s=$TRADE_LIMIT end_at=$END_AT"

if [ "${DRY_RUN:-}" = "1" ]; then
  log "DRY_RUN set; not trading"
  exit 0
fi

if [ "$MODE" = "stop" ]; then
  log "Past $END_AT and no open positions. Not starting a chunk."
  exit 0
fi

export MEMEDESK_END_AT="$END_AT"
if [ -n "${CHUNK_UNTIL:-}" ]; then
  export MEMEDESK_CHUNK_UNTIL="$CHUNK_UNTIL"
else
  unset MEMEDESK_CHUNK_UNTIL || true
fi

if [ "$MODE" = "mark" ]; then
  log "Past $END_AT with $OPENS open position(s). Marking to market."
  set +e
  timeout --signal=TERM --kill-after=20s "$TRADE_LIMIT" python3 -u "$ROOT/desk.py" >> "$ROOT/logs/stdout.log" 2>&1
  set -e
  persist final || log "final persist after mark failed"
  exit 0
fi

# Trade mode. timeout(1) is the backstop; desk.py exits earlier on CHUNK_UNTIL / END_AT.
set +e
timeout --signal=TERM --kill-after=25s "$TRADE_LIMIT" bash "$ROOT/run.sh" &
RUN_PID=$!
set -e
log "desk supervisor pid $RUN_PID (limit ${TRADE_LIMIT}s)"

SEEN_SCANS=0
NEXT_PERSIST="$EARLY_PERSIST"
SCAN_NOT_BEFORE=0
while kill -0 "$RUN_PID" 2>/dev/null; do
  sleep 20
  if ! kill -0 "$RUN_PID" 2>/dev/null; then
    break
  fi
  SCANS=0
  if [ -f "$ROOT/state.json" ]; then
    SCANS="$(scan_loops)"
  fi
  REASON=""
  if [ "$SCANS" -ge 1 ] && [ "$SEEN_SCANS" -eq 0 ] && [ "$SECONDS" -ge "$SCAN_NOT_BEFORE" ]; then
    REASON="first-scans"
  elif [ "$SECONDS" -ge "$NEXT_PERSIST" ]; then
    REASON="interval"
  fi
  if [ -n "$REASON" ]; then
    if persist "$REASON"; then
      SEEN_SCANS="$SCANS"
      NEXT_PERSIST=$((SECONDS + PERSIST_EVERY))
      SCAN_NOT_BEFORE=$((SECONDS + 30))
    else
      log "persist($REASON) failed; retrying in 2 minutes"
      NEXT_PERSIST=$((SECONDS + 120))
      SCAN_NOT_BEFORE="$NEXT_PERSIST"
    fi
  fi
done
set +e
wait "$RUN_PID"
RC=$?
set -e
log "supervisor finished status $RC after ${SECONDS}s (persists=$PERSIST_OK)"
persist final || log "final persist failed"

END_EPOCH="$(python3 - "$END_AT" << 'PY'
import datetime as dt, sys
s = sys.argv[1].strip()
if s.endswith("Z"):
    s = s[:-1] + "+00:00"
d = dt.datetime.fromisoformat(s)
if d.tzinfo is None:
    d = d.replace(tzinfo=dt.timezone.utc)
print(int(d.timestamp()))
PY
)"
NOW_EPOCH="$(date +%s)"
if [ "$NOW_EPOCH" -ge "$END_EPOCH" ]; then
  log "at or past $END_AT; not starting another chunk"
  exit 0
fi
if [ "$PERSIST_OK" -lt 1 ]; then
  log "state never reached the data branch; not dispatching. The backup cron will retry."
  exit 1
fi
if [ "$RC" -ne 0 ] && [ "$RC" -ne 124 ]; then
  log "supervisor exit $RC; state is on the data branch. Leaving the restart to the backup cron."
  exit 1
fi
if [ "$SECONDS" -lt 90 ]; then
  log "chunk ended too quickly (${SECONDS}s); not dispatching. The backup cron will retry."
  exit 1
fi
dispatch_next
log "chunk complete"
