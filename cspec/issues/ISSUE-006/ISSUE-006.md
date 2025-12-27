---
id: ISSUE-006
title: "Build specialized snapshot agents"
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
    - type: agent
      path: .claude/agents/snapshot-researcher.md
  recommended: []

depends_on:
  - ISSUE-004  # Needs base snapshot-researcher agent
blocks:
  - ISSUE-005  # Orchestrator dispatches these agents
---

## Problem

Different issue natures require different types of codebase exploration. The Research Phase needs specialized snapshot agents, each with its own workflow for documenting specific aspects of the codebase:

- Integration points (for features)
- Current behavior (for enhancements)
- Architecture (for refactors)
- Hot paths (for optimizations)
- Configuration layer (for configuration changes)
- Current state (for migrations)

These are specialized agents (not commands). The research orchestrator decides which agents to dispatch based on issue context. The base `snapshot-researcher` remains as a generic fallback.

## Scope

### In Scope

- [ ] `snapshot-integration.md` - Agent for mapping where new code connects to existing system
- [ ] `snapshot-behavior.md` - Agent for documenting existing behavior before modification
- [ ] `snapshot-architecture.md` - Agent for mapping system structure, components, boundaries
- [ ] `snapshot-hotpaths.md` - Agent for identifying performance-critical code paths
- [ ] `snapshot-config.md` - Agent for documenting configuration system and options
- [ ] `snapshot-migration.md` - Agent for full state documentation for migration source
- [ ] Each agent has its own focused workflow (what to look for, how to explore)
- [ ] Each agent outputs markdown to issue's research directory
- [ ] Consistent output format across all agents

### Out of Scope

- The base `snapshot-researcher` agent (handled in ISSUE-004, remains as fallback)
- Analysis agents (profiling, usage, dependency - ISSUE-007)
- Orchestration logic (ISSUE-005 decides which agents to dispatch)
- Direct user-facing commands (orchestrator is the entry point)

## Acceptance Criteria

- [ ] All 6 specialized agents are available in `.claude/agents/`
- [ ] Each agent accepts issue context and outputs to `cspec/issues/ISSUE-XXX/research/`
- [ ] Each agent has a distinct workflow appropriate to its focus area
- [ ] Output includes code references with file paths and line numbers
- [ ] `snapshot-researcher` remains as generic fallback for undefined focuses
- [ ] Agents can be invoked by orchestrator or directly via Task tool

## Notes

Source proposal: `docs/proposals/research-phase-proposal.md` (All Workflows table)

**Architecture decision**: Agents instead of commands. The orchestrator (ISSUE-005) reads issue context (nature, problem description) and decides which snapshot agents to dispatch. This keeps the command layer thin (`/research <issue-id>`) and lets Claude's reasoning decide the appropriate exploration strategy.

Example flow:
```
/research ISSUE-042 → Orchestrator reads issue (nature: refactor)
                    → Dispatches snapshot-architecture + snapshot-behavior
                    → Agents explore and write to research/
                    → Orchestrator synthesizes findings
```
