---
id: ISSUE-002
title: "Add cspec show command to display issue details"
nature: feature
impact: additive
version: minor
status: done
created: 2025-12-13
updated: 2025-12-13

context:
  required: []
  recommended: []

depends_on: []
blocks: []
---

## Problem

There's no way to view the details of a specific issue from the CLI. Users must either:
- Read the file directly (`cat specs/issues/ISSUE-001.md`)
- Use `cspec validate` which shows some info as a side effect

A `cspec show <issue-id>` command would provide a clean, formatted view of issue details, improving the developer experience and making the CLI more complete.

## Scope

### In Scope

- [ ] Add `cspec show <issue-id>` command
- [ ] Display formatted issue details (frontmatter + body sections)
- [ ] Support both `ISSUE-001` and `001` as valid input formats
- [ ] Show dependencies (depends_on, blocks) if present

### Out of Scope

- Interactive editing of issues
- Filtering or searching within show output
- Export to other formats (JSON, etc.)

## Acceptance Criteria

- [ ] `cspec show ISSUE-001` displays the issue details
- [ ] `cspec show 001` also works (auto-prefix)
- [ ] Output is well-formatted and readable in terminal
- [ ] Shows: id, title, nature, impact, version, status, dates, problem, scope, acceptance criteria
- [ ] Shows dependencies if any exist
- [ ] Returns error with helpful message if issue not found

## Notes

This completes the basic CRUD-like CLI experience: `list` shows all, `show` shows one, `validate` checks one. Creation is handled by the `/cspec:issue-create` slash command (LLM-assisted).
