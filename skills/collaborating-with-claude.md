# 与 Claude 协作

对应本地 skill：`collaborating-with-claude`

适用场景：
- 想让 Claude Code CLI 给第二意见
- 想让另一个模型帮忙做 diff review、设计权衡或调试分析
- 当前会话仍然要保留最终决策权

输入：
- 目标仓库路径
- 需要查看的文件 / 行号
- 期待输出格式（分析或 unified diff）

输出：
- Claude 的结构化回复
- `SESSION_ID`
- 后续继续协作所需的上下文胶囊

边界：
- Claude 在这里是协作者，不是直接改仓的主执行者
- 输出仍然需要当前会话本地复核和验证，不能直接盲信
