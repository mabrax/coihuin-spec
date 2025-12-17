# Migration Notes: Research Tools

## Summary

Successfully migrated research tools from global `~/.claude/` configuration into the project's local `.claude/` directory to make the project self-contained.

## Migrated Components

### 1. RCA Analysis Skill
- **Source**: `~/.claude/skills/rca-analysis/`
- **Destination**: `.claude/skills/rca-analysis/`
- **Status**: Complete
- **Files**:
  - `SKILL.md` - Main skill definition
  - `references/agent-prompt.md` - RCA agent system prompt template
  - `references/report-template.md` - Report generation template
- **Notes**: All relative path references within the skill are preserved and functional.

### 2. Web Research Command
- **Source**: `~/.claude/commands/web-research.md`
- **Destination**: `.claude/commands/web-research.md`
- **Status**: Complete
- **Notes**: Command is designed to work independently with no project-specific paths.

### 3. Snapshot-Researcher Agent
- **Source**: `~/.claude/agents/snapshot-researcher.md`
- **Destination**: `.claude/agents/snapshot-researcher.md`
- **Status**: Complete
- **Notes**: Custom agent for parallel codebase exploration. Used by snapshot commands to dispatch domain-specific research sub-agents.

## Verification

All migrated files are in place and functional:

```
.claude/
├── agents/
│   └── snapshot-researcher.md
├── commands/
│   └── web-research.md
└── skills/
    └── rca-analysis/
        ├── SKILL.md
        └── references/
            ├── agent-prompt.md
            └── report-template.md
```

## Usage

Both tools are now available for use within the project context:

- Use `/web-research <topic>` command to research external documentation and patterns
- Use the `rca-analysis` skill to perform root cause analysis on bugs and issues
- Reference `snapshot-researcher` as needed for codebase analysis

## Path References

No path adjustments were necessary. All files contain relative references that work correctly in the project structure.
