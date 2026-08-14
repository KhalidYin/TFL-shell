---
phase_index: 1
status: done
created: 2026-08-12
updated: 2026-08-12
priority: 1
estimated_rounds: 5-8
depends_on: []
tags: [tfl, layout, catalog, docx, figures, validation]
syncs_to:
  - PROJECT_SPEC.md
  - PROJECT_GUIDE.md
  - TEST_GUIDE.md
  - CODE_STYLE.md
---

# TFL Shell 临床实践与布局重构

> Lifecycle rule: this file's directory and `status` must match.
> `plans/backlog/` = `planning`; `plans/ongoing/` = `in-progress`; `plans/complete/` = `done`; `plans/deferred/` = `deferred`.

## 目标

以最小兼容性扩展修复当前 TFL shell 的临床统计展示语义、编程可实现布局、figure 语义、类型与来源映射，并重新生成可审阅的 Product 实际输出。

## 背景

- 当前状态：Product 可生成 206 个 shell，但数据模型只支持单层表头和简单行缩进；大量表被统一为 `Group 1 / Group 2 / ... / Overall`，部分 comparison 放入治疗组列，部分 figure 的实际图型与标题不一致，且存在 table/listing 与 source listing 误配。
- 约束：保持现有简单 shell 兼容；只修改 Product、治理文档、测试和实际输出；本轮不更新 `Skill/` 下衍生 skill；不通过新增指标掩盖布局问题；避免一次重写全部 206 个 shell。
- 方案来源：2026-08-12 实际输出复核报告与用户确认。
- 头脑风暴记录：比较了三条路线。A 仅逐表修内容，改动小但无法解决多层表头能力缺口；B 最小扩展 layout contract 并重构代表性 family，兼容性与收益最佳；C 全量重写 206 个 shell，风险和验证成本过高。用户批准采用 B。

## 涉及范围

- **包含**：可选多层表头与 layout profile；comparison block、treatment-row、shift/group-specific 等代表性布局；代表性 14.1/14.2/14.3/14.4/16.2 shell；错误 figure renderer 或安全回退；table/listing 分类与显式 source listing；DOCX 分页/续页；XLSX 最小结构审阅字段；治理与渲染测试；正式 DOCX/XLSX/SOP 重生成。
- **不包含**：最终 study-specific SAP 决策；真实结果；新增大量 endpoint/指标；全面重写全部 shell；衍生 `Skill/` 包同步；改变受控 CSR section 范围；为临时方便复制 Product 代码。

## 主文档影响

完成后需要更新：

- `PROJECT_SPEC.md`：§6 Shell 构造规则、§7 最小布局元数据、§13 同步质量闸。
- `PROJECT_GUIDE.md`：§5 目录职责、§9 工作原则、§10 已知问题与完成收敛。
- `TEST_GUIDE.md`：§4 输出结构、语义映射与 PDF/DOCX 渲染回归。
- `CODE_STYLE.md`：§8 结构性改动中的 layout contract、显式 source listing 与 figure profile 维护规则。

---

## Phase 总览

| Phase | 目标 | 预估轮次 | 依赖 | 状态 |
|-------|------|----------|------|------|
| P1 | 建立最小兼容 layout contract 与 DOCX 渲染能力 | R003-R004 | - | done |
| P2 | 重构各 section 的代表性 table/listing shell | R005-R006 | P1 | done |
| P3 | 修复 figure 语义与 mock-data profile | R007 | P1 | done |
| P4 | 收敛 applicability、family、类型与 source listing | R008 | P2, P3 | done |
| P5 | 分页、XLSX 审阅视图、正式输出与全量回归 | R009-R010 | P4 | done |

---

## P1: 最小兼容 layout contract

### 输入条件

- 复核报告中确认单层 `placeholder_columns` 无法表达独立 comparison block 和多层表头。
- 现有简单 shell 必须继续按当前接口生成。

### 产出

- 在 `TFLItem` 中增加可选、最小化的布局声明，保留 `placeholder_columns` 兼容路径。
- DOCX table renderer 支持跨列表头、重复表头及必要的列宽/对齐策略。
- 至少实现 `standard-treatment`、`model-comparison`、`treatment-row`、`shift-matrix`、`group-specific`、`listing-wide` 所需表达能力；不要求每类都新增独立生成器。

### 完成标准

- [x] 现有未声明复杂 layout 的 shell 输出结构不回归。
- [x] 一个 by-visit/model fixture 能把治疗组 estimate 和 `Group 1 vs Group 2` comparison 显示为独立列组。
- [x] renderer 能重复跨页表头，并对第一列、统计列、数值列使用声明式对齐。
- [x] layout schema 有模型级和 DOCX 结构级测试。

### 边界（本 Phase 明确不做）

- 不批量改 catalog 内容。
- 不修改 figure renderer。
- 不引入新的文档生成库。

### 涉及文件

| 文件 | 操作 | 预计行数 |
|------|------|----------|
| `src/tflshell/models/tfl_item.py` | 修改 | +60~100 |
| `src/tflshell/docx_utils/three_line_table.py` | 修改 | +100~180 |
| `src/tflshell/presentation.py` | 修改 | +20~50 |
| `tests/unit/test_presentation_profiles.py` | 修改 | +30~60 |
| `tests/unit/test_table_layout_contract.py` | 新建 | ~120 |

### 关键决策

- 布局 schema：选择“可选增强字段 + 旧字段兼容”，不选择替换所有 `placeholder_columns`，理由是减少 206 条 catalog 的一次性迁移风险。
- 表头实现：选择 declarative spans，不允许在 shell 定义中写 OOXML。

---

## P2: 代表性 table/listing 重构

### 输入条件

- P1 layout contract 与兼容测试通过。
- 代表性 shell 清单已由复核报告确认。

### 产出

- 14.2：重构 primary continuous endpoint、by-visit continuous endpoint、responder/event-rate 等 model/comparison 展示。
- 14.3：修正 AE grade、lab/vital by-visit、shift 表；将逐受试者“table”改为汇总或迁移为 listing 语义。
- 14.4：修正 PK/PD/PRO 的 group、dose/period/sequence 和 comparison 布局。
- 14.1/16.2：修正 study-specific general shell、exposure category 与 listing 排序/宽表配置。

### 完成标准

- [x] `T14.2.1` 和一个 by-visit 连续终点的 comparison 不再落入任一治疗组列。
- [x] `T14.2.32/33` 具有清晰的 comparison block 或明确标记为 descriptive-only。
- [x] subject-level Hy's Law/death/lab detail 不再以汇总 Table 伪装。
- [x] `T14.4.15/16` 正确表达 treatment/period comparison，且不强制 Group 1/2/Overall。
- [x] 至少一张宽 listing 具有专用排序说明和可读布局。
- [x] 不为满足形式而新增 OR、HR、p-value 等未由分析方法支持的指标。

### 边界（本 Phase 明确不做）

- 不全面逐条重写 206 个 shell；只修代表性 family，并机械迁移同构项。
- 不替 study-specific SAP 决定具体模型、visit 或 multiplicity。

### 涉及文件

| 文件 | 操作 | 预计行数 |
|------|------|----------|
| `src/tflshell/data/sections/section_14_1.py` | 修改 | +20~60 |
| `src/tflshell/data/sections/section_14_2.py` | 修改 | +100~220 |
| `src/tflshell/data/sections/section_14_3.py` | 修改 | +100~220 |
| `src/tflshell/data/sections/section_14_4.py` | 修改 | +60~140 |
| `src/tflshell/data/sections/section_16_2.py` | 修改 | +30~80 |
| `tests/unit/test_clinical_layout_practice.py` | 新建 | ~180 |

### 关键决策

- Comparison 层级：独立 `Treatment Comparison` 列组，默认不挂在 Group 2 下。
- by-visit 连续终点：允许 treatment-column 或 treatment-row，两者按列宽和信息直观度选择，不强求全库统一。

---

## P3: Figure 语义修复

### 输入条件

- P1 已提供稳定 figure/page 组合能力或保持现有接口可用。
- 已知错误包括 CDF、eDISH、QTcF-concentration、heatmap、PK profile 等。

### 产出

- 用专用 renderer/profile 修复高优先级错误图；无法可靠实现的图回退为明确的结构 placeholder。
- mock data 与轴、图例、参考线、caption 保持语义一致。
- 模拟图体明确标示 illustrative/mock，不让精确 N/HR/p-value 冒充结果。

### 完成标准

- [x] CDF 不再使用 longitudinal line-by-visit 图。
- [x] eDISH 是 ALT/TBL xULN 散点并包含正确参考线/区域表达。
- [x] QTcF-concentration 与 heatmap 不再复用错误 renderer。
- [x] PK concentration-time 使用采样时间与浓度轴，不使用 Baseline/Week visit。
- [x] figure profile 测试验证图型、必需字段及安全回退，不只验证 PNG 可生成。

### 边界（本 Phase 明确不做）

- 不追求出版级最终图形美化。
- 不生成真实研究结果或暗示真实统计显著性。

### 涉及文件

| 文件 | 操作 | 预计行数 |
|------|------|----------|
| `src/tflshell/figures/registry.py` | 修改 | +80~160 |
| `src/tflshell/figures/cdf.py` | 新建 | ~100 |
| `src/tflshell/figures/edish.py` | 新建 | ~110 |
| `src/tflshell/figures/heatmap.py` | 新建 | ~100 |
| `src/tflshell/figures/concentration_qtc.py` | 新建 | ~100 |
| `src/tflshell/figures/longitudinal.py` | 修改 | +20~60 |
| `tests/unit/test_figure_shell_rendering.py` | 修改 | +100~180 |

### 关键决策

- 对无法在本轮准确表达的 figure：选择显式 placeholder，不用语义近似图冒充正式 shell。

---

## P4: Catalog 治理与来源映射

### 输入条件

- P2/P3 已确定实际 shell 类型、布局和 figure profile。

### 产出

- 显式修正 source listing；减少标题关键词误配。
- 收敛 applicability、coverage summary、study phase scope 和 shell family。
- 修复 result-free 违规的固定结果值。

### 完成标准

- [x] `T14.2.1/2/4/5/6/7` 不再引用 protocol deviation listing。
- [x] Hy's Law、metabolic、PK、lab 等已知误配全部修正。
- [x] Food effect/crossover 不再被无依据限制为 Non-Oncology only。
- [x] cytokine、Holter、DLT/MTD、irAE 等条件性表不再自动声明为通用 Core。
- [x] 非 listing shell 的 source listing 要么显式合理，要么明确为空并带 study-specific 说明。
- [x] shell body 不包含硬编码结果值 `0` 或模拟结论文本（ECOG 等级分类值除外）。

### 边界（本 Phase 明确不做）

- 不删除受控 ID，除非类型纠正无法保持 ID 语义；优先弃用/重映射。
- 不更改当前 CSR section 总范围。

### 涉及文件

| 文件 | 操作 | 预计行数 |
|------|------|----------|
| `src/tflshell/data/definitions.py` | 修改 | -80~+80 |
| `src/tflshell/data/sections/*.py` | 修改 | +40~120 |
| `src/tflshell/data/domain_registry.json` | 修改 | +10~30 |
| `tests/unit/test_catalog_integrity.py` | 修改 | +50~100 |
| `tests/unit/test_section_14_1_practice.py` | 修改 | +20~50 |

### 关键决策

- Source listing：以 shell 定义中的显式声明为准，关键词映射只允许作为无歧义 fallback。

---

## P5: 输出、分页与回归

### 输入条件

- P1-P4 的结构和治理测试通过。

### 产出

- DOCX 续页重复表头和 TFL 上下文，figure/caption/note/footnotes 尽量成组，减少 footnote-only/blank pages。
- XLSX 增加最小 layout review 字段或独立审阅视图，不引入项目管理字段。
- SOP 修正与实际对齐方式和布局策略的矛盾。
- 更新 Product 主文档并重新生成三类正式输出。

### 完成标准

- [x] 代表性长表跨页时重复列头并可识别 TFL；不出现仅 footer 的空白页。
- [x] 高优先级 figure 不再产生 footnote-only continuation page；无法避免时续页包含明确上下文。
- [x] XLSX 可识别至少 layout profile、comparison position、sorting/denominator notes 中实际需要的最小集合。
- [x] SOP 不再声称所有表都应使用 Group 1/2/ellipsis 或所有单元格左对齐。
- [x] `tflshell validate`、Product 相关回归通过；全套仅有 3 个冻结 Skill 衍生契约测试按任务边界待同步。
- [x] Word/PDF 渲染抽查覆盖五个 section 和各 layout family。
- [x] `docs/main/` 与 `USAGE.md` 术语/规则一致。
- [x] 不修改 `Skill/` 下衍生 skill 文件。

### 边界（本 Phase 明确不做）

- 不以压缩字体到不可读来实现强制一页一 shell。
- 不将临时 PDF 审阅文件作为正式交付写入 output。

### 涉及文件

| 文件 | 操作 | 预计行数 |
|------|------|----------|
| `src/tflshell/generators/docx_shell.py` | 修改 | +50~120 |
| `src/tflshell/generators/xlsx_toc.py` | 修改 | +30~80 |
| `src/tflshell/data/sop_content.py` | 修改 | +10~30 |
| `tests/integration/test_cross_output_consistency.py` | 修改 | +30~80 |
| `tests/integration/test_workbook_structure.py` | 修改 | +30~80 |
| `tests/integration/test_docx_rendering.py` | 新建 | ~120 |
| `docs/main/*.md`、`USAGE.md` | 修改 | +50~120 |
| `output/TFL_*` | 重新生成 | - |

### 关键决策

- 分页验收：以可读续页和上下文完整为准，不把“一页一 shell”设为绝对约束。
- XLSX：增加最小审阅语义，不扩展为 workflow tracker。

---

## 执行中发现

| ID | 描述 | 发现于 | 类型 | 处理 |
|----|------|--------|------|------|
| F001 | 固定正式 DOCX 被 Word 锁定，无法覆盖 | P5 | external | 输出 `_REVIEW` 候选文件；不强制关闭用户 Word，审核后可替换 |
| F002 | Skill manifest/contract 仍期待旧 XLSX 字段与适用性计数 | P5 | boundary | 按用户边界不修改 Skill；记录为审核后独立同步任务 |
| F003 | DOCX 最末分页符产生空白尾页 | P5 | defect | 保存前仅移除最后一个 TFL separator；PDF 验证 224 页、空白页 0 |

## 关键决策记录

| 日期 | 决策 | 选项 | 选择 | 理由 |
|------|------|------|------|------|
| 2026-08-12 | 重构路线 | A 逐表修补 / B 最小 schema 扩展后按 family 重构 / C 全库重写 | B | 解决根因并控制兼容与验证风险 |
| 2026-08-12 | Skill 边界 | 同步 / 暂不同步 | 暂不同步 | 用户明确要求实际输出审核通过后再同步衍生 skill |
| 2026-08-12 | Figure 不完整时的行为 | 近似 renderer / placeholder | placeholder | 避免错误图形误导临床与编程审阅 |
| 2026-08-12 | 正式文件被锁时的交付 | 强制关闭 Word / 覆盖失败 / `_REVIEW` 候选 | `_REVIEW` 候选 | 不干扰用户进程，同时保留可审核实际输出 |

## 同步记录

| 日期 | 已同步到 | 说明 |
|------|----------|------|
| 2026-08-12 | `docs/main/PROJECT_SPEC.md` | 多级表头、comparison、figure 与布局元数据规则 |
| 2026-08-12 | `docs/main/PROJECT_GUIDE.md` | layout contract、source mapping 与当前完成状态 |
| 2026-08-12 | `docs/main/TEST_GUIDE.md` | layout/figure/XLSX/PDF 回归要求 |
| 2026-08-12 | `docs/main/CODE_STYLE.md` | 声明式布局与显式 source listing 维护纪律 |
| 2026-08-12 | `USAGE.md` | XLSX 布局审阅字段说明 |
