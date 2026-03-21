# Decision

- Skill: proactive-explorer
- Old version: unknown
- New version: 0.2.0
- Primary decision: move-to-agents
- Confidence: high

## Why this decision

- The stable rule already exists in [AGENTS.md](/home/cnfjlhj/.codex/AGENTS.md) and is therefore already in the correct always-on layer.
- The old skill body used a universal trigger and duplicated that same cross-task discipline.
- Keeping the skill enabled would preserve unnecessary routing surface and maintenance cost.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `move-to-agents` for the stable rule
- `keep-disabled` as a small archival note for future governance passes

## Required changes

- Add explicit `version` and `disable-model-invocation: true` frontmatter to [proactive-explorer/SKILL.md](/home/cnfjlhj/.codex/skills/proactive-explorer/SKILL.md)
- Rewrite the body into a short boundary note
- Leave [AGENTS.md](/home/cnfjlhj/.codex/AGENTS.md) unchanged because the necessary rule is already present

## Validation plan

- Re-run static audit on [proactive-explorer/SKILL.md](/home/cnfjlhj/.codex/skills/proactive-explorer/SKILL.md)
- Re-run `skills-governance` scan to confirm the skill is now disabled
- Manually verify that the key exploration rule still exists in [AGENTS.md](/home/cnfjlhj/.codex/AGENTS.md)

## Next version hypothesis

- If no future empirical case requires preserved examples, the next step can be full archive or deletion of the skill directory.
