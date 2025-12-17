---
id: ISSUE-006
title: "Build snapshot research commands"
nature: feature
impact: additive
version: minor
status: draft
created: 2025-12-17
updated: 2025-12-17

context:
  required:
    - type: proposal
      path: docs/proposals/research-phase-proposal.md
  recommended: []

depends_on:
  - ISSUE-004  # Needs snapshot-researcher agent
blocks:
  - ISSUE-005  # Orchestrator needs these commands
---

## Problem

Different issue natures require different types of codebase exploration. The Research Phase needs specialized snapshot commands to document specific aspects of the codebase:

- Integration points (for features)
- Current behavior (for enhancements)
- Architecture (for refactors)
- Hot paths (for optimizations)
- Configuration layer (for configuration changes)
- Current state (for migrations)

These are all variations of the `snapshot-researcher` agent, scoped to different focus areas.

## Scope

### In Scope

- [ ] `snapshot-integration-points` - Map where new code connects to existing system
- [ ] `snapshot-current-behavior` - Document existing behavior before modification
- [ ] `snapshot-architecture` - Map system structure, components, boundaries
- [ ] `snapshot-hot-paths` - Identify performance-critical code paths
- [ ] `snapshot-config-layer` - Document configuration system and options
- [ ] `snapshot-current-state` - Full state documentation for migration source
- [ ] Each command outputs markdown to issue's research directory
- [ ] Each command uses consistent output format

### Out of Scope

- The base `snapshot-researcher` agent (handled in ISSUE-004 migration)
- Analysis commands (profiling, usage, dependency - separate issue)
- Orchestration of these commands (handled by research-orchestrator)

## Acceptance Criteria

- [ ] All 6 snapshot commands are available in `.claude/commands/`
- [ ] Each command accepts an issue ID parameter
- [ ] Each command outputs to `cspec/issues/ISSUE-XXX/research/snapshot-<focus>.md`
- [ ] Output includes code references with file paths and line numbers
- [ ] Commands can be invoked independently or via orchestrator

## Notes

Source proposal: `docs/proposals/research-phase-proposal.md` (All Workflows table)

These commands wrap the `snapshot-researcher` agent with specific prompts and focus areas. The agent does the heavy lifting; the commands provide the scoping.
