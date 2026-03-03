# LangGraph Agent


一个使用 **LangGraph** 构建的 AI Agent 实验与实战仓库。

目标：探索和实现生产级别的、可控的、具备记忆与工具能力的智能体（Agent），包括单 Agent、多 Agent 协作、RAG 增强、视觉工具集成等模式。

当前包含：

- ReAct 风格研究助理 Agent（搜索 + 阅读 + 总结）
- 带持久化记忆的多轮任务型 Agent（客服/日程/报销场景）
- 多 Agent 协作系统（产品经理 + 工程师 + 测试）
- RAG + 自查询知识库 Agent
- 视觉理解 Agent（基于 Qwen-VL / LLaVA）

## 为什么选择 LangGraph？

- 原生支持**循环、分支、人机交互、状态持久化**
- 比 LangChain AgentExecutor 更灵活、可调试
- 完美适配 LangSmith 链路追踪
- 支持 LangGraph Cloud / 自建 API 部署

