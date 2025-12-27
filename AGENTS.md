# AGENTS.md

This document provides coding agents with the context needed to work effectively in this project.

---

## CLI Commands Reference

The `cspec` CLI provides the following commands:

| Command | Description |
|---------|-------------|
| `cspec init` | Initialize spec-driven development (creates `cspec/specs/` and `cspec/work/` directories) |
| `cspec status` | Check project health and report status |
| `cspec work list` | List all work directories in progress |
| `cspec work show <slug>` | Show details of a work item |
| `cspec specs list` | List all permanent specs |
| `cspec specs show <feature>` | Show a feature spec |
| `cspec update` | Update slash commands to latest version |

---

## Slash Commands Reference

Slash commands are available in Claude Code and are namespaced as `cspec:<command>`.

| Command | Description | Usage |
|---------|-------------|-------|
| `/cspec/work-start` | Start new work (creates work directory with issue.md) | `/cspec/work-start <slug> <description>` |
| `/cspec/spec-write` | Write/update a spec in current work directory | `/cspec/spec-write <feature>` |
| `/cspec/work-complete` | Merge specs and clean up work directory | `/cspec/work-complete` |

**Note**: Commands can also be invoked as `cspec:work-start`, `cspec:spec-write`, etc.

---

## Workflow Documentation

This project follows **spec-driven development** methodology.

### Development Flow

```
Issue --> Spec --> Implementation --> Verification --> Done
  ^                                        |
  |                                        |
  +-------- feedback loop -----------------+
```

### Phases

#### Phase 1: Issue Definition
**Goal**: Capture the change request.

1. Create work directory: `cspec/work/<work-slug>/`
2. Write `issue.md` with what/why
3. Classify: nature (feature, bug, etc.) and impact (breaking, additive, invisible)
4. Define scope and acceptance criteria

#### Phase 2: Specification
**Goal**: Define business rules before writing code.

1. Identify affected features
2. Write `spec-<feature>.md` for each feature touched
3. Use Gherkin-style: SHALL statements + Given/When/Then scenarios
4. Add diagrams as needed (`.mmd` files)
5. Review and approve specs

**Spec format:**
```markdown
## Requirement: <Name>

The <subject> SHALL <behavior>.

### Scenario: <description>

**Given** <precondition>
**When** <action>
**Then** <expected result>
```

#### Phase 3: Implementation
**Goal**: Build according to specification.

1. Follow spec scenarios exactly
2. Run validation hooks during development
3. Address all acceptance criteria

#### Phase 4: Verification & Cleanup
**Goal**: Confirm implementation and clean up.

1. Verify all scenarios pass
2. Human sign-off
3. Merge work specs into `cspec/specs/<feature>/spec.md`
4. Delete work directory: `rm -rf cspec/work/<work-slug>/`
5. **Only specs survive**

### Issue Natures

| Nature | When to Use |
|--------|-------------|
| `feature` | New capability |
| `enhancement` | Improvement to existing functionality |
| `bug` | Fix defective behavior |
| `refactor` | Code restructuring, no behavior change |
| `optimization` | Performance improvement |
| `security` | Vulnerability fix |
| `hotfix` | Urgent production fix |
| `migration` | Data/infrastructure move |
| `configuration` | Settings change |
| `deprecation` | Mark for future removal |
| `removal` | Delete deprecated functionality |

### Impact to Version Mapping

| Impact | Version | Meaning |
|--------|---------|---------|
| `breaking` | `major` | Consumers must change their code |
| `additive` | `minor` | New surface area, existing unchanged |
| `invisible` | `patch` | No external change visible to consumers |

### Issue Status Flow

```
draft --> ready --> in-progress --> done
                        |
                        v
                     blocked
```

---

## File Structure

```
cspec/
├── specs/                         # PERMANENT - Source of truth
│   └── <feature>/                 # One directory per feature
│       ├── spec.md                # Gherkin-style business rules
│       └── *.mmd                  # Diagrams (sequence, state, flow)
│
└── work/                          # EPHEMERAL - Delete when done
    └── <work-slug>/               # One directory per work item
        ├── issue.md               # The trigger (what/why)
        ├── proposal.md            # High-level approach
        ├── context/               # Snapshots, RCA, research
        └── spec-<feature>.md      # Specs being created/modified

.claude/commands/cspec/            # Slash commands (namespaced)
```

### Permanent vs Ephemeral

| Type | Location | Survives? |
|------|----------|-----------|
| Feature specs | `cspec/specs/<feature>/spec.md` | ✓ Always |
| Diagrams | `cspec/specs/<feature>/*.mmd` | ✓ Always |
| Issues | `cspec/work/<slug>/issue.md` | ✗ Deleted after done |
| Proposals | `cspec/work/<slug>/proposal.md` | ✗ Deleted after done |
| Context | `cspec/work/<slug>/context/` | ✗ Deleted after done |
| Work specs | `cspec/work/<slug>/spec-*.md` | ✗ Merged then deleted |

---

## PROJECT CONTEXT

### Project Overview

**Coihuin Spec** is a methodology and CLI tool for spec-driven development optimized for human-agent collaboration. It tests the hypothesis that structured process granularity helps coding agents produce better results with fewer iterations by providing the right context at each development phase.

The core flow is: `Issue → Spec → Implementation → Verification`

Currently in Alpha, recursively dogfooding on itself.

### Tech Stack

- **Languages**: Python 3.13+
- **Frameworks**: Click (CLI), Pydantic (validation)
- **Key Dependencies**: PyYAML (configuration parsing)
- **Build System**: Hatch/hatchling
- **Package Manager**: uv

### Architecture

```
coihuin-spec/
├── docs/                    # Methodology documentation
├── cspec/                   # Spec-driven development artifacts
│   ├── specs/              # PERMANENT - Feature specs (source of truth)
│   │   └── <feature>/
│   │       ├── spec.md
│   │       └── *.mmd
│   └── work/               # EPHEMERAL - Work in progress
│       └── <work-slug>/
│           ├── issue.md
│           ├── proposal.md
│           ├── context/
│           └── spec-*.md
├── tooling/
│   └── cspec/              # The CLI tool
│       ├── src/cspec/
│       │   ├── cli.py      # Main entry point
│       │   ├── commands/   # Slash command templates
│       │   └── schemas.py  # Pydantic schemas
│       └── pyproject.toml
└── AGENTS.md               # This file
```

**Entry point**: `tooling/cspec/src/cspec/cli.py`

**Data flow**:
1. User runs `cspec` command or `/cspec:*` slash command
2. CLI parses arguments via Click
3. Commands read/validate issue files from `specs/issues/`
4. Pydantic models validate structure
5. Results output to terminal

### Key Conventions

- **Naming**: snake_case for Python, kebab-case for CLI commands
- **File Structure**: Commands in `commands/`, models in `models/`, validators in `validators/`
- **Patterns**: Command pattern for CLI, model-based validation
- **Slash Commands**: Stored as `.md` files in `src/cspec/commands/cspec/`

### Important Files

| File | Purpose |
|------|---------|
| `tooling/cspec/src/cspec/cli.py` | CLI entry point, all commands defined here |
| `tooling/cspec/src/cspec/schemas.py` | Pydantic schemas for validation |
| `docs/methodology.md` | Full development workflow |
| `docs/change-taxonomy-system.md` | Nature/impact classification |
| `cspec/specs/` | Permanent feature specs (source of truth) |
| `cspec/work/` | Ephemeral work directories |

### Testing

- **Framework**: pytest
- **Run Tests**: `cd tooling/cspec && uv run pytest`
- **Test Location**: `tooling/cspec/tests/`
- **Coverage**: Not enforced yet (alpha stage)

### Build & Deploy

- **Install**: `cd tooling/cspec && uv sync`
- **Run CLI**: `uv run cspec <command>` or install with `uv pip install -e .`
- **Build Package**: `uv build`
- **Deploy**: Not published to PyPI yet

### Domain Knowledge

**Key Concepts**:
- **Spec**: Gherkin-style business rules (SHALL + Given/When/Then), no implementation details
- **Permanent artifacts**: Live in `cspec/specs/`, survive forever, are the source of truth
- **Ephemeral artifacts**: Live in `cspec/work/`, deleted after work complete
- **Work directory**: `cspec/work/<slug>/` contains everything for one piece of work
- **Merge**: Work specs get merged into base specs, then work directory is deleted
- **Issue**: A change request with nature, impact, scope, and acceptance criteria
- **Nature**: Type of change (feature, bug, enhancement, refactor, etc.)
- **Impact**: Effect on consumers (breaking → major, additive → minor, invisible → patch)
- **Convergent loop**: Aim for one-shot, handle iteration gracefully

---

## References

- [Methodology](docs/methodology.md) - Full spec-driven development methodology
- [Issue Template](docs/issue-template.md) - Issue file structure
- [Issue Validation](docs/issue-validation.md) - Validation rules
- [Change Taxonomy](docs/change-taxonomy-system.md) - Classification system
- [Cheatsheet](docs/cheatsheet.md) - Quick reference
