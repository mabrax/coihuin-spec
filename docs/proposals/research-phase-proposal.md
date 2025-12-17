# Research Phase Proposal

**Status**: Draft
**Created**: 2024-12-17
**Author**: Human + Agent collaboration

---

## Overview

This proposal defines a formal **Research Phase** in the spec-driven development methodology. The Research Phase sits between Issue (validated) and Spec, providing the contextual foundation needed to design solutions.

```
Issue (validated) → Research → Spec → Implementation → Verification
```

### Problem Statement

The current methodology defines **what context is required** per issue nature (in `issue-validation.md`), but lacks a formalized workflow for **how to gather that context**. This gap leads to:

- Ad-hoc research approaches
- Inconsistent context quality
- Missing information discovered late in spec/implementation
- No validation that research is "enough" before proceeding

### Solution

Introduce a formal Research Phase with:

1. **Nature-based routing** - Each issue nature maps to specific research workflow(s)
2. **Parallel execution** - Independent workflows run concurrently
3. **Orchestration** - A skill coordinates dispatch, collection, and merging
4. **Validation** - Rubric-based smell detection + human review
5. **Self-contained tooling** - All research tools live in this project

---

## Research Workflow Mapping

Each issue nature determines which research workflow(s) to execute.

### Primary Mapping

These mappings are **starting heuristics**, not rigid rules. Humans may override during the Propose step, and overrides are tracked to tune mappings over time.

| Nature | Primary Workflow | Secondary Workflow | Parallel? |
|--------|------------------|-------------------|-----------|
| **Bug** | `rca-analysis` | — | N/A |
| **Hotfix** | `rca-analysis` (fast mode) | — | N/A |
| **Feature** | `snapshot-integration-points` | `web-research` (patterns/prior art) | Yes |
| **Enhancement** | `snapshot-current-behavior` | — | N/A |
| **Refactor** | `snapshot-architecture` | `dependency-analysis` | Yes |
| **Optimization** | `snapshot-hot-paths` | `profiling-analysis` | Yes |
| **Security** | `rca-analysis` (attack-focused) | `web-research` (CVE/mitigation) | Yes |
| **Migration** | `snapshot-current-state` | `web-research` (target tech), `dependency-analysis` | Yes |
| **Configuration** | `snapshot-config-layer` | — | N/A |
| **Deprecation** | `usage-analysis` | — | N/A |
| **Removal** | Reference deprecation research | — | N/A |

### All Workflows

| Workflow | Type | Status | Purpose |
|----------|------|--------|---------|
| `rca-analysis` | Skill | Migrate | Root cause analysis for bugs/security issues |
| `web-research` | Command | Migrate | External documentation and patterns |
| `snapshot-researcher` | Agent | Migrate | Sub-agent for parallel codebase exploration |
| `snapshot-integration-points` | Command | Build | Map where new code connects to existing system |
| `snapshot-current-behavior` | Command | Build | Document existing behavior before modification |
| `snapshot-architecture` | Command | Build | Map system structure, components, boundaries |
| `snapshot-hot-paths` | Command | Build | Identify performance-critical code paths |
| `snapshot-config-layer` | Command | Build | Document configuration system and options |
| `snapshot-current-state` | Command | Build | Full state documentation for migration source |
| `profiling-analysis` | Command | Build | Collect/analyze performance metrics |
| `usage-analysis` | Command | Build | Find all consumers of a symbol, API, or feature |
| `dependency-analysis` | Command | Build | Map code and package dependency graphs |
| `research-orchestrator` | Skill | Build | Coordinates entire research phase |
| `/cspec:research-validate` | Slash Cmd | Build | Manual validation rubric check (alpha) |

---

## Orchestration Model

The Research Orchestrator coordinates the entire research phase.

```
┌─────────────────────────────────────────────────────────────────┐
│                    Research Orchestrator (Skill)                 │
│                                                                  │
│  Input: Validated Issue (nature, scope, context hints)           │
│                                                                  │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 1. PARSE                                                   │  │
│  │    - Load issue file                                       │  │
│  │    - Extract nature, scope, existing context               │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 2. PROPOSE (conversational)                                │  │
│  │    - Map nature → workflow(s) from heuristics              │  │
│  │    - Present: "I'll run X and Y for this issue"            │  │
│  │    - Human: "Yes" / "Skip Y" / "Also run Z"                │  │
│  │    - Track overrides to tune mappings over time            │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 3. DISPATCH                                                │  │
│  │    - Launch workflows (parallel if independent)            │  │
│  │    - Each workflow may spawn sub-agents                    │  │
│  │    - Monitor progress                                      │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 4. COLLECT                                                 │  │
│  │    - Gather findings from all workflows                    │  │
│  │    - Merge into unified Research Report                    │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 5. VALIDATE                                                │  │
│  │    - Run smell detection (general rubric)                  │  │
│  │    - Run nature-specific checks                            │  │
│  │    - Flag issues/gaps                                      │  │
│  └────────────────────────────────────────────────────────────┘  │
│                              │                                   │
│                              ▼                                   │
│  ┌────────────────────────────────────────────────────────────┐  │
│  │ 6. REVIEW                                                  │  │
│  │    - Present report + validation status to human           │  │
│  │    - Human approves OR requests more research              │  │
│  └────────────────────────────────────────────────────────────┘  │
│                                                                  │
│  Output: Research Report + Validation Status                     │
└─────────────────────────────────────────────────────────────────┘
```

### Execution Mode

**Semi-auto**: Propose workflows, human confirms. Used for testing, tuning, and building trust.

---

## Research Validation

> **Alpha Note**: During alpha, validation is exposed as `/cspec:research-validate <issue-id>` slash command. Manual invocation allows human oversight to detect system smells. Boundaries for "enough research" will be refined through real usage, not predetermined rules.

### General Rubric (All Natures)

| Dimension | Question | Smell if Missing |
|-----------|----------|------------------|
| **Completeness** | Does research cover all areas mentioned in issue scope? | Gaps in coverage |
| **Evidence** | Are findings backed by code refs, data, or sources? | Unsubstantiated claims |
| **Relevance** | Is the research focused on the issue, not wandering? | Scope creep |
| **Uncertainty** | Are unknowns explicitly flagged? | False confidence |
| **Actionability** | Can spec work begin with this context? | Dead ends, more questions than answers |

### Nature-Specific Checks

| Nature | Required Elements | Validation Criteria |
|--------|-------------------|---------------------|
| **Bug** | Root cause identified, reproduction confirmed, fix direction clear | RCA document with cause + proposed fix |
| **Hotfix** | Same as Bug + incident context | RCA + incident reference |
| **Feature** | Integration points mapped, no blocking unknowns, patterns identified | Snapshot + web research (if applicable) |
| **Enhancement** | Current behavior documented, delta clearly bounded | Snapshot with current behavior section |
| **Refactor** | Architecture mapped, equivalence boundary defined | Architecture snapshot |
| **Optimization** | Bottlenecks identified with evidence, target metrics feasible | Profiling data + baseline metrics |
| **Security** | Attack vector understood, mitigation patterns researched | RCA (attack) + CVE/mitigation research |
| **Migration** | Current→target mapping complete, rollback considered | Both state snapshots + transformation notes |
| **Configuration** | Current config documented, impact understood | Config snapshot |
| **Deprecation** | All consumers identified, migration path viable | Usage analysis report |
| **Removal** | Deprecation research referenced, consumers migrated | Reference to deprecation + confirmation |

---

## Research Output Structure

Research artifacts are co-located with the issue, not in a global folder.

```
cspec/issues/ISSUE-001/
├── ISSUE-001.md                    # The issue itself
├── research/
│   ├── _report.md                  # Merged findings (orchestrator output)
│   ├── snapshot-<focus>.md         # Codebase snapshot(s)
│   ├── web-research-<topic>.md     # External research
│   ├── rca.md                      # Root cause analysis (if bug/security)
│   ├── profiling.md                # Performance data (if optimization)
│   └── usage-analysis.md           # Consumer analysis (if deprecation)
└── spec/                           # (next phase - specification artifacts)
```

### Report Format (`_report.md`)

**Frontmatter**: issue, nature, date, git_commit, workflows_executed, validation_status

**Sections**: Summary → Findings by Workflow → Code References → Open Questions → Validation Results → Recommendation

---

## Scope Change Policy: Run Fresh

With agents, `Cost of incremental complexity > Cost of fresh restart`.

**When scope changes**: `git restore` → Update issue → Fresh research → Continue. No merge logic, no stale context.

---

## Migration Plan

This project must be self-contained. Migrate global tools (marked "Migrate" in All Workflows table) into `.claude/` directory. Test and iterate.

---

## CLI Integration

```bash
cspec research ISSUE-001        # Dispatch research (invokes orchestrator skill)
/cspec:research-validate ISSUE-001  # Manual validation (alpha, human oversight)
```

---

## Updated Methodology Flow

With the Research Phase formalized:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   Issue          Research        Spec         Implement      Verify         │
│     │               │              │              │             │           │
│     ▼               ▼              ▼              ▼             ▼           │
│  ┌──────┐       ┌──────┐      ┌──────┐      ┌──────┐      ┌──────┐         │
│  │ What │   →   │Context│  →  │ How  │  →   │ Code │  →   │ Done │         │
│  │ Why  │       │Gather │     │Detail│      │      │      │  ?   │         │
│  └──────┘       └──────┘      └──────┘      └──────┘      └──────┘         │
│                                                                             │
│  Outputs:       Outputs:      Outputs:      Outputs:      Outputs:         │
│  - Issue doc    - Research    - Spec        - Working     - Verification   │
│  - Validated      report        artifacts     code          report         │
│                 - Context     - Validation  - Passing     - Sign-off       │
│                   artifacts     hooks         hooks                        │
│                                                                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Quality Gates

| Gate | Criteria |
|------|----------|
| Issue → Research | Issue validated |
| Research → Spec | Report complete, validation passed, human approved |
| Spec → Implement | Specs reviewed, hooks defined |
| Implement → Verify | Hooks pass, code complete |
| Verify → Done | Human sign-off |

---

## Implementation Roadmap

- [ ] Migrate existing tools into project
- [ ] Build `research-orchestrator` skill (semi-auto mode)
- [ ] Implement for Bug (RCA) and Enhancement (snapshot) natures
- [ ] Test on real issues

