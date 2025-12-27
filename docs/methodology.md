# Spec-Driven Development Methodology

A framework for structured software development optimized for human-agent collaboration.

---

## Overview

This methodology provides a systematic approach to software development where specifications serve as the source of truth, enabling clear communication between humans and coding agents.

**Core Principle**: Every change flows through a defined process that ensures clarity, traceability, and verification.

---

## The Development Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   Issue          Spec           Implementation       Verification          │
│     │              │                  │                   │                 │
│     ▼              ▼                  ▼                   ▼                 │
│  ┌──────┐      ┌──────┐          ┌──────┐           ┌──────┐               │
│  │ What │  →   │ How  │    →     │ Code │     →     │ Done │               │
│  │ Why  │      │Detail│          │      │           │  ?   │               │
│  └──────┘      └──────┘          └──────┘           └──────┘               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

| Phase | Purpose | Output |
|-------|---------|--------|
| **Issue** | Define what needs to change and why | Validated issue document |
| **Spec** | Define how the change will be implemented | Specification artifacts |
| **Implementation** | Build according to spec | Working code |
| **Verification** | Confirm implementation matches spec | Acceptance sign-off |

---

## The System Model

The development flow is not a strict waterfall. It's a **convergent loop** — you aim for one-shot execution, but the system handles iteration gracefully when reality diverges from the plan.

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│  Issue → Spec → Implement → Validate ──┐            │
│    ↑                                   │            │
│    └───────── feedback loop ───────────┘            │
│                    │                                │
│                    ▼                                │
│              [Converged?] ──yes──→ Done             │
│                                      │              │
│                                      ▼              │
│                              Delete transient       │
│                              Keep persistent        │
└─────────────────────────────────────────────────────┘
```

### How the Loop Works

1. **Forward pass**: Issue → Spec → Implement → Validate
2. **Feedback**: Validation reveals gaps or discoveries
3. **Correction**: Flow returns to the appropriate phase
   - Spec gap → back to Spec
   - Problem misunderstood → back to Issue
4. **Convergence**: Loop exits when validation passes
5. **Cleanup**: Transient artifacts deleted, persistent artifacts updated

### Design Principles

- **Aim for one-shot**: Invest in upfront clarity to minimize iterations
- **Expect iteration**: The system handles feedback gracefully
- **Automate the loop**: Where possible, validation and refinement should be automated
- **Exit cleanly**: When done, delete transient artifacts — stale docs are worse than no docs

### Feedback Triggers

| Discovery | Return To | Action |
|-----------|-----------|--------|
| Spec ambiguity | Spec | Clarify and re-implement |
| Missing boundary | Spec | Add spec for boundary |
| Wrong assumption about problem | Issue | Revise issue, cascade to spec |
| Implementation reveals simpler solution | Spec | Update spec, re-verify |
| Acceptance criteria insufficient | Issue | Refine criteria, re-verify |

---

## Phase 1: Issue Definition

**Goal**: Capture and validate the change request before any spec work begins.

### Process

1. **Identify the change** - What needs to happen?
2. **Classify the change** - Nature + Impact → Version
3. **Gather required context** - Based on nature (see validation rules)
4. **Define scope** - What's in, what's explicitly out
5. **Set acceptance criteria** - How do we know it's done?
6. **Validate the issue** - Pass all validation rules

### Inputs

- Change request (user need, bug report, technical debt, etc.)
- Supporting context artifacts (RCA for bugs, research for features, etc.)

### Outputs

- Validated issue document (status: `ready`)

### Documents

- [Issue Template](./issue-template.md)
- [Issue Validation Rules](./issue-validation.md)
- [Change Taxonomy](./change-taxonomy-system.md)

---

## Phase 2: Specification

**Goal**: Define business rules before writing code.

### Process

1. **Create work directory** - `cspec/work/<work-slug>/`
2. **Identify affected features** - Which specs will this work touch?
3. **Write specs** - Gherkin-style business rules for each feature
4. **Add diagrams** - Sequence, state, or flow diagrams as needed
5. **Review spec** - Human approval before implementation

### Spec Principles

**Business rules, not implementation:**
- Use SHALL statements for requirements
- Use Given/When/Then scenarios for behavior
- No code, no API details, no database schemas
- Focus on WHAT the system does, not HOW

**Appropriate scope:**
- One feature per spec directory
- Split large features into sub-features
- A spec should be digestible in one reading

### Spec Artifacts by Nature

| Nature | Spec Approach |
|--------|---------------|
| Feature | New spec directory in `cspec/specs/<feature>/` |
| Enhancement | Work spec with ADDED/MODIFIED sections → merge into base |
| Bug Fix | Work spec with MODIFIED sections → merge into base |
| Refactor | May not need spec changes (behavior unchanged) |
| Deprecation | Work spec with REMOVED sections → merge into base |

### Outputs

- Specs in `cspec/work/<work-slug>/spec-<feature>.md`
- Diagrams as needed (`.mmd` files)
- Ready for implementation

### Documents

- [Spec-Driven Principle](./spec-driven-principle.md)
- [Agent-Optimized Spec Format](./agent-optimized-spec-format.md)

---

## Phase 3: Implementation

**Goal**: Build the solution according to the specification.

### Process

1. **Review spec** - Understand what needs to be built
2. **Implement** - Write code following spec exactly
3. **Self-verify** - Run validation hooks during development
4. **Complete** - All acceptance criteria addressed

### Agent-Optimized Implementation

For coding agents to work effectively:

- Spec provides explicit completion criteria
- Spec includes constraints (what NOT to do)
- Spec has concrete examples (input/output)
- Spec defines validation hooks (commands to verify)

### Outputs

- Working code
- Passing validation hooks

---

## Phase 4: Verification

**Goal**: Confirm the implementation matches the specification.

### Process

1. **Run validation hooks** - Automated checks from spec
2. **Review against acceptance criteria** - Manual or automated
3. **Verify scenarios** - Each Given/When/Then passes
4. **Regression check** - Existing functionality preserved
5. **Sign-off** - Human approval

### Post-Verification Cleanup

1. **Merge specs** - Work specs (`cspec/work/<slug>/spec-*.md`) merge into base specs (`cspec/specs/<feature>/spec.md`)
2. **Copy diagrams** - Any new diagrams move to permanent spec directories
3. **Delete work directory** - `rm -rf cspec/work/<work-slug>/`
4. **Only specs survive** - All other artifacts (issue, proposal, context) are deleted

### Outputs

- Updated base specs in `cspec/specs/`
- Issue closed
- Work directory deleted

---

## Artifact Lifecycle

### Permanent vs Ephemeral

| Type | Location | Description | Examples |
|------|----------|-------------|----------|
| **Permanent** | `cspec/specs/` | Source of truth, maintained over time | Feature specs, sequence diagrams, state diagrams |
| **Ephemeral** | `cspec/work/` | Discard after work complete | Issues, proposals, context snapshots, work-in-progress specs |

### Directory Structure

```
cspec/
├── specs/                         # PERMANENT - Source of truth
│   └── <feature>/                 # One directory per feature
│       ├── spec.md                # Gherkin-style business rules
│       ├── sequence.mmd           # Sequence diagrams
│       └── state.mmd              # State diagrams
│
└── work/                          # EPHEMERAL - Delete when done
    └── <work-slug>/               # One directory per work item
        ├── issue.md               # The trigger (what/why)
        ├── proposal.md            # High-level approach
        ├── context/               # Snapshots, RCA, research
        │   └── *.md
        └── spec-<feature>.md      # Specs being created/modified
```

### Spec Format

Specs use Gherkin-style business rules with SHALL statements:

```markdown
# <feature-name> Specification

## Requirement: <Requirement Name>

The <subject> SHALL <behavior>.

### Scenario: <scenario description>

**Given** <precondition>
**And** <additional precondition>
**When** <action>
**Then** <expected result>
**And** <additional expected result>
```

Key principles:
- **No implementation details** - Pure business rules, no code, no tech decisions
- **SHALL statements** - Each requirement is a testable obligation
- **Scenarios** - Given/When/Then for unambiguous behavior
- **Scoped appropriately** - No monolithic specs, one feature per directory

### Delta Management

When enhancing existing features:

1. **Create work directory**: `cspec/work/<work-slug>/`
2. **Write specs** as `spec-<feature>.md` in the work directory
3. **Include ADDED/MODIFIED/REMOVED sections** to show what changes
4. **After implementation**: Merge into base spec at `cspec/specs/<feature>/spec.md`
5. **Delete work directory**: `rm -rf cspec/work/<work-slug>/`

```
Work spec (ephemeral) + Base spec (permanent) → Updated base spec
```

A single piece of work may produce multiple specs targeting different features. Each gets merged into its respective base spec.

---

## Quality Gates

### Issue → Spec Gate

- [ ] Issue status is `ready`
- [ ] All validation rules pass
- [ ] Required context is present

### Spec → Implementation Gate

- [ ] All relevant boundaries have specs
- [ ] Specs are reviewed and approved
- [ ] Validation hooks are defined

### Implementation → Verification Gate

- [ ] All acceptance criteria addressed
- [ ] All validation hooks pass
- [ ] Code complete (no TODOs for this issue)

### Verification → Done Gate

- [ ] All scenarios pass
- [ ] Human sign-off obtained
- [ ] Work specs merged into `cspec/specs/`
- [ ] Work directory deleted

---

## Workflow Summary

```
1. Issue arrives
   │
   ├─→ Create work directory: cspec/work/<slug>/
   ├─→ Write issue.md (what/why)
   ├─→ Classify (nature + impact)
   ├─→ Define scope & acceptance criteria
   │
2. Write Specification
   │
   ├─→ Identify affected features
   ├─→ Write spec-<feature>.md for each
   ├─→ Add diagrams as needed
   ├─→ Review → Spec APPROVED
   │
3. Implement
   │
   ├─→ Follow spec scenarios exactly
   ├─→ Run validation hooks
   ├─→ Complete → Implementation DONE
   │
4. Verify & Cleanup
   │
   ├─→ Run all validation hooks
   ├─→ Check acceptance criteria
   ├─→ Merge work specs into cspec/specs/<feature>/spec.md
   ├─→ Delete work directory
   └─→ Sign-off → DONE (only specs survive)
```

---

## References

- [Issue Template](./issue-template.md)
- [Issue Validation Rules](./issue-validation.md)
- [Change Taxonomy](./change-taxonomy-system.md)
- [Spec-Driven Principle](./spec-driven-principle.md)
- [Agent-Optimized Spec Format](./agent-optimized-spec-format.md)
