# Codex Native Skills Stage 1 Review

Date: 2026-03-17
Scope: read-only review of public native directories under `~/.codex/skills`
Method: filesystem inventory + `skills-governance` scan + static audit + targeted heading/body reads + light external calibration

## Scope Notes

- In scope:
  - 70 public native skill directories in `~/.codex/skills`
  - enable/disable state as reported by `skills-governance`
  - initial semantic overlap and boundary-risk screening
- Out of scope:
  - 30 symlinked mirror/imported skills
  - hidden `.system` skills
  - mass edits to existing skills
- Important:
  - there are **no exact duplicate-name groups** in the current Codex scan
  - the real problem is **semantic overlap, boundary drift, and uneven quality**

## Inventory Snapshot

| Metric | Value | Notes |
| --- | ---: | --- |
| Public native skills | 70 | Real directories only, excludes symlinks and hidden `.system` |
| Enabled | 49 | Routed today |
| Disabled | 21 | Mostly legacy aliases, manual-only flows, or unfinished workflows |
| User-invocable | 4 | `last30days`, `skill-manager`, `skills-governance`, `telegram-session-brief` |
| Versioned | 11 | Only 15.7% of public native skills |
| Unversioned | 59 | Main maintainability gap |
| Symlinked non-native skills | 30 | Deferred to Stage 2 |
| Exact duplicate names | 0 | From `skills-governance --mode codex` |

## Repeated Structural Problems

Static audit is only a baseline, but the pattern density is already useful.

| Repeated finding | Count | Reading |
| --- | ---: | --- |
| Missing `version` frontmatter | 59 | Most skills have no durable iteration history |
| Missing explicit `When to Use` section | 57 | Routing depends too much on prose and luck |
| Missing explicit output/acceptance contract | 52 | Hard to judge whether a skill actually did its job |
| Description lacks concrete phrase examples | 48 | Trigger phrasing is weak or abstract |
| Missing explicit boundary/skip guidance | 48 | Skills collide because they do not say what they are not |
| Description does not clearly express trigger conditions | 27 | Model has to infer too much |
| Workflow not clearly stepwise | 27 | Hard to reproduce behavior consistently |

## Versioning + Invocation

### Versioned public native skills

| Skill | Version | Enabled | Comment |
| --- | --- | --- | --- |
| `baohe-codex-align` | `0.2.0` | yes | Host-specific sync flow |
| `claude-scholar-frontend-design` | `0.1.0` | no | Disabled alias |
| `claude-scholar-ml-paper-writing` | `1.0.0` | no | Disabled alias |
| `claude-scholar-planning-with-files` | `0.1.0` | no | Disabled alias |
| `human-machine-brainstorm` | `0.1.0` | no | Specialized manual workflow |
| `knowledge-absorber` | `4.4.0` | yes | Heavy learning workflow |
| `last30days` | `2.1` | no | Manual/external trend workflow |
| `ml-paper-writing` | `1.0.0` | yes | Mature primary paper-writing lane |
| `paperreview` | `0.1.0` | yes | External second-opinion lane |
| `skill-manager` | `0.2.0` | no | Manual inventory/category tool |
| `xhs-longform-private-publisher` | `0.1.0` | yes | Narrow publishing workflow |

### User-invocable skills

| Skill | Enabled | Static score | Interpretation |
| --- | --- | ---: | --- |
| `skills-governance` | yes | 83 | Good primary entry for inventory truth |
| `telegram-session-brief` | yes | 75 | Useful manual utility; needs reference-path cleanup |
| `skill-manager` | no | 93 | Strong structure, intentionally disabled/manual |
| `last30days` | no | 82 | Strong specialized workflow, intentionally disabled/manual |

## Lowest Static Scores

Low score does **not** mean delete. It means “review boundary, maintainability, and evidence first”.

| Skill | Enabled | Score | Why it is low |
| --- | --- | ---: | --- |
| `xlsx` | yes | 32 | Extremely broad surface, bloated body, weak trigger language, no versioning |
| `proactive-explorer` | yes | 37 | Feels like an always-on global rule disguised as a skill |
| `academic-paper-helper` | no | 42 | Generic helper bundle, weak trigger boundary, likely overlap-heavy |
| `pend` | no | 42 | Minimal utility but under-specified |
| `ping` | no | 42 | Minimal utility but under-specified |
| `mounted` | no | 47 | Utility skill with weak routing contract |
| `skill-hunter` | yes | 48 | Overgrown body, weak boundary, environment assumptions are brittle |
| `cc-clean` | yes | 49 | Broken path refs plus vague trigger framing |
| `codex-collaboration.bak` | no | 49 | Backup-like legacy entry, not a clean live workflow |
| `pdf` | yes | 49 | Broad utility bundle with weak routing/acceptance |
| `ask` | no | 51 | Too generic; likely an implementation helper, not a user-facing workflow |
| `research-executor` | no | 52 | Very broad promise, unclear boundary relative to adjacent research workflows |

## External Calibration

These are not used as a substitute for local evidence. They are only used to calibrate what “good skill governance” tends to look like.

| Source | Key takeaway | Local implication |
| --- | --- | --- |
| Anthropic Claude Code docs: https://docs.anthropic.com/en/docs/claude-code/sub-agents | Keep task-specific detail in subagent/skill prompts rather than bloating always-on context | Supports keeping `AGENTS.md` lean and moving only stable iron laws there |
| skills.sh docs: https://skills.sh | Skills are installable/discoverable, but quality is ecosystem-dependent | Supports keeping `find-skills` as registry-first discovery, but not assuming external quality |
| `ComposioHQ/awesome-claude-skills`: https://github.com/ComposioHQ/awesome-claude-skills | Community skill ecosystems grow fast and fragment by topic | Reinforces the need for local keep/disable/archive discipline |
| SWE-Skills-Bench paper: https://huggingface.co/papers/2603.05112 | Skill usefulness should be measured on real task instances with explicit acceptance criteria | Strong support for a future empirical evaluator beyond static linting |

## Cluster Review

### 1. Planning / Control

| Skills | Current shape | Risk | Stage 1 decision |
| --- | --- | --- | --- |
| `create-plan` | Quick read-only in-chat plan | Low overlap if kept narrow | keep |
| `all-plan` | Heavy ambiguous-task planning using external role flow | Boundary drift with `create-plan` if not explicit | keep, but clarify “when not to use” |
| `daily-todo` | Persistent day/task file workflow | Long body, but different lane from chat planning | keep |
| `hitl-guard` | Human-in-loop execution gate | Not a planner, but currently easy to confuse with cautious planning | keep |

Reading: this cluster is mostly healthy. The problem is not duplicate function; the problem is missing cross-references and weak boundary text.

### 2. Input / Alignment / Learning

| Skills | Current shape | Risk | Stage 1 decision |
| --- | --- | --- | --- |
| `input-triage` | Mixed-input cleaning gate | Good role, should stay | keep |
| `claim-audit` | Audit strong framing/hypotheses | Good role, adjacent but distinct | keep |
| `question-refiner` | Turn vague research ask into structured brief | Distinct if limited to research questions | keep |
| `prompt-polisher` | Turn messy notes/transcripts into a better prompt | Can collide with `question-refiner` on vague user asks | review boundary |
| `knowledge-absorber` | Heavy teaching/knowledge-note pipeline | Large, specialized, but distinct | keep, later trim |
| `memory-workflow` | Memory recall/writeback protocol | Healthy AGENTS-vs-skill split today | keep |
| `proactive-explorer` | “Explore before asking” principle | Strong smell of wrong layer | move core rule to AGENTS, shrink or archive skill |
| `human-machine-brainstorm` | Multi-model alignment loop | Specialized and intentionally disabled | keep-disabled |

Reading: `proactive-explorer` is the clearest wrong-layer candidate in the whole library. The core idea belongs in `AGENTS.md`; only optional examples or templates belong in a skill.

### 3. Search / Discovery

| Skills | Current shape | Risk | Stage 1 decision |
| --- | --- | --- | --- |
| `exa-search` | Source-first official/docs search | Healthy pair with `grok-search` | keep |
| `grok-search` | Fresh/live/community search | Healthy pair with `exa-search` | keep |
| `arxiv-search` | arXiv-only retrieval | Clear niche | keep |
| `find-skills` | Registry-first skill discovery | Good primary entry | keep |
| `skill-hunter` | GitHub mining fallback | Overlaps `find-skills`, assumes `gh search` exists | merge candidate or rewrite |
| `last30days` | Specialized last-30-days trend pipeline | Very distinct manual workflow | keep-disabled |

Reading: `find-skills` should be the main skill-discovery front door. `skill-hunter` should either become a small fallback reference under it or be rewritten around `gh api` / web search.

### 4. Skill Meta / Governance

| Skills | Current shape | Risk | Stage 1 decision |
| --- | --- | --- | --- |
| `skills-governance` | Inventory truth + duplicate/root scan | Clear first step | keep |
| `skill-governance-loop` | Case/audit/decision governance loop | Strong workflow, currently symlinked | keep |
| `skill-manager` | Category catalog + enable/disable operations | Clear post-inventory tool | keep-disabled/manual |
| `skill-creator-plus` | Create/improve/eval/benchmark skills | Broader than governance, but adjacent | keep |

Reading: this is the healthiest meta cluster. The main next step is not merging; it is making the order explicit:

1. `skills-governance`
2. `skill-governance-loop`
3. `skill-manager`

### 5. Research Writing / Review

| Skills | Current shape | Risk | Stage 1 decision |
| --- | --- | --- | --- |
| `ml-paper-writing` | Primary lane for original ML/AI conference papers | Good anchor skill | keep |
| `arxiv-paper-writer` | Review/survey/arXiv lane | Good anchor skill | keep |
| `paper-review-pipeline` | Local QA/review/rebuttal lane | Good anchor skill | keep |
| `paperreview` | External paperreview.ai lane | Good explicit downstream step | keep |
| `citation-validator` | Citation integrity sub-workflow | Good supporting lane | keep |
| `academic-paper-helper` | Generic helper bundle | Swallows adjacent lanes | merge/archive candidate |
| `academic-research-writer` | Generic academic writer | Overlaps with paper-writing lanes | merge/archive candidate |
| `research-paper-writer` | Generic research-paper generator | Overlaps with `ml-paper-writing` and `arxiv-paper-writer` | merge/archive candidate |
| `academic-writing-style` | Style/prose calibration for assignments and reports | Potentially salvageable if narrowed to style only | boundary cleanup |

Reading: this is the biggest semantic-overlap cluster in the current native library.

### 6. Multi-Model Collaboration / Legacy Provider Utilities

| Skills | Current shape | Risk | Stage 1 decision |
| --- | --- | --- | --- |
| `collaborating-with-claude` | Second-opinion workflow by provider | Healthy provider lane | keep |
| `collaborating-with-codex` | Second-opinion workflow by provider | Healthy provider lane | keep |
| `collaborating-with-gemini` | Second-opinion workflow by provider | Healthy provider lane | keep |
| `codex-collaboration.bak` | Legacy backup-like collaboration entry | Redundant + backup smell | archive candidate |
| `ask` / `pend` / `ping` / `mounted` | Provider utility helpers | Likely infra/ops layer, not polished user workflows | review separately as ops cluster |

Reading: the live collaboration trio is coherent. The legacy/ops layer needs a separate pass so utilities do not masquerade as polished end-user skills.

### 7. Session Recovery

| Skills | Current shape | Risk | Stage 1 decision |
| --- | --- | --- | --- |
| `session-recovery-codex` | Preferred active lane | Good primary route | keep |
| `session-recovery` | Older generic lane | Legacy alias | keep-disabled / archive later |
| `codex-resume` | Old phrase compatibility | Legacy alias | keep-disabled / archive later |

Reading: this cluster is mostly a legacy cleanup problem, not a routing-design problem.

## AGENTS.md Boundary Candidates

These are the most obvious “wrong layer” or “needs split” cases based on the `AGENTS.md vs skill` note.

| Candidate | Why it smells wrong-layer | Stage 1 view |
| --- | --- | --- |
| `proactive-explorer` | Core rule is stable, cross-task, always-on, and already close to AGENTS law | Move compact rule to `AGENTS.md`; leave optional examples elsewhere |
| `input-triage` | Core gate is globally useful, but body is still a real workflow | Current split is acceptable: short gate in AGENTS, heavy method in skill |
| `memory-workflow` | Stable principle plus optional detail | Current split is healthy |
| `self-review` | Partly global, partly task-specific | Review later after risky-task workflows are clearer |

## Priority Queue

This queue is ordered by governance leverage, not by static score alone.

| Rank | Skill or cluster | Why now | Likely action |
| ---: | --- | --- | --- |
| 1 | `proactive-explorer` | Enabled, very low score, wrong-layer smell, directly touches global behavior | move-to-AGENTS + slim/archive |
| 2 | `skill-hunter` | Enabled, overlaps `find-skills`, local `gh` capability mismatch already observed | merge into `find-skills` or rewrite |
| 3 | Research-writing generic trio | Highest semantic-overlap cluster | merge/archive/boundary cleanup |
| 4 | `codex-collaboration.bak` | Disabled backup-like entry with clearer modern replacements | archive |
| 5 | Session recovery legacy aliases | Easy cleanup with low conceptual risk | keep-disabled then archive |
| 6 | `xlsx` | Enabled, lowest score, very broad surface area | structural rewrite |
| 7 | `cc-clean` | Enabled, broken path refs, routing unclear | repair or disable |
| 8 | Provider utility mini-cluster: `ask` / `pend` / `ping` / `mounted` | Feels more like ops helpers than polished skills | separate ops governance pass |
| 9 | `pdf` / `pptx` / `docx` / `xlsx` broad document-tool family | Wide-surface utility skills need a shared quality bar | family-level rubric |
| 10 | `prompt-polisher` vs `question-refiner` vs `knowledge-absorber` | Likely future confusion around “messy input” vs “research brief” vs “teaching note” | boundary cleanup |

## Stage 1 Decisions

### Keep as anchors

- `skills-governance`
- `skill-governance-loop`
- `ml-paper-writing`
- `arxiv-paper-writer`
- `paper-review-pipeline`
- `paperreview`
- `claim-audit`
- `input-triage`
- `memory-workflow`
- `exa-search`
- `grok-search`
- `collaborating-with-claude`
- `collaborating-with-codex`
- `collaborating-with-gemini`

### Keep-disabled on purpose

- `skill-manager`
- `last30days`
- `human-machine-brainstorm`
- `session-recovery`
- `codex-resume`

### Merge / archive / move candidates

- `proactive-explorer`
- `skill-hunter`
- `academic-paper-helper`
- `academic-research-writer`
- `research-paper-writer`
- `codex-collaboration.bak`

## Recommended Next Pass

If only one cluster is tackled next, the best order is:

1. `proactive-explorer` and AGENTS boundary cleanup
2. `skill-hunter` + `find-skills` consolidation
3. research-writing generic trio cleanup

That order gives the highest reduction in routing confusion with the least destructive change.
