# Case

- Date: 2026-03-17
- Skill: proactive-explorer
- Current version: unknown
- Request class: AGENTS.md vs skill boundary
- Why this case exists: wrong-layer-global-rule

## Expected behavior

- Stable cross-task discipline such as "explore before asking" should live in [AGENTS.md](/home/cnfjlhj/.codex/AGENTS.md), not in an always-on skill body.
- If a skill remains, it should only hold optional examples or migration notes.

## Observed behavior

- [proactive-explorer/SKILL.md](/home/cnfjlhj/.codex/skills/proactive-explorer/SKILL.md) used the trigger "收到任何任务请求时", which is effectively global.
- The same rule already exists in [AGENTS.md](/home/cnfjlhj/.codex/AGENTS.md) section `2.1 推理与探索`.
- The old skill body was large, example-heavy, and partially stale relative to the current environment.
- Static audit baseline was **37/100**.

## Evidence

- Original user phrasing: the user asked for a thorough review of the whole skill library, with special emphasis on duplicates, unclear ownership, and what belongs in `AGENTS.md` versus a skill.
- Files / paths:
  - [AGENTS.md](/home/cnfjlhj/.codex/AGENTS.md)
  - [proactive-explorer/SKILL.md](/home/cnfjlhj/.codex/skills/proactive-explorer/SKILL.md)
  - [2026-03-17-codex-native-stage1-review.md](/home/cnfjlhj/projects/ai-collab-playbook/skill-governance-data/reviews/2026-03-17-codex-native-stage1-review.md)
- Triggered skill(s): `skill-governance-loop`, `skills-governance`
- Missing skill(s): none
- Output problem: the skill duplicates a stable global rule and adds unnecessary routing surface

## Failure mode

- should trigger but did not
- should not trigger but did
- triggered but low quality
- overlap / duplication
- belongs in AGENTS.md instead

## Working hypothesis

- `proactive-explorer` should not remain a live enabled skill.
- The rule should stay in [AGENTS.md](/home/cnfjlhj/.codex/AGENTS.md), while the skill becomes a disabled archival note or is later removed entirely.

## Next check

- Mark the skill with `disable-model-invocation: true`, rewrite it as a compact boundary note, and confirm the static audit improves without losing the rule in [AGENTS.md](/home/cnfjlhj/.codex/AGENTS.md).
