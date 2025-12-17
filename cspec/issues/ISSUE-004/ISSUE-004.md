---
id: ISSUE-004
title: "Migrate existing research tools into project"
nature: migration
impact: additive
version: minor
status: ready
created: 2025-12-17
updated: 2025-12-17

context:
  required:
    - type: proposal
      path: docs/proposals/research-phase-proposal.md
  recommended: []

depends_on: []
blocks:
  - ISSUE-005  # Research orchestrator needs these tools
---

## Problem

The Research Phase proposal requires several tools that currently exist in the global `~/.claude/` configuration:

- `rca-analysis` skill - Root cause analysis for bugs/security issues
- `web-research` command - External documentation and patterns research
- `snapshot-researcher` agent - Sub-agent for parallel codebase exploration

These tools must be migrated into this project's `.claude/` directory to make the project self-contained. Without migration, the research orchestrator cannot coordinate these workflows.

## Scope

### In Scope

- [ ] Copy `rca-analysis` skill from global config to `.claude/skills/`
- [ ] Copy `web-research` command from global config to `.claude/commands/`
- [ ] Copy `snapshot-researcher` agent configuration
- [ ] Update any paths or references to work within project scope
- [ ] Verify each tool works correctly after migration
- [ ] Document any modifications made during migration

### Out of Scope

- Building new tools (separate issues)
- Modifying tool behavior beyond what's needed for migration
- Removing tools from global config (they can coexist)

## Acceptance Criteria

- [ ] `rca-analysis` skill is available in project scope and functional
- [ ] `web-research` command is available in project scope and functional
- [ ] `snapshot-researcher` agent can be invoked from project context
- [ ] No dependencies on global `~/.claude/` configuration for these tools
- [ ] Each migrated tool tested with a simple invocation

## Notes

Source proposal: `docs/proposals/research-phase-proposal.md`

The migrated tools form the foundation for the research orchestrator. Migration should preserve existing behavior while ensuring project isolation.
