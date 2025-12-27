---
description: Create a GitHub issue using cspec templates
argument-hint: [optional: brief description of what you want to create]
---

# Create GitHub Issue

You are creating a GitHub issue using the cspec methodology. The issue will be created on GitHub for tracking, but you'll collect all information here in the TUI.

## User Input (if provided)

$ARGUMENTS

## Process

### Step 1: Determine Nature

Ask the user which type of issue they're creating:

| Nature | Description |
|--------|-------------|
| `feature` | New functionality that doesn't exist |
| `enhancement` | Improve existing functionality |
| `bug` | Something is broken |
| `refactor` | Restructure code, no behavior change |
| `optimization` | Improve performance/resources |
| `security` | Vulnerability or hardening |
| `hotfix` | Urgent production fix |
| `migration` | Data or system migration |
| `configuration` | Settings/config change |
| `deprecation` | Mark for future removal |
| `removal` | Remove deprecated functionality |

### Step 2: Collect Fields Based on Nature

Each nature has specific required fields. Collect them conversationally.

#### For `feature`:
- **Impact**: breaking / additive (dropdown becomes conversation)
- **Problem**: What problem does this solve?
- **In Scope**: Specific deliverables (checklist)
- **Out of Scope**: Explicitly excluded (optional)
- **Acceptance Criteria**: How do we know it's done?

#### For `enhancement`:
- **Impact**: invisible / additive / breaking
- **Current Behavior**: How does it work now?
- **Desired Behavior**: How should it work?
- **In Scope**: Specific changes
- **Acceptance Criteria**: How do we know it's done?

#### For `bug`:
- **Severity**: critical / high / medium / low
- **Current Behavior**: What's happening?
- **Expected Behavior**: What should happen?
- **Steps to Reproduce**: How to replicate
- **Environment**: OS, version, browser (optional)
- **Acceptance Criteria**: How do we know it's fixed?

#### For `refactor`:
- **Impact**: invisible / additive / breaking
- **Current State**: What's wrong with current code?
- **Target State**: What should it look like after?
- **In Scope**: Specific changes
- **Acceptance Criteria**: Tests pass, no behavior change

#### For `optimization`:
- **Impact**: invisible / additive / breaking
- **Type**: performance / memory / storage / network / cost
- **Current Metrics**: What are current measurements?
- **Target Metrics**: What should they be after?
- **Approach**: How will we achieve this?
- **Acceptance Criteria**: Metrics met, no regression

#### For `security`:
- **Severity**: critical / high / medium / low
- **Type**: vulnerability / hardening / compliance / dependency
- **Description**: What's the security issue?
- **Potential Impact**: What could happen if exploited?
- **Remediation**: How to fix?
- **Acceptance Criteria**: Vulnerability closed, test added

#### For `hotfix`:
- **Severity**: P0 / P1 / P2
- **Incident**: What's happening in production?
- **Root Cause**: If known
- **Proposed Fix**: How to fix?
- **Rollback Plan**: How to rollback if fix fails?
- **Acceptance Criteria**: Incident resolved, monitoring normal

#### For `migration`:
- **Type**: data / infrastructure / dependency / platform
- **Impact**: invisible / additive / breaking
- **From/To**: What are we migrating from and to?
- **Scope**: What's included?
- **Rollback Plan**: How to rollback?
- **Validation Plan**: How to verify success?
- **Acceptance Criteria**: Data migrated, no loss

#### For `configuration`:
- **Environment**: all / production / staging / development
- **Impact**: invisible / additive / breaking
- **Change**: What setting, current value, new value
- **Reason**: Why is this needed?
- **Rollback Plan**: How to revert?
- **Acceptance Criteria**: Config applied, system stable

#### For `deprecation`:
- **What**: What's being deprecated?
- **Reason**: Why deprecate?
- **Migration Path**: How should consumers migrate?
- **Timeline**: When warning, when removal?
- **Scope**: What needs to be done?
- **Acceptance Criteria**: Warnings in place, docs updated

#### For `removal`:
- **What**: What's being removed?
- **Deprecation Reference**: Link to deprecation issue
- **Impact Assessment**: Who's affected?
- **Scope**: What to remove?
- **Verification**: How to verify nothing depends on it?
- **Acceptance Criteria**: Removed, no references remain

### Step 3: Generate Title

Based on the collected information, suggest a concise title (max 100 chars).
Format: `<nature>: <brief description>`

Example: `feature: Add CSV export for reports`

### Step 4: Format Issue Body

Format the collected fields as markdown matching the GitHub template structure.

### Step 5: Create on GitHub

Use `gh issue create` to create the issue:

```bash
gh issue create \
  --title "<title>" \
  --label "<nature>" \
  --body "$(cat <<'EOF'
<formatted body>
EOF
)"
```

Add additional labels based on:
- `breaking-change` if impact is breaking
- `urgent` if hotfix
- Severity label for bugs/security (e.g., `severity:critical`)

### Step 6: Report Success

Output:
- The GitHub issue URL
- Issue number
- Summary of what was created
- Next step: `/cspec:issue-start <url>` to begin work

## Notes

- If `gh` is not authenticated, guide the user to run `gh auth login`
- If no repo is detected, ask user to confirm they're in a git repo with a GitHub remote
- Keep the conversation natural - don't dump all questions at once
- Use the user's initial input ($ARGUMENTS) to pre-fill fields if possible
