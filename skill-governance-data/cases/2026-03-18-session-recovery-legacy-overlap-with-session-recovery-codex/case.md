# Case

- Date: 2026-03-18
- Skill: session-recovery
- Current version: unknown
- Request class: inventory cleanup
- Why this case exists: legacy-overlap-with-session-recovery-codex

## Expected behavior

- Codex session recovery should have one active lane.
- The older generic entry should remain only as a legacy redirect, not as a competing workflow.

## Observed behavior

- [session-recovery/SKILL.md](/home/cnfjlhj/.codex/skills/session-recovery/SKILL.md) was already disabled, but still looked like a short usable workflow note.
- [session-recovery-codex/SKILL.md](/home/cnfjlhj/.codex/skills/session-recovery-codex/SKILL.md) already provides the active Codex-native recovery flow.
- Static audit baseline for [session-recovery/SKILL.md](/home/cnfjlhj/.codex/skills/session-recovery/SKILL.md) was **59/100**.

## Evidence

- Original user phrasing: the user asked for the local skill library to be reviewed and cleaned up one by one without needing repeated confirmation.
- Files / paths:
  - [session-recovery/SKILL.md](/home/cnfjlhj/.codex/skills/session-recovery/SKILL.md)
  - [session-recovery-codex/SKILL.md](/home/cnfjlhj/.codex/skills/session-recovery-codex/SKILL.md)
- Triggered skill(s): `skill-governance-loop`, `skills-governance`
- Missing skill(s): none
- Output problem: legacy overlap with the active Codex-native recovery lane

## Failure mode

- should trigger but did not
- should not trigger but did
- triggered but low quality
- overlap / duplication
- belongs in AGENTS.md instead

## Working hypothesis

- `session-recovery` should remain disabled and be rewritten as an archival redirect.
- The only live recovery route should be [session-recovery-codex](/home/cnfjlhj/.codex/skills/session-recovery-codex/SKILL.md).

## Next check

- Rewrite the file into a compact archived note and verify it stays disabled with better structure.
