# Case

- Date: 2026-03-18
- Skill: codex-resume
- Current version: unknown
- Request class: inventory cleanup
- Why this case exists: legacy-overlap-with-session-recovery-codex

## Expected behavior

- Explicit session-id recovery should have one active Codex-native lane.
- The older `codex resume` alias should remain only as a legacy redirect.

## Observed behavior

- [codex-resume/SKILL.md](/home/cnfjlhj/.codex/skills/codex-resume/SKILL.md) was already disabled, but still described a small standalone workflow.
- [session-recovery-codex/SKILL.md](/home/cnfjlhj/.codex/skills/session-recovery-codex/SKILL.md) already covers the explicit session-id recovery path.
- Static audit baseline for [codex-resume/SKILL.md](/home/cnfjlhj/.codex/skills/codex-resume/SKILL.md) was **63/100**.

## Evidence

- Original user phrasing: the user asked for the skill library to be cleaned up one by one without repeated confirmation.
- Files / paths:
  - [codex-resume/SKILL.md](/home/cnfjlhj/.codex/skills/codex-resume/SKILL.md)
  - [session-recovery-codex/SKILL.md](/home/cnfjlhj/.codex/skills/session-recovery-codex/SKILL.md)
- Triggered skill(s): `skill-governance-loop`, `skills-governance`
- Missing skill(s): none
- Output problem: legacy alias overlap with the active Codex-native recovery lane

## Failure mode

- should trigger but did not
- should not trigger but did
- triggered but low quality
- overlap / duplication
- belongs in AGENTS.md instead

## Working hypothesis

- `codex-resume` should remain disabled and be rewritten as an archival alias redirect.
- The only live route for explicit session-id recovery should remain [session-recovery-codex](/home/cnfjlhj/.codex/skills/session-recovery-codex/SKILL.md).

## Next check

- Rewrite the file into a compact archived alias note and verify it stays disabled with improved structure.
