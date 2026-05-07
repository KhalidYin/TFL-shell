# TFL Mock Shell 生成规范与产品化设计（中文版 V1）

日期：2026-04-28  
主题：当前 TFL mock shell 生成规范收敛，以及后续 Skill / MCP 产品化设计基线  
状态：V1，供 review

## 1. 文档目的

本文档用于把当前仓库内分散的 TFL mock shell 相关规则整理为一份可 review、可继承、可产品化的中文设计文档。其目标不是替代现有项目文档，而是在以下三层之间建立统一基线：

- 治理层：定义当前项目必须遵守的受控规则
- 生成层：说明当前 generator 实际如何生成 DOCX / XLSX / SOP 三类产物
- 产品化层：为后续封装成 Skill 或 MCP 提供稳定边界和抽象方向

本文档的定位是“总设计稿”，优先解决“规则分散、历史口径漂移、接口边界不清”三个问题。

## 2. 背景与现状

当前仓库已经具备临床 CSR 统计部分 TFL shell 的基础生成能力，且可同步生成三类正式产物：

- 主 DOCX shell 模板
- XLSX TOC / 使用指引工作簿
- SOP DOCX

现有规范分散在项目级文档、设计说明、SOP 内容源、XLSX 指引文本和生成器实现中。对于当前开发和局部修复，这种形态可以工作；但如果后续要抽象为 Skill 或 MCP，则存在明显问题：

- 规则分散，难以识别哪个文件是当前真正规范源
- 部分历史设计口径已过时，但仍残留在局部文本或实现中
- “项目治理规则”和“未来产品接口”尚未分层
- 外部调用者难以理解哪些能力可开放，哪些仍应视为内部实现细节

因此，需要先形成一份中文总设计稿，作为后续 review、修订和产品化抽象的母文档。

## 3. 当前规范源与优先级

建议将当前规范源按以下优先级理解：

### 3.1 一类规范源：当前治理真值

这些文件应视为当前项目治理层的主规范来源：

- `PROJECT_GUIDE.md`
- `PROJECT_SPEC.md`
- `CODE_STYLE.md`
- `test_guide.md`

其中：

- `PROJECT_GUIDE.md` 负责项目定位、用户角色、成熟度和路线图
- `PROJECT_SPEC.md` 负责范围、编号、标签、适用性、构造规则和元数据
- `CODE_STYLE.md` 负责文档同步、版本治理和变更纪律
- `test_guide.md` 负责测试契约和回归检查边界

### 3.2 二类规范源：设计与变更背景

以下文档描述了若干阶段性的设计决策与修复背景：

- `docs/superpowers/specs/2026-04-27-tfl-shell-generator-design.md`
- `docs/superpowers/specs/2026-04-28-documentation-governance-design.md`
- `docs/superpowers/specs/2026-04-28-format-and-traceability-remediation-design.md`

这些文档对理解演进过程非常重要，但其中部分规则已经被后续实现或项目文档修正，因此不应直接作为当前唯一真值。

### 3.3 三类规范源：实现行为真值

以下代码文件反映当前生成器的实际行为，应作为“生成层真值”使用：

- `src/tflshell/data/definitions.py`
- `src/tflshell/generators/docx_shell.py`
- `src/tflshell/generators/xlsx_toc.py`
- `src/tflshell/data/sop_content.py`
- `src/tflshell/docx_utils/three_line_table.py`
- `src/tflshell/docx_utils/xml_helpers.py`
- `src/tflshell/models/tfl_item.py`

如果文档与实现冲突，应明确标记冲突，而不是默认任何一侧自动正确。

## 4. 项目定位与边界

### 4.1 项目定位

`TFLshell` 的当前定位是：

- 用于临床研究 CSR 统计部分的 TFL shell 模板治理与生成
- 面向临床统计师、编程总负责人、QA / 监管审阅者
- 用于 study-specific shell 选择、审阅和交接
- 不用于生成真实统计结果

### 4.2 输出边界

当前受控输出只有三类：

- `TFL_Shell_Template_v<version>.docx`
- `TFL_TOC_v<version>.xlsx`
- `TFL_Shell_SOP_v<version>.docx`

三类输出必须共享同一套核心语义，而不应各自定义不同规则。

### 4.3 范围边界

当前受控章节仅包括：

- `14.1`
- `14.2`
- `14.3`
- `14.4`
- `16.2`

以下内容不在当前生成器正式范围内：

- 真实分析结果
- study-specific SAP 的最终裁决
- 伪造 subject-level mock records
- 项目管理型工作流字段

## 5. 治理层：核心受控规则

### 5.1 TFL 类型规则

项目当前治理三类 TFL：

- `Table`
- `Figure`
- `Listing`

其中：

- 表和列表必须是 shell-first、result-free
- 图可以保留模拟图形，以帮助审阅者理解目标布局

### 5.2 编号与显示标签规则

内部 ID 采用：

- `[Type][Section].[Sequence]`

示例：

- `T14.2.11`
- `F14.2.4`
- `L16.2.3`

面向审阅者的显示标签必须移除类型字母，只保留业务展示形式，例如：

- `Table 14.2.11`
- `Figure 14.2.4`
- `Listing 16.2.3`

### 5.3 适用性规则

当前受控适用性标签只有三种：

- `General`
- `Oncology only`
- `Non-Oncology only`

该字段用于 study-specific shell selection，而不是项目状态或执行状态管理。

### 5.4 元数据规则

每个受控 shell 至少应具备以下元数据：

- `TFL ID`
- `Display Label`
- `Title`
- `Type`
- `Section`
- `Shell Family`
- `Study Phase Scope`
- `Coverage Summary`
- `Population`
- `Applicability`
- `Dataset Source`
- `Program Reference`
- `Dictionary / Standard`
- `Placeholder Style`
- `Footnotes`
- `Remarks`

这些字段既是当前工作簿目录结构的治理基础，也是未来 Skill / MCP 数据模型的候选核心字段。

### 5.5 跨输出一致性规则

以下字段在 DOCX / XLSX / SOP 三类输出中应保持概念一致：

- ID
- Display Label
- Title
- Section
- Type
- Applicability
- Shell Family
- Study Phase Scope
- Coverage Summary
- 版本口径

“一致”并不意味着三类载体必须用完全相同的文本，而是要求它们表达同一治理规则。

## 6. 生成层：当前主生成契约

### 6.1 生成总模型

当前生成器以共享 catalog 为中心，向三个输出面投射：

- DOCX 主模板：面向 CSR 审阅和 study shell review
- XLSX 工作簿：面向目录、字段解释、适用性筛选和治理补充
- SOP：面向标准化治理描述和使用边界

因此，产品化时最应保留的不是某一个输出器，而是“共享 catalog + 多载体渲染”的整体架构。

### 6.2 主 DOCX 契约

主 DOCX 当前约定包括：

- 封面
- Word 原生 TOC
- 使用说明
- 分章节输出 `14.1 / 14.2 / 14.3 / 14.4 / 16.2`
- 每个 TFL 独立 heading、shell body、footnotes 和 traceability 信息

当前 DOCX 使用说明已经反映以下关键规则：

- 非结构列使用 result-free placeholders
- 受控表头使用 `Group 1`、`Group 2`
- 可存在独立 `...` 扩展列
- 扩展列不得与 `Overall`、`HR`、`Total` 或其他 analytic 列合并
- 表格使用三线表，且应自适应页面宽度

### 6.3 XLSX 契约

当前 XLSX 工作簿承担三类职责：

- 主目录
- 字段定义
- 使用指引和变更记录

其核心价值不是“项目管理”，而是“治理语义可检索、可筛选、可交接”。

因此，后续产品化时，XLSX 不应被视为一个普通导出文件，而应被视为“catalog 的治理视图”。

V1 版本确认：XLSX `Usage_Guide` 的 placeholder 指引已同步到当前实现口径，明确使用：

- `Group 1`
- `Group 2`
- 可选独立 `...` 扩展列
- 扩展列不得与 `Overall`、`Total`、`HR` 或其他 analytic 列合并

### 6.4 SOP 契约

SOP 当前承担的角色不是补充说明，而是正式治理文本。其职责包括：

- 说明 shell-first 规则
- 说明 placeholders 的使用边界
- 说明三类输出之间的一致性要求
- 说明格式要求和使用方法

因此，SOP 内容源在产品化时应被单独治理，而不是散落到 prompt 或临时模板中。

## 7. 表格构造规范

### 7.1 列结构规则

当前表格构造规范应以最新项目规则和实现行为为准：

- 第一列保留结构性业务项
- 非第一列使用 result-free placeholder
- 标准受控表头采用 `Group 1`、`Group 2`
- 可选保留独立 `...` 扩展列，用于表达多组扩展可能性
- `Overall` 仅在临床上有明确 pooled summary 语义时保留

### 7.2 严禁的列压缩模式

以下模式属于受控违规模式：

- 将 `...` 与 `Overall` 合并为一个列头
- 将 `...` 与 `HR [95% CI]` 合并为一个列头
- 将 `...` 与 `Total` 合并为一个列头
- 任意导致表头列数与 data values 数量不一致的压缩表头模式

### 7.3 组别命名规则

当前受控命名应统一为：

- `Group 1`
- `Group 2`

历史遗留别名如以下形式应统一归一化：

- `XXX Group 1`
- `Treatment A`
- `G1`
- `Group1`
- `Control`

这类归一化已体现在 `definitions.py` 的受控文本标准化逻辑中。

### 7.4 占位符规则

非结构单元格可使用与目标展示风格匹配的 placeholder，例如：

- `XX`
- `xx`
- `xx (xx.x)`
- `x.xxx`
- `[xx.x, xx.x]`

但不允许：

- 伪造真实统计结果
- 伪造受试者记录
- 伪造 derived summary

### 7.5 表格版式规则

当前正式版式规则包括：

- 使用三线表
- 表头和正文左对齐
- 表格宽度自适应页面
- 尽量保持单个 TFL 在一页内，但这是 best-effort 规则

## 8. 图形与列表规范

### 8.1 Figure 规则

图形 shell 允许保留模拟图，以表达目标展示形式。其主要用途是：

- 审阅布局
- 说明图形结构
- 帮助统计和编程团队提前对齐展示语义

但必须明确：

- 图形 shell 不是最终结果图
- 图例、arm label、注释和标题应与表格命名体系一致

### 8.2 Listing 规则

列表类 shell 的目标是保留结构，不是制造 mock records。受控要求包括：

- 可保留变量名、排序提示、显示字段
- 不允许引入 fabricated subject-level rows
- 应保持与相关表图的 traceability 对应关系

## 9. Traceability 与 source listing 规则

### 9.1 当前治理意图

当受控 listing 已存在时，表或图的 `source_listing` 应尽量映射到最相关的 governed listing，而不是泛化占位。

### 9.2 当前实现状态

`definitions.py` 中已经建立了一组基于 title / family / program_ref 的映射规则，用于以下高频场景：

- oncology response
- survival / landmark / forest
- TFST / subsequent therapy
- respiratory exacerbation
- cardiovascular events
- autoimmune flare / responder
- dose-limiting toxicity
- food-effect / crossover

### 9.3 产品化建议

后续 Skill / MCP 不应把 `source_listing` 视为纯展示文本，而应将其视为 catalog 中的结构化 traceability 关系。

## 10. 当前实现与治理间的关键偏移与处理结论

这是本文档最关键的 review 价值所在。当前仓库虽然整体已趋于一致，但仍存在少量重要漂移，需要在产品化前明确。

### 10.1 偏移 1：XLSX 使用指引口径已在 V1 同步

V1 决议如下：

- 已将 `xlsx_toc.py` 中 `Usage_Guide` 的 placeholder 指引同步为当前实现口径
- 今后以当前实现和项目级规范为准，不再沿用早期 `ellipsis + Total` 的宽泛描述
- 该项后续不再视为开放问题，而应转入持续测试与口径守护

### 10.2 偏移 2：历史设计文档中的旧 arm-label 方案仅作背景参考

早期设计文档中曾出现：

- `Treatment A / Treatment B`
- 禁止 `Group 1 / Group 2`
- 删除 ellipsis 扩展列

V1 结论如下：

- 这些口径已不再代表当前受控规则
- 后续产品化说明中不得再将其当作现行规范
- 历史设计文档仅用于解释演进背景，不再作为当前规则真值来源

### 10.3 偏移 3：设计文档与当前实现的“时间差”通过真值分层处理

仓库中的 design notes 记录了多次治理迭代，因此文档阅读者如果不区分“历史方案”和“当前真值”，很容易把已经被推翻的口径理解为现行规则。

V1 结论如下，后续产品化文档必须显式区分：

- 当前受控规则
- 历史设计背景
- 后续演进方向

## 11. 测试与质量门

当前测试契约强调“验证治理行为，而非复述实现细节”。这一原则对后续产品化同样适用。

### 11.1 当前重点机器校验规则

应优先持续机器校验以下规则：

- TFL ID 唯一性
- section 与 ID 一致
- metadata 完整性
- 适用性标签受控
- DOCX / XLSX / SOP 的关键字段一致性
- `...` 扩展列与 analytic 列分离
- header/value cardinality 一致
- source listing 不泛化
- 冗余 subgroup tables 不回流

### 11.2 产品化后的测试思路

如果做成 Skill 或 MCP，测试层不应只验证“能不能跑”，而应继续验证：

- 返回的 catalog 是否仍符合治理规则
- 输出产物是否仍满足结构契约
- 文档说明与输出行为是否同步

## 12. Skill 化设计建议

### 12.1 Skill 的定位

Skill 更适合作为“面向人类协作者的工作流封装层”，而不是底层渲染器。

建议 Skill 负责：

- 根据研究上下文推荐适用 shell 集合
- 解释某个 shell family 的治理适用范围
- 生成或更新三类正式输出
- 做 study-specific 选择建议
- 做规范审阅与差异提示

### 12.2 Skill 的输入建议

建议输入尽量围绕业务语义，而非内部实现细节。

除结构化参数外，Skill 应支持从实际工作材料中提取需求，常见输入来源包括：

- protocol 或方案文本
- SAP 或统计分析计划
- 相关文章、endpoint 定义或技术说明
- 统计需求清单
- 用户临时给出的 study-specific 说明或问题

Skill 不应要求用户一开始就把需求整理成固定字段；更合理的做法是先识别输入材料中的有效语义，再补齐缺失参数。

可直接显式输入的结构化参数仍建议包括：

- study phase
- therapeutic area
- required sections
- need figures or not
- output target
- naming preference
- whether to include non-oncology or oncology specific families
- whether to run validation

### 12.3 Skill 的中间过程建议

Skill 的中间过程不应只是机械解析输入，而应包含受控、可解释的工作流步骤。建议至少包含两类中间能力：

- 内容理解：先识别用户给出的 protocol、SAP、文章或统计需求中涉及的研究阶段、适应症、主要终点、关键分析集、输出范围和特殊 shell 需求
- 增量建议：在完成基础识别后，主动给出缺口提醒、可选扩展、相关 shell family、traceability 风险和 study-specific tailoring 建议

推荐的中间流程如下：

- 解析输入材料并抽取关键研究语义
- 将自由文本映射到当前 catalog 和治理字段
- 识别缺失信息和潜在冲突
- 先给出基础 shell 建议集
- 再给出额外建议或可扩展选项，而不是一开始就过度展开

### 12.4 Skill 的输出建议

建议输出可包含：

- 推荐 shell 集合摘要
- 正式生成产物路径
- 风险提示
- 缺口说明
- study-specific tailoring 建议

### 12.5 Skill 的边界

以下内容不建议直接暴露给 Skill 用户：

- 过细的内部 normalization helper
- Word XML 级别细节
- 仅供内部测试使用的 header/value 修正逻辑

Skill 应展示业务语义，而不是暴露实现噪音。

## 13. MCP 化设计建议

### 13.1 MCP 的定位

MCP 更适合作为“面向外部 agent 或系统的原子能力接口层”。与 Skill 相比，它更强调：

- 稳定 schema
- 可预测输入输出
- 小而清晰的能力边界

### 13.2 建议的 MCP 能力划分

建议后续优先考虑以下原子工具，而不是一开始就做大而全接口：

- `build_catalog`
- `filter_catalog`
- `validate_catalog`
- `generate_docx_shell`
- `generate_xlsx_toc`
- `generate_docx_sop`
- `generate_all_outputs`
- `inspect_cross_output_consistency`
- `summarize_coverage`
- `summarize_traceability`

### 13.3 建议的 MCP 输入输出模型

MCP 输入应尽量使用结构化参数，例如：

- phase
- domain
- sections
- include_figures
- include_listings
- output_dir
- validation_mode

MCP 输出建议分为两类：

- 结构化结果：catalog summary、validation result、rule violations
- 文件产物结果：生成路径、文件名、版本信息

### 13.4 不建议过早暴露的 MCP 能力

以下能力如果在当前阶段直接开放，容易因规则未完全稳定而导致接口频繁破坏：

- 任意自定义 shell 结构编辑
- 任意自定义 metadata schema
- 绕过治理约束的自由生成接口
- 直接操作 Word 内部 XML 的低层工具

## 14. 推荐演进路线

建议路线如下：

### 14.1 第一步：文档统一

先以本文档为母稿，统一：

- 当前真正规则
- 当前实现映射
- 漂移点清单
- 产品化边界

### 14.2 第二步：抽象稳定 schema

在文档通过 review 后，抽出统一的数据模型附录，至少包含：

- shell identity
- display fields
- metadata fields
- placeholder columns
- traceability fields
- output options

该部分的 V1 细化设计现已单独沉淀为：

- `docs/superpowers/specs/2026-04-28-tfl-skill-input-and-intermediate-schema-design.md`
- `docs/superpowers/specs/2026-04-28-tfl-skill-v1-workflow-and-minimum-implementation-plan.md`
- `docs/superpowers/specs/2026-04-28-tfl-skill-v1-recommend-slice-design.md`
- `docs/superpowers/specs/2026-04-28-tfl-skill-v1-presentation-profile-design.md`

### 14.3 第三步：先做 Skill

优先做 Skill，而不是直接做 MCP。理由如下：

- 当前最成熟的是治理语义和生成流程，不是外部 API
- Skill 更适合验证用户工作流价值
- Skill 可更容易吸收规范变动

### 14.4 第四步：再做 MCP

待 schema 和流程稳定后，再把其中成熟的原子能力封装成 MCP tools。

## 15. 对当前方案的总体判断

我的判断是：当前项目已经具备成为 Skill / MCP 基础的条件，但尚未达到“直接稳定开放接口”的状态。

原因不是生成能力不足，而是还缺一个更稳定的“治理语义中台”。这个中台并不一定先表现为代码模块，更可能首先表现为：

- 一份统一规范文档
- 一套稳定元数据 schema
- 一组明确的 drift 清单和同步机制

只有在这三者建立后，Skill / MCP 才不会在后续几轮迭代中频繁改接口。

## 16. 风险提示

- 技术风险：如果在当前规则尚有局部漂移时直接抽象外部接口，MCP schema 很快会失稳。
- 维护风险：如果不先抽出统一 schema，Skill 实现容易直接依赖当前内部对象结构，后续重构成本高。
- 项目风险：如果产品化文档不区分“当前已实现”和“未来规划”，在临床统计或监管 review 中容易被误解为过度承诺。

## 17. 优化建议

### 17.1 立即可做

- 以本文档为母稿，完成一次规则 review
- 保持 XLSX 使用指引与当前实现口径同步，并通过测试守护
- 在项目级文档中补一个“当前真值优先级说明”

### 17.2 中长期

- 抽出 machine-readable catalog schema
- 将 traceability 关系从自由文本逐步提升为结构化字段
- 把 study phase / domain / family 的选择逻辑进一步规则化

### 17.3 工具链

- 持续把 `generate`、`validate`、`pytest` 作为质量门
- 增加文档口径一致性检查，避免 SOP / DOCX / XLSX / 项目文档再次漂移
- 为未来 Skill / MCP 增加 contract tests，而不仅是功能测试

## 18. 建议的后续文档拆分

如果本文档 review 通过，建议后续拆分为三份正式文档：

- `TFL mock shell 治理规范`
- `TFL shell 生成契约与数据模型`
- `Skill / MCP 产品化设计说明`

拆分顺序应在 schema 稳定之后进行，而不是现在立即拆分。当前阶段保留单文档更有利于 review 和统一口径。
