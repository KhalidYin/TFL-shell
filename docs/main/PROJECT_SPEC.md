# 项目规范

## 1. 文档目的

本文档定义 `TFLshell` 项目的受控规范，是 `TFLs-Shell Product` 的核心规则来源。

它主要回答：

- 当前治理范围是什么
- shell 编号与标签如何保持一致
- applicability 如何受控
- 各类 shell family 的覆盖预期是什么
- 元数据需要满足哪些最低要求

## 2. 受控范围

### 2.1 当前纳入范围

- `14.1` Demographics and Baseline Characteristics
- `14.2` Efficacy
- `14.3` Safety
- `14.4` Special Assessments
- `16.2` Patient Data Listings

### 2.2 当前不纳入范围

- 最终统计结果
- study-specific SAP 最终裁决
- 受试者级伪造数据
- 仅围绕 owner、deadline、status 的项目追踪流程

## 3. 输出类型

本项目治理三类输出：

- `Table`
- `Figure`
- `Listing`

其中：

- `Table` 与 `Listing` 保持 shell-only、result-free
- `Figure` 可以保留模拟示意，但不得暗示最终分析结果

## 4. 编号与标签规则

### 4.1 内部 ID

内部 ID 采用：

`[Type][Section].[Sequence]`

示例：

- `T14.2.11`
- `F14.2.4`
- `L16.2.3`

### 4.2 对外标签

对外展示标签应去掉类型字母后的数字部分，例如：

- `Table 14.2.11`
- `Figure 14.2.4`
- `Listing 16.2.3`

### 4.3 同步规则

以下字段必须保持一致：

- internal ID
- display label
- section
- title
- type
- applicability
- shell family
- study phase scope
- coverage summary

修改其中任一字段时，应同步检查 catalog、生成器与文档。

## 5. Applicability 规则

每个 shell 必须带一个受控 applicability 标签：

- `General`
- `Oncology only`
- `Non-Oncology only`

### 5.1 含义

- `General`：默认可用于 oncology 与 non-oncology，除非 protocol 或 SAP 另有限制
- `Oncology only`：依赖 oncology 特定终点或审阅习惯，不应默认外推
- `Non-Oncology only`：依赖 non-oncology 特定实践，不应自动泛化

### 5.2 当前状态

当前 Product 在 oncology 覆盖上仍然更强，但已加入若干明确的
`Non-Oncology only` 家族，例如：

- responder
- event-rate
- time-to-event
- respiratory exacerbation
- cardiovascular event
- autoimmune flare

## 6. Shell 构造规则

### 6.1 Tables

- 保留表达展示语义所需的结构行
- 结果相关单元格保持通用 placeholder
- 允许使用与目标展示相符的 placeholder 样式
- 使用受控的 `Group 1 / Group 2` 结构
- 如需表示更多组，允许额外 ellipsis expansion 列，但不要与分析列合并
- 仅在临床上合理时保留 `Overall`
- 样本量表头保持通用，例如 `N=xx`
- 若主表加 forest plot 更合适，则不保留冗余 subgroup-only 表
- 如存在受控 listing，应使用具体 source-listing 引用
- 14.1 中通用人口学表不得混入疾病分期、ECOG、组织学等肿瘤特异 baseline disease 内容
- 14.1 中 baseline disease shell 如使用肿瘤分期、组织学或 ECOG 审阅语境，应显式标记 `Oncology only`

### 6.2 Listings

- 保留 listing 结构与关键变量标签
- 不引入虚构受试者记录
- 在需要时保留排序与展示规则

### 6.3 Figures

- 允许模拟示意图
- 不得暗示最终分析输出
- 标题、图体、注释与分页应尽量保持成组
- figure shell 应通过 `src/tflshell/figures/registry.py` 注册 renderer 与 mock data factory
- DOCX 生成默认应把可生成 figure 嵌入为 PNG；只有显式关闭或生成失败时才回退到文本占位

## 7. 元数据要求

每个受控 shell 至少应保留以下元数据：

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

## 8. 覆盖矩阵

| 研究语境 | `14.1` | `14.2` | `14.3` | `14.4` | `16.2` |
| --- | --- | --- | --- | --- | --- |
| Phase I Oncology | Core | Conditional | Core | Core | Core |
| Phase I Non-Oncology | Core | Conditional | Core | Core | Core |
| Phase II Oncology | Core | Core | Core | Conditional | Core |
| Phase II Non-Oncology | Core | Core | Core | Conditional | Core |
| Phase III Oncology | Core | Core | Core | Conditional | Core |
| Phase III Non-Oncology | Core | Core | Core | Conditional | Core |

说明：

- `Core`：通常应纳入
- `Conditional`：依赖方案、终点或机制
- `Gap`：治理上已识别但当前未充分覆盖

## 9. Study-specific Tailoring 规则

主库是受控基线，允许 study-specific tailoring，但必须遵循：

- 保持编号控制，除非已正式批准调整
- 仅保留当前研究真正适用的 shell 变体
- 用 protocol / SAP 语言定制标题、population 与 footnote
- 可以替换 placeholder，但不得破坏治理边界
- 不得静默删除 traceability 内容

## 10. Product 与 SKILL 的规范关系

在当前口径下：

- `TFLs-Shell Product` 是本规范的主要落地层
- `TFLs-Shell SKILL` 应参考本规范来提高推荐与生成的一致性

SKILL 不直接等于本规范，但若要生成高保真结果，应尽量对齐本规范与 Product。

## 11. 风险提示

- `技术风险`：元数据失控会削弱自动化可靠性
- `维护风险`：不受控复用会造成领域漂移
- `项目风险`：若 coverage 声明超出真实实现，会误导评审与审计

## 12. 优化建议

### 12.1 立即可做

- 保持非肿瘤家族显式化
- 保持规范、SOP 与 workbook 同步
- 保持 cross-output 规则可检查

### 12.2 中长期

- 建立更细粒度的 shell family registry
- 继续扩充 Phase I 设计家族
- 增强 machine-checkable coverage 规则

### 12.3 工具链

- 自动校验 coverage matrix 与 catalog 元数据
- 校验 DOCX、XLSX、SOP 与规范文案一致性
- 在 CI 中运行 `generate`、`validate` 与 `pytest`

## 13. 规范变更同步规则

规范文档是本项目的治理来源。任何规范变更必须同步到实现层面。

### 13.1 规范文档定义

以下文件视为规范文档，修改其中任何一条受控规则都视为规范变更：

- `docs/main/PROJECT_SPEC.md` — 编号规则、applicability、shell 构造规则、元数据要求、覆盖矩阵
- `docs/main/PROJECT_GUIDE.md` — 治理范围、工作原则、边界定义
- `docs/main/CODE_STYLE.md` — 命名规则、文档同步规则、编辑标准
- `docs/main/TEST_GUIDE.md` — 测试契约、最小回归集合

### 13.2 规范变更的必须动作

| 规范变更类型 | 必须同步更新 |
|-------------|-------------|
| 范围边界变化（新增/删除 section） | `data/sections/` 的 catalog builder、`output_manifest.json`、SKILL.md §6、contract 文档 |
| 编号或标签规则变化 | `data/sections/` 中所有相关 TFLItem、naming 工具、测试、contract 文档 |
| applicability 措辞变化 | `definitions.py` 中相关 shell 的 applicability 标签、catalog 验证测试、contract 文档 |
| metadata 字段变化 | `models/tfl_item.py`、`data/sections/`、catalog_subset 导出脚本、XLSX workbook contract |
| shell family 解释变化 | `domain_registry.json`、`data/sections/` 中 shell_family 标签、测试 fixture、contract 文档 |
| 测试契约变化 | 对应测试文件 + CI 配置 |

### 13.3 同步质量闸

规范变更提交前必须通过：

- [ ] `pytest` 全量通过
- [ ] `tflshell validate` 通过
- [ ] `tflshell generate -t all` 成功生成
- [ ] `scripts/validate_skill_package.py` 通过
- [ ] `scripts/validate_skill_baseline.py` 通过
- [ ] `scripts/install_skill_to_agents.py --dry-run` 通过
- [ ] `Skill/tfls-shell/scripts/validate_outputs.py` 对生成物通过
- [ ] `git diff -- output/` 确认 output 变更符合预期
- [ ] 规范文档中修改的条款已反映在代码变更中（人工 review）
