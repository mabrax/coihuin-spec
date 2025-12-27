# Issue Templates

Issues are created on GitHub using structured templates. Each issue nature has its own template with nature-specific fields.

## Installation

Issue templates are installed by `cspec init` to `.github/ISSUE_TEMPLATE/`.

To update templates to the latest version:
```bash
cspec update --force
```

## Issue Natures (Taxonomy)

| Nature | Description | Key Fields |
|--------|-------------|------------|
| **feature** | New functionality | impact, problem, scope, acceptance |
| **enhancement** | Improve existing | impact, current/desired behavior |
| **bug** | Something broken | severity, reproduction steps, environment |
| **refactor** | Restructure code | current/target state, scope |
| **optimization** | Performance improvement | current/target metrics, approach |
| **security** | Vulnerability or hardening | severity, type, remediation |
| **hotfix** | Urgent production fix | severity, incident, rollback plan |
| **migration** | Data or system migration | from/to, rollback, validation |
| **configuration** | Settings change | environment, change, rollback |
| **deprecation** | Mark as deprecated | what, reason, timeline, migration path |
| **removal** | Remove deprecated | what, deprecation ref, impact assessment |

## Impact Levels

- **breaking** - Requires consumer changes
- **additive** - New capability, backward compatible
- **invisible** - Internal only, no API changes

## Workflow

1. Create issue on GitHub using appropriate template
2. Run `/cspec:issue-start <github-url>` to import and start work
3. Follow the cspec workflow: proposal → spec → plan → implement → complete

## Template Location

Templates are stored in:
- Package: `cspec/templates/issue_templates/*.yml`
- Project: `.github/ISSUE_TEMPLATE/*.yml`
