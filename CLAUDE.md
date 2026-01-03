# CLAUDE.md

This document provides coding agents with the context needed to work effectively in this project.

---

## CLI Commands Reference

The `cspec` CLI provides the following commands:

| Command | Description |
|---------|-------------|
| `cspec init` | Initialize spec-driven development (creates directories + installs slash commands) |
| `cspec update` | Update slash commands, issue templates, and AGENTS.md to latest version |
| `cspec status` | Check project health and report status |
| `cspec onboard` | Onboard to a project (outputs prompt to populate PROJECT CONTEXT) |
| `cspec specs list` | List all permanent specs |
| `cspec specs show <feature>` | Show a feature spec |
| `cspec work list` | List all work in progress |
| `cspec work show <slug>` | Show details of a work item |
| `cspec templates list` | List all available issue templates (taxonomy) |
| `cspec templates get <name>` | Get a fillable issue template (markdown, yaml, or json) |

---

## Slash Commands Reference

Slash commands are available in Claude Code and are namespaced as `cspec:<command>`.

| Command | Description | Usage |
|---------|-------------|-------|
| `/cspec:issue-create` | Interactive issue creation with proper structure | `/cspec:issue-create <description>` |
| `/cspec:issue-start` | Import a GitHub issue and start work | `/cspec:issue-start <issue-url>` |
| `/cspec:proposal-write` | Write a proposal for the current work item | `/cspec:proposal-write` |
| `/cspec:spec-write` | Write a Gherkin-style spec from the proposal | `/cspec:spec-write` |
| `/cspec:plan-write` | Create an implementation plan from the spec | `/cspec:plan-write` |
| `/cspec:work-complete` | Complete work, merge spec, clean ephemeral files | `/cspec:work-complete` |

**Note**: Commands can also be invoked with `/cspec/` prefix (e.g., `/cspec/issue-create`).

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

1. Create issue: `/cspec:issue-create <description>` or `/cspec:issue-start <github-url>`
2. Classify: Determine nature (feature, bug, etc.) and impact (breaking, additive, invisible)
3. Define scope and acceptance criteria
4. Write proposal: `/cspec:proposal-write`
5. When approved, move to specification

#### Phase 2: Specification
**Goal**: Define business rules before writing code.

1. Write spec: `/cspec:spec-write`
2. Create Gherkin-style scenarios for each feature
3. Add diagrams as needed (sequence, state)
4. Review and approve specs

#### Phase 3: Implementation
**Goal**: Build according to specification.

1. Create implementation plan: `/cspec:plan-write`
2. Review spec and plan thoroughly
3. Implement following spec exactly
4. Run tests during development
5. Address all acceptance criteria

#### Phase 4: Verification & Cleanup
**Goal**: Confirm implementation matches specification and clean up.

1. Run all tests and validation
2. Check acceptance criteria
3. Complete work: `/cspec:work-complete`
   - Merges work specs into permanent specs
   - Deletes ephemeral work directory
4. Sign-off and close

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
├── PROJECT.yaml      # Project definition
├── CONSTITUTION.md   # Rules and philosophy
├── specs/            # PERMANENT - Source of truth
│   └── <feature>/
│       ├── spec.md   # Gherkin-style business rules
│       └── *.mmd     # Diagrams (sequence, state)
└── work/             # EPHEMERAL - Delete when done
    └── <work-slug>/
        ├── issue.md      # The trigger (what/why)
        ├── proposal.md   # High-level approach
        └── spec-*.md     # Specs being created/modified

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
