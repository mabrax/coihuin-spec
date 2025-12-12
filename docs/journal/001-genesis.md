# The Genesis of Coihuin Spec

*A journal of building a spec-driven development framework for the age of coding agents*

---

## The Problem

It started with a simple observation: coding agents are powerful, but they work best with structure. Without clear specifications, agents wander. Without validation, they hallucinate completion. Without a source of truth, they contradict themselves.

The question was: **How do we create a development methodology that plays to the strengths of AI coding agents while maintaining the rigor that software engineering demands?**

---

## Day 1: The Foundations

We began by defining the core flow:

```
Issue → Spec → Implementation → Verification
```

Not waterfall. A **convergent loop**. The system expects iteration but aims for one-shot success through upfront clarity.

We established the philosophy:
1. **Issue first** - Every change starts with "what" and "why"
2. **Spec before code** - Define the "how" before touching the keyboard
3. **Source of truth** - Specs are authoritative; code implements specs
4. **Validate against spec** - Correctness = spec compliance
5. **Clean exit** - Delete transient artifacts; stale docs are worse than no docs

We created the taxonomy:
- **11 natures** of change (feature, bug, enhancement, refactor, optimization, security, hotfix, migration, configuration, deprecation, removal)
- **3 impact levels** (breaking, additive, invisible)
- **Automatic versioning** (breaking→major, additive→minor, invisible→patch)

The documents piled up: `methodology.md`, `issue-template.md`, `issue-validation.md`, `change-taxonomy-system.md`, `spec-driven-principle.md`, `agent-optimized-spec-format.md`.

---

## Day 2: The Tooling Question

Documentation is nice. But agents need **tooling**.

We defined slash commands for Claude Code - the LLM-assisted workflows:
- `/issue-create` - Interactive issue creation
- `/issue-validate` - Check if an issue is ready

We implemented `/issue-create` first. It asks clarifying questions, determines the nature and impact, generates sequential IDs, creates properly structured YAML frontmatter.

Then `/issue-validate` - checking universal requirements and nature-specific context.

---

## The First Course Correction

Something was missing.

We had jumped straight to issues. But where does the project itself get defined? What establishes the rules that govern everything?

**We needed `/cspec-init`.**

The init command creates the foundation:
- `specs/PROJECT.yaml` - What is this project? Why does it exist?
- `specs/CONSTITUTION.md` - The rules. The philosophy. The law of the land.

Now the flow made sense:
```
/cspec-init → /issue-create → /issue-validate → (spec phase)
```

---

## The Second Course Correction

The slash commands were elegant. LLM-assisted, interactive, helpful.

But there was a problem: **validation shouldn't require an LLM**.

Schema validation is deterministic. Checking if `version: patch` matches `impact: breaking` doesn't need intelligence - it needs a rule engine. Running an LLM for this is wasteful, slow, and introduces unnecessary uncertainty.

The architecture needed to split:

| Layer | Tool | Purpose |
|-------|------|---------|
| Deterministic | Python CLI | Schema validation, format checking, rule enforcement |
| LLM-assisted | Slash commands | Interactive creation, semantic validation, suggestions |

---

## Day 3: Enter `cspec`

We built `cspec` - a Python CLI tool using UV.

```bash
uv init cspec --lib
uv add click pyyaml pydantic
```

**Pydantic** for schema validation - the perfect fit. Define the schema once, get validation for free:

```python
class IssueFrontmatter(BaseModel):
    id: str = Field(pattern=r"^ISSUE-\d{3,}$")
    title: str = Field(min_length=1, max_length=100)
    nature: Nature
    impact: Impact
    version: Version
    # ...

    @model_validator(mode="after")
    def validate_version_matches_impact(self):
        expected = IMPACT_VERSION_MAP[self.impact]
        if self.version != expected:
            raise ValueError(f"Version mismatch...")
```

**Click** for the CLI:

```
cspec init      # Create directories, install slash commands
cspec validate  # Deterministic schema validation
cspec list      # Show all issues
```

The key insight: `cspec init` **installs the slash commands**. The Python tool bootstraps the Claude Code integration.

---

## The Architecture That Emerged

```
┌─────────────────────────────────────────────────────────┐
│                    User Workflow                         │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   cspec init                                             │
│      │                                                   │
│      ├─→ Creates specs/issues/                          │
│      └─→ Installs slash commands to .claude/commands/   │
│                                                          │
│   /cspec-init "My Project"                                     │
│      │                                                   │
│      └─→ Creates PROJECT.yaml + CONSTITUTION.md         │
│                                                          │
│   /issue-create "Add user authentication"                │
│      │                                                   │
│      └─→ Interactive creation → ISSUE-001.md            │
│                                                          │
│   cspec validate specs/issues/ISSUE-001.md              │
│      │                                                   │
│      └─→ Deterministic schema check                     │
│                                                          │
│   /issue-validate ISSUE-001                              │
│      │                                                   │
│      ├─→ Runs cspec validate first                      │
│      └─→ Then semantic validation + suggestions         │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## What We Built

**Python CLI (`cspec`)**:
- `cspec init` - Bootstrap project structure
- `cspec validate` - Schema validation with clear error messages
- `cspec list` - Issue overview

**Slash Commands**:
- `/cspec-init` - Project definition (LLM-assisted)
- `/issue-create` - Issue creation (LLM-assisted)
- `/issue-validate` - Full validation (hybrid)

**Directory Structure**:
```
specs/
├── PROJECT.yaml
├── CONSTITUTION.md
└── issues/
    ├── ISSUE-001.md
    └── ISSUE-002.md

.claude/commands/
├── init.md
├── issue-create.md
└── issue-validate.md

tooling/
├── USAGE.md
└── cspec/
    └── (Python package)
```

---

## Lessons Learned

1. **Start with philosophy, then structure, then tools** - We needed the "why" before the "what" before the "how"

2. **Separate deterministic from probabilistic** - LLMs are great at creativity and judgment; terrible at rule enforcement

3. **The bootstrap problem matters** - How do you initialize a system that needs to validate its own initialization? `cspec init` solves this.

4. **Naming matters** - We almost called it "openspec" and "inspect" before landing on "cspec" (coihuin + spec). Short names win.

5. **Duck-footing works** - Start with the minimum viable loop (create → validate), prove it works, then expand

---

## What's Next

Phase 2: The spec phase.
- `/spec-create` - Generate spec artifacts based on issue nature
- `/spec-validate` - Check spec completeness
- `cspec validate-spec` - Deterministic spec schema validation

The convergent loop continues.

---

*Written during the construction of Coihuin Spec, December 2025*
