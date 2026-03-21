# Case

- Date: 2026-03-18
- Skill: codex-collaboration-bak
- Current version: unknown
- Request class: inventory cleanup
- Why this case exists: legacy-overlap-with-active-collaboration-skills

## Expected behavior

- The active collaboration lanes should be the only recommended second-opinion workflows.
- Backup-like legacy entries should not preserve competing live instructions.
- Archived collaboration notes should be short and safe.

## Observed behavior

- [codex-collaboration.bak/SKILL.md](/home/cnfjlhj/.codex/skills/codex-collaboration.bak/SKILL.md) was already disabled, but still presented itself as a usable workflow.
- The library already has active replacements:
  - [collaborating-with-codex](/home/cnfjlhj/.codex/skills/collaborating-with-codex/SKILL.md)
  - [collaborating-with-claude](/home/cnfjlhj/.codex/skills/collaborating-with-claude/SKILL.md)
  - [collaborating-with-gemini](/home/cnfjlhj/.codex/skills/collaborating-with-gemini/SKILL.md)
- The old body included legacy direct-invocation guidance and stale configuration details that should not remain a live recommendation.
- Static audit baseline was **49/100**.

## Evidence

- Original user phrasing: the user asked for a full local skill-library review, especially duplicate skills and unclear ownership.
- Files / paths:
  - [codex-collaboration.bak/SKILL.md](/home/cnfjlhj/.codex/skills/codex-collaboration.bak/SKILL.md)
  - [collaborating-with-codex/SKILL.md](/home/cnfjlhj/.codex/skills/collaborating-with-codex/SKILL.md)
  - [collaborating-with-claude/SKILL.md](/home/cnfjlhj/.codex/skills/collaborating-with-claude/SKILL.md)
  - [collaborating-with-gemini/SKILL.md](/home/cnfjlhj/.codex/skills/collaborating-with-gemini/SKILL.md)
- Triggered skill(s): `skill-governance-loop`, `skills-governance`
- Missing skill(s): none
- Output problem: legacy backup-like entry still described a parallel collaboration path instead of yielding to active lanes

## Failure mode

- should trigger but did not
- should not trigger but did
- triggered but low quality
- overlap / duplication
- belongs in AGENTS.md instead

## Working hypothesis

- `codex-collaboration.bak` should remain disabled and be rewritten as an archival redirect.
- The active collaboration skills should remain the only recommended second-opinion workflows.

## Next check

- Rewrite the file into a compact archived note and verify it stays disabled with higher structural quality.
