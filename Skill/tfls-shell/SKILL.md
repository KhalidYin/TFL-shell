---
name: "tfls-shell"
description: "用于把 protocol、SAP 与统计需求解释为 TFL shell 推荐与生成指令。适用于需要复用的 TFL shell 选择、说明与生成工作流。"
---

# TFLs-Shell SKILL

## 1. 定位

`TFLs-Shell SKILL` 是一个面向大众的、可复用的应用层 Skill 包。

它的目标是帮助用户把临床研究材料转成更清晰的 TFL shell 工作结果，例如：

- 推荐应使用哪些 TFL shell
- 说明推荐依据与适用范围
- 在需要时生成受控输出
- 给出风险提示与后续建议

它不要求调用方了解某个特定项目、仓库或内部实现结构。

## 2. 来源与边界

本 Skill 可以来源于真实项目经验的沉淀，但交付给调用方时，应保持为一个
可复用、尽量自洽的 Skill 包。

这意味着：

- 可以从既有项目中提炼 workflow、规则、示例、脚本或文档细节
- 但只应纳入真正有复用价值的精选部分
- 不应把整个项目实现或项目背景强行暴露给最终用户

本 Skill 的目标是独立定义“如何调用、如何理解输入、如何给出结果”，而不是
要求调用方在运行时依赖某个完整项目。

## 3. 何时调用

当用户需要以下能力时，调用本 Skill：

- 根据 prompt、protocol、SAP 或统计需求推荐受控 TFL shell 包
- 判断应纳入哪些 CSR section、shell family 或输出类型
- 生成受控的 TFL 交付物
- 给出推荐原因、风险提示、歧义说明与后续建议
- 在应用层协调“推荐 -> 生成 -> 验证摘要”的工作流

以下情况不要调用本 Skill：

- 与 TFL shell 选择或生成无关的一般代码重构
- 纯底层 Office 文档排版修补，且不影响应用层工作流
- 与当前治理范围无关的自由模板编辑

## 4. 输入来源

本 Skill 优先接受材料驱动输入，例如：

- 用户需求描述
- protocol 片段
- SAP 片段
- 统计需求说明
- study note
- article 或 method note

不要强迫用户先构造复杂 JSON；应优先从自然语言和材料中抽取结构化语境。

## 5. 工作目标

本 Skill 目标是把输入解释为：

- 受控 TFL shell 推荐
- 受控生成动作
- 风险提示
- 优化建议
- 稳定、清晰、可复用的结果说明

为提高可靠性，本 Skill 包可以内置或附带一部分精选资产，例如：

- workflow 说明
- 规则摘要
- 样例输入输出
- 字段说明
- 辅助脚本
- 模板片段
- Product 对齐输出契约
- DOCX / XLSX / SOP 结构约束
- table layout 与 placeholder 规则

这些资产应是可复用子集，而不是整个上游项目的直接镜像。

如果目标是把 Skill 包直接带到其他项目中使用，则至少应随包附带：

- contract registry
- catalog 子集
- output manifest
- Product 对齐契约文档
- 最小运行依赖清单
- 可执行样例输入
- 包内 runtime loader / wrapper

这些资产应由 Skill 包自身持有，而不是假设调用环境会从外部仓库补齐。

## 6. 适用范围

当前治理输出范围：

- `14.1` Demographics and Baseline Characteristics
- `14.2` Efficacy
- `14.3` Safety
- `14.4` Special Assessments
- `16.2` Patient Data Listings

当前不在范围内：

- 真实研究结果
- 最终 study-specific SAP 决策
- 绕过治理约束的任意 shell 结构编辑

## 7. 应遵循的工作流

### 7.1 收集输入

收集用户材料，并识别其来源类型与用途。

### 7.2 归一语境

抽取或推断最小治理语境，例如：

- 研究分期
- 治疗领域
- endpoint 类型
- analysis population
- 是否需要 figures
- 是否需要 listings
- 是否请求正式生成

### 7.3 映射治理语言

把自由文本映射到受控语言：

- section scope
- shell family
- applicability
- phase / domain 提示

在映射 table layout 时，必须同时考虑临床/统计报告实践、编程实现性和信息直观度：

- 不要把治疗组机械固定在列；group 可作为列、行或 grouped subheader。
- 单一 by-visit endpoint 以 Visit 为最高行层级；多参数安全性表可使用 Parameter > Visit > Statistic。
- observed value、model-based treatment estimate 与 between-group comparison 必须保持可独立识别。
- 不得因为模板可容纳某项统计量就硬塞 LS mean、CI、p-value 或其他指标；由 protocol/SAP 决定。
- 通用 AE 不按 cycle 汇总；DLT、输注、PK/PD 等明确按计划周期/时点采集的场景需单独判断。
- AE maximum CTCAE grade 在 SOC/PT 下作为行分组，不作为结果列。
- 同一表的缩写、统计定义和 MedDRA/CTCAE version footnote 应受控且不重复。

完整规则见 `docs/table_layout_contract.md`。

### 7.4 Recommend

给出推荐结果，至少区分：

- 基础包
- 可选扩展
- 排除项
- 歧义点
- 风险提示

### 7.5 Generate

如果用户请求生成：

- 复用 recommend 阶段解释出的语境
- 生成正式业务输出
- 返回生成摘要与验证摘要

如果 Skill 包内已经附带格式规则、字段说明或模板片段，应优先使用包内资产，
以保持结果稳定。

如果 Skill 包内提供 `recommend -> generate` 脚本，该脚本应尽量保留：

- `request_summary`
- `interpreted_context`
- `ingestion_state`
- `extraction_state`
- `normalization_state`
- `ambiguity_state`
- `recommendation_state`
- `generation_results`
- `validation_results`

如已从上游项目提炼出稳定细节 contract，建议把这些细节集中到独立 helper 模块，
并让脚本通过结构化字段声明本次实际引用了哪些细节规则，而不是仅在实现中隐式使用。

如目标是跨项目复用，脚本还应能报告包内自包含资产是否完整可用。

当前最小验证实现应至少覆盖一类正式输出的内容级一致性检查。
在现阶段，优先检查 `xlsx` 主表中的：

- TFL ID
- Display Label
- Type
- Section
- Shell Family
- Study Phase Scope
- Coverage Summary
- Population
- Applicability
- 行数

这些字段应与推荐后的受控 catalog 保持一致。

同时，`docx` 主模板的最小内容级一致性检查应至少覆盖：

- Heading 4 中的 `Display Label + Title` 顺序与推荐后的受控 catalog 一致
- shell heading 数量与推荐后的 shell 数量一致
- 推荐涉及的顶层 section heading 已出现在文档中
- header block 中的 `Display Label`、`Title`、`Analysis Set` 顺序与推荐后的受控 catalog 一致
- 每个 shell 的 `Protocol:` 与 `Sponsor:` 行均已出现

同时，`sop` 的最小内容级一致性检查应至少覆盖：

- 标准 SOP 标题与模板文案存在
- 受控 scope 文案包含 `14.1 / 14.2 / 14.3 / 14.4 / 16.2`
- 明确说明三类正式输出之间的对齐要求
- 明确包含 generation、catalog validation 与 regression tests 的 quality gate 文案
- 头表中 `SOP No. / Version / Effective Date / Department / Classification` 标签存在
- `Classification` 的值为 `CONFIDENTIAL`
- 关键 Heading 结构与 Appendix heading 存在

如果脚本运行了上述细节检查，`validation_results` 中还应返回：

- `declared_references`

该字段至少应说明：

- 当前引用的 helper 模块
- 当前引用的细节键集合
- 该组引用的用途说明

如果脚本具备跨项目自包含运行准备，还建议返回：

- `package_bundle`
- `runtime_summary`

该字段至少应说明：

- 自包含资产是否齐备
- contract registry 是否存在
- catalog 子集是否存在
- 最小运行依赖清单是否存在
- 示例请求文件是否存在

`runtime_summary` 至少应说明：

- 当前运行模式
- 当前使用的 catalog 来源
- 当前使用的 registry 来源
- 当前使用的 wrapper 层位置

### 7.6 Report

输出应至少包含：

- 解释后的语境
- 推荐摘要
- 生成摘要
- 风险提示
- 优化建议

不要只给文件路径，不给解释。

## 8. 建议输出结构

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

`recommend` 可以不真正生成文件，但字段结构应尽量稳定。

## 9. 输出物区分

始终区分以下四类东西：

- `TFLs-Shell SKILL`：当前可复用 Skill 包
- `上游项目资产`：可能被提炼为本 Skill 一部分的项目经验、脚本、模板或文档
- `Governance Docs`：范围、规则、设计、测试契约等规范文档
- `Formal Outputs`：DOCX / XLSX / SOP 等正式业务输出

混淆这些类别属于工作流错误。

## 10. 约束规则

- 不要把某个项目实现直接当成 SKILL 本体
- 不要把整个上游项目原样搬进 Skill 包
- 不要让生成结果反过来定义治理规则
- 不要在未更新文档与测试说明的情况下修改推荐或生成行为
- 不要把 `output/` 中业务文件当成规范真值源

## 11. 依赖口径

如果 Skill 包内已经附带补充资产，应优先使用 Skill 包内资产。

如果 Skill 包未附带足够资产，则以当前环境下可见的显式约束、稳定接口与
用户确认规则为准。

## 12. 包内补充文件

本 Skill 包的补充说明见：

- `PACKAGE_GUIDE.md`
- `DEVELOPMENT_RULES.md`

当前包内已提供直接生成脚本：

- `scripts/generate_project_aligned_outputs.py`
- `scripts/recommend_then_generate.py`

当前包内已提供最小自包含资产：

- `package_assets/contract_registry.json`
- `package_assets/catalog_subset.json`
- `package_assets/output_manifest.json`
- `package_assets/minimal_runtime_requirements.txt`
- `examples/recommend_then_generate_non_oncology.json`

当前包内已提供 Product 对齐契约文档：

- `docs/product_alignment_contract.md`
- `docs/catalog_schema_contract.md`
- `docs/docx_shell_contract.md`
- `docs/xlsx_workbook_contract.md`
- `docs/sop_contract.md`
- `docs/table_layout_contract.md`

当前包内还应提供最小运行层：

- `runtime/catalog_loader.py`
- `runtime/registry_loader.py`
- `runtime/wrappers/docx_wrapper.py`
- `runtime/wrappers/xlsx_wrapper.py`
- `runtime/wrappers/sop_wrapper.py`
- `scripts/export_catalog_subset.py`
- `scripts/export_product_contracts.py`
- `scripts/validate_outputs.py`

其中：

- runtime loader 用于优先读取 Skill 包自身携带的受控资产
- runtime wrapper 用于统一生成接口，逐步替代入口脚本直接依赖底层生成器
- 导出脚本用于把 Product 的当前 catalog 子集与输出契约受控同步到 Skill 包
- 输出验证脚本用于检查 DOCX / XLSX / SOP 是否符合包内 Product 对齐契约
- 仓库级 `scripts/install_skill_to_agents.py` 用于把本 Skill 安装到 agent skills 目录
- 仓库级 `scripts/validate_skill_baseline.py` 用于在维护时校验 Product 导出的 manifest / registry 与本 Skill 包内资产未漂移

这些脚本的目标只有一个：生成与当前项目保持一致命名和结构的正式输出。

其中 `scripts/recommend_then_generate.py` 应优先作为 schema-first 入口：

- 从材料输入开始
- 保留中间状态
- 生成正式输出
- 返回最小验证摘要

## 13. 示例

### 示例 1：只做推荐

用户说：

> 为一个 Phase II 非肿瘤研究推荐受控 TFL shell 包，主要终点是
> time-to-first exacerbation。

期望行为：

- 识别出 Phase II
- 识别出 Non-Oncology
- 推荐 `14.2` 与 `14.3` 为核心范围
- 大概率保留 `16.2`
- 输出必要风险提示

### 示例 2：推荐后生成

用户说：

> 为一个以 PFS 和安全性审阅为重点的 oncology 研究生成受控输出包。

期望行为：

- 推断出 oncology 生存分析导向语境
- 推荐相应基础包
- 在 Skill 自身规则范围内生成受控输出
- 返回 artifact 与 validation 摘要

## 14. 维护目标

本 Skill 应长期保持：

- 可复用
- 应用层导向
- 面向大众
- 边界清晰
- 输出可靠

## 15. 禁止模式（防守卫）

以下行为属于对本 Skill 的**根本性误解**，一旦出现应视为错误：

### 15.1 禁止把 SKILL 当成独立软件包

SKILL 是一套 AI 调用的规范文档，不是需要"独立运行"的程序包。

**错误做法：**
- 在 SKILL 包内新增 `runtime/naming.py`、`runtime/version_loader.py` 等独立工具模块，
  试图让 SKILL 脱离 Product 自行生成文件名、版本号
- 在 SKILL 包内新增 `runtime_mode()`、`has_full_repo_backend()` 等"运行模式检测"，
  试图让 SKILL 在没有 Product 的环境下"降级运行"
- 为 SKILL 包添加独立的 `setup.py`、`pyproject.toml` 或独立依赖声明

**正确做法：**
- SKILL 脚本依赖 `tflshell` Product 提供版本、命名、catalog、生成器等能力
- 脚本通过 `_bootstrap_repo_imports()` 引用 Product，这是**设计如此**，不是待解决的耦合
- `runtime/` 层的 loader 和 wrapper 是 Product 能力的**薄封装**，不是独立替代品

### 15.2 禁止把脚本当成 SKILL 本体

- SKILL.md 是主入口，脚本是辅助工具
- 不要因为脚本能独立运行就把脚本设计成"不需要 AI 也能用"的 CLI
- 不要让脚本承担 SKILL.md 中定义的推理、判断、语境归一职责

### 15.3 禁止让 catalog_subset.json 承载完整表结构

- `catalog_subset.json` 是给 AI 做推荐时参考的**元数据摘要**
- 不要把 `shell_rows`、`placeholder_columns`、`footnotes` 等完整结构信息塞入 subset
- 完整结构信息属于 Product `definitions.py`，不应在 SKILL 包内重复维护

### 15.4 禁止以"跨项目复用"为由复制 Product 代码

- SKILL 跨项目复用 = 复制 `Skill/tfls-shell/` 文件夹 + AI 读取 SKILL.md
- 不是 = 复制 Product 代码让 SKILL 在新环境独立生成文件
- 如果新环境需要生成文件，正确做法是 `pip install tflshell`，而非复制 Product 代码到 SKILL 包内

### 15.5 每轮审阅检查清单

每次修改 SKILL 包时，必须确认：

- [ ] 没有新增独立于 Product 的工具模块（命名、版本、模式检测等）
- [ ] `runtime/` 层仍然是 Product 的薄封装，不是独立替代品
- [ ] `catalog_subset.json` 仍然是元数据摘要，未膨胀为全量结构数据
- [ ] 新增脚本遵循 `_bootstrap_repo_imports()` + 引用 Product 的模式
- [ ] SKILL.md 仍然是纯规范文档，不含实现细节
