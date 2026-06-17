---
name: project-documentation-rules
description: 本项目采用 personal-assistant 文档结构，并将稳定规范集中到 docs/main 与 Skill 契约中。
type: project
---

本项目文档采用 `personal-assistant` 规范：

- `docs/main/` 是项目蓝图和长期规范的唯一主入口。
- `docs/dep/DEVLOG.md` 记录已完成开发轮次。
- `docs/dep/TASK_STATE.md` 只在任务进行中存在，完成后必须删除。
- `USAGE.md` 提供使用入口和常用命令。

**Why:** 用户明确要求按照 personal-assistant 规范约束文档，并且头脑风暴文档不保留。

**How to apply:** 新的稳定规则写入 `docs/main/` 或 `Skill/tfls-shell/docs/`；临时分析和草稿不要作为长期项目文档提交。
