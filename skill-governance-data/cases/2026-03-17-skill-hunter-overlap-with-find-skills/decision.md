# Decision

- Skill: skill-hunter
- Old version: unknown
- New version: 0.2.0
- Primary decision: merge
- Confidence: high

## Why this decision

- Skill discovery should have one active entry point, not parallel overlapping lanes.
- [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md) is already the better front door because it starts with installable registry results.
- `skill-hunter` depended on `gh search code`, which is not supported by the installed GitHub CLI on this machine.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `merge` the useful fallback idea into [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md)
- `keep-disabled` [skill-hunter/SKILL.md](/home/cnfjlhj/.codex/skills/skill-hunter/SKILL.md) as an archival note

## Required changes

- Add `version` and `disable-model-invocation: true` to [skill-hunter/SKILL.md](/home/cnfjlhj/.codex/skills/skill-hunter/SKILL.md)
- Rewrite [skill-hunter/SKILL.md](/home/cnfjlhj/.codex/skills/skill-hunter/SKILL.md) into a compact archival note
- Add `version` and `Output Contract` to [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md)
- Replace the brittle GitHub fallback wording in [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md) with a capability-aware fallback

## Validation plan

- Re-run static audits for both [skill-hunter/SKILL.md](/home/cnfjlhj/.codex/skills/skill-hunter/SKILL.md) and [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md)
- Re-run `skills-governance` scan to confirm [skill-hunter/SKILL.md](/home/cnfjlhj/.codex/skills/skill-hunter/SKILL.md) is disabled
- Confirm [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md) remains enabled and is now the only live discovery front door

## Next version hypothesis

- If the archived note remains unused, `skill-hunter` can be fully archived or deleted in a later cleanup pass.
