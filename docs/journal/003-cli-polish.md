# CLI Polish: The Little Things

*Continuing the journal of building a spec-driven development framework*

---

## The Issue

ISSUE-003: Show valid status values in cspec list --status help

A small thing. Users running `cspec list --status` couldn't discover what values were valid. The help showed:

```
--status TEXT  Filter by status
```

But what are the valid values? `draft`? `open`? `pending`? Users had to read documentation or source code to find out.

---

## The Fix

Two changes:

### 1. Click.Choice for Validation

```python
# Before
@click.option("--status", "-s", type=str, help="Filter by status")

# After
@click.option(
    "--status",
    "-s",
    type=click.Choice(["draft", "ready", "in-progress", "blocked", "done"], case_sensitive=False),
    help="Filter by status",
)
```

Now `cspec list --help` shows:

```
-s, --status [draft|ready|in-progress|blocked|done]
                                Filter by status
```

And invalid values produce helpful errors:

```
Error: Invalid value for '--status' / '-s': 'invalid' is not one of 'draft', 'ready', 'in-progress', 'blocked', 'done'.
```

### 2. Output Hint

When listing without a filter, show users their options:

```
Found 3 issue(s):

  ISSUE-001 [done] (removal)
    Remove /cspec:init slash command
  ...

Filter by status: --status=draft|ready|in-progress|blocked|done
```

The hint disappears when a filter is applied - you already know the options if you're using them.

---

## Why This Matters

CLI tools live or die by discoverability. Every time a user has to leave the terminal to read docs, that's friction. Every time they have to guess and fail, that's frustration.

Good CLIs teach you how to use them. `--help` should be sufficient. Error messages should guide you forward.

This was a 10-line change. But it removes a paper cut that would annoy users forever.

---

## The Spec-Driven Approach

This fix followed the spec workflow:

1. **Issue created** (ISSUE-003) with clear problem statement
2. **Scope defined** - just the `--status` option, not other commands
3. **Acceptance criteria** - testable conditions
4. **Implementation** - straightforward once the spec was clear
5. **Validation** - all criteria met

Even for small changes, the structure helps. The issue forced us to think about scope ("not tab completion - that's shell-specific") and acceptance criteria before touching code.

---

## Current State

All three initial issues are now done:

| ID | Status | Title |
|----|--------|-------|
| ISSUE-001 | done | Remove /cspec:init slash command |
| ISSUE-002 | done | Add cspec show command |
| ISSUE-003 | done | Show valid status values in --status help |

The CLI is clean:
- `cspec init` - Create structure
- `cspec onboard` - Populate context
- `cspec status` - Health check
- `cspec list` - Browse issues (with hints!)
- `cspec show` - Issue details
- `cspec validate` - Schema validation
- `cspec update` - Refresh resources

---

*Written while polishing the cspec CLI, December 2025*
