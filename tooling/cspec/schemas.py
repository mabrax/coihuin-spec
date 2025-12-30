"""Pydantic schemas for spec-driven development artifacts."""

from datetime import date
from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field, model_validator


class Nature(str, Enum):
    """Type of change."""
    FEATURE = "feature"
    ENHANCEMENT = "enhancement"
    BUG = "bug"
    REFACTOR = "refactor"
    OPTIMIZATION = "optimization"
    SECURITY = "security"
    HOTFIX = "hotfix"
    MIGRATION = "migration"
    CONFIGURATION = "configuration"
    DEPRECATION = "deprecation"
    REMOVAL = "removal"


class Impact(str, Enum):
    """Consumer impact level."""
    BREAKING = "breaking"
    ADDITIVE = "additive"
    INVISIBLE = "invisible"


class Version(str, Enum):
    """Semantic version increment."""
    MAJOR = "major"
    MINOR = "minor"
    PATCH = "patch"


class Status(str, Enum):
    """Issue lifecycle status."""
    DRAFT = "draft"
    READY = "ready"
    IN_PROGRESS = "in-progress"
    BLOCKED = "blocked"
    DONE = "done"


# Impact to version mapping
IMPACT_VERSION_MAP = {
    Impact.BREAKING: Version.MAJOR,
    Impact.ADDITIVE: Version.MINOR,
    Impact.INVISIBLE: Version.PATCH,
}


class ContextReference(BaseModel):
    """Reference to a context document."""
    type: str
    path: str


class IssueContext(BaseModel):
    """Context references for an issue."""
    required: list[ContextReference] = Field(default_factory=list)
    recommended: list[ContextReference] = Field(default_factory=list)


class IssueFrontmatter(BaseModel):
    """YAML frontmatter schema for issues."""
    id: str = Field(pattern=r"^ISSUE-\d{3,}$")
    title: str = Field(min_length=1, max_length=100)
    nature: Nature
    impact: Impact
    version: Version
    status: Status = Status.DRAFT
    created: date
    updated: date
    context: IssueContext = Field(default_factory=IssueContext)
    depends_on: list[str] = Field(default_factory=list)
    blocks: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def validate_version_matches_impact(self) -> "IssueFrontmatter":
        """Ensure version matches impact level."""
        expected = IMPACT_VERSION_MAP[self.impact]
        if self.version != expected:
            raise ValueError(
                f"Version mismatch: impact '{self.impact.value}' requires "
                f"version '{expected.value}', got '{self.version.value}'"
            )
        return self

    @model_validator(mode="after")
    def validate_updated_after_created(self) -> "IssueFrontmatter":
        """Ensure updated date is >= created date."""
        if self.updated < self.created:
            raise ValueError(
                f"Updated date ({self.updated}) cannot be before "
                f"created date ({self.created})"
            )
        return self


# Required context types by nature
REQUIRED_CONTEXT_BY_NATURE: dict[Nature, list[str]] = {
    Nature.BUG: ["rca"],
    Nature.FEATURE: ["problem-statement"],
    Nature.ENHANCEMENT: ["current-behavior", "delta-description"],
    Nature.REFACTOR: ["architecture-scope", "behavioral-equivalence"],
    Nature.OPTIMIZATION: ["baseline-metrics", "target-metrics", "measurement-method"],
    Nature.SECURITY: ["vulnerability-report", "attack-vector", "severity", "affected-versions"],
    Nature.HOTFIX: ["incident-reference", "impact-assessment", "rollback-plan"],
    Nature.MIGRATION: ["current-state", "target-state", "transformation-rules", "rollback-plan"],
    Nature.CONFIGURATION: ["current-config", "new-config", "impact-assessment"],
    Nature.DEPRECATION: ["sunset-timeline", "migration-path", "consumer-impact"],
    Nature.REMOVAL: ["deprecation-reference", "migration-confirmation", "impact-assessment"],
}
