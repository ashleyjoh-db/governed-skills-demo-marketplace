# Review rubric

Evaluate only the rules in `production-standards.md`.

Use these results:

- `Fail`: the supplied code clearly violates the rule.
- `Unknown`: the supplied material does not contain enough evidence to decide.
- `Pass`: the supplied code clearly satisfies the rule.

When the user asks for violations only, report `Fail` and `Unknown` results and omit passing rules.

Use this format:

## Production readiness

State `Ready` only when every rule passes. Otherwise state `Not ready`.

## Required findings

| Rule | Result | Code evidence | Required change |
|---|---|---|---|

Keep evidence specific to the supplied code. Do not invent missing files, configuration, or deployment behavior.

## Optional observations

Include this section only when the user asks for advice beyond the approved standards. Clearly label every item as optional.
