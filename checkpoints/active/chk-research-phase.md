---
checkpoint: chk-research-phase-001
created: 2025-12-17T10:39:20-03:00
anchor: research-phase-proposal-complete
---

## Problem

The spec-driven methodology defines what context is required per issue nature but lacks a formalized workflow for how to gather that context. This gap causes ad-hoc research, inconsistent context quality, and missing information discovered late in development.

## Session Intent

Design and document a formal Research Phase that sits between Issue and Spec phases. The phase should route to appropriate research workflows based on issue nature, run workflows in parallel when independent, and validate research completeness before proceeding.

## Essential Information

### Decisions

- Research is a **formal phase** in the methodology (not embedded in Issue phase)
- Orchestrator will be a **skill** (interactive mode for testing)
- Routing mode is **semi-auto** (propose workflows, human confirms)
- Scope changes trigger **fresh research** (no incremental updates - coding agents make restarts cheap)
- All tools must be **migrated into this project** (self-contained)
- Research outputs are **co-located with issues** (`specs/issues/ISSUE-XXX/research/`)

### Technical Context

- Project: coihuin-spec (spec-driven development methodology + CLI)
- CLI: `cspec` (Python, uv)
- Existing global tools to migrate: `rca-analysis` skill, `snapshot-codebase` command, `web-research` command, `investigate` command
- New tools to build: `research-orchestrator` skill, `profiling-analysis`, `usage-analysis`, `data-analysis`, `api-exploration`

### Play-By-Play

- Catch-up → Created STATUS.md quick reference → Complete
- Brainstorm → Identified Research Phase gap between Issue and Spec → Complete
- Design → Mapped all 11 natures to research workflows → Complete
- Design → Defined orchestration model (6-step flow) → Complete
- Design → Created validation rubric (general + nature-specific) → Complete
- Design → Defined "run fresh" philosophy for scope changes → Complete
- Documentation → Created comprehensive proposal at `docs/research-phase-proposal.md` → Complete

### Artifact Trail

| File | Status | Key Change |
|------|--------|------------|
| `STATUS.md` | created | Quick reference card for project state |
| `docs/research-phase-proposal.md` | created | Full Research Phase proposal with migration plan |

### Current State

- Research Phase fully designed and documented
- Proposal ready for human review
- No implementation started yet
- All beads closed (clean slate)

### Next Actions

1. Human reviews `docs/research-phase-proposal.md`
2. After approval, begin Phase 1 implementation:
   - Migrate existing tools into project
   - Build `research-orchestrator` skill (semi-auto mode)
   - Implement for Bug (RCA) and Enhancement (snapshot) first
   - Test on real issues

## User Rules

- Never commit without explicit user request
- No time estimates in plans
- Use `bd` for issue tracking
