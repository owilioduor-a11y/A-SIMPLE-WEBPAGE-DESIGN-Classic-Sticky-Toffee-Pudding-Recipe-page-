#!/bin/bash
set -u
cd "$(dirname "$0")"
LOG=/tmp/pr_merge.log
: > "$LOG"

gh pr list --state open --json number,headRefName --jq '.[] | "\(.number)|\(.headRefName)"' | sort -n > /tmp/prs.txt

while IFS='|' read -r num ref; do
  echo "===== PR $num ($ref) =====" | tee -a "$LOG"
  git fetch origin main >>"$LOG" 2>&1
  git fetch origin "$ref" >>"$LOG" 2>&1 || { echo "FETCH_FAIL $num" | tee -a "$LOG"; continue; }
  git checkout -B "merge-pr-$num" FETCH_HEAD >>"$LOG" 2>&1 || { echo "CHECKOUT_FAIL $num" | tee -a "$LOG"; continue; }
  if git merge --no-edit origin/main >>"$LOG" 2>&1; then
    echo "clean merge $num" | tee -a "$LOG"
  else
    # resolve all conflicts taking main's version
    git diff --name-only --diff-filter=U | while read -r f; do
      git checkout --theirs -- "$f" 2>/dev/null && git add -- "$f"
    done
    git commit --no-edit >>"$LOG" 2>&1 && echo "resolved+committed $num" | tee -a "$LOG" || { echo "COMMIT_FAIL $num" | tee -a "$LOG"; git merge --abort; }
  fi
  if git push origin "HEAD:$ref" >>"$LOG" 2>&1; then
    echo "pushed $num" | tee -a "$LOG"
  else
    echo "PUSH_FAIL $num" | tee -a "$LOG"; git checkout main >>"$LOG" 2>&1; continue
  fi
  # wait for GitHub to recompute mergeability, then merge
  for i in 1 2 3 4 5 6; do
    sleep 10
    state=$(gh pr view "$num" --json mergeable --jq '.mergeable' 2>/dev/null)
    [ "$state" = "MERGEABLE" ] && break
  done
  if gh pr merge "$num" --merge >>"$LOG" 2>&1; then
    echo "MERGED $num" | tee -a "$LOG"
  else
    echo "MERGE_FAIL $num (state=$state)" | tee -a "$LOG"
  fi
  git checkout main >>"$LOG" 2>&1
done < /tmp/prs.txt
echo "DONE" | tee -a "$LOG"
