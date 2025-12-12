# Methodology Tooling

Operational artifacts to implement the spec-driven development methodology.

---

## Slash Commands

### Issue Phase

| Command | Purpose | Status |
|---------|---------|--------|
| `/issue-create` | Create new issue with proper YAML frontmatter structure | Planned |
| `/issue-classify` | Determine nature + impact → version suggestion | Planned |
| `/issue-validate` | Check issue meets all validation rules for its nature | Planned |
| `/issue-ready` | Gate check: is issue ready to move to spec? | Planned |

### Spec Phase

| Command | Purpose | Status |
|---------|---------|--------|
| `/spec-boundaries` | Identify boundaries the change crosses | Planned |
| `/spec-create` | Generate spec artifacts based on nature + boundaries | Planned |
| `/spec-validate` | Check spec completeness for nature/boundaries | Planned |
| `/spec-review` | Gate check: is spec ready for implementation? | Planned |

### Implementation Phase

| Command | Purpose | Status |
|---------|---------|--------|
| `/implement-start` | Begin implementation, load spec context | Planned |
| `/implement-hooks` | Run validation hooks during development | Planned |

### Validation Phase

| Command | Purpose | Status |
|---------|---------|--------|
| `/validate` | Run all validation hooks + acceptance criteria | Planned |
| `/validate-boundaries` | Verify each boundary works correctly | Planned |

### Feedback Loop

| Command | Purpose | Status |
|---------|---------|--------|
| `/feedback` | Analyze validation failure → recommend return point (issue vs spec) | Planned |

### Closure

| Command | Purpose | Status |
|---------|---------|--------|
| `/close` | Mark done, delete transients, update persistent artifacts | Planned |

---

## Templates

| Template | Purpose | Location | Status |
|----------|---------|----------|--------|
| `issue.md` | Issue structure with YAML frontmatter | `docs/issue-template.md` | Done |
| `spec-feature.md` | Spec template for features | `tooling/templates/` | Planned |
| `spec-bugfix.md` | Spec template for bug fixes | `tooling/templates/` | Planned |
| `spec-enhancement.md` | Spec template for enhancements | `tooling/templates/` | Planned |
| `spec-refactor.md` | Spec template for refactors | `tooling/templates/` | Planned |
| `validation-report.md` | Output of validation phase | `tooling/templates/` | Planned |

---

## Scripts

| Script | Purpose | Location | Status |
|--------|---------|----------|--------|
| `classify.py` | Nature + impact → version calculation | `tooling/scripts/` | Planned |
| `validate-issue.py` | Rule checker for issues by nature | `tooling/scripts/` | Planned |
| `validate-spec.py` | Rule checker for specs by nature/boundary | `tooling/scripts/` | Planned |
| `identify-boundaries.py` | Analyze change scope → boundary list | `tooling/scripts/` | Planned |

---

## Folder Structure

```
tooling/
├── README.md              # This file
├── commands/              # Slash command definitions (.md files)
│   ├── issue-create.md
│   ├── issue-classify.md
│   ├── issue-validate.md
│   ├── issue-ready.md
│   ├── spec-boundaries.md
│   ├── spec-create.md
│   ├── spec-validate.md
│   ├── spec-review.md
│   ├── implement-start.md
│   ├── implement-hooks.md
│   ├── validate.md
│   ├── validate-boundaries.md
│   ├── feedback.md
│   └── close.md
├── templates/             # Artifact templates
│   ├── spec-feature.md
│   ├── spec-bugfix.md
│   ├── spec-enhancement.md
│   ├── spec-refactor.md
│   └── validation-report.md
└── scripts/               # Automation scripts
    ├── classify.py
    ├── validate-issue.py
    ├── validate-spec.py
    └── identify-boundaries.py
```

---

## Implementation Priority

For duck-footing — start with the core loop, add sophistication later:

### Phase 1: Core Creation & Validation
1. `/issue-create` + `/issue-validate` — can we create valid issues?
2. `/spec-create` + `/spec-validate` — can we create valid specs?

### Phase 2: Verification & Feedback
3. `/validate` — can we verify implementation?
4. `/feedback` — can we handle iteration?

### Phase 3: Automation & Cleanup
5. `/close` — can we clean up properly?
6. Gate commands (`/issue-ready`, `/spec-review`)
7. Helper commands (`/issue-classify`, `/spec-boundaries`)

---

## References

- [Methodology](../docs/methodology.md)
- [Issue Template](../docs/issue-template.md)
- [Issue Validation Rules](../docs/issue-validation.md)
- [Change Taxonomy](../docs/change-taxonomy-system.md)
- [Spec-Driven Principle](../docs/spec-driven-principle.md)
- [Agent-Optimized Spec Format](../docs/agent-optimized-spec-format.md)
