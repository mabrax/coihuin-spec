# Coihuin Spec Cheatsheet

## Setup

```bash
uv tool install ./tooling/cspec
```

## Quick Start

```bash
# 1. Initialize project structure
cspec init

# 2. Create project definition (in Claude Code)
/init "My Project"  # or cspec:init

# 3. Create an issue
/issue-create "Add user authentication"

# 4. Validate issue schema
cspec validate specs/issues/ISSUE-001.md

# 5. Full validation
/issue-validate ISSUE-001
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `cspec init` | Create directories + install slash commands |
| `cspec validate <path>` | Validate issue schema |
| `cspec validate <path> --strict` | Fail on warnings too |
| `cspec list` | List all issues |
| `cspec list --status=draft` | Filter by status |

## Slash Commands

| Command | Description |
|---------|-------------|
| `/init` | Create PROJECT.yaml + CONSTITUTION.md |
| `/issue-create <desc>` | Interactive issue creation |
| `/issue-validate <id>` | Full validation + suggestions |

Commands are namespaced as `cspec:<command>` (e.g., `cspec:init`, `cspec:issue-create`).

## Issue Natures

| Nature | When to use |
|--------|-------------|
| `feature` | New capability |
| `enhancement` | Improve existing |
| `bug` | Fix defect |
| `refactor` | Restructure, no behavior change |
| `optimization` | Performance improvement |
| `security` | Vulnerability fix |
| `hotfix` | Urgent production fix |
| `migration` | Move data/infrastructure |
| `configuration` | Settings change |
| `deprecation` | Mark for removal |
| `removal` | Delete deprecated |

## Impact → Version

| Impact | Version | Meaning |
|--------|---------|---------|
| `breaking` | `major` | Consumers must change |
| `additive` | `minor` | New surface, existing unchanged |
| `invisible` | `patch` | No external change |

## File Structure

```
specs/
├── PROJECT.yaml      # Project definition
├── CONSTITUTION.md   # Rules/philosophy
└── issues/
    └── ISSUE-XXX.md  # Issue files

.claude/commands/cspec/  # Slash commands (namespaced)
```

## Issue Template

```yaml
---
id: ISSUE-001
title: "Short description"
nature: feature
impact: additive
version: minor
status: draft
created: 2025-12-12
updated: 2025-12-12
context:
  required: []
  recommended: []
depends_on: []
blocks: []
---

## Problem
Why does this matter?

## Scope
### In Scope
- [ ] Deliverable 1

### Out of Scope
- Excluded item

## Acceptance Criteria
- [ ] Criterion 1

## Notes
Additional context.
```

## Status Flow

```
draft → ready → in-progress → done
                    ↓
                 blocked
```
