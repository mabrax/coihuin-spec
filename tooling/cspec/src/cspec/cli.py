"""Coihuin Spec - Spec-driven development for the age of coding agents."""

import re
import shutil
import sys
from pathlib import Path

import click
import yaml
from pydantic import ValidationError

from cspec.schemas import (
    IssueFrontmatter,
    REQUIRED_CONTEXT_BY_NATURE,
    Nature,
)

# Package directory for bundled resources
PACKAGE_DIR = Path(__file__).parent
COMMANDS_DIR = PACKAGE_DIR / "commands" / "cspec"
TEMPLATES_DIR = PACKAGE_DIR / "templates"

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


def install_commands(project_root: Path, force: bool = False) -> int:
    """Install slash commands to project. Returns count of installed commands."""
    commands_dest = project_root / ".claude" / "commands" / "cspec"
    commands_dest.mkdir(parents=True, exist_ok=True)

    installed = 0
    if COMMANDS_DIR.exists():
        for cmd_file in COMMANDS_DIR.glob("*.md"):
            dest = commands_dest / cmd_file.name
            if dest.exists() and not force:
                click.echo(f"  · /{cmd_file.stem} exists (use --force to overwrite)")
            else:
                shutil.copy(cmd_file, dest)
                click.echo(f"  ✓ Installed /{cmd_file.stem} (cspec:{cmd_file.stem})")
                installed += 1
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

    Creates directory structure, installs Claude Code slash commands,
    copies AGENTS.md template, and updates CLAUDE.md with reference.
    """
    click.echo(click.style(BANNER, fg="cyan"))

    project_root = Path.cwd()

    # Directories to create
    dirs = [
        project_root / "specs" / "issues",
        project_root / ".claude" / "commands" / "cspec",
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
    install_commands(project_root, force)

    # Install AGENTS.md template
    install_agents_md(project_root, force)

    # Update CLAUDE.md with reference to AGENTS.md (if it exists)
    update_claude_md(project_root)

    click.echo("\n✓ Initialization complete!")
    click.echo("\nNext steps:")
    click.echo("  1. Run /cspec/init to create PROJECT.yaml and CONSTITUTION.md")
    click.echo("  2. Run /cspec/issue-create <description> to create your first issue")
    click.echo("\nNote: Commands are namespaced as cspec/<command>")


@main.command()
@click.option("--force", "-f", is_flag=True, help="Overwrite existing files")
def update(force: bool):
    """Update cspec resources to latest version.

    Re-installs slash commands and refreshes AGENTS.md from the cspec package.
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
    installed = install_commands(project_root, force=force)

    # Update AGENTS.md
    click.echo("\nAGENTS.md:")
    update_agents_md(project_root, force=force)

    click.echo(f"\n✓ Update complete ({installed} command(s) refreshed)")


@main.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("--strict", "-s", is_flag=True, help="Fail on warnings too")
def validate(path: str, strict: bool):
    """Validate an issue file against the schema.

    PATH is the path to the issue markdown file.
    """
    issue_path = Path(path)

    click.echo(f"Validating {issue_path.name}...\n")

    # Read file
    content = issue_path.read_text()

    # Extract YAML frontmatter
    frontmatter_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not frontmatter_match:
        click.echo("❌ FAIL: No YAML frontmatter found")
        click.echo("   Issue files must start with ---\\n<yaml>\\n---")
        sys.exit(1)

    frontmatter_str = frontmatter_match.group(1)

    # Parse YAML
    try:
        frontmatter_data = yaml.safe_load(frontmatter_str)
    except yaml.YAMLError as e:
        click.echo(f"❌ FAIL: Invalid YAML in frontmatter")
        click.echo(f"   {e}")
        sys.exit(1)

    # Validate against schema
    errors = []
    warnings = []

    try:
        issue = IssueFrontmatter(**frontmatter_data)
        click.echo("Schema Validation:")
        click.echo("  ✓ ID format valid")
        click.echo("  ✓ Title present and under 100 chars")
        click.echo("  ✓ Nature valid")
        click.echo("  ✓ Impact valid")
        click.echo("  ✓ Version matches impact")
        click.echo("  ✓ Status valid")
        click.echo("  ✓ Dates valid")
    except ValidationError as e:
        click.echo("Schema Validation:")
        for error in e.errors():
            loc = ".".join(str(x) for x in error["loc"])
            msg = error["msg"]
            errors.append(f"{loc}: {msg}")
            click.echo(f"  ✗ {loc}: {msg}")

    # Check body sections
    click.echo("\nBody Validation:")
    body = content[frontmatter_match.end():]

    if "## Problem" in body:
        problem_section = re.search(r"## Problem\n+(.*?)(?=\n## |\Z)", body, re.DOTALL)
        if problem_section and problem_section.group(1).strip():
            click.echo("  ✓ Problem section present")
        else:
            errors.append("Problem section is empty")
            click.echo("  ✗ Problem section is empty")
    else:
        errors.append("Missing ## Problem section")
        click.echo("  ✗ Missing ## Problem section")

    if "## Scope" in body:
        click.echo("  ✓ Scope section present")
        if "### In Scope" in body:
            in_scope = re.search(r"### In Scope\n+(.*?)(?=\n### |\n## |\Z)", body, re.DOTALL)
            if in_scope and ("- [" in in_scope.group(1) or "- " in in_scope.group(1)):
                click.echo("  ✓ In-scope items defined")
            else:
                errors.append("No in-scope items defined")
                click.echo("  ✗ No in-scope items defined")
        else:
            errors.append("Missing ### In Scope subsection")
            click.echo("  ✗ Missing ### In Scope subsection")
    else:
        errors.append("Missing ## Scope section")
        click.echo("  ✗ Missing ## Scope section")

    if "## Acceptance Criteria" in body:
        ac_section = re.search(r"## Acceptance Criteria\n+(.*?)(?=\n## |\Z)", body, re.DOTALL)
        if ac_section and ("- [" in ac_section.group(1) or "- " in ac_section.group(1)):
            click.echo("  ✓ Acceptance criteria defined")
        else:
            errors.append("No acceptance criteria defined")
            click.echo("  ✗ No acceptance criteria defined")
    else:
        errors.append("Missing ## Acceptance Criteria section")
        click.echo("  ✗ Missing ## Acceptance Criteria section")

    # Check nature-specific context requirements
    if 'issue' in dir() and issue:
        nature = issue.nature
        required_ctx = REQUIRED_CONTEXT_BY_NATURE.get(nature, [])
        if required_ctx:
            click.echo(f"\nNature-Specific Requirements ({nature.value}):")
            provided_types = {ref.type for ref in issue.context.required}
            for ctx_type in required_ctx:
                if ctx_type in provided_types:
                    click.echo(f"  ✓ {ctx_type} referenced")
                else:
                    warnings.append(f"Missing recommended context: {ctx_type}")
                    click.echo(f"  ⚠ {ctx_type} not referenced (recommended)")

    # Summary
    click.echo("\n" + "=" * 40)
    if errors:
        click.echo(f"❌ VALIDATION FAILED - {len(errors)} error(s)")
        for err in errors:
            click.echo(f"   • {err}")
        sys.exit(1)
    elif warnings and strict:
        click.echo(f"❌ VALIDATION FAILED (strict mode) - {len(warnings)} warning(s)")
        for warn in warnings:
            click.echo(f"   • {warn}")
        sys.exit(1)
    elif warnings:
        click.echo(f"⚠ VALIDATION PASSED with {len(warnings)} warning(s)")
        sys.exit(0)
    else:
        click.echo("✓ VALIDATION PASSED")
        sys.exit(0)


def _check_file_status(path: Path) -> str:
    """Check if a file is missing, empty, or filled.

    Returns: 'missing', 'empty', or 'filled'
    """
    if not path.exists():
        return "missing"
    content = path.read_text().strip()
    if not content:
        return "empty"
    return "filled"


def _check_yaml_status(path: Path) -> str:
    """Check if a YAML file is missing, empty, has only comments/placeholders, or is filled.

    Returns: 'missing', 'empty', or 'filled'
    """
    if not path.exists():
        return "missing"
    content = path.read_text().strip()
    if not content:
        return "empty"

    # Check if it's just comments or placeholder content
    try:
        data = yaml.safe_load(content)
        if data is None or data == {}:
            return "empty"
        # Check for placeholder values (common patterns)
        if isinstance(data, dict):
            values = list(data.values())
            # If all values are None, empty strings, or placeholder markers
            if all(v is None or v == "" or v == "TODO" or v == "TBD" for v in values):
                return "empty"
        return "filled"
    except yaml.YAMLError:
        # If YAML is invalid, consider it empty/problematic
        return "empty"


@main.command()
def status():
    """Check project health and report status.

    Reports on directory structure, PROJECT.yaml, CONSTITUTION.md, and AGENTS.md.
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
        ("specs/", project_root / "specs"),
        ("specs/issues/", project_root / "specs" / "issues"),
        (".claude/commands/", project_root / ".claude" / "commands"),
    ]

    for name, dir_path in required_dirs:
        if dir_path.exists():
            click.echo(f"  [OK] {name}")
        else:
            click.echo(f"  [MISSING] {name}")
            issues_found = True

    click.echo()

    # Check PROJECT.yaml
    click.echo("Configuration Files:")
    project_yaml = project_root / "PROJECT.yaml"
    project_status = _check_yaml_status(project_yaml)
    if project_status == "filled":
        click.echo(f"  [OK] PROJECT.yaml (filled)")
    elif project_status == "empty":
        click.echo(f"  [WARN] PROJECT.yaml (empty - needs configuration)")
        issues_found = True
    else:
        click.echo(f"  [MISSING] PROJECT.yaml")
        issues_found = True

    # Check CONSTITUTION.md
    constitution = project_root / "CONSTITUTION.md"
    constitution_status = _check_file_status(constitution)
    if constitution_status == "filled":
        click.echo(f"  [OK] CONSTITUTION.md (filled)")
    elif constitution_status == "empty":
        click.echo(f"  [WARN] CONSTITUTION.md (empty - needs content)")
        issues_found = True
    else:
        click.echo(f"  [MISSING] CONSTITUTION.md")
        issues_found = True

    # Check AGENTS.md
    agents = project_root / "AGENTS.md"
    if agents.exists():
        click.echo(f"  [OK] AGENTS.md (exists)")
    else:
        click.echo(f"  [MISSING] AGENTS.md")
        issues_found = True

    click.echo()

    # Summary
    click.echo("=" * 40)
    if issues_found:
        click.echo("Status: ISSUES FOUND")
        click.echo("\nRun 'cspec init' to create missing directories.")
        click.echo("Use '/cspec:init' slash command to create configuration files.")
        sys.exit(1)
    else:
        click.echo("Status: HEALTHY")
        sys.exit(0)


@main.command("list")
@click.option("--status", "-s", type=str, help="Filter by status")
def list_issues(status: str):
    """List all issues in the project."""
    issues_dir = Path.cwd() / "specs" / "issues"

    if not issues_dir.exists():
        click.echo("No specs/issues directory found. Run 'cspec init' first.")
        sys.exit(1)

    issues = list(issues_dir.glob("ISSUE-*.md"))

    if not issues:
        click.echo("No issues found.")
        return

    click.echo(f"Found {len(issues)} issue(s):\n")

    for issue_path in sorted(issues):
        content = issue_path.read_text()
        frontmatter_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if frontmatter_match:
            try:
                data = yaml.safe_load(frontmatter_match.group(1))
                issue_status = data.get("status", "unknown")
                if status and issue_status != status:
                    continue
                title = data.get("title", "Untitled")
                nature = data.get("nature", "unknown")
                click.echo(f"  {data.get('id', issue_path.stem)} [{issue_status}] ({nature})")
                click.echo(f"    {title}")
            except yaml.YAMLError:
                click.echo(f"  {issue_path.stem} [error parsing]")


if __name__ == "__main__":
    main()
