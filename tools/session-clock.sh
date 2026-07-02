#!/bin/sh
# session-clock.sh — record a session's start clock time and report total elapsed.
#
# The autonomous run discipline (PROTOCOL.md) has no record of when a session's
# *initial prompt* fired: the journal JST stamp, the commits, and the merge all
# land at the *end* of a session, so "start -> merge" wall-clock could not be
# read back. This helper closes that gap.
#
#   tools/session-clock.sh start            # FIRST action of a session (PROTOCOL §1)
#   tools/session-clock.sh report [N]       # at the website step (PROTOCOL §5b)
#
# `start` writes the start epoch to .session-clock (gitignored, ephemeral — it
# lives only inside the run's container and is never committed). It does NOT
# overwrite an existing clock, so a re-invocation mid-session (e.g. after a
# context summary) keeps the true start; pass --force to reset deliberately.
#
# `report` reads .session-clock, takes "now" as the end, and prints the start
# and end JST clock times, the total elapsed, and a ready-to-paste journal-entry
# stamp. Give the session number as the optional argument N to fill it in.
#
# All clock times are Japan time (JST, UTC+9) to match the website convention.
# Elapsed is computed from epoch seconds, so it is timezone- and DST-safe.

set -eu

# Locate the repo root (the dir containing this tools/ directory), so the clock
# file sits at a stable path regardless of the caller's working directory.
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/.." && pwd)
CLOCK_FILE="$REPO_ROOT/.session-clock"

fmt_jst() {  # epoch -> "Month D, YYYY, HH:MM JST"
    TZ=Asia/Tokyo date -d "@$1" "+%B %-d, %Y, %H:%M JST"
}
fmt_jst_date() { TZ=Asia/Tokyo date -d "@$1" "+%B %-d, %Y"; }
fmt_jst_time() { TZ=Asia/Tokyo date -d "@$1" "+%H:%M"; }

fmt_elapsed() {  # seconds -> "Xh Ym" / "Ym" / "Xs"
    _s=$1
    _h=$(( _s / 3600 ))
    _m=$(( (_s % 3600) / 60 ))
    if [ "$_h" -gt 0 ]; then
        printf '%dh %dm' "$_h" "$_m"
    elif [ "$_m" -gt 0 ]; then
        printf '%dm' "$_m"
    else
        printf '%ds' "$_s"
    fi
}

cmd=${1:-}
case "$cmd" in
    start)
        force=${2:-}
        if [ -f "$CLOCK_FILE" ] && [ "$force" != "--force" ]; then
            start_epoch=$(cat "$CLOCK_FILE")
            echo "Session clock already started at $(fmt_jst "$start_epoch") — kept (use --force to reset)."
            exit 0
        fi
        now=$(date +%s)
        echo "$now" > "$CLOCK_FILE"
        echo "Session clock started: $(fmt_jst "$now")"
        ;;
    report)
        n=${2:-N}
        end_epoch=$(date +%s)
        if [ ! -f "$CLOCK_FILE" ]; then
            # Degrade gracefully: no start was recorded, so total is unknown.
            echo "WARNING: no .session-clock found — session start was not recorded."
            echo "  Run 'tools/session-clock.sh start' as the FIRST action of a session."
            echo "  End (now): $(fmt_jst "$end_epoch")"
            echo "Journal stamp (no total available): $(fmt_jst "$end_epoch") (session $n)"
            exit 0
        fi
        start_epoch=$(cat "$CLOCK_FILE")
        elapsed=$(( end_epoch - start_epoch ))
        [ "$elapsed" -lt 0 ] && elapsed=0
        total=$(fmt_elapsed "$elapsed")

        echo "Session clock"
        echo "  Start: $(fmt_jst "$start_epoch")"
        echo "  End:   $(fmt_jst "$end_epoch")"
        echo "  Total: $total"

        # Ready-to-paste journal-entry stamp. If the session stayed within one
        # JST calendar day, collapse to a single date with a HH:MM–HH:MM range;
        # otherwise spell out both dates.
        if [ "$(fmt_jst_date "$start_epoch")" = "$(fmt_jst_date "$end_epoch")" ]; then
            stamp="$(fmt_jst_date "$start_epoch"), $(fmt_jst_time "$start_epoch")–$(fmt_jst_time "$end_epoch") JST (session $n) · total $total"
        else
            stamp="$(fmt_jst "$start_epoch") – $(fmt_jst "$end_epoch") (session $n) · total $total"
        fi
        echo "Journal stamp: $stamp"
        ;;
    *)
        echo "usage: tools/session-clock.sh start [--force] | report [session-number]" >&2
        exit 2
        ;;
esac
