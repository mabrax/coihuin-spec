---
id: ISSUE-005
title: "Build research orchestrator command"
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

depends_on:
  - ISSUE-004  # Needs base snapshot-researcher agent
  - ISSUE-006  # Needs specialized snapshot agents
  - ISSUE-007  # Needs specialized analysis agents
blocks:
  - ISSUE-008  # Validation command needs orchestrator
---

## Problem

The Research Phase requires coordination of multiple research agents based on issue nature. Currently, there's no mechanism to:

- Route issues to appropriate agents based on their nature
- Execute multiple agents in parallel when independent
- Collect and merge findings into a unified report
- Validate that research is sufficient before proceeding to spec

A `/research` command is needed as the user-facing entry point that orchestrates the entire research phase.

## Scope

### In Scope

- [ ] Create `/cspec:research` command in `.claude/commands/cspec/`
- [ ] Implement PARSE step: load issue, extract nature/scope/context
- [ ] Implement PROPOSE step: map nature to agents, get human confirmation
- [ ] Implement DISPATCH step: launch agents via Task tool (parallel if independent)
- [ ] Implement COLLECT step: gather agent outputs, merge into report
- [ ] Implement VALIDATE step: run general + nature-specific checks
- [ ] Implement REVIEW step: present report to human for approval
- [ ] Generate `_report.md` in issue's research directory
- [ ] Track agent selection overrides to tune mappings over time

### Out of Scope

- Fully automatic mode (alpha is semi-auto with human confirmation)
- Building the individual agents (ISSUE-006, ISSUE-007)
- Advanced validation rules (will be refined through usage)

## Acceptance Criteria

- [ ] Command invoked with `/cspec:research ISSUE-XXX`
- [ ] Correctly maps issue nature to appropriate agents (snapshot + analysis)
- [ ] Human can approve, modify, or add agents in PROPOSE step
- [ ] Independent agents execute concurrently via parallel Task calls
- [ ] Generates merged `_report.md` with all agent findings
- [ ] Validation runs and flags gaps in research
- [ ] Human can approve research or request additional exploration

## Notes

Source proposal: `docs/proposals/research-phase-proposal.md` (Orchestration Model section)

**Architecture decision**: Command instead of skill. User explicitly invokes `/cspec:research ISSUE-XXX` to start research. The command reads issue context, proposes which agents to dispatch, gets human confirmation, then orchestrates the agents.

Example flow:
```
/cspec:research ISSUE-042
  → PARSE: Read issue (nature: optimization, problem: slow API)
  → PROPOSE: "I'll dispatch snapshot-hotpaths + analysis-profiling. Approve?"
  → DISPATCH: Task(snapshot-hotpaths), Task(analysis-profiling) in parallel
  → COLLECT: Merge outputs into research/_report.md
  → VALIDATE: Check for gaps (missing metrics? unclear bottleneck?)
  → REVIEW: "Research complete. Proceed to spec?"
```

Semi-auto mode is intentional for alpha: propose agents, human confirms. This builds trust and allows tuning of nature→agent mappings based on override patterns.
