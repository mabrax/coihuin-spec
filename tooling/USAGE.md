# Usage

## Setup

```bash
uv tool install ./tooling/cspec
```

## Workflow

| Step | Command |
|------|---------|
| Initialize project structure | `cspec init` |
| Create issue | `/cspec:issue-create <description>` |
| Start from GitHub issue | `/cspec:issue-start <github-url>` |
| Write proposal | `/cspec:proposal-write` |
| Write spec | `/cspec:spec-write` |
| Write implementation plan | `/cspec:plan-write` |
| Check project status | `cspec status` |
| List work in progress | `cspec work list` |
| Complete work | `/cspec:work-complete` |
| Update slash commands | `cspec update` |

Slash commands are namespaced as `cspec:<command>` (e.g., `cspec:issue-create`).
