---
description: Research external documentation, patterns, and best practices for a technology or domain
argument-hint: <topic>
---

# Purpose

Research external documentation, patterns, and best practices to understand a technology or domain before implementation.

## Variables

```
TOPIC: $1 (required - e.g., "React Server Components", "PostgreSQL RLS")
IDENTIFIER: $2 (optional - e.g., ticket number like "ISSUE-004")
OUTPUT_DIR: research/
OUTPUT_FILE: research/YYYY-MM-DD-<topic>.md (or research/YYYY-MM-DD-<IDENTIFIER>-<topic>.md if identifier provided)
```

**Note**: Get current date with `TZ='America/Santiago' date '+%Y-%m-%d'` for the filename.

## Instructions

- Focus on understanding the technology/domain, not our codebase
- Gather authoritative sources (official docs, reputable articles, known experts)
- Identify patterns, best practices, and common pitfalls
- Note version-specific information when relevant
- Do not critique or evaluate — gather and synthesize knowledge

## Workflow

### 1. Initial Setup

If no topic provided, ask the user what technology or domain they want to research.

### 2. Scope the Research

Identify key aspects to investigate:
- Core concepts and terminology
- Common patterns and best practices
- Pitfalls and anti-patterns
- Version/compatibility considerations
- Related technologies or alternatives

### 3. Spawn Sub-Agents

Size the research swarm based on the topic's breadth:
- Use 2-4 agents with web search capabilities
- Assign each agent a focused research area (e.g., core concepts, patterns, pitfalls)
- Ensure complementary coverage — agents should investigate different aspects

**How to invoke**: Use the `Task` tool with `subagent_type="Explore"` and include web search instructions in the prompt. Example:
```
Task(subagent_type="Explore", prompt="Research [specific aspect] of [topic]. Use WebSearch to find official documentation and authoritative sources. Focus on [core concepts|patterns|pitfalls|compatibility].")
```

Run agents in parallel for independent research areas (multiple Task calls in one message).

### 4. Synthesize Findings

Wait for all sub-agents to complete, then:
- Prioritize official documentation over blog posts
- Cross-reference multiple sources for accuracy
- Note conflicting information or opinions
- Organize by relevance to the user's likely use case

### 5. Output

Generate the research document per the Report format below. Present a summary to the user and invite follow-up questions. For follow-ups, append to the same document with a `## Follow-up: [topic]` section.

## Report

**When to create a file vs. respond inline:**
- **Create file**: Multi-faceted topics, topics requiring multiple sources, topics you'll reference later
- **Respond inline**: Single-question lookups, quick clarifications, trivial facts

If creating a file, write to `research/YYYY-MM-DD-<topic>.md` (or include identifier if provided).

**Document format:**
```markdown
---
date: <run: TZ='America/Santiago' date -Iseconds>
topic: "<research topic>"
tags: [research, web, <technology-names>]
status: complete
---

# Research: <topic>

## Research Question
<!-- What the user wanted to understand -->

## Summary
<!-- 2-3 paragraphs providing a clear understanding of the technology/domain.
     This should stand alone as a primer for someone unfamiliar with the topic. -->

## Core Concepts
<!-- Key terminology, mental models, and foundational understanding.
     What do you need to know to work with this technology? -->

## Patterns & Best Practices
<!-- Recommended approaches, common patterns, and industry conventions.
     How should this technology be used? -->

## Pitfalls & Anti-Patterns
<!-- Common mistakes, things to avoid, and gotchas.
     What should you NOT do? -->

## Version & Compatibility
<!-- Version-specific information, breaking changes, migration paths.
     What version considerations matter? -->

## Sources
<!-- List of sources with URLs.
     Format: [Title](url) - brief description of what this source covers -->

## Open Questions
<!-- Areas that need deeper investigation or have conflicting information.
     Be specific about what's uncertain and why. -->
```
