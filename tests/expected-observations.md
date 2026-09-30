# Expected observations for standards version 2.0

The fixed test pipeline should be assessed as `Not ready` with these five findings:

| Rule | Expected result | Evidence to identify |
|---|---|---|
| `PR-001` | `Fail` | `SOURCE_PATH` contains a hardcoded production volume path. |
| `PR-002` | `Fail` | The selected output has no ingestion timestamp or source-file identifier. |
| `PR-003` | `Fail` | The pipeline has no validation or quarantine path for invalid sensor records. |
| `PR-004` | `Fail` | The table definition declares neither its purpose nor its owning team. |
| `PR-005` | `Fail` | The pipeline declares no source-contract version and provides no quarantine path for unexpected fields or incompatible type changes. |

The reviewer should not introduce unrelated requirements, modify the code, or claim that the example represents universal Databricks guidance.
