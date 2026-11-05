#!/usr/bin/env bash
set -euo pipefail

cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.."
gh auth status
if [[ $# -gt 0 ]]; then
  target=$1
else
  owner=$(gh api user --jq .login)
  target="$owner/finance-tracker"
fi
repo=$(gh repo view "$target" --json nameWithOwner,isPrivate \
  --jq 'if .isPrivate then error("Repo public olmalı.") else .nameWithOwner end')

git init -b main
if [[ $(git symbolic-ref --short HEAD) != main ]]; then
  echo 'Kurulum main dalını gerektiriyor. Mevcut dalı kontrol edin.' >&2
  exit 1
fi

if ! git rev-parse --verify HEAD >/dev/null 2>&1; then
  git add -- README.md .gitignore .editorconfig .gitattributes docs/CHARTER.md scripts/setup-github.sh
  git commit -m "chore: initialize Finance Tracker repository"
fi

if git remote get-url origin >/dev/null 2>&1; then
  origin=$(git remote get-url origin)
  case "$origin" in
    "https://github.com/$repo"|"https://github.com/$repo.git"|"git@github.com:$repo.git") ;;
    *) echo "origin beklenen repoya işaret etmiyor: $repo" >&2; exit 1 ;;
  esac
else
  git remote add origin "https://github.com/$repo.git"
fi

gh repo edit "$repo" \
  --description 'Finance Tracker: self-hosted personal finance, asset and savings goal tracking.' \
  --enable-issues --enable-wiki=false \
  --enable-squash-merge --enable-merge-commit=false --enable-rebase-merge=false \
  --delete-branch-on-merge --squash-merge-commit-message pr-title-description \
  --add-topic personal-finance --add-topic python --add-topic streamlit --add-topic self-hosted
gh repo edit "$repo" --enable-secret-scanning
gh repo edit "$repo" --enable-secret-scanning-push-protection
git -c credential.helper= -c 'credential.helper=!gh auth git-credential' push -u origin main
gh repo edit "$repo" --default-branch main
gh repo view "$repo" --json url,visibility,defaultBranchRef
