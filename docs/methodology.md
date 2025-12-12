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

**Goal**: Define the detailed implementation approach before writing code.

### Process

1. **Identify boundaries** - What interfaces does this change cross?
2. **Select spec artifacts** - Based on nature and boundaries
3. **Write specifications** - Machine-readable where possible
4. **Define validation hooks** - How to verify implementation
5. **Review spec** - Human approval before implementation

### The Boundary Principle

The spec should cover every boundary a feature crosses:

| Boundary | Spec Artifacts |
|----------|----------------|
| User ↔ UI | Wireframes, interaction flows, copy |
| UI ↔ API | Request/response contracts, error handling |
| API ↔ Database | Schema changes, queries, migrations |
| Service ↔ Service | API contracts, message formats |
| System ↔ External | Integration specs, retry policies |

### Spec Artifacts by Nature

| Nature | Primary Artifacts |
|--------|-------------------|
| Feature | Requirements, API contracts, data models, UI specs |
| Enhancement | Delta spec, backward compatibility notes |
| Bug Fix | Fix criteria, regression test spec |
| Refactor | Before/after architecture, equivalence tests |
| Optimization | Target metrics, measurement plan |
| Security | Mitigation spec, security test cases |
| Migration | Data mapping, rollback procedure |
| Deprecation | Timeline, migration guide |
| Removal | Final cleanup checklist |

### Outputs

- Specification artifacts (varies by nature and boundaries)
- Validation hooks (commands/tests to verify implementation)

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
3. **Verify boundaries** - Each crossed boundary works correctly
4. **Regression check** - Existing functionality preserved
5. **Sign-off** - Human approval

### Outputs

- Verification report
- Issue closed (status: `done`)

---

## Artifact Lifecycle

### Transient vs Persistent

| Type | Description | Examples |
|------|-------------|----------|
| **Transient** | Discard after issue complete | Feature wireframes, implementation plans, task breakdowns |
| **Persistent** | Source of truth, maintained over time | API contracts, database schema, business rules, ADRs |

### Delta Management

For changes to existing systems:

```
Current Truth + Delta Spec = New Truth
```

The delta spec documents what changes; upon completion, the persistent source of truth is updated.

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

- [ ] Verification report complete
- [ ] Human sign-off obtained
- [ ] Persistent artifacts updated
- [ ] Transient artifacts archived/deleted

---

## Workflow Summary

```
1. Issue arrives
   │
   ├─→ Classify (nature + impact)
   ├─→ Gather required context
   ├─→ Define scope & acceptance criteria
   ├─→ Validate → Issue READY
   │
2. Write Specification
   │
   ├─→ Identify boundaries crossed
   ├─→ Create spec artifacts per boundary
   ├─→ Define validation hooks
   ├─→ Review → Spec APPROVED
   │
3. Implement
   │
   ├─→ Follow spec exactly
   ├─→ Run validation hooks
   ├─→ Complete → Implementation DONE
   │
4. Verify
   │
   ├─→ Run all validation hooks
   ├─→ Check acceptance criteria
   ├─→ Update persistent artifacts
   └─→ Sign-off → Issue CLOSED
```

---

## References

- [Issue Template](./issue-template.md)
- [Issue Validation Rules](./issue-validation.md)
- [Change Taxonomy](./change-taxonomy-system.md)
- [Spec-Driven Principle](./spec-driven-principle.md)
- [Agent-Optimized Spec Format](./agent-optimized-spec-format.md)
