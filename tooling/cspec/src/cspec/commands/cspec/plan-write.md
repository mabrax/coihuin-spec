---
description: Create an implementation plan from the spec
argument-hint: [work-slug or leave empty to auto-detect]
---

# Write Implementation Plan

You are creating an implementation plan that translates the spec into concrete coding tasks. This plan guides the actual implementation work.

## Target Work Item

$ARGUMENTS

If no argument, auto-detect current work item.

## Process

### Step 1: Load Context

Read from the current work directory:
- `issue.md` - Original issue
- `proposal.md` - Approved approach
- `spec-<feature>.md` - The spec to implement
- `context/*.md` - Supporting analysis

### Step 2: Analyze the Spec

For each requirement and scenario in the spec:
- What code changes are needed?
- What files are affected?
- What's the dependency order?

### Step 3: Create Implementation Plan

Create `cspec/work/<slug>/plan.md`:

```markdown
---
issue: <number>
spec: <feature>
status: draft
created: <today>
---

# Implementation Plan: <title>

## Overview

<!-- Brief summary of what we're implementing -->

Spec: `cspec/work/<slug>/spec-<feature>.md`
Target: `cspec/specs/<feature>/spec.md`

## Pre-Implementation Checklist

- [ ] Proposal approved
- [ ] Spec reviewed (no implementation details)
- [ ] Context gathered (snapshots, RCA if needed)
- [ ] Dependencies identified

## Implementation Phases

### Phase 1: <name>

**Goal:** <what this phase achieves>

**Tasks:**
1. [ ] <specific task>
   - Files: `path/to/file.py`
   - Change: <what to do>

2. [ ] <specific task>
   - Files: `path/to/other.py`
   - Change: <what to do>

**Validation:**
- [ ] <how to verify phase is complete>

### Phase 2: <name>

**Goal:** <what this phase achieves>

**Tasks:**
1. [ ] <specific task>
2. [ ] <specific task>

**Validation:**
- [ ] <how to verify phase is complete>

### Phase 3: Testing

**Goal:** Verify implementation matches spec

**Tasks:**
1. [ ] Write tests for Scenario: <name>
2. [ ] Write tests for Scenario: <name>
3. [ ] Run full test suite

**Validation:**
- [ ] All new tests pass
- [ ] No regression in existing tests

## File Changes Summary

| File | Action | Description |
|------|--------|-------------|
| `path/to/file.py` | modify | ... |
| `path/to/new.py` | create | ... |
| `path/to/old.py` | delete | ... |

## Dependencies

### Blocking
- [ ] <thing that must be done first>

### Non-Blocking
- [ ] <thing that can be done in parallel>

## Risks & Mitigations

| Risk | Mitigation |
|------|------------|
| ... | ... |

## Rollback Plan

If implementation fails or causes issues:
1. <rollback step>
2. <rollback step>

## Definition of Done

- [ ] All phases complete
- [ ] All tests passing
- [ ] Spec validation checklist complete
- [ ] Code reviewed
- [ ] Ready for `/cspec:work-complete`
```

### Step 4: Determine Seniority Level

For each phase, assess complexity:

| Indicator | Junior | Senior |
|-----------|--------|--------|
| Files affected | 1-2 | 3+ |
| Cross-cutting concerns | No | Yes |
| New patterns/architecture | No | Yes |
| Risk level | Low | Medium-High |

Tag phases with seniority for task routing.

### Step 5: Review with User

Present the plan:
- Is the phasing logical?
- Are tasks clear and actionable?
- Any missing steps?
- Ready to implement?

### Step 6: Update Status

Once approved:

```yaml
status: approved
approved: <today>
```

### Step 7: Report Next Step

Output:
- Plan location
- Phase summary
- Estimated complexity
- Next step: Start implementing Phase 1

## Plan Guidelines

### Good Tasks

✅ Specific and actionable
✅ Single responsibility
✅ Clear completion criteria
✅ File paths identified
✅ Ordered by dependency

### Bad Tasks

❌ Vague ("improve the code")
❌ Too large ("implement the feature")
❌ No clear completion
❌ Missing context

### Phase Sizing

- **Small phase**: 1-3 tasks, ~30 min
- **Medium phase**: 4-6 tasks, ~1-2 hours
- **Large phase**: 7+ tasks — consider splitting

## Notes

- Plans are ephemeral — deleted when work completes
- Plans can be updated during implementation
- If spec changes, update plan accordingly
- Use TodoWrite to track progress during implementation
