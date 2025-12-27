---
description: Write a Gherkin-style spec from the proposal
argument-hint: [feature-name or leave empty to derive from issue]
---

# Write Spec

You are writing a **permanent spec** — a Gherkin-style document that captures business rules and behavior. This spec will survive after the work is complete and serve as the source of truth for this feature.

## Target

$ARGUMENTS

If no feature name provided:
1. Load the current work item's issue
2. Derive feature name from the issue (e.g., "csv-export", "user-auth")
3. Confirm with user

## Process

### Step 1: Load Context

Read from the current work directory:
- `issue.md` - What we're solving
- `proposal.md` - How we're solving it
- `context/*.md` - Supporting analysis

### Step 2: Determine Spec Type

Is this a **new spec** or a **delta to existing spec**?

Check if `cspec/specs/<feature>/spec.md` exists:
- **New**: Create fresh spec
- **Delta**: Write additions/modifications to merge later

### Step 3: Write the Spec

#### For NEW specs:

Create `cspec/work/<slug>/spec-<feature>.md`:

```markdown
# <Feature Name> Spec

> Source of truth for <feature> behavior

## Overview

<!-- 2-3 sentences describing what this feature does -->

## Requirements

### SHALL Statements

<!-- Normative requirements using RFC 2119 language -->

1. The system SHALL <requirement>
2. The system SHALL NOT <anti-requirement>
3. The system MAY <optional behavior>

## Behavior

### Scenario: <Happy Path>

```gherkin
Given <precondition>
When <action>
Then <expected outcome>
```

### Scenario: <Edge Case>

```gherkin
Given <precondition>
When <action>
Then <expected outcome>
```

### Scenario: <Error Case>

```gherkin
Given <precondition>
When <invalid action>
Then <error handling>
```

## Validation

How to verify implementation matches spec:

- [ ] <Test or verification step>
- [ ] <Test or verification step>

## Notes

<!-- Non-normative notes, examples, rationale -->
```

#### For DELTA specs (modifying existing):

Create `cspec/work/<slug>/spec-<feature>.md`:

```markdown
# <Feature Name> Spec Delta

> Changes to existing spec for issue #<number>

## ADDED

### New Requirements

1. The system SHALL <new requirement>

### New Scenarios

#### Scenario: <New Behavior>

```gherkin
Given <precondition>
When <action>
Then <expected outcome>
```

## MODIFIED

### Changed Requirements

1. ~~The system SHALL <old>~~ → The system SHALL <new>

### Changed Scenarios

#### Scenario: <Modified Behavior>

**Was:**
```gherkin
Given <old precondition>
When <old action>
Then <old outcome>
```

**Now:**
```gherkin
Given <new precondition>
When <new action>
Then <new outcome>
```

## REMOVED

### Deprecated Requirements

1. ~~The system SHALL <removed requirement>~~ (Reason: ...)

## Migration

<!-- If breaking change, how consumers should adapt -->
```

### Step 4: Validate Spec Quality

Check the spec against these criteria:

| Criterion | Check |
|-----------|-------|
| No implementation details | No code, no file paths, no method names |
| Testable scenarios | Each scenario can be verified |
| Complete coverage | All acceptance criteria from issue covered |
| Clear language | Unambiguous, uses SHALL/SHOULD/MAY correctly |
| Atomic scenarios | Each scenario tests one thing |

If issues found, fix before proceeding.

### Step 5: Review with User

Present the spec and confirm:
- Are the requirements complete?
- Are the scenarios correct?
- Any edge cases missing?
- Ready for implementation planning?

### Step 6: Report Next Step

Output:
- Spec file location
- Summary of requirements and scenarios
- Whether this is new or delta
- Next step: `/cspec:plan-write` to create implementation plan

## Spec Format Guidelines

### SHALL/SHOULD/MAY (RFC 2119)

- **SHALL**: Absolute requirement
- **SHALL NOT**: Absolute prohibition
- **SHOULD**: Recommended, but exceptions allowed
- **SHOULD NOT**: Discouraged, but exceptions allowed
- **MAY**: Optional

### Gherkin Best Practices

- **Given**: Set up the context (state before action)
- **When**: The action being tested (single action)
- **Then**: Expected outcome (observable result)
- **And**: Continue previous keyword

### What Belongs in Specs

✅ Business rules
✅ User-facing behavior
✅ API contracts (inputs/outputs)
✅ Error conditions
✅ Edge cases

### What Does NOT Belong in Specs

❌ File paths
❌ Class/function names
❌ Database schemas
❌ Implementation algorithms
❌ Performance targets (unless user-facing)

## Notes

- Specs are PERMANENT — they survive after work is complete
- Specs prevent regressions — if behavior changes, spec must change first
- Keep specs focused — one spec per feature/capability
- Deltas merge into main spec when work completes
