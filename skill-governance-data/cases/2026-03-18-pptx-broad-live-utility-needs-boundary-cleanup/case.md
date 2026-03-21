# Case

- Date: 2026-03-18
- Skill: pptx
- Current version: unknown
- Request class: inventory-wide skill governance, one-skill-at-a-time cleanup
- Why this case exists: broad-live-utility-needs-boundary-cleanup

## Expected behavior

- `pptx` should stay as the generic PowerPoint lane for existing deck operations and non-academic deck creation.
- The live body should set a clear boundary against `academic-pptx` and route to the bundled scripts instead of inlining a full handbook.

## Observed behavior

- The prior entry-point file was extremely large and tried to cover many workflows directly.
- It lacked `version`, trigger-focused description, and an explicit output contract.
- It referenced missing local helpers such as `scripts/unpack.py`, `scripts/validate.py`, and `scripts/pack.py`.
- It mixed generic PPTX operations with image-pipeline and academic-deck style guidance that belongs in other layers or lanes.

## Evidence

- Original user phrasing:
  - “我需要对我的整个skill的库做一次彻彻底底的review”
  - “我很想知道我是否有一些skill是重复的，或者说职权不清的”
  - “继续吧。但是我希望你逐个继续，一个一个来，就是不要我确认了”
- Files / paths:
  - `/home/cnfjlhj/.codex/skills/pptx/SKILL.md`
  - `/home/cnfjlhj/.codex/skills/pptx/html2pptx.md`
  - `/home/cnfjlhj/.codex/skills/pptx/ooxml.md`
  - `/home/cnfjlhj/.codex/skills/pptx/scripts/inventory.py`
  - `/home/cnfjlhj/.codex/skills/pptx/scripts/rearrange.py`
  - `/home/cnfjlhj/.codex/skills/pptx/scripts/replace.py`
  - `/home/cnfjlhj/.codex/skills/pptx/scripts/thumbnail.py`
  - `/home/cnfjlhj/.codex/skills/academic-pptx/SKILL.md`
- Triggered skill(s):
  - `skill-governance-loop`
  - `skills-governance`
- Missing skill(s):
  - none
- Output problem:
  - too broad for a live skill
  - broken path references in the entry-point file
  - unclear boundary with `academic-pptx`
  - existing helper scripts were not used as the primary progressive-disclosure route
  - follow-up user feedback flagged over-compression risk after the first rewrite

## Failure mode

- triggered but low quality
- overlap / duplication

## Working hypothesis

- Keep `pptx` enabled, but reduce the live body into a router over `analyze / edit / restructure / create / ooxml`.
- Explicitly delegate academic slide-authoring to `academic-pptx`.
- Route generic deck work through the bundled scripts and remove dead helper-path references.
- Preserve a medium-depth generic workflow layer so the live skill is not just a thin shell.

## Next check

- Re-run static audit after rewrite.
- Confirm the inventory scanner still reports `pptx` as enabled.
- Verify the rewritten body links to the bundled scripts and to `academic-pptx`.
