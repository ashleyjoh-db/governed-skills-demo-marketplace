# Governed skills demo marketplace

A small, synthetic plugin marketplace for testing how Git-authored agent skills can be synchronized to Unity Catalog and consumed through Unity Gateway.

The repository deliberately contains one skill, `production-pipeline-review`. It reviews a fixed factory-telemetry pipeline against a short set of fictional production standards. The example is intentionally simple because the focus is skill publication, governance, discovery, and updates rather than pipeline implementation.

## Repository layout

```text
.claude-plugin/marketplace.json
plugins/production-pipeline-review/
  .claude-plugin/plugin.json
  skills/production-pipeline-review/
    SKILL.md
    references/
      production-standards.md
      review-rubric.md
tests/
  sample-pipeline.py
  expected-observations.md
```

## Fixed test prompt

> Review `tests/sample-pipeline.py` using the governed `production-pipeline-review` skill. Do not modify the code. Report only violations of the bundled production standards, cite each rule ID, and conclude whether the pipeline is ready for production.

The production standards are fictional organizational conventions created for this demonstration. They are not universal Databricks requirements.
