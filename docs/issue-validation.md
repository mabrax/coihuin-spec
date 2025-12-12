# Issue Validation Rules

This document defines validation rules for issues. An issue must pass validation before it can transition from `draft` to `ready` status.

---

## Universal Requirements

These apply to **all issues**, regardless of nature:

| Field | Rule |
|-------|------|
| `id` | Must be unique, follow pattern `ISSUE-XXX` |
| `title` | Non-empty, max 100 characters |
| `nature` | Must be valid enum value |
| `impact` | Must be valid enum value |
| `version` | Must match impact (breaking→major, additive→minor, invisible→patch) |
| `status` | Must be valid enum value |
| `created` | Valid ISO date |
| `updated` | Valid ISO date, >= created |
| Problem section | Non-empty, explains why this matters |
| Scope section | At least one in-scope item defined |
| Acceptance Criteria | At least one measurable criterion |

---

## Context Requirements by Nature

### Bug

| Context | Required | Description |
|---------|----------|-------------|
| RCA document | **Yes** | Root cause analysis with findings and proposed fix |
| Reproduction steps | **Yes** | Can be in RCA or issue body |
| Error logs/evidence | Recommended | Supporting diagnostic data |

**Validation**: Issue must reference an RCA document in `context.required`.

---

### Feature

| Context | Required | Description |
|---------|----------|-------------|
| Problem statement | **Yes** | Clear articulation of user need or opportunity |
| User impact description | **Yes** | Who benefits and how |
| User research | Recommended | Interviews, surveys, usage data |
| Competitive analysis | Recommended | How others solve this |
| Design exploration | Recommended | Early concepts, wireframes |

**Validation**: Problem statement can be in issue body or separate document.

---

### Enhancement

| Context | Required | Description |
|---------|----------|-------------|
| Current behavior reference | **Yes** | Link to existing functionality documentation |
| Delta description | **Yes** | What changes from current state |
| Backward compatibility notes | Recommended | Impact on existing users |

**Validation**: Must reference existing documentation showing current behavior.

---

### Refactor

| Context | Required | Description |
|---------|----------|-------------|
| Architecture scope | **Yes** | What code/systems are affected |
| Behavioral equivalence statement | **Yes** | Explicit "no behavior change" commitment |
| Current architecture reference | Recommended | Diagrams, documentation of as-is state |
| Target architecture | Recommended | Diagrams, documentation of to-be state |

**Validation**: Must explicitly state that external behavior remains unchanged.

---

### Optimization

| Context | Required | Description |
|---------|----------|-------------|
| Baseline metrics | **Yes** | Current performance measurements |
| Target metrics | **Yes** | Specific improvement goals |
| Measurement methodology | **Yes** | How metrics are captured |
| Profiling data | Recommended | Evidence of bottlenecks |

**Validation**: Must include quantifiable current and target metrics.

---

### Security Patch

| Context | Required | Description |
|---------|----------|-------------|
| Vulnerability report | **Yes** | Description of the security issue |
| Attack vector | **Yes** | How the vulnerability can be exploited |
| Severity assessment | **Yes** | CVSS score or equivalent rating |
| Affected versions | **Yes** | Which versions are vulnerable |
| Mitigation approach | Recommended | Proposed fix strategy |

**Validation**: Must reference vulnerability report with severity.

---

### Hotfix

| Context | Required | Description |
|---------|----------|-------------|
| Incident reference | **Yes** | Link to production incident |
| Impact assessment | **Yes** | Users/systems affected |
| Rollback plan | **Yes** | How to revert if fix fails |
| RCA (post-fix) | Recommended | Full analysis after immediate fix |

**Validation**: Must reference active incident and include rollback plan.

---

### Migration

| Context | Required | Description |
|---------|----------|-------------|
| Current state mapping | **Yes** | What exists today |
| Target state mapping | **Yes** | What it becomes |
| Data transformation rules | **Yes** | How data maps from old to new |
| Rollback plan | **Yes** | How to reverse if needed |
| Validation checklist | Recommended | How to verify migration success |

**Validation**: Must have documented current/target states and rollback plan.

---

### Configuration

| Context | Required | Description |
|---------|----------|-------------|
| Current configuration | **Yes** | Existing settings |
| New configuration | **Yes** | Proposed settings |
| Impact assessment | **Yes** | What changes as a result |
| Rollback values | Recommended | Previous values to restore if needed |

**Validation**: Must document before and after configuration values.

---

### Deprecation

| Context | Required | Description |
|---------|----------|-------------|
| Sunset timeline | **Yes** | When functionality will be removed |
| Migration path | **Yes** | How consumers should adapt |
| Consumer impact analysis | **Yes** | Who is affected |
| Communication plan | Recommended | How affected parties will be notified |

**Validation**: Must include timeline and migration path for consumers.

---

### Removal

| Context | Required | Description |
|---------|----------|-------------|
| Deprecation reference | **Yes** | Link to original deprecation issue |
| Final migration confirmation | **Yes** | Evidence all consumers migrated |
| Impact assessment | **Yes** | Confirmation of affected parties |
| Point of no return acknowledgment | Recommended | Sign-off that this is irreversible |

**Validation**: Must reference completed deprecation and confirm migration.

---

## Validation State Machine

```
draft ──[validate]──> ready ──[assign]──> in-progress ──[complete]──> done
                        │                      │
                        │                      v
                        │                   blocked
                        v
                     [failed] (stays draft, fix issues)
```

An issue can only move from `draft` to `ready` when:
1. All universal requirements are met
2. All required context for its nature is present
3. Version matches impact correctly

---

## Validation Checklist Generator

Based on `nature`, generate the validation checklist:

```python
def get_required_context(nature: str) -> list[str]:
    requirements = {
        "bug": ["rca"],
        "feature": ["problem-statement"],
        "enhancement": ["current-behavior", "delta-description"],
        "refactor": ["architecture-scope", "behavioral-equivalence"],
        "optimization": ["baseline-metrics", "target-metrics", "measurement-method"],
        "security": ["vulnerability-report", "attack-vector", "severity", "affected-versions"],
        "hotfix": ["incident-reference", "impact-assessment", "rollback-plan"],
        "migration": ["current-state", "target-state", "transformation-rules", "rollback-plan"],
        "configuration": ["current-config", "new-config", "impact-assessment"],
        "deprecation": ["sunset-timeline", "migration-path", "consumer-impact"],
        "removal": ["deprecation-reference", "migration-confirmation", "impact-assessment"],
    }
    return requirements.get(nature, [])
```

---

## Error Messages

When validation fails, provide actionable feedback:

| Error | Message |
|-------|---------|
| Missing RCA | "Bug issues require an RCA document. Add `context.required` with type `rca`." |
| Missing metrics | "Optimization issues require baseline and target metrics in context." |
| Version mismatch | "Impact is `breaking` but version is `patch`. Breaking changes require `major` version." |
| Empty scope | "At least one in-scope item must be defined." |
| No acceptance criteria | "At least one acceptance criterion must be defined." |
