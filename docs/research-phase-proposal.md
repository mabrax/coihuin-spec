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

| Nature | Primary Workflow | Secondary Workflow | Parallel? |
|--------|------------------|-------------------|-----------|
| **Bug** | `rca-analysis` | — | N/A |
| **Hotfix** | `rca-analysis` (fast mode) | — | N/A |
| **Feature** | `snapshot-codebase` (integration points) | `web-research` (patterns/prior art) | Yes |
| **Enhancement** | `snapshot-codebase` (current behavior) | — | N/A |
| **Refactor** | `snapshot-codebase` (architecture) | — | N/A |
| **Optimization** | `snapshot-codebase` (hot paths) | `profiling-analysis` | Yes |
| **Security** | `rca-analysis` (attack-focused) | `web-research` (CVE/mitigation) | Yes |
| **Migration** | `snapshot-codebase` (current state) | `web-research` (target tech) | Yes |
| **Configuration** | `snapshot-codebase` (config layer) | — | N/A |
| **Deprecation** | `usage-analysis` | — | N/A |
| **Removal** | Reference deprecation research | — | N/A |

### Workflow Descriptions

#### Existing Workflows (to migrate)

| Workflow | Current Location | Purpose |
|----------|------------------|---------|
| `rca-analysis` | Global skill | Root cause analysis for bugs/security issues |
| `snapshot-codebase` | Global command | Point-in-time codebase research |
| `web-research` | Global command | External documentation and patterns |
| `snapshot-researcher` | Global agent | Sub-agent for parallel codebase exploration |

#### New Workflows (to build)

| Workflow | Purpose | When Needed |
|----------|---------|-------------|
| `profiling-analysis` | Collect/analyze performance metrics, identify bottlenecks | Optimization |
| `usage-analysis` | Find all consumers/usages of a symbol, API, or feature | Deprecation, Removal, Refactor impact |
| `data-analysis` | Query and analyze existing data shape, volume, patterns | Migration (data), Feature (data-driven) |
| `api-exploration` | Probe external APIs, document contracts, test responses | External integrations |

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
│  │ 2. PROPOSE                                                 │  │
│  │    - Map nature → workflow(s)                              │  │
│  │    - Present to human for confirmation                     │  │
│  │    - Human adjusts if needed                               │  │
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

### Execution Modes

| Mode | Description | When to Use |
|------|-------------|-------------|
| **Semi-auto** (current) | Propose workflows, human confirms | Testing, tuning, building trust |
| **Full-auto** (future) | Dispatch based on nature, no confirmation | After validation in production |
| **Headless** (future) | Run without interaction, report results | CI/CD integration |

---

## Research Validation

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

### Report Format

The merged `_report.md` follows this structure:

```markdown
---
issue: ISSUE-001
nature: <nature>
date: <ISO 8601>
git_commit: <hash>
workflows_executed:
  - <workflow-1>
  - <workflow-2>
validation_status: passed | warnings | failed
---

# Research Report: <issue title>

## Summary
<!-- 2-3 paragraphs synthesizing all findings -->

## Findings by Workflow

### <Workflow Name>
<!-- Key findings from this workflow -->
<!-- Link to full artifact: [Full Report](./snapshot-*.md) -->

## Consolidated Code References
<!-- Key files across all workflows -->

## Open Questions
<!-- Uncertainties flagged across all workflows -->

## Validation Results

### General Rubric
- [ ] Completeness: ...
- [ ] Evidence: ...
- [ ] Relevance: ...
- [ ] Uncertainty: ...
- [ ] Actionability: ...

### Nature-Specific (<nature>)
- [ ] <check 1>: ...
- [ ] <check 2>: ...

## Recommendation
<!-- Ready to proceed to Spec? Or needs more research? -->
```

---

## Scope Change Policy: Run Fresh

### Philosophy

Traditional development resists restarts because human labor is expensive. With coding agents, the equation flips:

```
Cost of incremental complexity > Cost of fresh restart
```

### The Restart Protocol

When scope changes mid-development:

```
Scope changed?
     │
     ▼
┌─────────────────┐
│  git restore    │  ← Return to clean state (commit before change)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Update Issue   │  ← New scope, re-validate
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Fresh Research │  ← No stale context, no merge complexity
└────────┬────────┘
         │
         ▼
    Continue flow
```

### Benefits

- No incremental research logic needed
- No "merge old + new findings" complexity
- No stale context pollution
- Always working from validated, coherent state
- Simpler implementation, easier to reason about

---

## Migration Plan

This project must be self-contained. The following global tools need to be migrated into this repository.

### Tools to Migrate

| Tool | Current Location | Target Location | Type |
|------|------------------|-----------------|------|
| `rca-analysis` | `~/.claude/skills/rca-analysis.md` | `.claude/skills/rca-analysis.md` | Skill |
| `snapshot-codebase` | `~/.claude/commands/snapshot-codebase.md` | `.claude/commands/snapshot-codebase.md` | Command |
| `web-research` | `~/.claude/commands/web-research.md` | `.claude/commands/web-research.md` | Command |
| `investigate` | `~/.claude/commands/investigate.md` | `.claude/commands/investigate.md` | Command |
| `snapshot-researcher` | Built-in agent | Document in AGENTS.md | Agent reference |

### Migration Steps

1. **Copy tools** - Bring global tools into project `.claude/` directory
2. **Adapt paths** - Update any hardcoded paths to be project-relative
3. **Update AGENTS.md** - Document all available tools and their usage
4. **Test** - Verify tools work from project context
5. **Iterate** - Evolve tools within this project, feed improvements back to global if desired

### New Tools to Build

| Tool | Type | Priority | Description |
|------|------|----------|-------------|
| `research-orchestrator` | Skill | P1 | Coordinates research phase |
| `profiling-analysis` | Skill/Command | P2 | Performance metrics collection |
| `usage-analysis` | Skill/Command | P2 | Find all consumers of a symbol/API |
| `data-analysis` | Skill/Command | P3 | Query and analyze data patterns |
| `api-exploration` | Skill/Command | P3 | External API documentation |

---

## CLI Integration

### Proposed Commands

```bash
# Dispatch research for an issue (invokes skill in semi-auto mode)
cspec research ISSUE-001

# Validate research completeness
cspec research-validate ISSUE-001

# List research artifacts for an issue
cspec research-list ISSUE-001
```

### Skill Invocation

The `cspec research` command would invoke the `research-orchestrator` skill:

```bash
cspec research ISSUE-001
# Equivalent to triggering skill with issue context
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

| Gate | From → To | Criteria |
|------|-----------|----------|
| Issue Gate | Issue → Research | Issue validated, status `ready` |
| Research Gate | Research → Spec | Research report complete, validation passed, human approved |
| Spec Gate | Spec → Implementation | Specs reviewed, validation hooks defined |
| Implementation Gate | Implementation → Verification | All hooks pass, code complete |
| Verification Gate | Verification → Done | Human sign-off, artifacts updated |

---

## Open Questions for Future Iteration

1. **Research caching** - Can we reuse research across similar issues?
2. **Research templates** - Pre-filled prompts per nature to speed up workflow?
3. **Metrics** - Track research time, iteration count, correlation with spec quality?
4. **Cross-issue research** - When one issue's research informs another?

---

## Implementation Roadmap

### Phase 1: Foundation
- [ ] Migrate existing tools into project
- [ ] Build `research-orchestrator` skill (semi-auto mode)
- [ ] Implement for Bug (RCA) and Enhancement (snapshot) natures
- [ ] Test on real issues

### Phase 2: Expansion
- [ ] Add remaining nature mappings
- [ ] Build `usage-analysis` tool
- [ ] Build `profiling-analysis` tool
- [ ] Refine validation rubric based on usage

### Phase 3: Automation
- [ ] Add full-auto mode to orchestrator
- [ ] CLI integration (`cspec research`)
- [ ] Headless mode for CI/CD

---

## References

- [Methodology](./methodology.md) - Overall development flow
- [Issue Validation](./issue-validation.md) - Context requirements by nature
- [Change Taxonomy](./change-taxonomy-system.md) - Nature classification
- [Spec-Driven Principle](./spec-driven-principle.md) - Philosophy of specs as source of truth
