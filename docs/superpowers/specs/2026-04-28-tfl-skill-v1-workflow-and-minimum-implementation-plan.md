# TFL Skill V1 工作流与最小实现计划（中文版）

日期：2026-04-28  
主题：基于当前 TFLshell 仓库能力的 Skill V1 工作流设计与最小实现计划  
状态：V1，`recommend` 原型已落首版基线，供 review

## 1. 文档目的

本文档用于把前两份设计文档进一步收敛为一份“可执行的 V1 实现计划”：

- `TFL Mock Shell 生成规范与产品化设计（中文版 V1）`
- `TFL Skill V1 输入与中间状态 Schema 设计（中文版）`
- `TFL Skill V1 格式契约与 Presentation Profile 设计（中文版）`

本文档聚焦三个问题：

- Skill V1 先做什么
- Skill V1 不做什么
- Skill V1 如何复用当前 `TFLshell` 仓库能力，而不是另起一套平行系统

## 2. V1 实现目标

Skill V1 的目标不是做成一个全能临床统计助手，而是先做成一个“受控、可解释、可落地”的工作流封装层。

V1 应优先支持两类高价值场景：

- `recommend`：用户给出 protocol / SAP / 统计需求，Skill 推荐适用 shell 包与扩展建议
- `generate`：在推荐或用户指定基础上，生成受控的 DOCX / XLSX / SOP 产物，并给出验证结果

这两个模式已经覆盖最核心的使用链路：

- 理解输入
- 映射治理字段
- 选择 shell
- 输出结果

## 3. V1 明确范围

### 3.1 In Scope

- 接收非结构化输入材料与结构化偏好参数
- 抽取研究语义并形成中间状态
- 将研究语义映射到现有 catalog 和治理字段
- 给出基础 shell 推荐包
- 给出增量扩展建议与缺口提醒
- 调用现有生成器生成正式产物
- 调用现有验证能力并返回结果摘要

### 3.2 Out of Scope

- 自动编写 study-specific SAP 结论
- 任意自定义 TFL 表头结构
- 允许绕过治理约束自由增删字段
- 从复杂 Word / PDF 原件中做高保真结构反向抽取
- 实现完整 MCP server
- 一次性支持全部 `task_mode`

## 4. V1 推荐任务模式

虽然 schema 文档中定义了五种 `task_mode`，但 V1 最小实现建议只落两个：

- `recommend`
- `generate`

其余模式建议暂缓：

- `review`：可在 V1.5 或 V2 复用推荐链路扩展
- `compare`：等输入材料解析与推荐结果结构稳定后再做
- `extend`：可先作为 `recommend` 输出中的“扩展建议”体现，不必单独立模式

这是为了减少首版范围膨胀，避免刚开始就把状态机做复杂。

## 5. Skill V1 总体工作流

V1 工作流建议拆成七个顺序步骤：

1. 输入收集
2. 输入规范化
3. 研究语义抽取
4. 治理字段映射
5. shell 推荐
6. 生成与验证
7. 结果回传

其中，`recommend` 运行到第 5 步即可完成，`generate` 则会继续执行到第 7 步。

## 6. 详细工作流设计

### 6.1 步骤 1：输入收集

输入来源应允许包括：

- 用户 prompt
- protocol 文本或节选
- SAP 文本或节选
- 文章或方法说明
- 统计需求清单
- study-specific 补充说明

此步骤产出：

- `input_bundle`
- 初始 `execution_preferences`
- `user_overrides`

### 6.2 步骤 2：输入规范化

目标是把不同来源材料整理成统一可处理的对象，而不是立即下结论。

此步骤需要完成：

- 识别输入来源类型
- 判断文本是否可用
- 标记主要来源与次要来源
- 记录语言、质量和信息完整性

此步骤产出：

- `ingestion_state`

### 6.3 步骤 3：研究语义抽取

目标是从材料中抽出后续推荐真正需要的研究上下文。

V1 建议至少抽取以下信息：

- study phase
- therapeutic area
- indication
- development intent
- primary endpoints
- secondary endpoints
- analysis populations
- special assessment signals
- 是否需要 patient listings

此步骤产出：

- `extraction_state`

### 6.4 步骤 4：治理字段映射

目标是将自由文本语义转换为当前仓库可消费的治理语言。

V1 建议至少映射以下字段：

- `section_scope`
- `applicability_hint`
- `shell_family_candidates`
- `study_phase_scope_hint`
- `include_figures`
- `include_listings`

如果存在冲突或缺失，应同步形成：

- `ambiguity_state`

此步骤产出：

- `normalization_state`
- `ambiguity_state`

### 6.5 步骤 5：shell 推荐

目标是基于当前 catalog 给出：

- 基础包
- 可选扩展
- 排除建议
- 风险和缺口说明

V1 推荐逻辑应以现有 catalog 为主，不应另起一套平行知识库。

此步骤产出：

- `recommendation_state`

### 6.6 步骤 6：生成与验证

只有在 `task_mode=generate` 时才进入此步骤。

执行内容包括：

- 构造过滤条件
- 应用受控 `presentation_profile` 与对象级 layout policy
- 调用现有生成器
- 调用现有验证能力
- 汇总结果路径、统计信息和 warnings

此步骤产出：

- `generation_plan_state`
- `generation_results`
- `validation_results`

### 6.7 步骤 7：结果回传

返回结果时应同时包含：

- 结论
- 依据
- 风险
- 建议

而不是只返回文件路径或 shell ID 列表。

## 7. 与现有仓库能力的映射

Skill V1 不应重写底层能力，而应优先复用当前代码入口。

### 7.1 Catalog 构建

当前应直接复用：

- `build_catalog()` in `src/tflshell/data/definitions.py`

作用：

- 获取当前完整受控 shell 库
- 继承现有元数据、header normalization、source listing 映射规则

### 7.2 Catalog 查询与摘要

当前应直接复用：

- `TFLCatalog.all()`
- `TFLCatalog.by_section()`
- `TFLCatalog.by_type()`
- `TFLCatalog.by_therapeutic_area()`
- `TFLCatalog.get()`
- `TFLCatalog.summary_stats()`
- `TFLCatalog.section_summary()`
- `TFLCatalog.validate()`

作用：

- 提供推荐前的数据基础
- 提供生成后的汇总与验证能力

### 7.3 正式输出生成

当前应直接复用：

- `DocxShellGenerator`
- `XlsxTocGenerator`
- `DocxSopGenerator`

V1 不建议再套一层新的渲染逻辑；Skill 只负责组织调用条件和解释结果。

### 7.4 CLI 逻辑借鉴

当前 `main.py` 已经体现出三类最小能力：

- generate
- list
- validate

Skill V1 可以把这三类能力提升为更面向用户语义的工作流，而不必重写其所有实现。

## 8. V1 最小实现架构

建议 Skill V1 内部拆分为五个逻辑组件。

### 8.1 `InputResolver`

职责：

- 接收多来源输入
- 形成 `input_bundle`
- 判断来源类型和可用性

### 8.2 `ContextExtractor`

职责：

- 从输入材料中抽取研究语义
- 形成 `extraction_state`
- 标记缺失和冲突

### 8.3 `GovernanceMapper`

职责：

- 将研究语义映射为当前 catalog 可消费的治理字段
- 形成 `normalization_state`
- 产出推荐所需过滤条件

### 8.4 `ShellRecommender`

职责：

- 基于 `TFLCatalog` 选择基础包
- 给出扩展建议与排除项
- 形成 `recommendation_state`

### 8.5 `OutputOrchestrator`

职责：

- 调用现有 generator
- 调用现有 validation
- 汇总结果路径、统计信息与 warnings

V1 阶段，这五个组件即使最开始并不完全拆成独立模块，也应在设计上保持职责分离。

## 9. V1 结果返回形态

V1 返回建议采用“结构化状态 + 面向用户摘要”双层形式。

### 9.1 面向程序的结构化返回

保留：

- `request_summary`
- `interpreted_context`
- `recommendation_state`
- `generation_results`
- `validation_results`
- `risk_notes`
- `optimization_suggestions`

### 9.2 面向用户的摘要返回

输出内容建议包括：

- 当前识别到的研究语境
- 推荐的 sections 与 shell families
- 生成了哪些文件
- 哪些规则需要人工确认
- 有哪些额外扩展建议

这样既方便用户理解，也方便未来转成 MCP tool 输出。

## 10. V1 建议实现顺序

建议按以下顺序实现，而不是并行铺开。

### 10.1 第一阶段：只做 `recommend`

目标：

- 能接收多来源输入
- 能抽取最小研究语义
- 能映射到治理字段
- 能输出基础包与扩展建议

完成标准：

- 不生成文件，也能稳定给出推荐和风险说明
- 当前仓库已落地 `tflshell recommend` 原型，作为该阶段的首版基线

### 10.2 第二阶段：接入 `generate`

目标：

- 在推荐结果基础上调用现有 generator
- 生成 DOCX / XLSX / SOP
- 返回路径和统计摘要

完成标准：

- 不引入新的底层生成实现
- 输出结果与现有 CLI 行为一致

### 10.3 第三阶段：接入验证结果

目标：

- 调用现有 validation
- 汇总 warnings
- 将验证结果结构化回传

完成标准：

- 用户能在一次 Skill 调用中看到推荐、生成和验证的完整闭环

## 11. V1 最小测试计划

虽然本轮仍是文档设计，但 V1 一旦实施，建议至少准备以下测试层次。

### 11.1 Schema 层

- 输入对象是否满足最小字段要求
- `task_mode` 是否在受控集合内
- 中间状态对象字段是否齐全

### 11.2 工作流层

- `recommend` 模式是否能在仅有 user prompt 时正常工作
- `recommend` 模式是否能从 SAP 片段抽出基本研究语义
- `generate` 模式是否能调用现有 generator 并返回文件路径

### 11.3 治理层

- 推荐结果是否仍遵守 section / applicability / shell family 规则
- 生成结果是否保留当前规范中的 group naming 和 ellipsis 规则
- 验证结果是否真实反映 catalog state

## 12. V1 明确不做的实现捷径

为避免 V1 变形，建议明确禁止以下捷径：

- 用单个大 prompt 把解析、推荐、生成、验证全糊在一起
- 不保留中间状态，只返回最终摘要
- 在 Skill 内复制一份独立 catalog
- 为了图快绕过现有 generator，直接在 Skill 中拼接输出内容

这些做法短期看似省事，长期会让 Skill 无法测试、无法迁移到 MCP、也无法稳定维护。

## 13. 与 MCP 的衔接策略

V1 工作流建议把 Skill 视为“编排层”，而不是“MCP 的替代品”。

后续适合逐步下沉为 MCP tools 的能力包括：

- `build_catalog`
- `filter_catalog`
- `summarize_catalog`
- `validate_catalog`
- `generate_outputs`

而以下能力更适合保留在 Skill 上层：

- 从非结构化材料抽取研究语义
- 生成面向用户的扩展建议
- 处理低风险假设并解释理由

## 14. 对 V1 的总体判断

我认为 Skill V1 完全可以基于当前仓库落地，但必须坚持“小步、受控、可解释”的原则。

最重要的不是首版支持多少功能，而是把以下链路做实：

- 输入材料
- 中间状态
- 推荐结果
- 生成结果
- 验证结果

只要这条链路是稳定的，后续无论扩到 `review`、`compare`，还是拆出 MCP，都有稳固基础。

## 15. 风险提示

- 技术风险：如果 V1 同时实现全部 `task_mode`，状态机会迅速复杂化，反而拖慢可用版本。
- 维护风险：如果推荐逻辑不复用现有 catalog，而是在 Skill 内重新写规则，后续会产生双重真值。
- 项目风险：如果 `recommend` 与 `generate` 的边界不清，用户会误以为 Skill 能直接给出 study-specific 最终监管结论。

## 16. 优化建议

### 16.1 立即可做

- 先把 `recommend` 模式做成最小闭环
- 再把 `generate` 接到现有 generator
- 保持中间状态对象可见、可测试
- `recommend` 首切片的进一步设计见 `docs/superpowers/specs/2026-04-28-tfl-skill-v1-recommend-slice-design.md`
- `generate` 前的格式边界设计见 `docs/superpowers/specs/2026-04-28-tfl-skill-v1-presentation-profile-design.md`

### 16.2 中长期

- 逐步把 `review` 和 `compare` 拆成独立模式
- 为 endpoint intent、analysis class 等补充更稳定的受控枚举
- 将推荐理由进一步结构化

### 16.3 工具链

- 为 Skill V1 增加 workflow fixture
- 为中间状态对象增加 contract tests
- 在 Skill 与未来 MCP 之间共享 schema 校验规则
