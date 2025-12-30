---
description: Write a proposal for the current work item
argument-hint: [work-slug or leave empty to auto-detect]
---

# Write Proposal

You are writing a proposal that describes HOW to solve the issue. The proposal bridges the gap between "what we want" (issue) and "what we'll build" (spec).

## Target Work Item

$ARGUMENTS

If no argument provided, detect the current work item:
1. Check if we're in a `cspec/work/<slug>/` directory
2. Or find the most recently modified work directory
3. Or list available work items and ask

## Process

### Step 1: Load the Issue

Read `cspec/work/<slug>/issue.md` to understand:
- What problem are we solving?
- What's the nature (feature, bug, etc.)?
- What are the acceptance criteria?
- What's in/out of scope?

### Step 2: Gather Context (if needed)

Based on the issue nature, you may need to gather context first:

| Nature | Recommended Context |
|--------|---------------------|
| bug | RCA - investigate root cause |
| feature | Codebase snapshot of affected areas |
| enhancement | Current implementation snapshot |
| refactor | Architecture analysis |
| optimization | Performance baseline |

If context is needed, suggest running appropriate analysis first and saving to `context/`.

### Step 3: Explore the Codebase

Before proposing a solution, understand the current state:
- What files/modules are affected?
- What patterns does the codebase use?
- What constraints exist?
- What would be the simplest solution?

### Step 4: Draft the Proposal

Update `proposal.md` with:

```markdown
---
issue: <number>
status: draft
created: <today>
---

# Proposal: <title>

## Summary

<!-- 2-3 sentences describing the approach -->

## Approach

### Option 1: <name> (Recommended)

<!-- Describe the recommended approach -->

**Pros:**
- ...

**Cons:**
- ...

### Option 2: <name> (Alternative)

<!-- If there's a meaningful alternative -->

**Pros:**
- ...

**Cons:**
- ...

## Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| ... | ... | ... |

## Affected Components

| Component | Change Type | Description |
|-----------|-------------|-------------|
| `path/to/file.py` | modify | ... |
| `path/to/new.py` | create | ... |

## Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| ... | low/med/high | low/med/high | ... |

## Out of Scope

- Explicitly excluded: ...

## Open Questions

- [ ] Question that needs answering before spec?
```

### Step 5: Review with User

Present the proposal and ask:
- Does this approach make sense?
- Any concerns with the key decisions?
- Should we explore alternatives?
- Ready to move to spec?

### Step 6: Update Status

Once approved, update the frontmatter:

```yaml
status: approved
approved: <today>
```

### Step 7: Report Next Step

Output:
- Summary of the proposal
- Key decisions made
- Next step: `/cspec:spec-write` to write the spec

## Notes

- Keep proposals high-level - implementation details go in the spec
- If the issue is simple (small bug fix, config change), proposal can be minimal
- Proposals are ephemeral - they exist to communicate intent, not as permanent record
- The spec is what survives; the proposal is just the journey there
