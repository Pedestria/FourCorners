#!/usr/bin/env bash
# Hook: evaluate-agent-work
# Fires on SubagentStop — reads the prompt from the companion .md file
# and outputs it as a prompt-style JSON response for Claude to evaluate.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROMPT="$(cat "$SCRIPT_DIR/evaluate-agent-work.md")"

# Pass the prompt as additionalContext so Claude sees it after the agent returns
printf '{"additionalContext": "%s"}\n' "$(echo "$PROMPT" | sed 's/"/\\"/g' | tr '\n' ' ')"
