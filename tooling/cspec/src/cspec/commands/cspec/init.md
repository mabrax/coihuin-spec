---
description: Initialize a spec-driven project with project definition and constitution
argument-hint: [project name]
---

# Project Initialization

You are initializing a new spec-driven development project.

## User Input

$ARGUMENTS

## Process

### Step 1: Gather Project Information

Ask the user for:

1. **Project Name**: Short identifier
2. **Description**: What is this project? (1-2 sentences)
3. **Purpose**: Why does it exist? What problem does it solve?
4. **Scope**: What's in and out of bounds for this project?
5. **Key Stakeholders**: Who uses or depends on this?

### Step 2: Create Directory Structure

Create the following structure:

```
specs/
├── PROJECT.yaml      # Project definition
├── CONSTITUTION.md   # Rules and philosophy
└── issues/           # Issue files go here
```

### Step 3: Create PROJECT.yaml

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

stakeholders:
  - "<stakeholder 1>"

methodology: spec-driven
version: 0.1.0
```

### Step 4: Create CONSTITUTION.md

```markdown
# Constitution

## Philosophy

This project follows **spec-driven development**:

1. **Issue first**: Every change starts with an issue (the "what and why")
2. **Spec before code**: Specs define the "how" before implementation
3. **Source of truth**: Specs are authoritative; code implements specs
4. **Validate against spec**: Implementation correctness = spec compliance
5. **Clean exit**: Delete transient artifacts; keep persistent ones updated

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

### Artifacts

| Type | Lifecycle |
|------|-----------|
| Wireframes, task breakdowns, design explorations | Transient (delete when done) |
| API contracts, schemas, business rules, ADRs | Persistent (source of truth) |

## Versioning

- **Breaking** changes → Major version
- **Additive** changes → Minor version
- **Invisible** changes → Patch version
```

### Step 5: Update tooling/USAGE.md

Add the init command as the first step.

### Step 6: Confirm Initialization

Output:
- Created files and their locations
- Remind user that `/issue-create` is the next step when ready to start work
