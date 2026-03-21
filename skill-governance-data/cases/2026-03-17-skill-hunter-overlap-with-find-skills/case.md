# Case

- Date: 2026-03-17
- Skill: skill-hunter
- Current version: unknown
- Request class: inventory cleanup
- Why this case exists: overlap-with-find-skills

## Expected behavior

- There should be one active front door for skill discovery.
- Registry-first search and GitHub fallback should belong to the same routing lane.
- Environment-specific CLI assumptions should be explicit.

## Observed behavior

- [skill-hunter/SKILL.md](/home/cnfjlhj/.codex/skills/skill-hunter/SKILL.md) and [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md) both claimed GitHub-based fallback discovery space.
- `skill-hunter` was a large always-on body with a static audit score of **48/100**.
- `find-skills` already contained a fallback section, but still mentioned `gh search code` as if it were generally available.
- On this machine, `gh` is installed and authenticated, but `gh search` is not supported by the installed CLI.

## Evidence

- Original user phrasing: the user asked for a thorough review of the skill library, especially duplicate skills and unclear ownership.
- Files / paths:
  - [skill-hunter/SKILL.md](/home/cnfjlhj/.codex/skills/skill-hunter/SKILL.md)
  - [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md)
  - [2026-03-17-codex-native-stage1-review.md](/home/cnfjlhj/projects/ai-collab-playbook/skill-governance-data/reviews/2026-03-17-codex-native-stage1-review.md)
- Triggered skill(s): `skill-governance-loop`, `skills-governance`
- Missing skill(s): none
- Output problem: duplicated fallback ownership plus brittle GitHub CLI assumptions

## Failure mode

- should trigger but did not
- should not trigger but did
- triggered but low quality
- overlap / duplication
- belongs in AGENTS.md instead

## Working hypothesis

- `skill-hunter` should not stay enabled as a parallel skill-discovery lane.
- Its remaining useful content should be merged into [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md), which becomes the sole active entry point.

## Next check

- Disable [skill-hunter/SKILL.md](/home/cnfjlhj/.codex/skills/skill-hunter/SKILL.md), upgrade [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md), and verify scan/audit results.
