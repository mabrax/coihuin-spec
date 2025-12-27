---
checkpoint: chk-cspec-restructure
created: 2025-12-27T15:45:00-03:00
updated: 2025-12-27
anchor: Project cleanup and restructure session
---

## Problem

The cspec project had accumulated stale artifacts (issues, proposals, journals, checkpoints) and lacked clear separation between permanent and ephemeral work products. The issue template was too heavy, trying to be both issue AND spec.

## Session Intent

Clean the project to a fresh state and establish a proper model where:
- Everything starts from a lightweight **issue** (the trigger)
- Issues spawn **proposals** (high-level approach)
- Proposals lead to **specs** (Gherkin-style testable business rules - PERMANENT)
- Supporting context (snapshots, RCA reports) aids implementation
- Only specs survive; all other artifacts are ephemeral

## Essential Information

### Decisions

1. **Specs are permanent, everything else is ephemeral**
   - Specs = Gherkin-style testable business rules (survive forever)
   - Issues, proposals, context, implementation plans = deleted when work is done

2. **Specs accumulate over time**
   - Features get specs in `cspec/specs/<feature>/spec.md`
   - Enhancements add deltas that merge into existing specs
   - Specs prevent regressions by serving as business rule reference

3. **New directory structure adopted**
   ```
   cspec/
   ├── specs/                    # PERMANENT - Source of truth
   │   └── <feature>/
   │       ├── spec.md           # Gherkin business rules
   │       └── *.mmd             # Diagrams
   └── work/                     # EPHEMERAL - Delete when done
       └── <work-slug>/
           ├── issue.md
           ├── proposal.md
           ├── context/
           └── spec-<feature>.md # Merge into specs/ then delete
   ```

4. **Spec format: Gherkin-style business rules**
   - SHALL statements for requirements
   - Given/When/Then scenarios for behavior
   - ADDED/MODIFIED/REMOVED sections for deltas
   - No implementation details

### Technical Context

- Project: coihuin-spec (spec-driven development methodology + CLI)
- Stack: Python 3.13+, Click, Pydantic, PyYAML
- CLI: `tooling/cspec/` with slash commands for Claude Code
- Issue tracking: beads (`bd` commands) - 8 closed issues, clean slate

### Completed Work

#### 1. docs/methodology.md

Updated with:
- New directory structure (specs/ vs work/)
- Spec format documentation (Gherkin style with example)
- Delta management workflow
- Updated phases and quality gates

#### 2. AGENTS.md

Updated with:
- New file structure diagram
- Permanent vs ephemeral table
- Updated workflow phases with spec format example
- Updated CLI commands reference
- Updated architecture and domain knowledge sections

#### 3. cspec CLI

Refactored:
- `init` creates `cspec/specs/` and `cspec/work/`
- `status` reports specs and work in progress
- New `specs list` and `specs show <feature>` commands
- New `work list` and `work show <slug>` commands
- Removed old issue validation (no longer needed)
- Simplified `onboard` command

New CLI structure:
```
cspec init              # Create cspec/specs/ and cspec/work/
cspec status            # Project health check
cspec specs list        # List permanent specs
cspec specs show <feat> # Show a feature spec
cspec work list         # List work in progress
cspec work show <slug>  # Show work item details
cspec update            # Update slash commands
cspec onboard           # Populate AGENTS.md context
```

### Artifact Trail

| File | Status | Key Change |
|------|--------|------------|
| `docs/methodology.md` | updated | New structure, spec format, phases |
| `AGENTS.md` | updated | CLI commands, structure, workflow |
| `tooling/cspec/src/cspec/cli.py` | refactored | New commands, removed old issue validation |
| `cspec/work/issues/` | deleted | Stale subdirectory |
| `cspec/work/proposals/` | deleted | Stale subdirectory |
| `cspec/work/context/` | deleted | Stale subdirectory |

### Current State

- Project restructured with new permanent/ephemeral model
- Documentation updated (methodology.md, AGENTS.md)
- CLI refactored with new commands
- Ready for first real workflow test

### Next Actions

1. **Test the workflow** - Create first real issue → spec → implementation cycle
2. **Create new slash commands**:
   - `/cspec:work-start <slug> <description>`
   - `/cspec:spec-write <feature>`
   - `/cspec:work-complete`
3. **Move example spec.md** into `cspec/specs/unit-detail-page/spec.md` as template

## User Rules

- Never commit without explicit user approval
- No time estimates in plans
- Use `bd` for issue tracking, not markdown TODOs
