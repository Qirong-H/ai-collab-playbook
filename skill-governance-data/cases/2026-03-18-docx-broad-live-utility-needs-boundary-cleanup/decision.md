# Decision

- Skill: docx
- Old version: unknown
- New version: 0.2.0
- Primary decision: keep-enabled
- Confidence: high

## Why this decision

- DOCX is a legitimate file-format lane with unique fidelity concerns such as tracked changes, comments, and OOXML structure.
- The issue was not that the skill should disappear; it was that the entry-point body tried to inline too much detailed procedure.
- Keeping it enabled while shrinking it into a router preserves capability and reduces confusion with adjacent document skills.

## Alternatives considered

- keep-enabled
- keep-disabled
- merge
- split
- archive
- move-to-agents
- move-to-skill

Chosen path:

- `keep-enabled` as a compact DOCX lane
- make `redline` the default for risky document-review scenarios
- route deep detail to `docx-js.md`, `ooxml.md`, and `scripts/document.py`

## Required changes

- Add `version` to `/home/cnfjlhj/.codex/skills/docx/SKILL.md`
- Rewrite the live body around `analyze / create / edit / redline`
- Remove broken `scripts/unpack.py` and `scripts/pack.py` guidance from the entry-point file
- Add explicit boundaries against `pdf`, `pptx`, and `xlsx`
- Promote `docx-js.md`, `ooxml.md`, and `scripts/document.py` as the progressive-disclosure path

## Validation plan

- Re-run static audit on `/home/cnfjlhj/.codex/skills/docx`
- Re-run `skills-governance` scan to confirm `/home/cnfjlhj/.codex/skills/docx` remains enabled
- Verify the rewritten body links to `docx-js.md`, `ooxml.md`, and `scripts/document.py`

## Next version hypothesis

- The next nearby candidate should likely be `/home/cnfjlhj/.codex/skills/pptx/SKILL.md`, which shows a similar entry-point inflation problem in the same document-family neighborhood.
