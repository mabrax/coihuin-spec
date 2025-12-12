---
description: Onboard to an existing project - check status, draft missing configs, populate AGENTS.md context
argument-hint: [optional: path to project root]
---

# Project Onboarding

You are onboarding to a spec-driven development project. This command helps set up missing configuration and populates project context for coding agents.

## User Input

$ARGUMENTS

## Process

### Step 1: Check Project Status

Run `cspec status` to assess the current state of the project:

```bash
cspec status
```

Review the output to understand:
- Whether specs/ directory exists
- Whether PROJECT.yaml exists and has content
- Whether CONSTITUTION.md exists and has content
- Current issue count and statuses

### Step 2: Handle PROJECT.yaml

If PROJECT.yaml is missing or empty, gather information from the user:

**Ask the user:**

1. **Project Name**: What is this project called?
2. **Description**: What does this project do? (1-2 sentences)
3. **Purpose**: Why does this project exist? What problem does it solve?
4. **Tech Stack**: What languages, frameworks, and key dependencies are used?
5. **Scope**: What's in and out of bounds for this project?
6. **Stakeholders**: Who uses or depends on this project?

**Then create `specs/PROJECT.yaml`:**

```yaml
name: "<project name>"
description: "<description>"
purpose: "<why it exists>"
created: <YYYY-MM-DD>

scope:
  includes:
    - "<what's in scope>"
  excludes:
    - "<what's out of scope>"

tech_stack:
  languages:
    - "<primary language>"
  frameworks:
    - "<framework>"
  dependencies:
    - "<key dependency>"

stakeholders:
  - "<stakeholder 1>"

methodology: spec-driven
version: 0.1.0
```

If PROJECT.yaml already exists with content, read it and proceed to Step 3.

### Step 3: Handle CONSTITUTION.md

If CONSTITUTION.md is missing or empty, gather information from the user:

**Ask the user:**

1. **Philosophy**: What guiding principles should this project follow?
2. **Rules/Constraints**: Are there any hard rules or constraints for development?
3. **Quality Standards**: What quality bars must be met?
4. **Anti-patterns**: What practices should be avoided?
5. **Decision Framework**: How should technical decisions be made?

**Then create `specs/CONSTITUTION.md`:**

```markdown
# Constitution

## Philosophy

This project follows **spec-driven development**:

1. **Issue first**: Every change starts with an issue (the "what and why")
2. **Spec before code**: Specs define the "how" before implementation
3. **Source of truth**: Specs are authoritative; code implements specs
4. **Validate against spec**: Implementation correctness = spec compliance
5. **Clean exit**: Delete transient artifacts; keep persistent ones updated

<Add any project-specific philosophy from user input>

## Rules

### Issues

- Every change requires an issue
- Issues must have: nature, impact, scope, acceptance criteria
- Issues must be validated before moving to spec phase

### Specs

- Specs must cover every boundary a change crosses
- Specs must be machine-readable where possible
- Specs include validation hooks (how to verify implementation)

### Implementation

- Implementation follows spec, not the other way around
- Deviations from spec require spec update first
- Feedback loops return to appropriate phase (issue or spec)

<Add any project-specific rules from user input>

## Quality Standards

<Add quality standards from user input, or use defaults:>

- All code must pass linting
- All tests must pass before merge
- Code review required for all changes

## Anti-patterns

<Add anti-patterns from user input, or use defaults:>

- Avoid premature optimization
- Avoid over-engineering
- Avoid undocumented "magic"

## Artifacts

| Type | Lifecycle |
|------|-----------|
| Wireframes, task breakdowns, design explorations | Transient (delete when done) |
| API contracts, schemas, business rules, ADRs | Persistent (source of truth) |

## Versioning

- **Breaking** changes to Major version
- **Additive** changes to Minor version
- **Invisible** changes to Patch version
```

If CONSTITUTION.md already exists with content, read it and proceed to Step 4.

### Step 4: Analyze the Codebase

Explore the project to gather context for AGENTS.md. Analyze:

1. **Project Structure**: Examine directory layout and organization
2. **Tech Stack**: Identify languages from file extensions, package files (package.json, pyproject.toml, Cargo.toml, go.mod, etc.)
3. **Architecture**: Look for architectural patterns, key modules, entry points
4. **Conventions**: Check for linting configs, formatting rules, naming patterns
5. **Important Files**: Identify entry points, configuration files, core modules
6. **Testing**: Find test directories, test frameworks, test commands
7. **Build/Deploy**: Check for build scripts, CI/CD configs, deployment files
8. **Documentation**: Review existing README, docs, comments

### Step 5: Update AGENTS.md PROJECT CONTEXT

Locate the AGENTS.md file (typically in the project root or created by `cspec init`). Find the `## PROJECT CONTEXT` section and populate it with your findings:

```markdown
## PROJECT CONTEXT

### Project Overview

<Brief description synthesized from PROJECT.yaml and codebase analysis>

### Tech Stack

- **Languages**: <list languages>
- **Frameworks**: <list frameworks>
- **Key Dependencies**: <list important dependencies>
- **Package Manager**: <npm/pip/cargo/etc>

### Architecture

<Describe high-level architecture>
- Entry points: <main files>
- Key modules: <core components>
- Data flow: <how data moves through the system>

### Key Conventions

- **Naming**: <camelCase/snake_case/PascalCase patterns>
- **File Structure**: <how files are organized>
- **Patterns**: <design patterns used>
- **Linting**: <linting tools and configs>

### Important Files

| File | Purpose |
|------|---------|
| <path> | <description> |
| <path> | <description> |

### Testing

- **Framework**: <test framework>
- **Run Tests**: `<test command>`
- **Test Location**: <test directory>
- **Coverage**: <coverage requirements if any>

### Build & Deploy

- **Build**: `<build command>`
- **Dev Server**: `<dev command>`
- **Deploy**: <deployment process>

### Domain Knowledge

<Project-specific terminology, business logic, domain concepts that an agent should understand>
```

### Step 6: Summary

Output a summary of what was done:

1. **Status Check Results**: What was found
2. **Files Created/Updated**:
   - PROJECT.yaml: created/existed/updated
   - CONSTITUTION.md: created/existed/updated
   - AGENTS.md: PROJECT CONTEXT section populated
3. **Project Context Gathered**:
   - Tech stack identified
   - Architecture insights
   - Key conventions
   - Important files
4. **Next Steps**:
   - Review the generated content and adjust as needed
   - Use `/cspec/issue-create` to start tracking work
   - Run `cspec validate` to check any existing issues

## Notes

- If the project already has all configuration, this command focuses on populating the PROJECT CONTEXT section in AGENTS.md
- Always preserve existing content - don't overwrite user customizations
- Ask clarifying questions when information is ambiguous
- The goal is to give coding agents enough context to work effectively in this project
