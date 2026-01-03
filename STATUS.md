# Coihuin Spec - Quick Reference

**Last Updated**: 2025-12-30

## What Is This

Spec-driven development methodology + CLI (`cspec`) for human-agent collaboration. Structured specs as context engineering to reduce iteration cycles.

Flow: `Issue → Proposal → Spec → Implementation → Verification`

## Current State

All work complete. Clean slate. Ready for next feature or real-world testing.

## CLI Commands

```
cspec init             # Initialize spec-driven dev
cspec status           # Check project health
cspec update           # Update to latest templates
cspec onboard          # Onboard to a project
cspec specs list       # List permanent specs
cspec specs show       # View a spec
cspec work list        # List work in progress
cspec work show        # View work item details
cspec templates list   # List issue templates
cspec templates get    # Get a fillable template
```

## Slash Commands

```
/cspec:issue-create    # Create new issue
/cspec:issue-start     # Start from GitHub issue
/cspec:proposal-write  # Write proposal
/cspec:spec-write      # Write Gherkin spec
/cspec:plan-write      # Write implementation plan
/cspec:work-complete   # Complete and clean up
```

## Key Docs

- `README.md` - Full overview
- `AGENTS.md` - Agent workflow reference
- `docs/methodology.md` - Development flow
- `docs/change-taxonomy-system.md` - Issue classification
