# Decision

- Skill: research-writing-generic-cluster
- Old version: unknown
- New version: 0.2.0 on each rewritten generic skill
- Primary decision: merge
- Confidence: high

## Why this decision

- The active paper-writing system already has clear anchor lanes for draft creation, review-paper writing, and near-final QA.
- The generic trio was not adding a distinct routing surface; it was mostly preserving broad overlapping entry points.
- Keeping the trio disabled but rewriting them into routing notes preserves context while reducing confusion.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `merge` the generic entry-point role into the anchor lanes conceptually
- `keep-disabled` the three generic skills as archival routing notes

## Required changes

- Rewrite [academic-paper-helper](/home/cnfjlhj/.codex/skills/academic-paper-helper/SKILL.md) into a disabled routing note
- Rewrite [academic-research-writer](/home/cnfjlhj/.codex/skills/academic-research-writer/SKILL.md) into a disabled routing note
- Rewrite [research-paper-writer](/home/cnfjlhj/.codex/skills/research-paper-writer/SKILL.md) into a disabled routing note
- Add explicit `version` fields to the rewritten generic skills
- Leave the anchor lanes unchanged in this pass

## Validation plan

- Re-run static audits on the rewritten generic trio
- Re-run `skills-governance` scan to confirm all three remain disabled
- Manually verify that the anchor lanes are still the only live routes in this area

## Next version hypothesis

- If the archived routing notes prove unnecessary, a later pass can fully archive or delete the generic trio.
