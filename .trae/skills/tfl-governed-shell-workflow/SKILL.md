---
name: "tfl-governed-shell-workflow"
description: "用于把 protocol/SAP/统计需求解释为受控 TFL shell 推荐与生成步骤。适用于需要复用的应用层 TFL shell 选择或生成工作流。"
---

# TFL 受控 Shell 工作流

> 历史说明：本目录保留为早期命名版本。当前正式复用 Skill 请以
> `.trae/skills/tfls-shell/` 下的 `TFLs-Shell SKILL` 为准。

## 目的

这个 Skill 是一个可复用的、面向应用层的工作流包，用于把用户材料转成
受控的 TFL shell 推荐与生成动作。

它适合把如下输入：

- protocol 片段
- SAP 片段
- 统计需求说明
- study note
- 其他研究上下文材料

转换为：

- 受控 TFL shell 推荐
- 受控输出生成指令
- 明确的风险提示与后续建议

这个 Skill 是包级别的工作流定义，不等同于某个项目里的单个实现文件。

本 Skill 包的补充说明见：

- `PACKAGE_GUIDE.md`
- `DEVELOPMENT_RULES.md`

## 何时调用

当用户需要以下任一能力时调用本 Skill：

- 从 prompt、protocol、SAP 或 study note 中推荐受控 TFL shell 包
- 判断应纳入哪些 CSR section 或 shell family
- 在推荐基础上生成受控 TFL 输出
- 解释 recommend、generate 与正式输出物之间的关系
- 产出正式 TFL 交付文件

以下情况不要调用本 Skill：

- 与 TFL shell 选择或生成无关的一般性代码重构
- 不影响推荐/生成流程的底层 DOCX XML 修补
- MCP 打包工作，除非用户明确要求

## 适用范围

本 Skill 适用于“受控 TFL shell 推荐与生成”这一类应用场景，可绑定到具体
项目实现，但不应把某个项目的内部文件结构当成它的前置条件。

当前受控输出范围：

- `14.1` Demographics and Baseline Characteristics
- `14.2` Efficacy
- `14.3` Safety
- `14.4` Special Assessments
- `16.2` Patient Data Listings

超出范围：

- 真实研究结果
- 最终的 study-specific SAP 结论
- 绕过治理约束的自由 shell 结构编辑

## 概念边界

请始终区分以下几层：

- `Generator layer`：正式 DOCX / XLSX / SOP 的生成能力
- `Skill package`：这个可复用的工作流定义
- `Project implementation`：某个项目里对这个工作流的具体落地实现
- `Formal outputs`：最终交付给用户的 DOCX / XLSX / SOP 文件

Skill 包是可复用定义，项目实现只是它的一种落地方式。

## 规范来源

本 Skill 是应用层工作流包，因此不要硬编码依赖某几个项目文档一定存在。

如果所在项目提供了以下类型文档，应优先读取并遵循：

- 项目总览或使用指南
- 业务规范或治理规则
- 代码规范或变更纪律
- 测试契约或回归说明
- 与 TFL shell 工作流相关的设计说明

如果这些文档不存在，就以当前应用的显式行为约束、可见输入输出契约和用户
确认的规则为准。

如果文档与实现冲突，不要静默猜测，应明确指出冲突并在同一变更集中解决。

## 工作流

按以下顺序执行。

### 1. 收集输入

可接受输入来源包括：

- user prompt
- protocol 片段
- SAP 片段
- article 或 method note
- study note
- statistical request list

优先支持“材料驱动输入”，不要强迫用户先手工拼好 JSON。

### 2. 归一上下文

抽取或推断最小治理上下文：

- study phase
- therapeutic area
- endpoint 信号
- analysis populations
- 是否需要 figures
- 是否需要 listings
- 若请求生成，则识别期望输出类型

如果上下文不完整，可以带着受控默认值继续，但必须把假设显式说清楚。

### 3. 映射到治理语言

把自由研究语言转换为治理语言：

- section scope
- applicability hint
- shell family candidates
- phase scope hint

不要另起一套平行 shell 分类体系。

### 4. Recommend

给出清晰拆分的推荐结果：

- base package
- optional expansions
- exclusions
- ambiguity 或 risk notes

推荐结果应建立在当前 catalog 或治理规则之上，而不是纯自由叙述。

### 5. Generate

如果用户请求生成输出：

- 复用 recommend 阶段解释出来的上下文
- 应用受控过滤条件
- 生成正式输出
- 返回 artifact 路径与 validation 摘要

正式输出文件通常包括：

- `TFL_Shell_Template_v<version>.docx`
- `TFL_TOC_v<version>.xlsx`
- `TFL_Shell_SOP_v<version>.docx`

这些是业务输出物，不是治理规则真值源。

### 6. Report

结果至少应返回：

- interpreted context
- recommendation summary
- 如果发生生成，则返回 generation summary
- validation summary
- risk notes
- optimization suggestions

不要只返回文件路径而不给解释。

## 推荐输出结构

如需结构化输出，优先采用以下字段：

- `task_mode`
- `request_summary`
- `interpreted_context`
- `ingestion_state`
- `extraction_state`
- `normalization_state`
- `ambiguity_state`
- `recommendation_state`
- `generation_results`
- `validation_results`
- `risk_notes`
- `optimization_suggestions`

`recommend` 可以让 `generation_results` 为空，但在可能的情况下，字段结构
最好保持一致。

## 输出类别区分

始终明确区分以下几类东西：

- `Governance documents`：项目文档与设计说明
- `Reusable Skill package`：这份 `SKILL.md`
- `Project implementation`：代码、CLI、测试等具体实现
- `Formal business outputs`：最终生成的 DOCX / XLSX / SOP 文件

混淆这些类别就是工作流错误。

## 实现入口示例

如果当前应用已经提供实现入口，可在遵循本 Skill 包边界的前提下使用其推荐
命令。

以下命令只是某个项目实现的示例，不构成 Skill 包本体。

Recommend 示例：

```bash
tflshell skill --mode recommend --text "<study context>" --json
```

Generate 示例：

```bash
tflshell skill --mode generate --text "<study context>" --type all --json
```

如果将来实现入口发生变化，应同步更新本 Skill 包中的示例说明，并避免把
项目实现误写成 Skill 定义本身。

## 约束规则

- 不要绕过受控 shell metadata。
- 不要在未实现时承诺 MCP 能力。
- 不要把某个项目里的 `skill.py` 当成 Skill 包本体。
- 不要让生成结果反过来定义项目规则。
- 不要在不更新文档与测试的情况下修改 recommend 或 generate 行为。

## 文档同步

当这个 Skill 包发生实质变化时，建议同步检查：

- 应用的总览文档
- 业务规范或治理文档
- 代码规范文档
- 测试契约文档
- 相关设计说明
- `PACKAGE_GUIDE.md`
- `DEVELOPMENT_RULES.md`

如果这些文档不存在，就至少同步更新这份 `SKILL.md` 与对应实现说明。

## 示例

### 示例 1：只做 Recommend

用户说：

> 为一个 Phase II 非肿瘤研究推荐受控 TFL shell 包，主要终点是
> time-to-first exacerbation。

期望行为：

- 识别出 Phase II
- 识别出 Non-Oncology
- 纳入 `14.2` efficacy 与 `14.3` safety
- 大概率保留 `16.2` listings
- 如果 phase/domain 证据不足，补充风险提示

### 示例 2：Recommend + Generate

用户说：

> 为一个以 PFS 和安全性审阅为重点的 oncology 研究生成受控输出包。

期望行为：

- 推断出 oncology 生存分析导向的 efficacy 语境
- 推荐相应的 base package
- 生成正式 DOCX / XLSX / SOP 输出
- 返回 artifact 路径和 validation 摘要

## 维护目标

这份 Skill 包应保持：

- 可复用
- 场景清晰
- governance-first
- 边界明确

如果后续应用扩展出新的 workflow mode，应在新行为文档化、测试化、稳定后，
再扩展这份 Skill 包。
