# Decision

- Skill: session-recovery
- Old version: unknown
- New version: 0.2.0
- Primary decision: archive
- Confidence: high

## Why this decision

- The active Codex-native recovery lane already exists and is more specific.
- Archiving the old generic entry reduces routing ambiguity without losing historical traceability.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `archive` the legacy entry in place
- leave [session-recovery-codex](/home/cnfjlhj/.codex/skills/session-recovery-codex/SKILL.md) unchanged

## Required changes

- Add `version` to [session-recovery/SKILL.md](/home/cnfjlhj/.codex/skills/session-recovery/SKILL.md)
- Rewrite it as an archival redirect
- Keep `disable-model-invocation: true`

## Validation plan

- Re-run static audit on [session-recovery/SKILL.md](/home/cnfjlhj/.codex/skills/session-recovery/SKILL.md)
- Re-run `skills-governance` scan to confirm it remains disabled
- Confirm [session-recovery-codex](/home/cnfjlhj/.codex/skills/session-recovery-codex/SKILL.md) stays enabled

## Next version hypothesis

- `codex-resume` can likely undergo the same archive cleanup next.
