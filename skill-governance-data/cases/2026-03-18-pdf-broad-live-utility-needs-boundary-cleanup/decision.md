# Decision

- Skill: pdf
- Old version: unknown
- New version: 0.2.0
- Primary decision: keep-enabled
- Confidence: high

## Why this decision

- PDF work is a real operational lane with distinct tooling, especially for extraction, page edits, and form handling.
- The problem was not the lane itself; it was that the live skill body tried to be a handbook instead of a routing layer.
- Keeping it enabled while shrinking the body preserves utility and reduces overlap with neighboring format skills.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `keep-enabled` as a compact PDF lane
- keep advanced detail behind existing references
- make form workflows and CJK generation explicit instead of burying them in a giant body

## Required changes

- Add `version` to `/home/cnfjlhj/.codex/skills/pdf/SKILL.md`
- Rewrite the live body around `extract / edit / form / create`
- Add explicit “Do Not Use” boundaries against `docx`, `pptx`, and `xlsx`
- Route form work to `forms.md` and the bundled validation scripts
- Route advanced extraction and repair work to `reference.md`
- Route Chinese or CJK generation to `chinese-pdf-guide.md`

## Validation plan

- Re-run static audit on `/home/cnfjlhj/.codex/skills/pdf`
- Re-run `skills-governance` scan to confirm `/home/cnfjlhj/.codex/skills/pdf` remains enabled
- Verify the rewritten body links to the existing reference files and form scripts

## Next version hypothesis

- The next broad utility candidate should likely be `/home/cnfjlhj/.codex/skills/docx/SKILL.md`, which shows a similar handbook-heavy shape and neighboring scope pressure.
