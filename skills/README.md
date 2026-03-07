# Skills

[中文] | [English](README.en.md)

这里是这个仓库的人类可读技能入口。

如果你第一次来到这里，可以这样理解当前结构：

- `skills/*.md`：中文技能卡片，适合先快速判断“这是不是我需要的东西”。
- `skills/full/<skill>/`：公开版完整 skill 包，通常至少包含 `SKILL.md`，有的还会带 `references/`、`scripts/` 或额外 `README.md`。

如果你只是想先看最有代表性的几项，我建议先从下面这些开始：

- [`paper-review-pipeline`](paper-review-pipeline.md)
- [`paperreview`](paperreview.md)
- [`skills-governance`](skills-governance.md)
- [`session-recovery-codex`](session-recovery-codex.md)
- [`collaborating-with-codex`](collaborating-with-codex.md)
- [`prompt-polisher`](prompt-polisher.md)
- [`writing-anti-ai`](writing-anti-ai.md)
- [`xhs-longform-private-publisher`](xhs-longform-private-publisher.md)

## 研究与写作

- [`academic-paper-helper`](academic-paper-helper.md) / [`full`](full/academic-paper-helper/)：LaTeX、BibTeX、论文结构模板与常用写作支架。
- [`paper-review-pipeline`](paper-review-pipeline.md) / [`full`](full/paper-review-pipeline/)：论文自审、投稿前 QA、rebuttal 与审稿意见回复的总管式流程。
- [`paperreview`](paperreview.md) / [`full`](full/paperreview/)：把接近定稿的 PDF 提交到 `paperreview.ai` 做外部第二意见。
- [`question-refiner`](question-refiner.md) / [`full`](full/question-refiner/)：把模糊研究问题收敛成结构化研究任务说明。
- [`writing-anti-ai`](writing-anti-ai.md) / [`full`](full/writing-anti-ai/)：去掉 AI 味，尽量保留原本的真实语气和立场。
- [`timestamped-video-summary`](timestamped-video-summary.md) / [`full`](full/timestamped-video-summary/)：把带时间戳的字幕整理成结构稳定的纪要，并可导出 PDF。

## 协作、规划与恢复

- [`proactive-explorer`](proactive-explorer.md) / [`full`](full/proactive-explorer/)：先搜索、先读文件、先摸清事实，再去问用户。
- [`all-plan`](all-plan.md) / [`full`](full/all-plan/)：用多视角计划生成、评分和纠偏来处理复杂任务。
- [`human-machine-brainstorm`](human-machine-brainstorm.md) / [`full`](full/human-machine-brainstorm/)：做人机协同的需求对齐与多模型头脑风暴。
- [`prompt-polisher`](prompt-polisher.md) / [`full`](full/prompt-polisher/)：把散乱输入整理成真正可执行的 prompt。
- [`session-recovery-codex`](session-recovery-codex.md) / [`full`](full/session-recovery-codex/)：恢复 Codex 会话现场，提取任务、TODO、关键报错与上下文。
- [`skill-creator`](skill-creator.md) / [`full`](full/skill-creator/)：把零散工作流变成更稳定、可复用的 skill。
- [`skills-governance`](skills-governance.md) / [`full`](full/skills-governance/)：盘点、分组、去重、治理本地 skill 集合。
- [`find-skills`](find-skills.md) / [`full`](full/find-skills/)：先查 skills.sh，再用 GitHub 深搜兜底，去寻找合适 skill。

## 多模型协作

- [`collaborating-with-claude`](collaborating-with-claude.md) / [`full`](full/collaborating-with-claude/)：把 Claude Code CLI 拉进来做第二意见。
- [`collaborating-with-codex`](collaborating-with-codex.md) / [`full`](full/collaborating-with-codex/)：把第二个 Codex CLI 会话拉进来做原型、复核或协作。
- [`collaborating-with-gemini`](collaborating-with-gemini.md) / [`full`](full/collaborating-with-gemini/)：把 Gemini CLI 拉进来做对照验证或补充视角。

## 发布与内容生产

- [`xhs-note-creator`](xhs-note-creator.md) / [`full`](full/xhs-note-creator/)：从内容撰写、卡片 Markdown 到渲染与可选发布的小红书笔记生产线。
- [`xhs-longform-private-publisher`](xhs-longform-private-publisher.md) / [`full`](full/xhs-longform-private-publisher/)：把已有 Markdown 长文和插图尽量无损地私密发布到小红书。

## 说明

- `skills/` 这一层更偏“给人先看懂”。
- `skills/full/` 这一层更偏“把真实 skill 包公开出来”。
- 目前我优先公开的是和主文章直接相关、并且适合分享出去的 skill；并不是所有本地私有环境内容都会同步到这里。
