"""Coihuin Spec - Spec-driven development for the age of coding agents."""

import re
import shutil
import sys
from pathlib import Path

import click
import yaml

# Package directory for bundled resources
PACKAGE_DIR = Path(__file__).parent
COMMANDS_DIR = PACKAGE_DIR / "commands" / "cspec"
TEMPLATES_DIR = PACKAGE_DIR / "templates"
ISSUE_TEMPLATES_DIR = PACKAGE_DIR / "templates" / "issue_templates"

# Reference to add to CLAUDE.md
AGENTS_REFERENCE = "\nSee [AGENTS.md](AGENTS.md) for cspec workflow and project context.\n"

# Marker for preserving user content in AGENTS.md
AGENTS_PROJECT_CONTEXT_MARKER = "## PROJECT CONTEXT"

BANNER = r"""
   _____ ____  _____ _    _ _    _ _____ _   _    _____ _____  ______ _____
  / ____/ __ \|_   _| |  | | |  | |_   _| \ | |  / ____|  __ \|  ____/ ____|
 | |   | |  | | | | | |__| | |  | | | | |  \| | | (___ | |__) | |__ | |
 | |   | |  | | | | |  __  | |  | | | | | . ` |  \___ \|  ___/|  __|| |
 | |___| |__| |_| |_| |  | | |__| |_| |_| |\  |  ____) | |    | |___| |____
  \_____\____/|_____|_|  |_|\____/|_____|_| \_| |_____/|_|    |______\_____|

  Spec-driven development for the age of coding agents
"""


# Commands to exclude from slash command installation (handled by CLI instead)
EXCLUDED_COMMANDS = {"onboard.md"}


def install_commands(project_root: Path, force: bool = False) -> int:
    """Install slash commands to project. Returns count of installed commands."""
    commands_dest = project_root / ".claude" / "commands" / "cspec"
    commands_dest.mkdir(parents=True, exist_ok=True)

    installed = 0
    if COMMANDS_DIR.exists():
        for cmd_file in COMMANDS_DIR.glob("*.md"):
            # Skip excluded commands (these are handled by CLI instead)
            if cmd_file.name in EXCLUDED_COMMANDS:
                continue
            dest = commands_dest / cmd_file.name
            if dest.exists() and not force:
                click.echo(f"  · /{cmd_file.stem} exists (use --force to overwrite)")
            else:
                shutil.copy(cmd_file, dest)
                click.echo(f"  ✓ Installed /{cmd_file.stem} (cspec:{cmd_file.stem})")
                installed += 1
    return installed


def install_issue_templates(project_root: Path, force: bool = False) -> int:
    """Install GitHub issue templates to project. Returns count of installed templates."""
    templates_dest = project_root / ".github" / "ISSUE_TEMPLATE"
    templates_dest.mkdir(parents=True, exist_ok=True)

    installed = 0
    if ISSUE_TEMPLATES_DIR.exists():
        for template_file in ISSUE_TEMPLATES_DIR.glob("*.yml"):
            dest = templates_dest / template_file.name
            if dest.exists() and not force:
                click.echo(f"  · {template_file.stem} template exists (use --force to overwrite)")
            else:
                shutil.copy(template_file, dest)
                click.echo(f"  ✓ Installed {template_file.stem} issue template")
                installed += 1
    else:
        click.echo("  ! Issue templates not found in package")
    return installed


def install_agents_md(project_root: Path, force: bool = False) -> bool:
    """Copy AGENTS.md template to project root. Returns True if installed."""
    agents_template = TEMPLATES_DIR / "AGENTS.md"
    agents_dest = project_root / "AGENTS.md"

    if not agents_template.exists():
        click.echo("  ! AGENTS.md template not found in package")
        return False

    if agents_dest.exists() and not force:
        click.echo("  · AGENTS.md exists (use --force to overwrite)")
        return False

    shutil.copy(agents_template, agents_dest)
    click.echo("  ✓ Installed AGENTS.md")
    return True


def update_claude_md(project_root: Path) -> bool:
    """Append AGENTS.md reference to CLAUDE.md if it exists and doesn't already have it."""
    claude_md = project_root / "CLAUDE.md"

    if not claude_md.exists():
        click.echo("  · CLAUDE.md not found (skipping reference)")
        return False

    content = claude_md.read_text()

    # Check if reference already exists (looking for the link pattern)
    if "AGENTS.md" in content:
        click.echo("  · CLAUDE.md already references AGENTS.md")
        return False

    # Append the reference
    with claude_md.open("a") as f:
        f.write(AGENTS_REFERENCE)

    click.echo("  ✓ Added AGENTS.md reference to CLAUDE.md")
    return True


def update_agents_md(project_root: Path, force: bool = False) -> bool:
    """Update AGENTS.md while preserving PROJECT CONTEXT section.

    If AGENTS.md exists, replaces everything before ## PROJECT CONTEXT
    with the new template content. Preserves user's custom content.

    If AGENTS.md doesn't exist, copies fresh template.

    If force is True, overwrites AGENTS.md with the package template.

    Returns True if updated/created, False otherwise.
    """
    agents_template = TEMPLATES_DIR / "AGENTS.md"
    agents_dest = project_root / "AGENTS.md"

    if not agents_template.exists():
        click.echo("  ! AGENTS.md template not found in package")
        return False

    template_content = agents_template.read_text()

    # Find the marker in the template
    template_marker_idx = template_content.find(AGENTS_PROJECT_CONTEXT_MARKER)
    if template_marker_idx == -1:
        click.echo("  ! Template missing PROJECT CONTEXT marker")
        return False

    # Get the new header content (everything before the marker)
    new_header = template_content[:template_marker_idx]

    if not agents_dest.exists():
        # Fresh install - copy entire template
        shutil.copy(agents_template, agents_dest)
        click.echo("  ✓ Created AGENTS.md (fresh)")
        return True

    if force:
        shutil.copy(agents_template, agents_dest)
        click.echo("  ✓ Overwrote AGENTS.md (--force)")
        return True

    # AGENTS.md exists - merge with preserved user content
    existing_content = agents_dest.read_text()
    existing_marker_idx = existing_content.find(AGENTS_PROJECT_CONTEXT_MARKER)

    if existing_marker_idx == -1:
        # No marker found - append existing content after new template
        # This handles legacy files without the marker
        merged_content = template_content + "\n\n<!-- Legacy content preserved below -->\n" + existing_content
        click.echo("  ⚠ AGENTS.md had no PROJECT CONTEXT marker - content preserved at end")
    else:
        # Preserve everything from the marker onwards
        preserved_content = existing_content[existing_marker_idx:]
        merged_content = new_header + preserved_content

    agents_dest.write_text(merged_content)
    click.echo("  ✓ Updated AGENTS.md (preserved PROJECT CONTEXT)")
    return True


@click.group()
@click.version_option(version="0.1.0", prog_name="Coihuin Spec")
def main():
    """Coihuin Spec - Spec-driven development for the age of coding agents."""
    pass


@main.command()
@click.option("--force", "-f", is_flag=True, help="Overwrite existing files")
def init(force: bool):
    """Initialize spec-driven development in current project.

    Creates directory structure (cspec/specs/ and cspec/work/),
    installs Claude Code slash commands, copies AGENTS.md template,
    and updates CLAUDE.md with reference.
    """
    click.echo(click.style(BANNER, fg="cyan"))

    project_root = Path.cwd()

    # Directories to create
    dirs = [
        project_root / "cspec" / "specs",
        project_root / "cspec" / "work",
        project_root / ".claude" / "commands" / "cspec",
        project_root / ".github" / "ISSUE_TEMPLATE",
    ]

    click.echo("Initializing project...\n")

    # Create directories
    for d in dirs:
        if not d.exists():
            d.mkdir(parents=True)
            click.echo(f"  ✓ Created {d.relative_to(project_root)}/")
        else:
            click.echo(f"  · {d.relative_to(project_root)}/ exists")

    # Install slash commands
    click.echo("\nSlash Commands:")
    install_commands(project_root, force)

    # Install GitHub issue templates
    click.echo("\nGitHub Issue Templates:")
    install_issue_templates(project_root, force)

    # Install AGENTS.md template
    click.echo("\nAgent Configuration:")
    install_agents_md(project_root, force)

    # Update CLAUDE.md with reference to AGENTS.md (if it exists)
    update_claude_md(project_root)

    click.echo("\n✓ Initialization complete!")
    click.echo("\nDirectory structure:")
    click.echo("  cspec/specs/         - Permanent feature specs (source of truth)")
    click.echo("  cspec/work/          - Ephemeral work directories")
    click.echo("  .github/ISSUE_TEMPLATE/ - GitHub issue templates (11 natures)")
    click.echo("\nWorkflow:")
    click.echo("  1. Create issue on GitHub (use templates)")
    click.echo("  2. /cspec:issue-start <github-url>  - Import and classify")
    click.echo("  3. /cspec:proposal-write            - Draft proposal")
    click.echo("  4. /cspec:spec-write                - Write spec")
    click.echo("  5. /cspec:plan-write                - Create impl plan")
    click.echo("  6. /cspec:work-complete             - Merge spec, cleanup")


@main.command()
@click.option("--force", "-f", is_flag=True, help="Overwrite existing files")
def update(force: bool):
    """Update cspec resources to latest version.

    Re-installs slash commands, GitHub issue templates, and refreshes AGENTS.md.
    AGENTS.md is merged to preserve the PROJECT CONTEXT section.
    """
    project_root = Path.cwd()
    commands_dest = project_root / ".claude" / "commands" / "cspec"

    if not commands_dest.exists():
        click.echo("No cspec commands found. Run 'cspec init' first.")
        sys.exit(1)

    click.echo("Updating cspec resources...\n")

    # Update slash commands
    click.echo("Slash Commands:")
    commands_installed = install_commands(project_root, force=force)

    # Update GitHub issue templates
    click.echo("\nGitHub Issue Templates:")
    templates_installed = install_issue_templates(project_root, force=force)

    # Update AGENTS.md
    click.echo("\nAGENTS.md:")
    update_agents_md(project_root, force=force)

    click.echo(f"\n✓ Update complete ({commands_installed} command(s), {templates_installed} template(s) refreshed)")




@main.command()
def status():
    """Check project health and report status.

    Reports on directory structure, specs, and work in progress.
    Exit code 0 if healthy, 1 if issues found.
    """
    project_root = Path.cwd()
    issues_found = False

    click.echo("Coihuin Spec Project Status")
    click.echo("=" * 40)
    click.echo()

    # Check directory structure
    click.echo("Directory Structure:")
    required_dirs = [
        ("cspec/specs/", project_root / "cspec" / "specs"),
        ("cspec/work/", project_root / "cspec" / "work"),
        (".claude/commands/", project_root / ".claude" / "commands"),
    ]

    for name, dir_path in required_dirs:
        if dir_path.exists():
            click.echo(f"  [OK] {name}")
        else:
            click.echo(f"  [MISSING] {name}")
            issues_found = True

    click.echo()

    # Count specs
    specs_dir = project_root / "cspec" / "specs"
    if specs_dir.exists():
        spec_dirs = [d for d in specs_dir.iterdir() if d.is_dir() and (d / "spec.md").exists()]
        click.echo(f"Permanent Specs: {len(spec_dirs)}")
        for spec_dir in sorted(spec_dirs):
            click.echo(f"  • {spec_dir.name}/spec.md")
    else:
        click.echo("Permanent Specs: (directory missing)")

    click.echo()

    # Count work in progress
    work_dir = project_root / "cspec" / "work"
    if work_dir.exists():
        work_dirs = [d for d in work_dir.iterdir() if d.is_dir()]
        click.echo(f"Work in Progress: {len(work_dirs)}")
        for wd in sorted(work_dirs):
            # Check what's in the work directory
            has_issue = (wd / "issue.md").exists()
            spec_files = list(wd.glob("spec-*.md"))
            status_parts = []
            if has_issue:
                status_parts.append("issue")
            if spec_files:
                status_parts.append(f"{len(spec_files)} spec(s)")
            status_str = ", ".join(status_parts) if status_parts else "empty"
            click.echo(f"  • {wd.name}/ ({status_str})")
    else:
        click.echo("Work in Progress: (directory missing)")

    click.echo()

    # Check AGENTS.md
    agents = project_root / "AGENTS.md"
    if agents.exists():
        click.echo(f"AGENTS.md: [OK]")
    else:
        click.echo(f"AGENTS.md: [MISSING]")
        issues_found = True

    click.echo()

    # Summary
    click.echo("=" * 40)
    if issues_found:
        click.echo("Status: ISSUES FOUND")
        click.echo("\nRun 'cspec init' to create missing directories.")
        sys.exit(1)
    else:
        click.echo("Status: HEALTHY")
        sys.exit(0)


ONBOARD_PROMPT = '''# Project Onboarding

You are onboarding to a spec-driven development project. This command helps populate the AGENTS.md PROJECT CONTEXT section with codebase analysis.

## Process

### Step 1: Check Project Status

Run `cspec status` to assess the current state:

```bash
cspec status
```

Review:
- Whether cspec/specs/ and cspec/work/ directories exist
- What permanent specs exist
- What work is in progress

### Step 2: Analyze the Codebase

Explore the project to gather context for AGENTS.md. Analyze:

1. **Project Structure**: Examine directory layout and organization
2. **Tech Stack**: Identify languages from file extensions, package files (package.json, pyproject.toml, Cargo.toml, go.mod, etc.)
3. **Architecture**: Look for architectural patterns, key modules, entry points
4. **Conventions**: Check for linting configs, formatting rules, naming patterns
5. **Important Files**: Identify entry points, configuration files, core modules
6. **Testing**: Find test directories, test frameworks, test commands
7. **Build/Deploy**: Check for build scripts, CI/CD configs, deployment files
8. **Existing Specs**: Review any specs in cspec/specs/

### Step 3: Update AGENTS.md PROJECT CONTEXT

Find the `## PROJECT CONTEXT` section in AGENTS.md and populate it:

```markdown
## PROJECT CONTEXT

### Project Overview

<Brief description from codebase analysis>

### Tech Stack

- **Languages**: <list languages>
- **Frameworks**: <list frameworks>
- **Key Dependencies**: <list important dependencies>
- **Package Manager**: <npm/pip/cargo/etc>

### Architecture

<Describe high-level architecture>
- Entry points: <main files>
- Key modules: <core components>
- Data flow: <how data moves through the system>

### Key Conventions

- **Naming**: <camelCase/snake_case/PascalCase patterns>
- **File Structure**: <how files are organized>
- **Patterns**: <design patterns used>

### Important Files

| File | Purpose |
|------|---------|
| <path> | <description> |

### Testing

- **Framework**: <test framework>
- **Run Tests**: `<test command>`
- **Test Location**: <test directory>

### Build & Deploy

- **Build**: `<build command>`
- **Dev Server**: `<dev command>`

### Domain Knowledge

<Project-specific terminology, business logic, domain concepts>
```

### Step 4: Summary

Output what was done:
- Directory structure status
- Existing specs found
- AGENTS.md PROJECT CONTEXT populated
- Next steps: Start work with /cspec:work-start

## Notes

- The goal is to give coding agents enough context to work effectively
- Preserve existing content - don\'t overwrite user customizations
- Ask clarifying questions when information is ambiguous
'''


@main.command()
@click.option("--force", "-f", is_flag=True, help="Run onboarding even if already onboarded")
def onboard(force: bool):
    """Onboard to a spec-driven project.

    Checks if AGENTS.md PROJECT CONTEXT is populated.
    Outputs the LLM prompt for Claude to execute the onboarding process.
    """
    project_root = Path.cwd()

    # Check if AGENTS.md exists and has PROJECT CONTEXT filled
    agents_md = project_root / "AGENTS.md"
    is_onboarded = False

    if agents_md.exists():
        content = agents_md.read_text()
        # Check if PROJECT CONTEXT section has actual content (not just the header)
        if "## PROJECT CONTEXT" in content:
            # Look for subsections that indicate it's been filled
            if "### Project Overview" in content and "### Tech Stack" in content:
                # Check if there's actual content (not just placeholders)
                overview_match = content.find("### Project Overview")
                tech_match = content.find("### Tech Stack")
                if overview_match < tech_match:
                    between = content[overview_match:tech_match]
                    # If there's substantial content between sections, consider it onboarded
                    if len(between.strip().split("\n")) > 3:
                        is_onboarded = True

    if is_onboarded and not force:
        click.echo("Project appears to be already onboarded.")
        click.echo("AGENTS.md PROJECT CONTEXT section has content.")
        click.echo()
        click.echo("Use --force to re-run onboarding anyway.")
        sys.exit(0)

    # Output the onboarding prompt for Claude to execute
    if is_onboarded and force:
        click.echo("# Re-running onboarding (--force)")
        click.echo()

    click.echo(ONBOARD_PROMPT)


@main.group()
def templates():
    """Commands for querying issue templates."""
    pass


@templates.command("list")
def templates_list():
    """List all available issue templates."""
    if not ISSUE_TEMPLATES_DIR.exists():
        click.echo("No issue templates found in package.")
        sys.exit(1)

    template_files = sorted(ISSUE_TEMPLATES_DIR.glob("*.yml"))

    if not template_files:
        click.echo("No issue templates found.")
        sys.exit(1)

    click.echo(f"Available issue templates ({len(template_files)}):\n")

    for tf in template_files:
        content = yaml.safe_load(tf.read_text())
        name = tf.stem
        description = content.get("description", "No description")
        labels = content.get("labels", [])
        labels_str = f" [{', '.join(labels)}]" if labels else ""

        click.echo(f"  {name}")
        click.echo(f"    {description}{labels_str}")


@templates.command("get")
@click.argument("name")
@click.option("--format", "-f", "output_format", type=click.Choice(["markdown", "yaml", "json"]), default="markdown", help="Output format")
def templates_get(name: str, output_format: str):
    """Get an issue template by name.

    Outputs a fillable template that agents can use to create issues.

    Examples:
        cspec templates get feature
        cspec templates get bug --format yaml
    """
    import json as json_module

    template_file = ISSUE_TEMPLATES_DIR / f"{name}.yml"

    if not template_file.exists():
        click.echo(f"Template not found: {name}", err=True)
        available = [f.stem for f in ISSUE_TEMPLATES_DIR.glob("*.yml")]
        if available:
            click.echo(f"Available: {', '.join(sorted(available))}", err=True)
        sys.exit(1)

    content = yaml.safe_load(template_file.read_text())

    if output_format == "yaml":
        click.echo(template_file.read_text())
        return

    if output_format == "json":
        click.echo(json_module.dumps(content, indent=2))
        return

    # Markdown format - convert to fillable template
    template_name = content.get("name", name.title())
    description = content.get("description", "")

    lines = [f"# {template_name}", ""]
    if description:
        lines.append(f"> {description}")
        lines.append("")

    body = content.get("body", [])
    for field in body:
        field_type = field.get("type")
        attrs = field.get("attributes", {})
        validations = field.get("validations", {})

        label = attrs.get("label", "")
        field_desc = attrs.get("description", "")
        placeholder = attrs.get("placeholder", "")
        required = validations.get("required", False)
        options = attrs.get("options", [])

        # Section header
        req_marker = " *" if required else ""
        lines.append(f"## {label}{req_marker}")

        # Description as comment
        if field_desc:
            lines.append(f"<!-- {field_desc} -->")

        # Options for dropdowns
        if field_type == "dropdown" and options:
            opts_str = ", ".join(options)
            lines.append(f"<!-- Options: {opts_str} -->")
            lines.append("")
            lines.append(f"[SELECT: {opts_str}]")

        # Placeholder content
        elif placeholder:
            lines.append("")
            lines.append(placeholder.rstrip())

        else:
            lines.append("")

        lines.append("")

    click.echo("\n".join(lines))


@main.group()
def specs():
    """Commands for managing permanent specs."""
    pass


@specs.command("list")
def specs_list():
    """List all permanent specs."""
    specs_dir = Path.cwd() / "cspec" / "specs"

    if not specs_dir.exists():
        click.echo("No cspec/specs directory found. Run 'cspec init' first.")
        sys.exit(1)

    spec_dirs = [d for d in specs_dir.iterdir() if d.is_dir() and (d / "spec.md").exists()]

    if not spec_dirs:
        click.echo("No specs found.")
        click.echo("\nCreate a spec by starting work: /cspec:work-start <slug> <description>")
        return

    click.echo(f"Found {len(spec_dirs)} spec(s):\n")

    for spec_dir in sorted(spec_dirs):
        spec_file = spec_dir / "spec.md"
        # Read first line to get title
        content = spec_file.read_text()
        first_line = content.split("\n")[0].strip()
        if first_line.startswith("#"):
            title = first_line.lstrip("#").strip()
        else:
            title = spec_dir.name

        # Count diagrams
        diagrams = list(spec_dir.glob("*.mmd"))
        diagram_str = f" (+{len(diagrams)} diagrams)" if diagrams else ""

        click.echo(f"  {spec_dir.name}/")
        click.echo(f"    {title}{diagram_str}")


@specs.command("show")
@click.argument("feature")
def specs_show(feature: str):
    """Show a feature spec."""
    spec_dir = Path.cwd() / "cspec" / "specs" / feature

    if not spec_dir.exists():
        click.echo(f"Spec not found: {feature}")
        # Suggest similar
        specs_dir = Path.cwd() / "cspec" / "specs"
        if specs_dir.exists():
            existing = [d.name for d in specs_dir.iterdir() if d.is_dir()]
            if existing:
                click.echo(f"\nAvailable specs: {', '.join(sorted(existing))}")
        sys.exit(1)

    spec_file = spec_dir / "spec.md"
    if not spec_file.exists():
        click.echo(f"No spec.md found in {feature}/")
        sys.exit(1)

    content = spec_file.read_text()
    click.echo(content)

    # List diagrams
    diagrams = list(spec_dir.glob("*.mmd"))
    if diagrams:
        click.echo("\n---")
        click.echo("Diagrams:")
        for d in diagrams:
            click.echo(f"  • {d.name}")


@main.group()
def work():
    """Commands for managing work in progress."""
    pass


@work.command("list")
def work_list():
    """List all work in progress."""
    work_dir = Path.cwd() / "cspec" / "work"

    if not work_dir.exists():
        click.echo("No cspec/work directory found. Run 'cspec init' first.")
        sys.exit(1)

    work_dirs = [d for d in work_dir.iterdir() if d.is_dir()]

    if not work_dirs:
        click.echo("No work in progress.")
        click.echo("\nStart work: /cspec:work-start <slug> <description>")
        return

    click.echo(f"Found {len(work_dirs)} work item(s):\n")

    for wd in sorted(work_dirs):
        # Check contents
        has_issue = (wd / "issue.md").exists()
        has_proposal = (wd / "proposal.md").exists()
        spec_files = list(wd.glob("spec-*.md"))
        context_files = list((wd / "context").glob("*.md")) if (wd / "context").exists() else []

        parts = []
        if has_issue:
            parts.append("issue")
        if has_proposal:
            parts.append("proposal")
        if spec_files:
            parts.append(f"{len(spec_files)} spec(s)")
        if context_files:
            parts.append(f"{len(context_files)} context")

        status_str = ", ".join(parts) if parts else "empty"
        click.echo(f"  {wd.name}/ ({status_str})")


@work.command("show")
@click.argument("slug")
def work_show(slug: str):
    """Show details of a work item."""
    work_item = Path.cwd() / "cspec" / "work" / slug

    if not work_item.exists():
        click.echo(f"Work item not found: {slug}")
        # Suggest similar
        work_dir = Path.cwd() / "cspec" / "work"
        if work_dir.exists():
            existing = [d.name for d in work_dir.iterdir() if d.is_dir()]
            if existing:
                click.echo(f"\nAvailable work items: {', '.join(sorted(existing))}")
        sys.exit(1)

    click.echo(click.style(f"═══ Work: {slug} ═══", fg="cyan", bold=True))
    click.echo()

    # Show issue if exists
    issue_file = work_item / "issue.md"
    if issue_file.exists():
        click.echo(click.style("Issue:", underline=True))
        content = issue_file.read_text()
        # Show first few lines
        lines = content.split("\n")[:10]
        for line in lines:
            click.echo(f"  {line}")
        if len(content.split("\n")) > 10:
            click.echo("  ...")
        click.echo()

    # Show proposal if exists
    proposal_file = work_item / "proposal.md"
    if proposal_file.exists():
        click.echo(click.style("Proposal:", underline=True))
        click.echo(f"  {proposal_file.name} exists")
        click.echo()

    # Show specs
    spec_files = list(work_item.glob("spec-*.md"))
    if spec_files:
        click.echo(click.style("Specs:", underline=True))
        for sf in sorted(spec_files):
            feature = sf.stem.replace("spec-", "")
            click.echo(f"  • {sf.name} → cspec/specs/{feature}/spec.md")
        click.echo()

    # Show context
    context_dir = work_item / "context"
    if context_dir.exists():
        context_files = list(context_dir.glob("*.md"))
        if context_files:
            click.echo(click.style("Context:", underline=True))
            for cf in sorted(context_files):
                click.echo(f"  • {cf.name}")
            click.echo()


if __name__ == "__main__":
    main()
