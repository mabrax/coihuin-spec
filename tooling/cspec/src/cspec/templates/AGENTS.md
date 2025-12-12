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

<!--
============================================================================
TO BE FILLED BY ONBOARD COMMAND

This section should be populated with project-specific context that helps
coding agents understand this particular codebase. The onboard command will
analyze your project and fill in the relevant details below.
============================================================================
-->

### Project Overview

<!-- Brief description of what this project does -->

### Tech Stack

<!-- Languages, frameworks, and key dependencies -->

### Architecture

<!-- High-level architecture and key components -->

### Key Conventions

<!-- Coding standards, naming conventions, patterns used -->

### Important Files

<!-- Key files an agent should know about -->

### Testing

<!-- How to run tests, testing conventions -->

### Build & Deploy

<!-- Build commands, deployment process -->

### Domain Knowledge

<!-- Project-specific terminology and concepts -->

---

## References

- [Methodology](docs/methodology.md) - Full spec-driven development methodology
- [Issue Template](docs/issue-template.md) - Issue file structure
- [Issue Validation](docs/issue-validation.md) - Validation rules
- [Change Taxonomy](docs/change-taxonomy-system.md) - Classification system
- [Cheatsheet](docs/cheatsheet.md) - Quick reference
