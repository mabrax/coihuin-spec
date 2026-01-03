# Tooling

The `cspec` CLI tool for spec-driven development.

---

## Structure

```
tooling/
├── README.md           # This file
├── USAGE.md            # Usage documentation
└── cspec/              # Python package
    ├── cli.py          # Main CLI implementation
    ├── schemas.py      # Pydantic schemas for validation
    ├── commands/       # Slash command definitions
    │   └── cspec/      # Namespaced slash commands
    │       ├── issue-create.md
    │       ├── issue-start.md
    │       ├── proposal-write.md
    │       ├── spec-write.md
    │       ├── plan-write.md
    │       └── work-complete.md
    └── templates/      # Bundled templates
        ├── AGENTS.md           # Agent guidance template
        └── issue_templates/    # Issue templates by nature
            ├── bug.yaml
            ├── feature.yaml
            ├── enhancement.yaml
            └── ...
```

---

## CLI Commands

| Command | Description |
|---------|-------------|
| `cspec init` | Initialize spec-driven development in a project |
| `cspec update` | Update slash commands and templates to latest version |
| `cspec status` | Check project health and report status |
| `cspec onboard` | Onboard to a spec-driven project |
| `cspec specs list` | List all permanent specs |
| `cspec specs show <feature>` | Show a feature spec |
| `cspec work list` | List all work in progress |
| `cspec work show <slug>` | Show details of a work item |
| `cspec templates list` | List available issue templates |
| `cspec templates get <name>` | Get a fillable issue template |

---

## Slash Commands

Installed to `.claude/commands/cspec/` by `cspec init`:

| Command | Description |
|---------|-------------|
| `/cspec:issue-create` | Interactive issue creation |
| `/cspec:issue-start` | Import a GitHub issue and start work |
| `/cspec:proposal-write` | Write a proposal for current work item |
| `/cspec:spec-write` | Write a Gherkin-style spec from proposal |
| `/cspec:plan-write` | Create an implementation plan from spec |
| `/cspec:work-complete` | Complete work, merge spec, clean up |

---

## Installation

```bash
# From repo root
cd tooling/cspec
uv sync

# Or install as a tool
uv tool install ./tooling/cspec
```

---

## Development

```bash
# Run CLI
uv run cspec --help

# Run tests
uv run pytest
```

---

## References

- [Methodology](../docs/methodology.md)
- [Issue Template](../docs/issue-template.md)
- [Issue Validation Rules](../docs/issue-validation.md)
- [Change Taxonomy](../docs/change-taxonomy-system.md)
