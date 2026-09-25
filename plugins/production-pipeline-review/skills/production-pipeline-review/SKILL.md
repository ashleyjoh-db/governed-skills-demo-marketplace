---
name: production-pipeline-review
description: Review Python or SQL data pipeline code against the bundled fictional production standards. Use for production-readiness reviews of pipeline implementations or pull requests, not for incident diagnosis or deployment.
---

# Production pipeline review

Review pipeline code against this skill's approved production standards.

## Required references

Before reviewing code, read:

- [Production standards](references/production-standards.md)
- [Review rubric](references/review-rubric.md)

The references define the complete review scope and required output.

## Review rules

- Evaluate every bundled standard against the supplied code.
- Cite the rule ID and concrete code evidence for each finding.
- Mark missing evidence as `Unknown` rather than assuming an implementation exists elsewhere.
- Report required changes separately from optional suggestions.
- Do not introduce generic best practices as requirements. These are fictional organizational standards, not universal Databricks requirements.
- Do not modify, execute, or deploy the pipeline unless the user separately asks for that work.
