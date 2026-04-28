# Skill 包说明

> 历史说明：本目录保留为早期命名版本。当前正式复用 Skill 请以
> `.trae/skills/tfls-shell/` 下的 `TFLs-Shell SKILL` 为准。

## 1. 目的

本文件用于说明这个 Skill 包的组成方式，避免把 `SKILL.md` 误解为唯一
交付物。

一个可复用 Skill 的最小有效入口是 `SKILL.md`，但为了让调用结果更可靠，
Skill 包可以同时包含补充文档、规则文件、示例和辅助资产。

## 2. 当前包结构

当前包建议按以下意图维护：

- `SKILL.md`：主入口，定义 Skill 的用途、触发条件、主流程和输出边界
- `PACKAGE_GUIDE.md`：说明 Skill 包的组成、目录作用和维护方式
- `DEVELOPMENT_RULES.md`：约束未来如何定义、扩展和实现这个 Skill

后续如果确实有必要，可以继续加入：

- `examples/`：典型调用样例
- `assets/`：固定模板、辅助映射表、提示片段
- `scripts/`：用于增强可靠性的辅助脚本
- `references/`：术语、映射规则、输出字段说明

## 3. 设计原则

- `SKILL.md` 是入口，不是全部
- 包内补充文档应服务于可靠调用，而不是重复无效描述
- 能写成稳定规则的内容，优先进入包内文档
- 能沉淀成可复用辅助脚本的内容，可以进入 `scripts/`
- 某个项目的内部 CLI 或实现文件，不自动等于 Skill 包本体

## 4. 与项目实现的关系

Skill 包是应用层定义。

项目实现是某个仓库里为了支撑该 Skill 而存在的代码、测试、生成器或辅助逻辑。

两者关系应理解为：

- Skill 包定义“应该如何被调用、应该产出什么、遵守什么边界”
- 项目实现负责“在当前仓库里如何落地这些要求”

如果项目实现变化，但 Skill 的应用层意图没有变化，应优先维护 Skill 包的
稳定边界。

## 5. 输出物区分

请始终区分以下几类东西：

- `Skill package deliverables`：Skill 包自身文件
- `Project documents`：某个项目的总览、规范、测试说明
- `Implementation files`：某个项目的代码、脚本、测试
- `Business outputs`：最终生成的 DOCX / XLSX / SOP 等业务文件

Skill 包不应被业务输出覆盖，也不应被某个实现文件替代。
