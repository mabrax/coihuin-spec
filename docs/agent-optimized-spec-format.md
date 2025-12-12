# Agent-Optimized Spec Format

Guidelines for writing specifications that coding agents can execute effectively.

---

## Core Requirements

### 1. Machine-Readable Over Prose

Prefer structured formats that can be parsed and validated:

```yaml
# Good: Precise and validatable
endpoint: /users/{id}
method: PUT
request:
  required: [name, email]
response:
  status: 200
  schema: User
```

```markdown
# Avoid: Ambiguous prose
"The user update endpoint should accept name and email"
```

### 2. Explicit Completion Criteria

Define when the work is done:

```yaml
completion_criteria:
  - [ ] Endpoint returns 200 with valid input
  - [ ] Returns 400 if email invalid
  - [ ] Returns 404 if user not found
```

### 3. Constraints (What NOT to Do)

Boundaries prevent over-engineering:

```yaml
constraints:
  - Do NOT add caching
  - Do NOT refactor adjacent code
  - Do NOT add fields beyond spec
```

### 4. Concrete Examples

Examples resolve ambiguity better than descriptions:

```yaml
examples:
  - input: { "name": "Alice", "email": "a@b.com" }
    output: { "id": 1, "name": "Alice", "email": "a@b.com" }
  - input: { "name": "", "email": "invalid" }
    error: { "status": 400, "message": "Validation failed" }
```

### 5. Current State Reference

For deltas, provide easy access to existing state:

```yaml
current_state:
  ref: specs/current/api.yaml#/users/{id}
```

### 6. Atomic Scope

One spec = one focused change. Large specs lead to partial implementations and drift.

### 7. Dependency Declaration

```yaml
depends_on:
  - specs/current/user-schema.yaml
  - specs/current/auth-middleware.md
affects:
  - specs/current/api.yaml
```

### 8. Validation Hooks

Provide verification commands:

```yaml
validate: npm run test:contract
```

---

## Complete Spec Template

```yaml
id: enhance-user-profile
type: enhancement
impact: additive

depends_on: [user-schema, api-contract]
affects: [api-contract]

current_state:
  ref: specs/current/api.yaml#/users/{id}

change:
  description: Add optional 'avatar' field
  schema_delta:
    add_field: { name: avatar, type: string, required: false }

examples:
  - input: { name: "Alice", avatar: "http://..." }
    output: { id: 1, name: "Alice", avatar: "http://..." }

constraints:
  - Do not modify existing fields
  - Do not add validation beyond URL format

completion_criteria:
  - [ ] Field accepts valid URL
  - [ ] Field is optional (null allowed)
  - [ ] Existing tests pass

validate: npm run test:api
```

---

## Why This Format Works

| Element | Agent Benefit |
|---------|---------------|
| Machine-readable | Parse and validate precisely |
| Completion criteria | Know when done |
| Constraints | Avoid over-engineering |
| Examples | Resolve ambiguity |
| Current state ref | No searching through code |
| Dependencies | Work systematically |
| Validation hooks | Self-verify implementation |
