---
id: ISSUE-007
title: "Build analysis research commands"
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

depends_on: []
blocks:
  - ISSUE-005  # Orchestrator needs these commands
---

## Problem

The Research Phase requires specialized analysis tools that go beyond codebase snapshots:

- **Profiling analysis** - For optimization issues, need to collect and analyze performance metrics
- **Usage analysis** - For deprecation issues, need to find all consumers of a symbol, API, or feature
- **Dependency analysis** - For refactor/migration issues, need to map code and package dependency graphs

These are distinct from snapshot commands because they perform specific analytical tasks rather than documenting existing state.

## Scope

### In Scope

- [ ] `profiling-analysis` - Collect/analyze performance metrics
  - Identify bottlenecks
  - Generate baseline metrics
  - Output profiling data to research directory
- [ ] `usage-analysis` - Find all consumers of a symbol, API, or feature
  - Trace call sites
  - Identify dependent code paths
  - Report consumer count and locations
- [ ] `dependency-analysis` - Map code and package dependency graphs
  - Internal code dependencies
  - External package dependencies
  - Circular dependency detection
- [ ] Each command outputs markdown to issue's research directory
- [ ] Each command uses consistent output format

### Out of Scope

- Snapshot commands (separate issue ISSUE-006)
- Deep profiling tool integration (start with grep/ast-based analysis)
- Orchestration of these commands (handled by research-orchestrator)

## Acceptance Criteria

- [ ] All 3 analysis commands are available in `.claude/commands/`
- [ ] Each command accepts an issue ID parameter
- [ ] Each command outputs to `cspec/issues/ISSUE-XXX/research/<analysis-type>.md`
- [ ] `profiling-analysis` identifies hot paths and generates metrics table
- [ ] `usage-analysis` finds and counts all usages of specified symbols
- [ ] `dependency-analysis` generates dependency graph representation
- [ ] Commands can be invoked independently or via orchestrator

## Notes

Source proposal: `docs/proposals/research-phase-proposal.md` (All Workflows table)

These commands may need to invoke external tools (profilers, static analyzers). Start with grep/ast-based approaches and iterate based on real usage.
