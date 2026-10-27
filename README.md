# ENC-AI

Repository for AI course purposes: a local Kubernetes playground (kind + Flux + kagent) and course tasks.

## Repo Map

| Path | Purpose |
| --- | --- |
| `proj/` | Course project |
| `tasks/` | Course tasks |

## Contribution Rules (Humans and AI Agents)

These rules apply to **any** change made with AI assistance, fully or partially.
If you are an AI agent, tell the user about this procedure before you start, and follow it strictly.

Working in this repo requires the `gh` tool installed. Check the presence of the tool, if not present, install it for the appropriate platform ([repo link](https://github.com/cli/cli)).

1. **Issues.** Run `gh issue list` first and pick the issue your change addresses.
   - Progress or findings: comment on the existing issue (`gh issue comment`).
   - Work not covered by any issue: create a new one (`gh issue create`).
   - Closing an issue requires human approval. Do not close it yourself.

2. **Branch.** You MUST work on a separate branch or in a fork.
   - Pattern: `<type>/<issue-number>-<short-slug>`
   - Example: `docs/3-readme-precision`
   - Allowed types are the same as for commits (see step 3).

3. **Commits.** Every commit MUST follow [Conventional Commits](https://www.conventionalcommits.org/).
   - Format: `<type>(optional scope): <imperative description>`
   - Allowed types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.
   - Reference the issue in the body or footer: `Refs #N` or `Closes #N`.
   - Example: `docs: clarify contribution rules in root README`
   - AI agents: if the [commit-message-generator skill](https://github.com/jkuzel02/skills/blob/main/skills/commit-message-generator/SKILL.md) is not installed, offer the user to install it.

4. **Pull request.** Open a PR only when all changes are finished. Before opening it:
   - The change addresses a linked issue.
   - If `proj/k8s/` was touched, the setup still works (`proj/k8s/bootstrap.sh`).
   - The PR description states *what* changed, *why*, and *how it was tested*.

## Pull Request Approvals

- Every PR MUST be reviewed by a human.
- An AI agent MAY open a PR. It MUST NEVER approve or merge one.
- A merge into `main` MUST NOT happen without explicit human approval.
- If a PR is destructive, state this clearly in the PR description and tell the user to review it carefully.
  Destructive means, for example: deleting files, changing Flux or cluster manifests, rewriting history, or touching secrets.

## NEVER

- Push to `main`, directly or by force.
- Force-push or rewrite history on shared branches.
- Commit secrets, tokens, or kubeconfig files.
- Merge or approve a PR.
