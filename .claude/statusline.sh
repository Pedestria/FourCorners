#!/usr/bin/env bash
# Claude Code status line: model | context usage | git branch

input=$(cat)

model=$(echo "$input" | jq -r '.model.display_name // "Unknown"')

used_pct=$(echo "$input" | jq -r '.context_window.used_percentage // 0' | cut -d. -f1)
cost=$(echo "$input" | jq -r '.cost.total_cost_usd // 0')
duration_ms=$(echo "$input" | jq -r '.cost.total_duration_ms // 0')

if [ "$used_pct" -ge 90 ] 2>/dev/null; then bar_color="\033[31m"
elif [ "$used_pct" -ge 70 ] 2>/dev/null; then bar_color="\033[33m"
else bar_color="\033[32m"; fi

filled=$((used_pct / 10)); empty=$((10 - filled))
bar=$(printf "%${filled}s" | tr ' ' '█')$(printf "%${empty}s" | tr ' ' '░')

cost_fmt=$(printf '$%.2f' "$cost")
mins=$((duration_ms / 60000)); secs=$(((duration_ms % 60000) / 1000))

work_dir=$(echo "$input" | jq -r '.workspace.current_dir // "."')

git_branch=$(git -C "$work_dir" branch --show-current 2>/dev/null)
if [ -z "$git_branch" ]; then
  git_branch="no-branch"
fi

added=$(git -C "$work_dir" diff --numstat HEAD 2>/dev/null | awk '{ a += $1 } END { print a+0 }')
removed=$(git -C "$work_dir" diff --numstat HEAD 2>/dev/null | awk '{ r += $2 } END { print r+0 }')
changed=$(git -C "$work_dir" diff --name-only HEAD 2>/dev/null | wc -l | tr -d ' ')

green="\033[32m"
red="\033[31m"
yellow="\033[33m"
reset="\033[0m"

printf "%s  |  ${bar_color}%s${reset} %s%%  |  ${yellow}%s${reset}  |  %dm %ds\n" "$model" "$bar" "$used_pct" "$cost_fmt" "$mins" "$secs"
suffix="files"; [ "$changed" -eq 1 ] 2>/dev/null && suffix="file"
printf "Branch: %s  ${green}+%s${reset}  ${red}-%s${reset}  ${yellow}%s %s${reset}" "$git_branch" "$added" "$removed" "$changed" "$suffix"
