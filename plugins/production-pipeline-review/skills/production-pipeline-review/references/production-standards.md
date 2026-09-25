# Production pipeline standards

Standards version: 1.0

These are fictional organizational standards created for the governed-skills demonstration. They are not universal Databricks requirements.

## PR-001: Configure production input locations

Production input locations must come from deployment configuration rather than a path hardcoded in pipeline source code.

Pass when the reviewed code obtains the input location from a parameter, environment-specific configuration, or another clearly externalized setting.

## PR-002: Add ingestion metadata

Every bronze record must include:

- The time it was ingested.
- The source file or source object identifier.

Pass when both values are added to the output records by the pipeline.

## PR-003: Quarantine invalid sensor records

The pipeline must identify and route invalid records to a quarantine destination. At minimum, it must handle:

- Missing `device_id`.
- Missing or invalid `event_time`.
- Sensor measurements outside the documented operating range.

Silently dropping invalid records does not satisfy this standard.

## PR-004: Declare purpose and ownership

The published table definition must declare:

- A short description of the table's purpose.
- The team responsible for the table.

Pass when both values are present in the pipeline definition or metadata declared alongside it.
