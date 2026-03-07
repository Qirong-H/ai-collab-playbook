# 与 Gemini 协作

对应本地 skill：`collaborating-with-gemini`

适用场景：
- 想让 Gemini CLI 作为第二意见来源
- 需要补一个不同模型视角做对照验证
- 想让它帮忙看设计、debug 或 patch review

输入：
- 工作目录
- 任务 prompt
- 可选的 `SESSION_ID`
- 需要它读取的文件或工作区内图片路径

输出：
- Gemini 的结构化回复
- 可复用的 `SESSION_ID`
- 当前协作会话的状态胶囊

边界：
- 它依旧是协作者，不会替你承担最终验证责任
- 图片等附件必须位于工作区可访问路径，不是任意路径都能直接读
