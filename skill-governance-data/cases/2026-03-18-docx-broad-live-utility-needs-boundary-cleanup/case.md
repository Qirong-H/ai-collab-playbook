# Case

- Date: 2026-03-18
- Skill: docx
- Current version: unknown
- Request class: inventory-wide skill governance, one-skill-at-a-time cleanup
- Why this case exists: broad-live-utility-needs-boundary-cleanup

## Expected behavior

- `docx` should stay as a live lane because Word documents have format-specific workflows such as tracked changes, comments, and OOXML-aware edits.
- The live body should route by task mode and default risky edits into a review-friendly redline path.

## Observed behavior

- The prior body mixed analysis, creation, OOXML surgery, redlining, and dependency notes into one long entry-point file.
- It lacked `version`, clear trigger phrasing, and an explicit `When to Use` section.
- The live body referenced `scripts/unpack.py` and `scripts/pack.py`, but those paths do not exist in this skill directory.
- Deep references like `docx-js.md` and `ooxml.md` existed, but the main skill body still tried to carry too much of their content directly.

## Evidence

- Original user phrasing:
  - “我需要对我的整个skill的库做一次彻彻底底的review”
  - “我很想知道我是否有一些skill是重复的，或者说职权不清的”
  - “继续吧。但是我希望你逐个继续，一个一个来，就是不要我确认了”
- Files / paths:
  - `/home/cnfjlhj/.codex/skills/docx/SKILL.md`
  - `/home/cnfjlhj/.codex/skills/docx/docx-js.md`
  - `/home/cnfjlhj/.codex/skills/docx/ooxml.md`
  - `/home/cnfjlhj/.codex/skills/docx/scripts/document.py`
  - `/home/cnfjlhj/.codex/skills/pdf/SKILL.md`
  - `/home/cnfjlhj/.codex/skills/pptx/SKILL.md`
- Triggered skill(s):
  - `skill-governance-loop`
  - `skills-governance`
- Missing skill(s):
  - none
- Output problem:
  - too broad for a live skill
  - broken path references in the entry-point guidance
  - overlap risk with neighboring document-format lanes
  - progressive disclosure assets existed but were not used as the primary route

## Failure mode

- triggered but low quality
- overlap / duplication

## Working hypothesis

- Keep `docx` enabled, but shrink the live body into a router over `analyze / create / edit / redline`.
- Remove broken local path references from the entry-point file.
- Make redlining the default for externally authored or formal documents.

## Next check

- Re-run static audit after rewrite.
- Confirm the inventory scanner still reports `docx` as enabled.
- Verify the rewritten body links to `docx-js.md`, `ooxml.md`, and `scripts/document.py`.
