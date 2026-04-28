# TFL Skill V1 `recommend` 模式最小实现切片设计（中文版）

> 当前术语说明：本文中的 `Skill V1` 在现行口径下主要归属于
> `TFLs-Shell Product` 的支撑设计，用于说明仓库内的推荐实现切片。
> 正式可复用交付物请以 `.trae/skills/tfls-shell/` 下的
> `TFLs-Shell SKILL` 为准。

日期：2026-04-28  
主题：TFL Skill V1 中 `recommend` 模式的首个可落地闭环设计  
状态：V1，已对应首版 recommend 原型实现基线，供 review

## 1. 文档目的

本文档用于从 `Skill V1 工作流与最小实现计划` 中再向下切一层，定义首个真正建议落地的实现切片：

- 只做 `recommend`
- 不做正式文件生成
- 不做完整验证闭环

目标是先把下面这条链路做实：

- 接收输入材料
- 提取研究语义
- 映射治理字段
- 给出基础 shell 推荐与扩展建议

这应成为 Skill V1 的第一个可交付闭环。

## 2. 为什么先做 `recommend`

先做 `recommend` 而不是 `generate`，有三个原因：

- 它最能验证 Skill 是否真的理解用户输入，而不是只会调用已有生成器
- 它能先把中间状态 schema 跑通，为后续生成和验证打基础
- 它风险最低，不会一开始就引入 Office 输出、路径管理和文件覆盖等复杂度

因此，`recommend` 不是“功能缩减版”，而是最适合首发的核心能力。

## 3. 切片目标

`recommend` 模式最小实现切片的目标是：

- 用户给出 prompt、protocol、SAP、文章或统计需求中的任意一种或多种
- Skill 能抽取基本研究语义
- Skill 能基于当前 catalog 返回基础 shell 推荐包
- Skill 能给出增量建议、缺口提醒和必要假设

V1 切片不要求：

- 生成 DOCX / XLSX / SOP
- 修改现有 shell 内容
- 输出 study-specific 最终结论

## 4. 切片边界

### 4.1 In Scope

- `task_mode = recommend`
- 解析 `input_bundle.sources`
- 支持最小 `execution_preferences`
- 形成 `ingestion_state`
- 形成 `extraction_state`
- 形成 `normalization_state`
- 形成 `ambiguity_state`
- 形成 `recommendation_state`
- 输出用户可读摘要

### 4.2 Out of Scope

- 正式文件生成
- catalog 验证调用
- output path 管理
- sponsor / protocol 覆写写回
- 跨输出一致性检查
- 任意自定义 shell ID 级别精修

## 5. 成功标准

当以下条件满足时，可认为该切片落地成功：

1. 用户只给一句自由文本需求时，Skill 仍能返回基础推荐
2. 用户给 SAP 或 protocol 节选时，Skill 能识别至少部分研究语义
3. 推荐结果包含基础包、扩展建议、风险和假设
4. 推荐结果明确基于当前 catalog，而不是自由发挥
5. 全流程不要求文件输出即可完成

## 6. 输入约束

### 6.1 最小输入

最低要求：

- 至少一条 `sources`

例如：

- 用户 prompt
- SAP 片段
- protocol 节选

### 6.2 推荐支持的输入组合

建议优先支持以下三种组合：

- `仅 user_prompt`
- `user_prompt + SAP`
- `user_prompt + protocol`

这三种已能覆盖最常见的真实使用场景。

### 6.3 暂不优先支持的复杂输入

以下输入可保留接口，但首版不应依赖其完整支持：

- 多篇文章混合输入
- 多协议版本对比
- 长篇复杂 Office 文档原件解析

## 7. 最小中间状态

虽然 schema 文档定义了较完整状态层，但 `recommend` 首切片建议只强制落以下五个状态对象。

### 7.1 `ingestion_state`

必须记录：

- 识别到的来源类型
- 各来源是否可用
- 是否存在明显信息缺口

### 7.2 `extraction_state`

V1 最少抽取以下字段：

- `study_phase`
- `therapeutic_area`
- `primary_endpoints`
- `analysis_populations`
- `key_safety_focus`

如果抽不出来，也必须记录“未知”，不能静默忽略。

### 7.3 `normalization_state`

V1 最少映射以下治理字段：

- `section_scope`
- `applicability_hint`
- `shell_family_candidates`
- `study_phase_scope_hint`

### 7.4 `ambiguity_state`

必须显式记录：

- 缺失字段
- 冲突字段
- 当前假设

### 7.5 `recommendation_state`

必须包含：

- `base_package`
- `optional_expansions`
- `governance_warnings`
- `gap_notes`

## 8. 推荐逻辑的最小版本

首版推荐逻辑建议非常克制，不追求“聪明”，只追求“稳定、可解释”。

### 8.1 基础规则

首版推荐应遵循以下简单顺序：

1. 先确定 section 范围
2. 再确定 therapeutic area 倾向
3. 再确定是否存在 efficacy / safety / special-assessment 明确信号
4. 最后选择基础 shell family 与可选扩展

### 8.2 默认基础包规则

如果信息不足但仍要给出推荐，建议使用如下保守默认：

- `14.1`
- `14.3`
- `16.2`

理由：

- 这三类通常是最稳的基础包
- 即使研究信息不完整，也较少完全不需要

### 8.3 efficacy 信号规则

当输入中出现以下信号时，应优先加入 `14.2`：

- primary endpoint
- efficacy endpoint
- response
- survival
- time-to-event
- responder
- exacerbation
- MACE / cardiovascular event

### 8.4 special assessment 信号规则

当输入中出现以下信号时，可建议加入 `14.4` 相关 family：

- PK
- ADA
- biomarker
- PD
- PRO
- food effect
- crossover

### 8.5 oncology / non-oncology 倾向规则

如果输入明确显示：

- tumor response / RECIST / BOR / ORR / PFS / OS 等肿瘤特征语言，则倾向 `Oncology`
- exacerbation / cardiovascular / autoimmune flare / responder 等非肿瘤特征语言，则倾向 `Non-Oncology`
- 未明确时保持 `General`

首版不应过度推断；判断不清时应保留不确定性。

## 9. 与当前 catalog 的映射方式

`recommend` 首切片不应维护自己的一套推荐库，而应始终基于当前 `TFLCatalog`。

### 9.1 直接复用对象

建议直接复用：

- `build_catalog()`
- `TFLCatalog.all()`
- `TFLCatalog.by_section()`
- `TFLCatalog.by_therapeutic_area()`
- `TFLCatalog.summary_stats()`

### 9.2 推荐的生成方式

建议逻辑如下：

- 先根据 `section_scope` 过滤
- 再根据 `therapeutic_area` 过滤
- 再根据 shell family 候选组装基础推荐包
- 最后补充扩展建议和 gap 说明

### 9.3 首版不做的细粒度能力

首版不建议：

- 直接逐条做 item-level 智能排序优化
- 自动做细粒度 title 级 study-specific 改写
- 直接按统计方法级别定制出最终 shell 集

## 10. 用户返回格式

`recommend` 切片的返回建议拆为两层。

### 10.1 结构化返回

至少包含：

- `interpreted_context`
- `recommendation_state`
- `risk_notes`
- `optimization_suggestions`

### 10.2 用户摘要返回

建议至少包含四段内容：

- 当前理解到的研究语境
- 推荐的 sections / shell families
- 为什么这样推荐
- 还缺什么信息以及可扩展什么

## 11. 首版建议的用户摘要模板

建议摘要模板如下：

- `研究语境判断`：说明当前识别到的 phase、治疗领域、endpoint 倾向
- `基础推荐`：说明建议优先保留哪些 section 和 family
- `扩展建议`：说明哪些 shell 属于条件性扩展
- `不确定性`：说明当前依赖了哪些假设，哪些信息还缺

这个模板有利于保持输出稳定，也方便后续加入 tests。

## 12. 最小实现步骤

建议按以下顺序实现该切片：

### 12.1 第一步：输入与状态骨架

先实现：

- `input_bundle`
- `ingestion_state`
- `extraction_state`
- `ambiguity_state`

目标：

- 即使推荐逻辑还很简单，也先把状态结构搭起来

### 12.2 第二步：最小推荐规则

再实现：

- section 默认规则
- efficacy / safety / special signal 规则
- oncology / non-oncology 倾向规则

目标：

- 在不引入复杂模型的情况下，先稳定给出基础包

### 12.3 第三步：用户摘要输出

最后实现：

- 可读摘要
- 风险提示
- 扩展建议

目标：

- 先让用户能用
- 再考虑后续结构化扩展

## 13. 最小测试建议

### 13.1 输入测试

- 仅有 `user_prompt` 时是否能进入推荐流程
- `user_prompt + SAP` 时是否能识别额外语义

### 13.2 状态测试

- 缺失 phase 时是否写入 `ambiguity_state`
- 推断出 non-oncology 时是否形成对应 `applicability_hint`

### 13.3 推荐测试

- 只给安全导向需求时，是否至少推荐 `14.3`
- 给 time-to-event 或 responder 信号时，是否建议 `14.2`
- 给 PK / ADA / biomarker 信号时，是否提示 `14.4` 扩展可能

## 14. 切片后的下一步

当 `recommend` 切片稳定后，再进入下一步最合适：

- 把 `recommendation_state` 接到 `generate`
- 复用现有 generator
- 返回正式产物路径

这时再做 `generate`，复杂度会明显低很多，因为输入理解和推荐层已经稳定。

## 15. 风险提示

- 技术风险：如果首版就在 `recommend` 中加入过细粒度规则，后续很容易失控并难以测试。
- 维护风险：如果推荐结果不显式记录假设和缺口，后续用户会误以为这些推荐是完全确定的。
- 项目风险：如果 `recommend` 结果被误读为最终 study-specific 监管结论，可能导致使用边界被高估。

## 16. 优化建议

### 16.1 立即可做

- 保持当前 `recommend` 原型仍只覆盖本文档定义的最小闭环
- 默认推荐规则保持保守
- 中间状态优先于复杂推荐算法

### 16.2 中长期

- 增加 endpoint intent 的受控枚举
- 把 family 推荐理由进一步结构化
- 为不同疾病领域逐步补充分层规则

### 16.3 工具链

- 为 `recommend` 模式准备最小 fixture 集
- 将状态对象纳入 contract tests
- 保持 recommend 输出模板稳定，便于回归测试
