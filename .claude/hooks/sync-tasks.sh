#!/usr/bin/env bash
# Hook: sync-tasks (Stop)
# After Claude finishes work, prompt it to update .tasks/ files.
# Uses a marker file to prevent the sync pass from triggering another sync.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
TASKS_DIR="$REPO_ROOT/.tasks"
MARKER="/tmp/.claude-my-app-task-sync"

# Loop prevention: skip if marker was touched in the last 2 minutes
if [ -f "$MARKER" ]; then
  MARKER_MTIME=$(stat -f %m "$MARKER" 2>/dev/null || echo 0)
  NOW=$(date +%s)
  if [ $(( NOW - MARKER_MTIME )) -lt 120 ]; then
    exit 0
  fi
fi

# Skip if no task files exist
if [ ! -d "$TASKS_DIR" ]; then
  exit 0
fi

# Skip if no active tasks
if ! grep -qrl 'Status.*: *\(Not Started\|In Progress\)' "$TASKS_DIR"/*.md 2>/dev/null; then
  exit 0
fi

# Set marker before output to prevent loop on next Stop
touch "$MARKER"

# Read the companion prompt and output as additionalContext
PROMPT="$(cat "$SCRIPT_DIR/sync-tasks.md")"
printf '{"additionalContext": "%s"}\n' "$(echo "$PROMPT" | sed 's/"/\\"/g' | tr '\n' ' ')"
