---
description: Import a GitHub issue and start work
argument-hint: <github-issue-url or issue-number>
---

# Start Work on GitHub Issue

You are importing a GitHub issue to begin the cspec workflow. This creates a local work directory with the issue content and prepares for proposal/spec writing.

## Target Issue

$ARGUMENTS

## Process

### Step 1: Parse the Issue Reference

Accept either:
- Full URL: `https://github.com/owner/repo/issues/42`
- Issue number: `42` or `#42`

If just a number, use the current repo (detected via `gh repo view --json nameWithOwner`).

### Step 2: Fetch Issue from GitHub

```bash
gh issue view <number> --json number,title,body,labels,state
```

Extract:
- **Number**: For work directory naming
- **Title**: For reference
- **Body**: The full issue content
- **Labels**: To determine nature (feature, bug, etc.)
- **State**: Should be "open" (warn if closed)

### Step 3: Determine Nature from Labels

Map GitHub labels to cspec nature:
- `feature` → feature
- `enhancement` → enhancement
- `bug` → bug
- `refactor` → refactor
- `optimization` → optimization
- `security` → security
- `hotfix` → hotfix
- `migration` → migration
- `configuration` → configuration
- `deprecation` → deprecation
- `removal` → removal

If no nature label found, ask the user to classify.

### Step 4: Create Work Directory

Create the work directory structure:

```
cspec/work/<number>-<slug>/
├── issue.md          ← Issue content from GitHub
├── proposal.md       ← Empty, for next step
└── context/          ← For supporting documents
```

Where `<slug>` is derived from the title (lowercase, hyphens, max 30 chars).

Example: Issue #42 "Add CSV export for reports" → `cspec/work/42-add-csv-export/`

### Step 5: Write issue.md

Format the GitHub issue content as markdown:

```markdown
---
github: <issue-url>
number: <number>
nature: <nature>
title: "<title>"
imported: <today YYYY-MM-DD>
---

# <title>

<body content from GitHub>
```

### Step 6: Create Empty proposal.md

```markdown
---
issue: <number>
status: draft
---

# Proposal: <title>

## Approach

<!-- High-level approach to solving this issue -->

## Key Decisions

<!-- Important decisions and trade-offs -->

## Risks

<!-- Potential risks and mitigations -->

## Out of Scope

<!-- What this proposal explicitly does NOT cover -->
```

### Step 7: Create context/ Directory

```bash
mkdir -p cspec/work/<slug>/context
```

This is where supporting documents go:
- `snapshot-*.md` - Codebase snapshots
- `rca-*.md` - Root cause analysis (for bugs)
- `research-*.md` - Technical research

### Step 8: Report Success

Output:
- Work directory path created
- Issue summary (number, title, nature)
- Files created
- Next step: `/cspec:proposal-write` to draft the proposal

## Notes

- If work directory already exists, warn and ask to overwrite or resume
- If `gh` is not authenticated, guide user to `gh auth login`
- If issue is closed, warn but allow proceeding (user might be resuming)
- Update the GitHub issue with a comment noting work has started (optional, ask user)
