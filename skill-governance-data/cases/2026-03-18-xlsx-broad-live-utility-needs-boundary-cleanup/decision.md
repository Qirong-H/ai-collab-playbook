# Decision

- Skill: xlsx
- Old version: unknown
- New version: 0.2.0
- Primary decision: keep-enabled
- Confidence: high

## Why this decision

- Spreadsheet artifacts, workbook fidelity, and formula validation are a real enough lane to justify a live skill.
- The problem was not existence; it was lack of routing discipline and progressive disclosure.
- Keeping it enabled while shrinking the body preserves usefulness and reduces confusion.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `keep-enabled` as a live utility skill
- move finance-specific detail into a reference file
- narrow the live body around routing, tool choice, and validation

## Required changes

- Add `version` to [xlsx/SKILL.md](/home/cnfjlhj/.codex/skills/xlsx/SKILL.md)
- Rewrite the live body around `analyze / edit / create` routing
- Add [financial-model-guidelines.md](/home/cnfjlhj/.codex/skills/xlsx/references/financial-model-guidelines.md)
- Keep [recalc.py](/home/cnfjlhj/.codex/skills/xlsx/recalc.py) as the mandatory validation path for formula changes

## Validation plan

- Re-run static audit on [xlsx/SKILL.md](/home/cnfjlhj/.codex/skills/xlsx/SKILL.md)
- Re-run `skills-governance` scan to confirm [xlsx/SKILL.md](/home/cnfjlhj/.codex/skills/xlsx/SKILL.md) remains enabled
- Verify that the new reference file exists and is linked from the main skill

## Next version hypothesis

- The next file-format utility candidate is likely [pdf/SKILL.md](/home/cnfjlhj/.codex/skills/pdf/SKILL.md), which shows a similar handbook-style tendency.
