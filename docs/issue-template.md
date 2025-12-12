# Issue Template

Use this template when creating new issues. The YAML frontmatter enables machine parsing; the markdown body provides human-readable context.

---

## Template

```markdown
---
id: ISSUE-XXX
title: ""
nature: ""        # feature | enhancement | bug | refactor | optimization | security | hotfix | migration | configuration | deprecation | removal
impact: ""        # breaking | additive | invisible
version: ""       # major | minor | patch (derived from impact)
status: draft     # draft | ready | in-progress | blocked | done
created: YYYY-MM-DD
updated: YYYY-MM-DD

# Context references (paths relative to project root)
context:
  required: []
  recommended: []

# Dependencies
depends_on: []    # Other issue IDs that must complete first
blocks: []        # Issue IDs this blocks
---

## Problem

What is the problem or opportunity? Why does this matter?

## Scope

### In Scope

- [ ] Specific deliverable 1
- [ ] Specific deliverable 2

### Out of Scope

- Explicitly excluded item 1
- Explicitly excluded item 2

## Acceptance Criteria

How do we know this is done?

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Notes

Additional context, constraints, or considerations.
```

---

## Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Unique identifier (e.g., ISSUE-001) |
| `title` | string | Yes | Brief, descriptive title |
| `nature` | enum | Yes | Type of change (see taxonomy) |
| `impact` | enum | Yes | Consumer impact level |
| `version` | enum | Yes | Semantic version increment |
| `status` | enum | Yes | Current issue state |
| `created` | date | Yes | Creation date |
| `updated` | date | Yes | Last modification date |
| `context.required` | array | Conditional | Required references (varies by nature) |
| `context.recommended` | array | No | Optional supporting references |
| `depends_on` | array | No | Blocking dependencies |
| `blocks` | array | No | Issues this blocks |

---

## Example: Bug Issue

```markdown
---
id: ISSUE-042
title: "Authentication token expires during long uploads"
nature: bug
impact: invisible
version: patch
status: ready
created: 2025-01-15
updated: 2025-01-16

context:
  required:
    - type: rca
      path: docs/rca/ISSUE-042-rca.md
  recommended:
    - type: logs
      path: docs/evidence/ISSUE-042-logs.txt

depends_on: []
blocks: []
---

## Problem

Users uploading large files (>500MB) experience authentication failures mid-upload. The token expires before the upload completes, causing data loss and user frustration.

## Scope

### In Scope

- [ ] Extend token validity during active uploads
- [ ] Add token refresh mechanism for long-running operations

### Out of Scope

- General token refresh architecture overhaul
- Upload chunking implementation

## Acceptance Criteria

- [ ] Uploads >500MB complete without auth errors
- [ ] Token refresh occurs transparently during upload
- [ ] No regression in normal authentication flow
- [ ] Covered by automated test

## Notes

See RCA document for root cause analysis and proposed fix approach.
```

---

## Example: Feature Issue

```markdown
---
id: ISSUE-043
title: "Add export to CSV functionality"
nature: feature
impact: additive
version: minor
status: draft
created: 2025-01-15
updated: 2025-01-15

context:
  required:
    - type: problem-statement
      path: docs/problems/ISSUE-043-export-need.md
  recommended:
    - type: user-research
      path: docs/research/export-user-interviews.md
    - type: competitive-analysis
      path: docs/research/competitor-export-features.md

depends_on: []
blocks:
  - ISSUE-044  # Export to Excel depends on this
---

## Problem

Users need to export their data for use in spreadsheet applications. Currently, there's no way to get data out of the system in a portable format.

## Scope

### In Scope

- [ ] CSV export for user data table
- [ ] Column selection UI
- [ ] Date range filtering for export

### Out of Scope

- Excel format export (separate issue)
- Scheduled/automated exports
- Export API endpoint

## Acceptance Criteria

- [ ] User can export visible data to CSV
- [ ] Exported CSV opens correctly in Excel and Google Sheets
- [ ] Large exports (>10k rows) complete within 30 seconds
- [ ] Export includes headers matching column names

## Notes

This is the foundation for future export formats. Keep the architecture extensible.
```
