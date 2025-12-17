---
checkpoint: chk-research-phase
created: 2025-12-17T12:42:11-03:00
anchor: issue-004-complete
---

## Problem

The cspec methodology defines **what context is required** per issue nature (in `issue-validation.md`), but lacks a formalized workflow for **how to gather that context**. This leads to ad-hoc research approaches, inconsistent context quality, and missing information discovered late in spec/implementation.

## Session Intent

Implement the Research Phase as defined in `docs/proposals/research-phase-proposal.md`. The Research Phase sits between Issue (validated) and Spec, providing the contextual foundation needed to design solutions:

```
Issue (validated) → Research → Spec → Implementation → Verification
```

## Essential Information

### Decisions

- **Multiple issues**: Work split into 6 separate issues for better tracking
- **Impact**: All issues are `additive` (new features, no breaking changes)
- **Version**: All issues are `minor` version increments
- **Execution mode**: Semi-auto (propose workflows, human confirms) for alpha
- **Self-contained**: All tools must live in project's `.claude/` directory
- **Testing**: Accept structural validation without formal smoke tests (ISSUE-004)

### Technical Context

- Project: coihuin-spec (spec-driven development methodology)
- CLI tool: `cspec` (Python, in `tooling/cspec/`)
- Issue tracking: beads (`bd` commands) + cspec issues
- Slash commands: `.claude/commands/`
- Skills: `.claude/skills/`
- Agents: `.claude/agents/`
- Agent configs: Project CLAUDE.md + AGENTS.md

### Play-By-Play

- Read proposal → Understood scope and requirements
- Created 6 issues → ISSUE-004 through ISSUE-009
- Created dependency graph → `cspec/issues/DEPENDENCY-GRAPH.md`
- Validated ISSUE-004 → Passed with warnings, updated to `ready`
- **Implemented ISSUE-004** → Migrated 3 tools (rca-analysis, web-research, snapshot-researcher)
- Junior implementer missed snapshot-researcher agent → Fixed manually
- Fixed web-research.md issues → Added agent invocation, date command, output clarity
- Multi-agent review → Completeness, correctness, acceptance criteria, documentation all passed

### Artifact Trail

| File | Status | Key Change |
|------|--------|------------|
| `docs/proposals/research-phase-proposal.md` | exists | Source proposal defining Research Phase |
| `cspec/issues/ISSUE-004/ISSUE-004.md` | created | Migrate existing tools (ready) |
| `cspec/issues/ISSUE-005/ISSUE-005.md` | created | Build research-orchestrator skill (draft) |
| `cspec/issues/ISSUE-006/ISSUE-006.md` | created | Build snapshot commands (draft) |
| `cspec/issues/ISSUE-007/ISSUE-007.md` | created | Build analysis commands (draft) |
| `cspec/issues/ISSUE-008/ISSUE-008.md` | created | Build research-validate command (draft) |
| `cspec/issues/ISSUE-009/ISSUE-009.md` | created | Update documentation (draft) |
| `cspec/issues/DEPENDENCY-GRAPH.md` | created | Mermaid diagram of issue dependencies |
| `.claude/skills/rca-analysis/` | **created** | RCA skill (SKILL.md + references/) |
| `.claude/commands/web-research.md` | **created** | External research command |
| `.claude/agents/snapshot-researcher.md` | **created** | Codebase exploration agent |
| `docs/MIGRATION-NOTES.md` | **created** | Migration documentation |

### Current State

**ISSUE-004 complete** (pending commit). 5 issues remaining:

| Issue | Title | Status | Depends On |
|-------|-------|--------|------------|
| ISSUE-004 | Migrate existing research tools | **complete** | — |
| ISSUE-005 | Build research-orchestrator skill | draft | 004, 006, 007 |
| ISSUE-006 | Build snapshot research commands | draft | 004 ✓ |
| ISSUE-007 | Build analysis research commands | draft | — |
| ISSUE-008 | Build /cspec:research-validate command | draft | 005 |
| ISSUE-009 | Update documentation for Research Phase | draft | 004-008 |

**Dependency graph** (004 unblocked):
```
ISSUE-004 ✓─┬──> ISSUE-006 ──┐
            │                ├──> ISSUE-005 ──> ISSUE-008
ISSUE-007 ──┴────────────────┘                     │
                                                   v
                                            ISSUE-009
```

### Next Actions

1. **Commit ISSUE-004 changes** (awaiting user approval)
2. **Begin ISSUE-007** (analysis commands) - no blockers, parallel track
3. **Begin ISSUE-006** (snapshot commands) - 004 now unblocked
4. Validate remaining issues (005-009) to `ready` status

## User Rules

- NEVER commit changes without user approval
- NEVER include time estimations in plans
- Use `bd` commands for tracking (beads workflow)
- Run `TZ='America/Santiago' date` for date-related tasks
