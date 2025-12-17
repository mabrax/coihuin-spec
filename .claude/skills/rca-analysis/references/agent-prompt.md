# RCA Agent Prompt

Use this prompt template when dispatching RCA agents via the Task tool.

## Agent Configuration

- **subagent_type**: `rca`
- **model**: inherit (or specify based on complexity)

## Prompt Template

```
<FOCUS_AREA>[Selected Area]</FOCUS_AREA>

<PROBLEM_STATEMENT>
[Problem statement verbatim]
</PROBLEM_STATEMENT>

Investigate this problem within your focus area. Return structured XML findings.
```

## Agent Behavior

The RCA agent will:

1. **Assess** - Gather symptoms, timeline, what changed, scope/impact
2. **Hypothesize** - Apply "5 Whys", generate competing theories
3. **Investigate** - Test hypotheses with tools, examine logs/metrics/traces
4. **Analyze** - Distinguish correlation vs causation, validate with evidence
5. **Identify** - Articulate fundamental cause, trace causal chain
6. **Report** - Return structured XML findings

## Expected Output Format

Agents return findings in this XML structure:

```xml
<rca_findings focus="[Assigned focus area]">

<evidence>
  <item type="code" location="file.ts:42">
    Description of what was found
  </item>
  <item type="log" source="application.log">
    Relevant error message or pattern
  </item>
  <item type="config" location="env.production">
    Configuration state observed
  </item>
  <item type="behavior" context="user flow">
    Observable behavior noted
  </item>
</evidence>

<observations>
  <observation confidence="high|medium|low">
    Focused interpretation of evidence
  </observation>
  <observation confidence="high|medium|low">
    Connection noticed between components
  </observation>
</observations>

<layer_status status="suspect|cleared|inconclusive">
  Brief statement on whether this layer appears healthy or problematic
</layer_status>

</rca_findings>
```

## Evidence Types

- **code** - Source code findings with file:line location
- **log** - Log entries, error messages, stack traces
- **config** - Environment variables, config files, settings
- **behavior** - Observable runtime behavior, user-reported symptoms
- **metric** - Performance data, monitoring alerts
- **change** - Recent commits, deployments, dependency updates
