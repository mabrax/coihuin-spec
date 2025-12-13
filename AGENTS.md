# AGENTS.md

This document provides coding agents with the context needed to work effectively in this project.

---

## CLI Commands Reference

The `cspec` CLI provides the following commands:

| Command | Description |
|---------|-------------|
| `cspec init` | Initialize spec-driven development (creates directories + installs slash commands) |
| `cspec validate <path>` | Validate an issue file against the schema |
| `cspec validate <path> --strict` | Validate with strict mode (fail on warnings) |
| `cspec list` | List all issues in the project |
| `cspec list --status=<status>` | Filter issues by status (draft, ready, in-progress, blocked, done) |
| `cspec update` | Update slash commands to latest version |

---

## Slash Commands Reference

Slash commands are available in Claude Code and are namespaced as `cspec:<command>`.

| Command | Description | Usage |
|---------|-------------|-------|
| `/cspec/init` | Create PROJECT.yaml and CONSTITUTION.md | `/cspec/init <project name>` |
| `/cspec/issue-create` | Interactive issue creation with proper structure | `/cspec/issue-create <description>` |
| `/cspec/issue-validate` | Full validation with suggestions and fixes | `/cspec/issue-validate <issue-id>` |

**Note**: Commands can also be invoked as `cspec:init`, `cspec:issue-create`, etc.

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
**Goal**: Capture and validate the change request.

1. Create issue: `/cspec/issue-create <description>`
2. Classify: Determine nature (feature, bug, etc.) and impact (breaking, additive, invisible)
3. Define scope and acceptance criteria
4. Validate schema: `cspec validate specs/issues/ISSUE-XXX.md`
5. Full validation: `/cspec/issue-validate ISSUE-XXX`
6. When passing, update status to `ready`

#### Phase 2: Specification
**Goal**: Define detailed implementation approach before writing code.

1. Identify boundaries the change crosses
2. Create spec artifacts per boundary
3. Define validation hooks (how to verify implementation)
4. Review and approve specs

#### Phase 3: Implementation
**Goal**: Build according to specification.

1. Review spec thoroughly
2. Implement following spec exactly
3. Run validation hooks during development
4. Address all acceptance criteria

#### Phase 4: Verification
**Goal**: Confirm implementation matches specification.

1. Run all validation hooks
2. Check acceptance criteria
3. Update persistent artifacts
4. Sign-off and close issue

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
specs/
├── PROJECT.yaml      # Project definition
├── CONSTITUTION.md   # Rules and philosophy
└── issues/
    └── ISSUE-XXX.md  # Issue files

.claude/commands/cspec/  # Slash commands (namespaced)
```

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
├── specs/                   # Project specs (source of truth)
│   ├── PROJECT.yaml        # Project definition
│   ├── CONSTITUTION.md     # Rules and philosophy
│   └── issues/             # Issue tracking
├── tooling/
│   └── cspec/              # The CLI tool
│       ├── src/cspec/
│       │   ├── cli.py      # Main entry point
│       │   ├── commands/   # Slash command templates
│       │   ├── models/     # Pydantic models
│       │   └── validators/ # Validation logic
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
| `tooling/cspec/src/cspec/models/issue.py` | Issue Pydantic model |
| `tooling/cspec/src/cspec/validators/issue_validator.py` | Issue validation logic |
| `docs/methodology.md` | Full development workflow |
| `docs/issue-template.md` | Issue file structure |
| `docs/change-taxonomy-system.md` | Nature/impact classification |

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
- **Issue**: A change request with nature, impact, scope, and acceptance criteria
- **Nature**: Type of change (feature, bug, enhancement, refactor, etc.)
- **Impact**: Effect on consumers (breaking → major, additive → minor, invisible → patch)
- **Spec**: Detailed implementation design created before coding
- **Validation hooks**: Commands/tests to verify implementation matches spec
- **Transient artifacts**: Delete when done (wireframes, plans)
- **Persistent artifacts**: Source of truth (API contracts, schemas)
- **Convergent loop**: Aim for one-shot, handle iteration gracefully

---

## References

- [Methodology](docs/methodology.md) - Full spec-driven development methodology
- [Issue Template](docs/issue-template.md) - Issue file structure
- [Issue Validation](docs/issue-validation.md) - Validation rules
- [Change Taxonomy](docs/change-taxonomy-system.md) - Classification system
- [Cheatsheet](docs/cheatsheet.md) - Quick reference
