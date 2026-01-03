# Coihuin Spec Cheatsheet

## Setup

```bash
uv tool install ./tooling/cspec
```

## Quick Start

```bash
# 1. Initialize project structure
cspec init

# 2. Create an issue (in Claude Code)
/cspec:issue-create "Add user authentication"

# 3. Check project status
cspec status

# 4. List work in progress
cspec work list
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `cspec init` | Create directories + install slash commands |
| `cspec status` | Check project health |
| `cspec update` | Update to latest templates |
| `cspec onboard` | Onboard to a project |
| `cspec specs list` | List permanent specs |
| `cspec specs show <feature>` | View a feature spec |
| `cspec work list` | List work in progress |
| `cspec work show <slug>` | View work item details |
| `cspec templates list` | List issue templates |
| `cspec templates get <name>` | Get a fillable template |

## Slash Commands

| Command | Description |
|---------|-------------|
| `/cspec:issue-create` | Interactive issue creation |
| `/cspec:issue-start` | Start from GitHub issue |
| `/cspec:proposal-write` | Write proposal for work item |
| `/cspec:spec-write` | Write Gherkin-style spec |
| `/cspec:plan-write` | Write implementation plan |
| `/cspec:work-complete` | Complete and clean up |

Commands are namespaced as `cspec:<command>` (e.g., `cspec:issue-create`).

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
cspec/
├── PROJECT.yaml      # Project definition
├── CONSTITUTION.md   # Rules/philosophy
├── specs/            # PERMANENT - Source of truth
│   └── <feature>/
│       ├── spec.md   # Gherkin-style business rules
│       └── *.mmd     # Diagrams
└── work/             # EPHEMERAL - Delete when done
    └── <work-slug>/
        ├── issue.md
        ├── proposal.md
        └── spec-*.md

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

## Workflow

```
1. Issue (/cspec:issue-create or /cspec:issue-start)
2. Proposal (/cspec:proposal-write)
3. Spec (/cspec:spec-write)
4. Plan (/cspec:plan-write)
5. Implement
6. Complete (/cspec:work-complete)
```
