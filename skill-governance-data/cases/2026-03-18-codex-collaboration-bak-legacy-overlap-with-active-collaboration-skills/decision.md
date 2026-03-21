# Decision

- Skill: codex-collaboration-bak
- Old version: unknown
- New version: 0.2.0
- Primary decision: archive
- Confidence: high

## Why this decision

- The library already has active, better-scoped collaboration lanes for Codex, Claude, and Gemini.
- The old backup-like file preserved a competing workflow that is no longer needed.
- Archiving in place keeps the migration history while removing it as a plausible live entry point.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `archive` the legacy skill in place
- keep the active collaboration skills unchanged

## Required changes

- Add `version` to [codex-collaboration.bak/SKILL.md](/home/cnfjlhj/.codex/skills/codex-collaboration.bak/SKILL.md)
- Rewrite the body into a compact archived redirect
- Leave [collaborating-with-codex/SKILL.md](/home/cnfjlhj/.codex/skills/collaborating-with-codex/SKILL.md), [collaborating-with-claude/SKILL.md](/home/cnfjlhj/.codex/skills/collaborating-with-claude/SKILL.md), and [collaborating-with-gemini/SKILL.md](/home/cnfjlhj/.codex/skills/collaborating-with-gemini/SKILL.md) unchanged

## Validation plan

- Re-run static audit on [codex-collaboration.bak/SKILL.md](/home/cnfjlhj/.codex/skills/codex-collaboration.bak/SKILL.md)
- Re-run `skills-governance` scan to confirm it remains disabled and backup-like
- Confirm the active collaboration skills remain enabled

## Next version hypothesis

- A later pass can delete the archived backup directory entirely if no historical value remains.
