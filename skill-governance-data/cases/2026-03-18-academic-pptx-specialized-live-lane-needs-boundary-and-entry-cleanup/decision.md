# Decision

- Skill: academic-pptx
- Old version: unknown
- New version: 0.2.0
- Primary decision: keep-enabled
- Confidence: high

## Why this decision

- `academic-pptx` is a real specialized lane with enough domain-specific behavior to justify a heavier live body.
- The generic `pptx` cleanup made the boundary problem more important: this skill needed a sharper entry contract, not a body amputation.
- User feedback about possible over-compression confirmed that this skill should be governance-framed while preserving its detailed expert content.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `keep-enabled` as a specialized heavy lane
- add boundary and governance metadata at the top
- preserve the detailed academic rules, phases, and QA body

## Required changes

- Add `version` to `/home/cnfjlhj/.codex/skills/academic-pptx/SKILL.md`
- Add explicit `When to Use`, `Do Not Use`, `Entry Rule`, and `Output Contract` sections
- Preserve the existing hard rules and action phases rather than replacing them with a thin router
- Keep the boundary with `/home/cnfjlhj/.codex/skills/pptx/SKILL.md` explicit

## Validation plan

- Re-run static audit on `/home/cnfjlhj/.codex/skills/academic-pptx`
- Confirm the detailed body remains present
- Re-check the generic-vs-academic boundary against `/home/cnfjlhj/.codex/skills/pptx/SKILL.md`

## Next version hypothesis

- Future cleanup, if needed, should move only truly secondary detail into references, not compress the live skill into a shell.
