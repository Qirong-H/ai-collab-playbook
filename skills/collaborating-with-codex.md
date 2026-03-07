# 与 Codex 协作

对应本地 skill：`collaborating-with-codex`

适用场景：
- 想拉第二个 Codex CLI 会话进来做原型、复核或调试
- 想保留多轮 session，而不是一次性问答
- 想通过 bridge 脚本拿到更稳定的结构化输出

输入：
- 工作目录
- 任务 prompt
- 可选的 `SESSION_ID`
- 是否要求 unified diff patch

输出：
- Codex 协作者的结构化回复
- 可继续复用的 `SESSION_ID`
- 便于继续追问的会话标识与返回结果

边界：
- 它本质上仍然是一个 CLI bridge，不是“多 Codex 协作平台”
- 危险参数和高权限模式不能被当成默认安全能力来宣传
独立仓库：<https://github.com/cnfjlhj/collaborating-with-codex>
