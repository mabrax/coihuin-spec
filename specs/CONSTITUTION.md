# Constitution

## Philosophy

This project follows **spec-driven development** with these guiding principles:

### Core Methodology

1. **Issue first**: Every change starts with an issue (the "what and why")
2. **Spec before code**: Specs define the "how" before implementation
3. **Source of truth**: Specs are authoritative; code implements specs
4. **Validate against spec**: Implementation correctness = spec compliance
5. **Clean exit**: Delete transient artifacts; keep persistent ones updated

### Project-Specific Principles

1. **Pragmatic minimal**: Only add structure that reduces iterations. If a process step creates more friction than it saves, remove it. The goal is convergence, not compliance.

2. **Agent-first design**: Optimize for LLM comprehension over human aesthetics. Machine-readable formats, explicit constraints, concrete examples, and clear completion criteria matter more than elegant prose.

3. **Experiment openly**: This is a hypothesis being tested, not a manifesto. Share learnings, adjust methodology based on data, and be honest about what works and what doesn't.

## Rules

### Issues

- Every change requires an issue
- Issues must have: nature, impact, scope, acceptance criteria
- Issues must be validated before moving to spec phase
- Use `/cspec:issue-create` for proper structure

### Specs

- Specs must cover every boundary a change crosses
- Specs must be machine-readable where possible
- Specs include validation hooks (how to verify implementation)
- Prefer explicit constraints over implicit assumptions

### Implementation

- Implementation follows spec, not the other way around
- Deviations from spec require spec update first
- Feedback loops return to appropriate phase (issue or spec)
- Self-dogfooding: use cspec methodology to develop cspec

## Quality Standards

1. **Tests required**: All code must have tests and pass linting
2. **Self-dogfooding**: Changes must use cspec methodology itself
3. **Documentation first**: User-facing changes require docs updated
4. **Validation passes**: `cspec validate` must pass for all issues

## Anti-patterns

- **Process for process sake**: Don't add ceremony that doesn't reduce iterations
- **Premature optimization**: Don't build for hypothetical future needs
- **Stale documentation**: Delete transient docs when done; stale docs are worse than none
- **Human-optimized formats**: Don't sacrifice agent comprehension for human aesthetics
- **Waterfall thinking**: This is a convergent loop, not a one-way pipeline

## Artifacts

| Type | Lifecycle |
|------|-----------|
| Wireframes, task breakdowns, design explorations | Transient (delete when done) |
| API contracts, schemas, business rules, ADRs | Persistent (source of truth) |
| Issue documents | Transient (archive after done) |
| Methodology documentation | Persistent |

## Versioning

- **Breaking** changes to Major version
- **Additive** changes to Minor version
- **Invisible** changes to Patch version
