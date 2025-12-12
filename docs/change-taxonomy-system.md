# Development Change Taxonomy System

## Purpose

Classify development changes by combining **nature**, **impact**, and **versioning** to derive appropriate workflows.

---

## Dimension 1: Nature of Change

What kind of work is this?

| Type | Definition |
|------|------------|
| **Feature** | New capability that didn't exist before |
| **Enhancement** | Improvement to existing functionality |
| **Bug Fix** | Correction of defective behavior |
| **Refactor** | Code restructuring without behavioral change |
| **Optimization** | Improving speed, memory, or resource efficiency |
| **Security Patch** | Addressing vulnerabilities |
| **Hotfix** | Urgent production fix (bypasses normal release cycle) |
| **Migration** | Moving data, infrastructure, or dependencies |
| **Configuration** | Adjusting settings without code changes |
| **Deprecation** | Marking functionality for future removal |
| **Removal** | Eliminating deprecated functionality |

---

## Dimension 2: Breaking Impact

Does this require consumers to change?

| Impact | Definition |
|--------|------------|
| **Breaking** | Consumers must modify their code or behavior |
| **Additive** | New surface area; existing behavior unchanged |
| **Invisible** | No external-facing change |

---

## Dimension 3: Semantic Version

What version increment results?

| Version | When |
|---------|------|
| **Major** | Breaking changes |
| **Minor** | Additive changes |
| **Patch** | Invisible changes (fixes, internal refactors) |

---

## Combining Dimensions

Each change is classified as: **Nature + Impact → Version**

Examples:

| Nature | Impact | Version | Example |
|--------|--------|---------|---------|
| Feature | Breaking | Major | New auth system replacing old one |
| Feature | Additive | Minor | New optional endpoint |
| Enhancement | Breaking | Major | Required parameter added |
| Enhancement | Additive | Minor | Optional parameter added |
| Bug Fix | Invisible | Patch | Fixing incorrect calculation |
| Refactor | Invisible | Patch | Internal code cleanup |
| Removal | Breaking | Major | Dropping deprecated API |
