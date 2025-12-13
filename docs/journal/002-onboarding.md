# The Onboarding Problem

*Continuing the journal of building a spec-driven development framework*

---

## The Gap

We had `cspec init`. It creates the directory structure and installs slash commands. We had `/cspec:init` that creates PROJECT.yaml and CONSTITUTION.md.

But something was broken.

After running these commands, an agent dropping into the project had no idea what to do. Empty files. No context. The AGENTS.md had placeholder comments where project-specific knowledge should live.

**The onboarding problem**: How does a coding agent learn enough about a project to be useful?

---

## Day 4: Designing Onboarding

We identified three gaps:

1. **PROJECT.yaml** - Empty after init. Who fills it? With what?
2. **CONSTITUTION.md** - Empty after init. What rules apply?
3. **AGENTS.md PROJECT CONTEXT** - Placeholder comments. Agents need real context.

The solution: `cspec onboard` - a hybrid command.

### The Architecture Decision

The same split we applied to issue validation applies here:

| Task | Type | Tool |
|------|------|------|
| Check if files exist and are filled | Deterministic | Python CLI |
| Ask user about project philosophy | LLM-assisted | Claude interaction |
| Analyze codebase for context | LLM-assisted | Claude exploration |
| Generate PROJECT.yaml content | LLM-assisted | Claude writing |
| Generate CONSTITUTION.md content | LLM-assisted | Claude writing |
| Populate AGENTS.md context | LLM-assisted | Claude synthesis |

The CLI checks status. If not onboarded, it outputs a detailed prompt for the agent to follow.

---

## The Onboarding Flow

```
cspec onboard
    │
    ├─→ Check status (deterministic)
    │   ├── PROJECT.yaml exists & filled?
    │   ├── CONSTITUTION.md exists & filled?
    │   └── AGENTS.md PROJECT CONTEXT populated?
    │
    └─→ If not onboarded, output LLM prompt:
        │
        ├─→ Step 1: Run cspec status
        ├─→ Step 2: Handle PROJECT.yaml
        │   └── Ask user: name, purpose, scope, tech stack, stakeholders
        ├─→ Step 3: Handle CONSTITUTION.md
        │   └── Ask user: philosophy, rules, quality standards, anti-patterns
        ├─→ Step 4: Analyze codebase
        │   └── Explore: structure, tech stack, architecture, conventions
        ├─→ Step 5: Update AGENTS.md PROJECT CONTEXT
        │   └── Synthesize findings into structured context
        └─→ Step 6: Summary
```

---

## First Run: Dogfooding

We ran `cspec onboard` on Coihuin Spec itself.

**Status check revealed**:
- `specs/` directory: OK
- `specs/issues/`: OK
- PROJECT.yaml: MISSING
- CONSTITUTION.md: MISSING
- AGENTS.md: exists but PROJECT CONTEXT empty

**User questions asked**:
1. Stakeholders → "Solo devs with agents, Methodology explorers"
2. Out of scope → "IDE integration, enterprise features, multi-agent swarm orchestration (deferred)"
3. Quality standards → "Tests + linting, self-dogfooding, docs first"
4. Philosophy → "Pragmatic minimal, agent-first design, experiment openly"

**Files created**:
- `specs/PROJECT.yaml` - Project definition with scope, tech stack, stakeholders
- `specs/CONSTITUTION.md` - Philosophy, rules, quality standards, anti-patterns

**AGENTS.md updated** with:
- Project overview and core flow
- Tech stack (Python 3.13+, Click, Pydantic, PyYAML, Hatch)
- Architecture diagram and data flow
- Key conventions
- Important files table
- Testing and build commands
- Domain knowledge (key concepts defined)

---

## The Bug We Found

Running `cspec status` after onboarding still showed MISSING files.

The problem: `cspec status` looks for PROJECT.yaml and CONSTITUTION.md in the **project root**. But the methodology (and `cspec onboard`) places them in **`specs/`**.

```python
# Status command (wrong):
project_yaml = project_root / "PROJECT.yaml"

# Should be:
project_yaml = project_root / "specs" / "PROJECT.yaml"
```

A bug in our own tooling, discovered through dogfooding. The system works.

---

## What Emerged

The onboarding command creates a **complete context package** for agents:

1. **PROJECT.yaml** - The "what" and "who"
   - Name, description, purpose
   - Scope (in/out)
   - Tech stack
   - Stakeholders

2. **CONSTITUTION.md** - The "rules"
   - Core methodology principles
   - Project-specific philosophy
   - Quality gates
   - Anti-patterns to avoid

3. **AGENTS.md PROJECT CONTEXT** - The "how to navigate"
   - Architecture overview
   - Key files and their purposes
   - Conventions
   - Testing/build commands
   - Domain knowledge

An agent entering this project now has everything it needs to be productive.

---

## Lessons Learned

1. **Init is not enough** - Creating empty files creates the illusion of progress. Real onboarding requires content.

2. **Context is multi-layered** - PROJECT.yaml defines the project, CONSTITUTION.md defines the rules, AGENTS.md bridges to practical usage.

3. **Hybrid commands work** - Deterministic checks + LLM-assisted content generation is a powerful pattern.

4. **Dogfooding finds bugs** - We found the path inconsistency in `cspec status` only by using our own tools.

5. **Ask, don't assume** - The onboarding questions ensure human intent is captured, not hallucinated.

---

## What's Next

1. Fix the `cspec status` path bug
2. Add `--force` flag to re-onboard existing projects
3. Consider `cspec doctor` for health checks
4. Continue to Phase 2: specification tooling

---

*Written during the onboarding of Coihuin Spec to itself, December 2025*
