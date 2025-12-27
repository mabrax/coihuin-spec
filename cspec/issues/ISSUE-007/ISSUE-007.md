---
id: ISSUE-007
title: "Build specialized analysis agents"
nature: feature
impact: additive
version: minor
status: draft
created: 2025-12-17
updated: 2025-12-18

context:
  required:
    - type: proposal
      path: docs/proposals/research-phase-proposal.md
  recommended: []

depends_on: []
blocks:
  - ISSUE-005  # Orchestrator dispatches these agents
---

## Problem

The Research Phase requires specialized analysis agents that go beyond codebase snapshots:

- **Profiling analysis** - For optimization issues, need to collect and analyze performance metrics
- **Usage analysis** - For deprecation issues, need to find all consumers of a symbol, API, or feature
- **Dependency analysis** - For refactor/migration issues, need to map code and package dependency graphs

These are distinct from snapshot agents because they perform specific analytical tasks rather than documenting existing state. The research orchestrator decides which agents to dispatch based on issue context.

## Scope

### In Scope

- [ ] `analysis-profiling.md` - Agent for collecting/analyzing performance metrics
  - Identify bottlenecks and hot paths
  - Generate baseline metrics
  - Look for existing benchmarks, profiling hints
- [ ] `analysis-usage.md` - Agent for finding all consumers of a symbol, API, or feature
  - Trace call sites
  - Identify dependent code paths
  - Report consumer count and locations
- [ ] `analysis-dependency.md` - Agent for mapping code and package dependency graphs
  - Internal code dependencies
  - External package dependencies
  - Circular dependency detection
- [ ] Each agent has its own focused workflow
- [ ] Each agent outputs markdown to issue's research directory
- [ ] Consistent output format across all agents

### Out of Scope

- Snapshot agents (ISSUE-006)
- Deep profiling tool integration (start with grep/ast-based analysis)
- Orchestration logic (ISSUE-005 decides which agents to dispatch)
- Direct user-facing commands (orchestrator is the entry point)

## Acceptance Criteria

- [ ] All 3 analysis agents are available in `.claude/agents/`
- [ ] Each agent accepts issue context and outputs to `cspec/issues/ISSUE-XXX/research/`
- [ ] Each agent has a distinct workflow appropriate to its analysis type
- [ ] `analysis-profiling` identifies hot paths and generates metrics table
- [ ] `analysis-usage` finds and counts all usages of specified symbols
- [ ] `analysis-dependency` generates dependency graph representation
- [ ] Agents can be invoked by orchestrator or directly via Task tool

## Notes

Source proposal: `docs/proposals/research-phase-proposal.md` (All Workflows table)

**Architecture decision**: Agents instead of commands. The orchestrator (ISSUE-005) reads issue context and decides which analysis agents to dispatch. This keeps the command layer thin and lets Claude's reasoning decide the appropriate analysis strategy.

These agents may leverage external tools (profilers, static analyzers). Start with grep/ast-based approaches and iterate based on real usage.
