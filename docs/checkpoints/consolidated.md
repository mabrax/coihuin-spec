# Coihuin Spec - Checkpoint

## Problem

Developing a framework/methodology for spec-driven development optimized for coding agents, enabling structured work, artifact validation, and source of truth management throughout the software lifecycle.

---

## Framework Design

### Development Flow

```
Issue → Spec → Implement → Validate ──┐
  ↑                                   │
  └───────── feedback loop ───────────┘
                  │
                  ▼
            [Converged?] ──yes──→ Done → Delete transient, Keep persistent
```

### Core Principles

1. **Issue first** - every change starts with an issue (what and why)
2. **Spec before code** - specs define the "how" before implementation
3. **Source of truth** - specs are authoritative; code implements specs
4. **Validate against spec** - implementation correctness = spec compliance
5. **Clean exit** - delete transient artifacts; keep persistent ones updated

### Design Philosophy

- **Aim for one-shot**: Invest in upfront clarity to minimize iterations
- **Expect iteration**: The system handles feedback gracefully
- **Automate the loop**: Validation and refinement should be automated
- **Exit cleanly**: Stale docs are worse than no docs

---

## Change Taxonomy

### Nature (11 types)

feature, enhancement, bug, refactor, optimization, security, hotfix, migration, configuration, deprecation, removal

### Impact (3 levels)

| Impact | Version Bump | Description |
|--------|--------------|-------------|
| breaking | major | Incompatible API changes |
| additive | minor | New functionality, backward compatible |
| invisible | patch | Bug fixes, internal changes |

### Required Artifacts by Nature

| Nature | Required Artifacts |
|--------|-------------------|
| Feature | Requirements, API contracts, data models, UI specs |
| Enhancement | Delta from current, backward compatibility notes |
| Bug | Repro steps, root cause, expected vs actual, fix criteria |
| Refactor | Before/after architecture, behavioral equivalence proof |
| Optimization | Baseline metrics, target metrics, measurement method |
| Security | Vulnerability description, attack vector, mitigation |
| Migration | Data mapping, rollback plan, validation checklist |
| Deprecation | Sunset timeline, migration path, affected consumers |
| Removal | Impact assessment, final migration confirmation |

---

## The Boundary Principle

Spec must cover every boundary a feature crosses:
- User↔UI, UI↔API, API↔Database, Service↔Service, System↔External
- Each boundary requires specific artifacts (wireframes, API contracts, schemas)

---

## Artifact Lifecycle

| Transient (delete after done) | Persistent (source of truth) |
|------------------------------|------------------------------|
| Feature wireframes | API contracts |
| Implementation plans | Database schema |
| Task breakdowns | Business rules |
| Design exploration docs | Interface definitions, ADRs |

**Delta Pattern**: Current Truth + Delta Spec = New Truth

---

## Agent-Optimized Spec Requirements

1. Machine-readable formats over prose
2. Explicit completion criteria
3. Constraints (what NOT to do)
4. Concrete examples (input/output)
5. Current state reference for deltas
6. Atomic scope (one focused change per spec)
7. Dependency declarations
8. Validation hooks (commands to verify implementation)

---

## What Was Built

### Python CLI Tool (`cspec`)

Location: `tooling/cspec/`
Built with: UV, Click, Pydantic, PyYAML
Branding: "Coihuin Spec" with ASCII banner

**Commands**:
- `cspec init` - creates `specs/issues/` and installs slash commands to `.claude/commands/`
- `cspec validate <path>` - Pydantic schema validation
- `cspec validate <path> --strict` - fail on warnings
- `cspec list` - list issues with status/nature
- `cspec list --status=<status>` - filter by status

**Install**: `uv tool install ./tooling/cspec`

### Slash Commands

| Command | Purpose |
|---------|---------|
| `/cspec-init <project>` | Creates PROJECT.yaml and CONSTITUTION.md |
| `/issue-create <desc>` | Interactive issue creation with LLM guidance |
| `/issue-validate <id>` | Full validation (schema + semantic checks) |

Note: `/init` renamed to `/cspec-init` to avoid Claude Code conflict.

### Architecture Split

| Deterministic (Python) | LLM-Assisted (Slash Commands) |
|------------------------|------------------------------|
| Schema validation | Interactive creation |
| Format checking | Semantic validation |
| Version-impact matching | Fixing suggestions |

---

## File Structure

```
specs/
├── PROJECT.yaml      # Project definition
├── CONSTITUTION.md   # Rules and philosophy
└── issues/           # Issue files (ISSUE-XXX.md)

.claude/commands/     # Project-specific slash commands
├── cspec-init.md
├── issue-create.md
└── issue-validate.md

tooling/
├── USAGE.md          # Workflow documentation
└── cspec/            # Python CLI package
```

---

## Issue Schema

**YAML Frontmatter** (Pydantic-validated):
- `id` - pattern `ISSUE-XXX`
- `title` - max 100 chars
- `nature` - one of 11 types
- `impact` - breaking, additive, invisible
- `version` - must match impact
- `status` - draft, ready, in-progress, blocked, done
- `created`, `updated` - ISO dates
- `context.required`, `context.recommended` - references
- `depends_on`, `blocks` - dependencies

**Body Sections**: Problem, Scope (In/Out), Acceptance Criteria, Notes

---

## Workflow

```bash
cspec init                              # Bootstrap project
/cspec-init "Project Name"              # Create project definition
/issue-create "description"             # Create issue interactively
cspec validate specs/issues/ISSUE-XXX.md  # Schema validation
/issue-validate ISSUE-XXX               # Full validation + suggestions
```

---

## Feedback Triggers

| Discovery | Return To | Action |
|-----------|-----------|--------|
| Spec ambiguity | Spec | Clarify and re-implement |
| Missing boundary | Spec | Add spec for boundary |
| Wrong assumption | Issue | Revise issue, cascade to spec |
| Simpler solution found | Spec | Update spec, re-verify |
| Insufficient criteria | Issue | Refine criteria, re-verify |

---

## Implementation Status

| Phase | Status | Commands |
|-------|--------|----------|
| 1 | ✅ Complete | `/issue-create`, `/issue-validate`, `cspec` CLI |
| 2 | Next | `/spec-create`, `/spec-validate` |
| 3 | Later | `/validate`, `/feedback`, `/close`, gate commands |

### Git History

- `0ec4046` - fix: rename /init to /cspec-init to avoid Claude Code conflict
- `8d01fc3` - feat: implement cspec CLI and Phase 1 slash commands
- `fba2f5e` - chk: docs
- `18ebb2d` - init
