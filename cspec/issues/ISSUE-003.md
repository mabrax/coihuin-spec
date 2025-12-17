---
id: ISSUE-003
title: "Show valid status values in cspec list --status help"
nature: enhancement
impact: invisible
version: patch
status: done
created: 2025-12-13
updated: 2025-12-13

context:
  required:
    - type: current-behavior
      path: tooling/cspec/src/cspec/cli.py
  recommended: []

depends_on: []
blocks: []
---

## Problem

Users running `cspec list --status` cannot discover valid status values. The help output shows:

```
--status TEXT  Filter by status
```

But doesn't indicate what values are valid (draft, ready, in-progress, blocked, done). Users must either:
- Read the documentation
- Read the source code
- Guess and fail

This creates unnecessary friction in a common workflow.

## Scope

### In Scope

- [ ] Update `--status` option to use `click.Choice` with valid status values
- [ ] Ensure `--help` displays the valid choices
- [ ] Invalid status values produce helpful error message listing valid options

### Out of Scope

- Adding new status values
- Tab completion (shell-specific, separate concern)
- Changes to other commands

## Acceptance Criteria

- [ ] `cspec list --help` shows valid status values in the --status option description
- [ ] `cspec list --status=invalid` returns error message listing valid values
- [ ] `cspec list --status=draft` continues to work as before
- [ ] All existing status values supported: draft, ready, in-progress, blocked, done

## Notes

Valid status values per issue-template.md: `draft | ready | in-progress | blocked | done`

The fix involves changing the Click option from `click.option('--status', '-s')` to use `click.Choice(['draft', 'ready', 'in-progress', 'blocked', 'done'])`.
