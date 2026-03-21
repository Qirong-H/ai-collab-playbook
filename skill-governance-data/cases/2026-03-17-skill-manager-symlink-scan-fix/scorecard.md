# Scorecard

- Skill: skill-manager
- Version: unversioned
- Auditor: Codex
- Date: 2026-03-17

| Dimension | Score | Notes |
|---|---:|---|
| Trigger Fit | 10 | Description was understandable but did not clearly express routing boundaries or real trigger phrases. |
| Scope Discipline | 14 | The skill had one coherent job, but mixed inventory, categorization, enable/disable, and stats without enough boundary language. |
| Progressive Disclosure | 10 | Body length was manageable, but there were no references or scripts linked from `SKILL.md` to separate core instructions from implementation detail. |
| Structural Integrity | 11 | The directory and scripts existed, but the skill lacked versioning and the scanner missed symlinked directories in real use. |
| Empirical Gain | 8 | Real utility is clear because catalog management is valuable, but this case exposed a concrete blind spot in the scanner. |
| Maintenance Cost | 10 | The maintenance cost is acceptable, but the skill must track real filesystem patterns such as symlinked skill folders. |
| Total | 63 | Matches the first static audit baseline. |

## Strongest keep evidence

The skill already owns a high-leverage workflow: category cataloging and enable/disable governance for a large local skill collection.

## Strongest disable evidence

Without correct scanning, the catalog becomes stale or misleading, which undermines the entire governance loop.

## Nearest competing skill

`skills-governance` is the nearest neighbor. It is stronger on inventory truth and keep/disable/archive reasoning, while `skill-manager` is stronger on category persistence and stateful enable/disable operations.

## Routing / content / scope diagnosis

Primary problem: routing and specification quality were weaker than the underlying idea. The first fix should be versioning, clearer boundaries, and scanner correctness, not a full rewrite.
