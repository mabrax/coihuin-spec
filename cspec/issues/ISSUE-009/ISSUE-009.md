---
id: ISSUE-009
title: "Update documentation for Research Phase"
nature: enhancement
impact: additive
version: minor
status: draft
created: 2025-12-17
updated: 2025-12-18

context:
  required:
    - type: proposal
      path: docs/proposals/research-phase-proposal.md
    - type: current-behavior
      path: docs/issue-validation.md
  recommended: []

depends_on:
  - ISSUE-004  # Tool migration completes first
  - ISSUE-005  # Orchestrator command ready
  - ISSUE-006  # Snapshot agents ready
  - ISSUE-007  # Analysis agents ready
  - ISSUE-008  # Validation command ready
blocks: []
---

## Problem

Once the Research Phase tooling is implemented, the methodology documentation needs to reflect the updated workflow:

- `Issue (validated) -> Research -> Spec -> Implementation -> Verification`

Currently, documentation describes required context per nature but lacks:
- How to gather that context (research workflows)
- The Research Phase in the overall methodology flow
- Quality gates between phases
- Slash commands for research (`/cspec:research`, `/cspec:research-validate`)

## Scope

### In Scope

- [ ] Update AGENTS.md to document research commands and workflow
- [ ] Update methodology flow documentation to include Research Phase
- [ ] Document quality gates between phases
- [ ] Document `/cspec:research ISSUE-XXX` command usage
- [ ] Document `/cspec:research-validate ISSUE-XXX` command usage
- [ ] Document research output structure (issue directory layout)
- [ ] Add research phase to workflow diagrams

### Out of Scope

- Writing the proposal (already done)
- Implementing the tools (separate issues)
- Tutorial or getting-started content (future enhancement)

## Acceptance Criteria

- [ ] AGENTS.md includes research workflow documentation
- [ ] Methodology flow shows Research Phase between Issue and Spec
- [ ] Quality gates documented for all phase transitions
- [ ] Slash commands documented with examples
- [ ] Research output structure documented with directory layout
- [ ] Documentation is consistent with implemented behavior

## Notes

Source proposal: `docs/proposals/research-phase-proposal.md` (CLI Integration, Updated Methodology Flow sections)

This issue should be done last, after implementation is complete, to ensure documentation matches actual behavior.
