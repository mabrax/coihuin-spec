# Eval & Archive Proposal

**Status**: Draft
**Created**: 2024-12-17
**Author**: Human + Agent collaboration

---

## Overview

This proposal defines two complementary features for the cspec workflow:

1. **Eval System** - Capture learnings from completed issues to improve the methodology
2. **Archive System** - Move completed issues out of active workspace

Both support the dogfooding philosophy: learn from real usage, refine through experience.

---

## Eval System

### Purpose

Capture human observations + LLM analysis after completing an issue. Used to:
- Identify methodology gaps
- Tune workflow mappings
- Track what works/fails across real projects

### Invocation

```bash
/cspec:eval ISSUE-001
```

### Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                      /cspec:eval ISSUE-001                       │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 1. LOAD CONTEXT                                            │  │
│  │    - Issue file + artifacts (research/, spec/)             │  │
│  │    - Git diff of uncommitted changes                       │  │
│  │    - Spawn explore agent to map what changed               │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 2. LLM ANALYSIS                                            │  │
│  │    - Analyze diffs → form observations                     │  │
│  │    - Identify gaps between research and actual changes     │  │
│  │    - Note unexpected modifications                         │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 3. HUMAN QUESTIONS                                         │  │
│  │    - Ask fixed dimension questions (see rubric below)      │  │
│  │    - Human answers based on lived experience               │  │
│  │    - Capture qualitative observations                      │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 4. SYNTHESIS                                               │  │
│  │    - Correlate: human answers ↔ code changes               │  │
│  │    - Reason about discrepancies                            │  │
│  │    - Generate scores + narrative                           │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 5. OUTPUT                                                  │  │
│  │    - Write to cspec/evals/ISSUE-001-eval.md                │  │
│  │    - Human reviews before finalizing                       │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Eval Dimensions

| Dimension | Question | Scale |
|-----------|----------|-------|
| **Research Quality** | Did research provide enough context? What was missing? | 1-5 |
| **Spec Accuracy** | Did spec predict implementation needs? Surprises? | 1-5 |
| **Validation Effectiveness** | Did validation catch real issues? False positives? | 1-5 |
| **Workflow Friction** | Where did the process slow you down? | 1-5 |
| **Tool Gaps** | What tooling was missing or broken? | 1-5 |
| **Scope Stability** | Did scope change? How was it handled? | 1-5 |

### Output Format

Hybrid: YAML frontmatter (structured, parseable) + Markdown body (human readable).

```markdown
---
issue: ISSUE-001
date: 2024-12-17
nature: feature
git_commit: abc123
scores:
  research_quality: 3
  spec_accuracy: 4
  validation_effectiveness: 2
  workflow_friction: 3
  tool_gaps: 2
  scope_stability: 5
---

# Eval: ISSUE-001

## Summary
<!-- 1-2 paragraph synthesis of the eval -->

## Research Quality (3/5)

**Human**: "Missing integration point with auth module, discovered during implementation."

**LLM**: Found 3 files touching auth (`src/auth/*.ts`), not mentioned in research artifacts.

**Correlation**: Human observation confirmed by code analysis. Research workflow did not explore auth layer.

## Spec Accuracy (4/5)

**Human**: "Spec was mostly accurate, one edge case missed."

**LLM**: Spec mentioned 4 components, implementation touched 5. Extra component was error handler.

**Correlation**: Minor gap. Error handling often emerges during implementation.

<!-- ... remaining dimensions ... -->

## Recommendations

- Add auth layer to `snapshot-integration-points` checklist
- Consider error handling as standard spec section
```

### Output Location

```
cspec/evals/
├── ISSUE-001-eval.md
├── ISSUE-002-eval.md
└── _summary.md          # (future) Aggregated learnings
```

---

## Archive System

### Purpose

Move completed issues out of active workspace while preserving history for evaluation.

### Commands

| Command | Type | What it does |
|---------|------|--------------|
| `cspec archive --list` | CLI | Lists archived issues (deterministic) |
| `/cspec:archive ISSUE-001` | Slash Cmd | Sanity checks then archives |

### `/cspec:archive` Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    /cspec:archive ISSUE-001                      │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 1. SANITY CHECKS                                           │  │
│  │    - Issue exists?                                         │  │
│  │    - Status is complete/closed?                            │  │
│  │    - No uncommitted changes related to issue?              │  │
│  │    - Eval exists? (warn if missing)                        │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 2. CONFIRM                                                 │  │
│  │    - Show what will be archived                            │  │
│  │    - Human confirms                                        │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 3. ARCHIVE                                                 │  │
│  │    - Move issue folder to cspec/issues/_archive/           │  │
│  │    - Report success                                        │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### `cspec archive --list` Output

```
Archived Issues:
  ISSUE-001  feature   Research Phase Proposal        2024-12-15
  ISSUE-002  bug       Fix validation edge case       2024-12-16
  ISSUE-003  feature   Add snapshot workflows         2024-12-17
```

### Directory Structure

```
cspec/issues/
├── ISSUE-004/           # Active
├── ISSUE-005/           # Active
└── _archive/
    ├── ISSUE-001/       # Completed
    ├── ISSUE-002/       # Completed
    └── ISSUE-003/       # Completed
```

---

## Implementation Roadmap

- [ ] Create `cspec/evals/` directory
- [ ] Build `/cspec:eval` slash command
- [ ] Build `/cspec:archive` slash command
- [ ] Add `cspec archive --list` to CLI

---

## Integration with Workflow

Recommended flow after completing an issue:

```
Implementation done
        │
        ▼
  /cspec:eval ISSUE-001     ← Capture learnings
        │
        ▼
  Review eval, edit if needed
        │
        ▼
  /cspec:archive ISSUE-001  ← Move to archive
        │
        ▼
  Continue to next issue
```
