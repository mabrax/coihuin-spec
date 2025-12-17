---
id: ISSUE-008
title: "Build /cspec:research-validate slash command"
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
  - ISSUE-005  # Needs orchestrator to generate reports to validate
blocks: []
---

## Problem

During alpha, research validation needs human oversight to:
- Detect system smells in the research process
- Refine boundaries for "enough research" through real usage
- Catch issues before proceeding to spec phase

A manual validation command allows humans to run the validation rubric on demand, providing visibility into research quality and identifying gaps.

## Scope

### In Scope

- [ ] Create `/cspec:research-validate` slash command
- [ ] Implement general rubric checks (all natures):
  - Completeness: Does research cover all areas in issue scope?
  - Evidence: Are findings backed by code refs, data, or sources?
  - Relevance: Is research focused on the issue, not wandering?
  - Uncertainty: Are unknowns explicitly flagged?
  - Actionability: Can spec work begin with this context?
- [ ] Implement nature-specific checks per validation table
- [ ] Output validation report with pass/fail/warning per dimension
- [ ] Highlight specific gaps or concerns for human review

### Out of Scope

- Automatic blocking (validation is advisory in alpha)
- Integration with orchestrator's VALIDATE step (that's internal)
- Automated remediation of validation failures

## Acceptance Criteria

- [ ] Command is available as `/cspec:research-validate ISSUE-XXX`
- [ ] Loads issue and its research artifacts from issue directory
- [ ] Runs all 5 general rubric checks
- [ ] Runs nature-specific checks based on issue nature
- [ ] Outputs clear validation report with status per dimension
- [ ] Identifies actionable gaps (e.g., "Missing baseline metrics for optimization")
- [ ] Returns overall status: pass / needs-attention / fail

## Notes

Source proposal: `docs/proposals/research-phase-proposal.md` (Research Validation section)

Alpha note from proposal: "Boundaries for 'enough research' will be refined through real usage, not predetermined rules." This command provides the feedback loop for that refinement.
