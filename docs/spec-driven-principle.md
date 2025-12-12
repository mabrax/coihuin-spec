# Spec-Driven Development Principle

The spec should cover **every boundary** your feature crosses.

| Boundary | Spec Needed |
|----------|-------------|
| User ↔ UI | Wireframes, interaction specs |
| UI ↔ API | API contract, request/response shapes |
| API ↔ Database | Schema, migrations |
| Service ↔ Service | Interface contracts |
| System ↔ External | Integration specs |

---

## Spec Artifacts by Nature of Change

| Nature | Key Spec Artifacts |
|--------|-------------------|
| **Feature** | Requirements, API contracts, data models, UI specs |
| **Enhancement** | Delta from current behavior, backward compatibility notes |
| **Bug Fix** | Repro steps, root cause, expected vs actual, fix criteria |
| **Refactor** | Before/after architecture, behavioral equivalence proof |
| **Optimization** | Baseline metrics, target metrics, measurement method |
| **Security Patch** | Vulnerability description, attack vector, mitigation |
| **Migration** | Data mapping, rollback plan, validation checklist |
| **Deprecation** | Sunset timeline, migration path, affected consumers |
| **Removal** | Impact assessment, final migration confirmation |

---

## Determining Spec Depth

Two inputs define what specification you need:

```
Nature of Change  →  What to specify
Impact + Scope    →  How deep to specify
```

---

## Related Documents

- [Agent-Optimized Spec Format](./agent-optimized-spec-format.md) - Guidelines for writing specs that coding agents can execute effectively
