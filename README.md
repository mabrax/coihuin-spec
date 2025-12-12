# Coihuin Spec

**Spec-driven development for the age of coding agents.**

A methodology and CLI tool for structured software development optimized for human-agent collaboration. Context is king — this project explores whether upfront structure reduces total iterations.

> **Status**: Alpha. Actively dogfooding on itself. This is an experiment, not a manifesto.

---

## The Problem

Coding agents are powerful, but they wander. Without clear specifications, they hallucinate completion. Without validation checkpoints, they contradict themselves. Without a source of truth, they drift.

## The Hypothesis

**Context is an information optimization problem.**

- Too little context → high entropy, hallucination fills gaps
- Too much context → noise drowns signal, exceeds capacity
- Right context → optimal information density, higher success rate

Coihuin Spec tests one dimension of this: **Does structured process granularity help find the right context?**

The flow: `Issue → Spec → Implementation → Verification`

Each artifact provides context for the next phase. Validation catches drift early. The goal is convergence in fewer iterations.

---

## Quick Start

### Install

```bash
# Clone the repo
git clone https://github.com/mabrax/coihuin-spec.git
cd coihuin-spec

# Install the CLI (requires Python 3.13+, uv recommended)
cd tooling/cspec
uv sync
```

### Initialize a project

```bash
# From your project root
uv run cspec init
```

This creates:
- `specs/issues/` — Where issues live
- `.claude/commands/cspec/` — Slash commands for Claude Code

### Create and validate an issue

```bash
# Use the slash command in Claude Code
/cspec:issue-create "Add user authentication"

# Validate the issue
uv run cspec validate specs/issues/ISSUE-001.md

# List all issues
uv run cspec list
```

---

## The Methodology

### Core Phases

| Phase | Question | Output |
|-------|----------|--------|
| **Issue** | What needs to change? Why? | Validated issue document |
| **Spec** | How will it be implemented? | Specification artifacts |
| **Implementation** | Build according to spec | Working code |
| **Verification** | Does it match the spec? | Acceptance sign-off |

### The Convergent Loop

Not waterfall. A loop that aims for one-shot execution but handles iteration gracefully.

```
Issue → Spec → Implement → Validate ──┐
  ↑                                   │
  └───────── feedback loop ───────────┘
                  │
                  ▼
            [Converged?] ──yes──→ Done → Clean up transients
```

### Change Taxonomy

11 natures of change, each with specific validation requirements:

| Nature | Version Impact | Required Context |
|--------|---------------|------------------|
| Feature | minor | problem-statement |
| Bug | patch | root-cause-analysis |
| Enhancement | minor | current-behavior, delta-description |
| Refactor | patch | architecture-scope, behavioral-equivalence |
| Security | patch | vulnerability-report, attack-vector |
| Migration | varies | current-state, target-state, rollback-plan |
| ... | ... | ... |

See [Change Taxonomy](docs/change-taxonomy-system.md) for the full list.

---

## Documentation

| Document | Purpose |
|----------|---------|
| [Methodology](docs/methodology.md) | The full development flow |
| [Issue Template](docs/issue-template.md) | How to structure issues |
| [Issue Validation](docs/issue-validation.md) | Validation rules by nature |
| [Change Taxonomy](docs/change-taxonomy-system.md) | Classification system |
| [Spec-Driven Principle](docs/spec-driven-principle.md) | Philosophy of specs as source of truth |
| [Agent-Optimized Format](docs/agent-optimized-spec-format.md) | Designing specs for LLM consumption |

---

## The CLI: `cspec`

```
Usage: cspec [OPTIONS] COMMAND [ARGS]...

Commands:
  init      Initialize spec-driven development in current project
  validate  Validate an issue file against the schema
  list      List all issues in the project
  update    Update slash commands to latest version
```

### Validation Example

```bash
$ cspec validate specs/issues/ISSUE-001.md

Validating ISSUE-001.md...

Schema Validation:
  ✓ ID format valid
  ✓ Title present and under 100 chars
  ✓ Nature valid
  ✓ Impact valid
  ✓ Version matches impact
  ✓ Status valid
  ✓ Dates valid

Body Validation:
  ✓ Problem section present
  ✓ Scope section present
  ✓ In-scope items defined
  ✓ Acceptance criteria defined

========================================
✓ VALIDATION PASSED
```

---

## Philosophy

### Why This Exists

I'm testing whether structured process helps coding agents produce better results with fewer iterations. The hypothesis is about **context engineering** — finding the right amount of information at each step.

This is an experiment. If the granularity creates more friction than it saves, I'll adjust. The point is to find out.

### Recursive Dogfooding

Coihuin Spec is developed using Coihuin Spec. The first project to use this methodology is the methodology itself. If the process is broken, I feel it immediately.

### Anti-Hype

No promises of 10x productivity. No claims this is THE answer. Just a structured approach being tested in production, shared at alpha so others can experiment too.

---

## Contributing

This is early-stage software. If you try it and have feedback:
- Open an issue describing your experience
- What worked? What didn't?
- Where was the friction?

---

## License

MIT

---

## Author

[@mabrax](https://github.com/mabrax) — Production AI Toolsmith. Building tools that turn one engineer into a team.
