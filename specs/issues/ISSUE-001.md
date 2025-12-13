---
id: ISSUE-001
title: "Remove /cspec:init slash command"
nature: removal
impact: invisible
version: patch
status: done
created: 2025-12-13
updated: 2025-12-13

context:
  required: []
  recommended: []

depends_on: []
blocks: []
---

## Problem

The `/cspec:init` slash command duplicates functionality already provided by the `cspec init` CLI command, creating unnecessary UX complexity. The desired workflow is:

1. User runs `cspec init` (CLI) to create directory structure and install slash commands
2. User runs `cspec onboard` (CLI) to populate PROJECT.yaml, CONSTITUTION.md, and AGENTS.md context

The slash command `/cspec:init` sits awkwardly between these two - it creates directories AND generates content via LLM, which doesn't match the hybrid architecture pattern (deterministic CLI + LLM-assisted slash commands for semantic tasks).

## Scope

### In Scope

- [ ] Delete `/cspec:init` slash command (`tooling/cspec/src/cspec/commands/cspec/init.md`)
- [ ] Update AGENTS.md slash commands reference table to remove `/cspec:init`
- [ ] Update any documentation referencing `/cspec:init`

### Out of Scope

- Changes to `cspec init` CLI command
- Changes to `cspec onboard` CLI command
- Adding new slash commands

## Acceptance Criteria

- [ ] `/cspec:init` slash command file no longer exists
- [ ] AGENTS.md accurately reflects available slash commands
- [ ] `cspec init` still installs remaining slash commands correctly
- [ ] Documentation is consistent (no references to removed command)

## Notes

This is a cleanup task as part of refining the cspec UX. The slash command was created early in development before the hybrid architecture pattern was fully established.
