# Usage

## Setup

```bash
uv tool install ./tooling/cspec
```

## Workflow

| Step | Command |
|------|---------|
| Initialize project structure | `cspec init` |
| Create project definition | `/init <project name>` |
| Create issue | `/issue-create <description>` |
| Validate issue (schema) | `cspec validate specs/issues/ISSUE-XXX.md` |
| Validate issue (full) | `/issue-validate <issue-id>` |
| Update slash commands | `cspec update` |

Slash commands are namespaced as `cspec:<command>` (e.g., `cspec:init`).
