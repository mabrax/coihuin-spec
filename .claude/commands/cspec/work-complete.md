---
description: Complete work, merge spec, clean ephemeral files
argument-hint: [work-slug or leave empty to auto-detect]
---

# Complete Work

You are completing a work item. This means:
1. Merging the spec into the permanent specs directory
2. Closing the GitHub issue
3. Deleting the ephemeral work directory

## Target Work Item

$ARGUMENTS

If no argument, auto-detect current work item.

## Process

### Step 1: Verify Completion

Check that the work is actually done:

```
cspec/work/<slug>/
├── issue.md       ← Has GitHub reference?
├── proposal.md    ← Status: approved?
├── spec-*.md      ← Exists and reviewed?
├── plan.md        ← All tasks checked?
└── context/       ← Can be deleted?
```

Ask user to confirm:
- [ ] Implementation complete
- [ ] Tests passing
- [ ] Code reviewed/merged

If not complete, stop and guide to finish remaining work.

### Step 2: Load the Spec

Read `cspec/work/<slug>/spec-<feature>.md`

Determine:
- Feature name (for destination path)
- Is this new spec or delta?

### Step 3: Merge Spec

#### If NEW spec:

Create the permanent spec:

```bash
mkdir -p cspec/specs/<feature>/
cp cspec/work/<slug>/spec-<feature>.md cspec/specs/<feature>/spec.md
```

#### If DELTA spec:

Merge into existing spec:

1. Read existing `cspec/specs/<feature>/spec.md`
2. Read delta `cspec/work/<slug>/spec-<feature>.md`
3. Apply changes:
   - **ADDED**: Append new requirements and scenarios
   - **MODIFIED**: Replace old with new
   - **REMOVED**: Delete (with comment noting removal)
4. Update the spec header with modification date
5. Write merged spec back

Present the merged spec for user review before saving.

### Step 4: Close GitHub Issue

Get the issue number from `issue.md` frontmatter.

Close with comment:

```bash
gh issue close <number> --comment "Completed. Spec merged to cspec/specs/<feature>/spec.md"
```

### Step 5: Clean Ephemeral Files

Delete the work directory:

```bash
rm -rf cspec/work/<slug>/
```

Confirm with user before deleting:
- Show what will be deleted
- Offer to keep context/ if valuable
- Proceed only with explicit approval

### Step 6: Verify Final State

Check:
- [ ] Spec exists at `cspec/specs/<feature>/spec.md`
- [ ] GitHub issue is closed
- [ ] Work directory is deleted
- [ ] No orphaned files

### Step 7: Report Completion

Output:
- Work item completed: <slug>
- Spec location: `cspec/specs/<feature>/spec.md`
- GitHub issue: #<number> (closed)
- Files cleaned: <count>

Summary:
```
✓ Spec merged to cspec/specs/<feature>/spec.md
✓ GitHub issue #<number> closed
✓ Work directory deleted
```

## Handling Edge Cases

### Incomplete Work

If work isn't done:
- List remaining tasks
- Guide to complete them
- Don't proceed with cleanup

### No Spec Written

If there's no `spec-*.md`:
- Some issues don't need specs (small bug, config)
- Confirm with user this is intentional
- Proceed to close issue and cleanup

### Delta Merge Conflicts

If merging delta creates conflicts:
- Show both versions
- Let user resolve
- Write resolved version

### Keep Context

If user wants to keep context:
- Move `context/` to `cspec/specs/<feature>/context/`
- Or copy specific files elsewhere
- Then delete work directory

## Notes

- This is the FINAL step - ephemeral files are deleted permanently
- Always confirm before deleting
- Specs are the only survivors - make sure they're correct
- If anything goes wrong, work directory is still there until explicitly deleted
