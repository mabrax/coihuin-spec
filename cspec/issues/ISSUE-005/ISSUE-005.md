---
id: ISSUE-005
title: "Build research-orchestrator skill"
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
  - ISSUE-004  # Needs migrated tools
  - ISSUE-006  # Needs snapshot commands
  - ISSUE-007  # Needs analysis commands
blocks: []
---

## Problem

The Research Phase requires coordination of multiple research workflows based on issue nature. Currently, there's no mechanism to:

- Route issues to appropriate research workflows based on their nature
- Execute multiple workflows in parallel when independent
- Collect and merge findings into a unified report
- Validate that research is sufficient before proceeding to spec

A Research Orchestrator skill is needed to coordinate the entire research phase workflow.

## Scope

### In Scope

- [ ] Create `research-orchestrator` skill in `.claude/skills/`
- [ ] Implement PARSE step: load issue, extract nature/scope/context
- [ ] Implement PROPOSE step: map nature to workflows, get human confirmation
- [ ] Implement DISPATCH step: launch workflows (parallel if independent)
- [ ] Implement COLLECT step: gather findings, merge into report
- [ ] Implement VALIDATE step: run general + nature-specific checks
- [ ] Implement REVIEW step: present report to human for approval
- [ ] Generate `_report.md` in issue's research directory
- [ ] Track workflow overrides to tune mappings over time

### Out of Scope

- Fully automatic mode (alpha is semi-auto with human confirmation)
- Building the individual workflows (separate issues)
- Advanced validation rules (will be refined through usage)

## Acceptance Criteria

- [ ] Orchestrator can be invoked with `cspec research ISSUE-XXX`
- [ ] Correctly routes issues to workflows based on nature mapping table
- [ ] Human can approve, modify, or add workflows in PROPOSE step
- [ ] Parallel workflows execute concurrently
- [ ] Generates merged `_report.md` with all findings
- [ ] Validation runs and flags issues/gaps
- [ ] Human can approve research or request more

## Notes

Source proposal: `docs/proposals/research-phase-proposal.md` (Orchestration Model section)

Semi-auto mode is intentional for alpha: propose workflows, human confirms. This builds trust and allows tuning of nature->workflow mappings based on override patterns.
