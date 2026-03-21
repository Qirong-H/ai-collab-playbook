# Decision

- Skill: pptx
- Old version: unknown
- New version: 0.2.1
- Primary decision: keep-enabled
- Confidence: high

## Why this decision

- PowerPoint manipulation is a legitimate generic lane, especially for existing-deck operations, structural edits, and thumbnail-based review.
- The problem was not the existence of `pptx`; it was that the live entry point tried to carry too much detail and blurred into adjacent specialized workflows.
- Keeping it enabled while shrinking it around the bundled scripts preserves utility and clarifies ownership against `academic-pptx`.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `keep-enabled` as the generic PowerPoint lane
- delegate academic or paper-derived deck creation to `academic-pptx`
- route generic work to the real bundled scripts and references
- after user feedback about over-compression, restore a medium-depth generic workflow layer instead of leaving a thin router only

## Required changes

- Add `version` to `/home/cnfjlhj/.codex/skills/pptx/SKILL.md`
- Rewrite the live body around `analyze / edit / restructure / create / ooxml`
- Remove dead `scripts/unpack.py`, `scripts/validate.py`, and `scripts/pack.py` references from the entry-point guidance
- Add an explicit boundary against `/home/cnfjlhj/.codex/skills/academic-pptx/SKILL.md`
- Promote `inventory.py`, `rearrange.py`, `replace.py`, `thumbnail.py`, `html2pptx.md`, and `ooxml.md` as the progressive-disclosure path
- Add `/home/cnfjlhj/.codex/skills/pptx/references/generic-workflows.md` to retain generic deck know-how without re-inflating the entry-point file

## Validation plan

- Re-run static audit on `/home/cnfjlhj/.codex/skills/pptx`
- Re-run `skills-governance` scan to confirm `/home/cnfjlhj/.codex/skills/pptx` remains enabled
- Verify the rewritten body links to the bundled scripts and to `academic-pptx`

## Next version hypothesis

- The next worthwhile target may be either `/home/cnfjlhj/.codex/skills/academic-pptx/SKILL.md` for lane-boundary tightening, or a different broad live utility outside the document family.
