# Decision

- Skill: codex-resume
- Old version: unknown
- New version: 0.2.0
- Primary decision: archive
- Confidence: high

## Why this decision

- The active Codex-native recovery lane already covers explicit session-id restoration.
- Archiving the old alias preserves historical continuity without keeping a competing workflow surface.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `archive` the legacy alias in place
- leave [session-recovery-codex](/home/cnfjlhj/.codex/skills/session-recovery-codex/SKILL.md) unchanged

## Required changes

- Add `version` to [codex-resume/SKILL.md](/home/cnfjlhj/.codex/skills/codex-resume/SKILL.md)
- Rewrite it as an archival redirect
- Keep `disable-model-invocation: true`

## Validation plan

- Re-run static audit on [codex-resume/SKILL.md](/home/cnfjlhj/.codex/skills/codex-resume/SKILL.md)
- Re-run `skills-governance` scan to confirm it remains disabled
- Confirm [session-recovery-codex](/home/cnfjlhj/.codex/skills/session-recovery-codex/SKILL.md) stays enabled

## Next version hypothesis

- The next sequential cleanup target is likely the broad document-tool family, starting with `xlsx`.
