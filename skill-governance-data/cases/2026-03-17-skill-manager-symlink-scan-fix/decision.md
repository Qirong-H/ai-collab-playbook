# Decision

- Skill: skill-manager
- Old version: unversioned
- New version: 0.2.0
- Primary decision: keep-disabled
- Confidence: medium-high

## Why this decision

`skill-manager` is worth keeping because it owns category persistence and operational enable/disable workflows that `skills-governance` does not replace. It should remain disabled by default for now because it is a power tool, not an always-on routing target. The right move is to fix the real scanner bug, add versioning, and tighten the skill contract instead of merging or archiving it.

## Alternatives considered

- keep-enabled: rejected for now because this is still an operator tool and not a broad default workflow.
- merge: rejected because `skills-governance` and `skill-manager` serve adjacent but distinct jobs.
- archive: rejected because the category catalog and enable/disable flow are still useful.

## Required changes

1. Fix `scan.js` so symlinked skill directories are scanned.
2. Add a version field to `SKILL.md`.
3. Improve description and boundary language so the skill routes more cleanly.
4. Add explicit `When to Use`, `Do not use`, and output expectations.

## Validation plan

1. Re-run `node ~/.codex/skills/skill-manager/scan.js`.
2. Confirm `skill-governance-loop` appears in scan output.
3. Re-run `static_audit.py` on `skill-manager`.
4. Check whether the next governance task can use the skill with less ambiguity.

## Validation result

- `skill-manager` scan output now includes `skill-governance-loop`.
- Static audit improved from `63/100` to `93/100`.
- The skill now has versioning, clearer boundaries, and an explicit output contract.

## Next version hypothesis

If the next few cases show that category persistence and enable/disable are still high-value, split operational catalog management from broader inventory reporting. Otherwise, keep `skill-manager` narrow and explicitly subordinate to `skills-governance` for discovery-first workflows.
