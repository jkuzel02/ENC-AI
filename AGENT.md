# AI Agent Instructions

Before making **any** change in this repository, you MUST read [CONTRIBUTING.md](./CONTRIBUTING.md), tell the user about the contribution procedure before you start, and follow it strictly.

## Mandatory Workflow

1. **Tooling:** Ensure the GitHub CLI (`gh`) is installed.
2. **Issues:** Run `gh issue list` first. Pick an existing issue (and post progress via `gh issue comment`) or create a new one (`gh issue create`). Do not close issues without human approval.
3. **Branch:** Run `git fetch origin` and branch from up-to-date `origin/main` using `<type>/<issue-number>-<short-slug>` (e.g., `docs/3-readme-precision`). Carry or stash any existing uncommitted changes safely—never discard local work.
4. **Commits:** Follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat`, `fix`, `docs`, `chore`, `refactor`, `test`) and reference the issue in the commit body or footer (`Refs #N` or `Closes #N`).
5. **Pull Request:** Open a PR only when all changes are complete. State *what* changed, *why*, and *how it was tested*.
6. **Cleanup:** After the PR is merged (or before starting unrelated work), switch back to `main`, run `git pull --ff-only`, and delete the merged local branch.

## Hard Rules (NEVER)

- **NEVER** approve or merge a pull request—a human must review and merge via their own GitHub session.
- **NEVER** push directly to `main` or force-push / rewrite history on shared branches.
- **NEVER** edit `README.md`.
- **NEVER** commit secrets, tokens, or kubeconfig files.
