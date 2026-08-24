---
phase_index: 2
status: in-progress
created: 2026-08-14
updated: 2026-08-14
priority: 1
estimated_rounds: 4-6
depends_on: ["P1-tfl-shell-layout-refactor.md"]
tags: [tfl, table-layout, clinical-review, skill, release]
syncs_to:
  - PROJECT_SPEC.md
  - PROJECT_GUIDE.md
  - TEST_GUIDE.md
  - CODE_STYLE.md
---

# 全表 Layout 审查、Skill 同步与远端发布

## 目标

按用户确认的临床统计报告标准逐一复核所有 Table，修复重复脚注、非常规 AE 表、by-visit 层级和重复表；生成逐表审查矩阵与正式输出，并把稳定规则同步到 `Skill/tfls-shell/` 后提交推送远端。

## 背景

- Product 当前包含 140 张 Table，已有布局 contract，但仍存在 AE cycle 汇总、重复 SOC/PT 表、非常规 relationship × grade 布局和 dictionary/version 脚注重复。
- 用户确认：AE 常规不按 cycle 汇总；单一 by-visit 终点以 Visit 为最高行层级；全频 PT 表不应与 SOC/PT 表重复；relationship 与 grade 不采用非常规二维布局。
- 上一轮冻结 Skill 同步，本轮用户已明确授权同步 Skill 与远端。

## 范围

- **包含**：140 张 Table 逐表审查矩阵；Catalog 删除/合并/重构；脚注去重；by-visit 和 AE layout；DOCX/XLSX/SOP 重生成；Skill contract/manifest/catalog 同步；测试、提交、推送与 PR。
- **不包含**：真实研究结果；替代 study-specific SAP 决策；为表格硬塞新指标；把 Product 全量代码复制进 Skill；未经依据新增固定 visit/cycle/threshold。

## 主文档影响

- `PROJECT_SPEC.md`：Table 分类布局、AE 时间分析和脚注唯一性规则。
- `PROJECT_GUIDE.md`：审查矩阵及 Product→Skill 同步闭环。
- `TEST_GUIDE.md`：逐表审查、脚注去重、删除项和 Skill 对齐验证。
- `CODE_STYLE.md`：受控脚注组合与布局审计实现约定。

## Phase 总览

| Phase | 目标 | 依赖 | 状态 |
|---|---|---|---|
| P1 | 审查 140 张 Table，形成判定矩阵并修复重复/非常规 AE 表 | - | completed |
| P2 | 按表族修正 by-visit 层级及其他高优先级 layout | P1 | completed |
| P3 | 生成审查工作簿与正式输出，完成 DOCX/PDF/XLSX 验收 | P2 | completed |
| P4 | 同步 Skill 契约与资产，全套回归并发布远端 | P3 | completed |

## P1：全表审查与 AE/脚注治理

### 输入条件

- 用户已确认分类审核标准。
- Catalog validation 当前无结构 warning。

### 产出

- 每张 Table 的分类、层级、判定、问题和处置记录。
- dictionary/version/abbreviation 脚注不重复。
- 移除或合并 AE by-cycle、重复 full-frequency PT、非常规 relationship × grade 表。

### 完成标准

- [x] 140 张初始 Table 均有审查记录，不以自动规则代替临床判断。
- [x] 同表 MedDRA/CTCAE 说明只保留一个合并后的 coding/grading footnote。
- [x] AE by-cycle 表不再作为通用 catalog 项。
- [x] 重复的全频 PT 和非常规 relationship × grade 表从 catalog 移除或合并。
- [x] Catalog validation 与针对性测试通过。

### 边界

- 本 Phase 不重生成正式输出。
- 不修改 Skill；待 Product Gate 通过后统一同步。

## P2：表族 Layout 重构

### 输入条件

- P1 删除/合并清单稳定。

### 产出

- 单一 by-visit endpoint 使用 `Visit → Statistic/Model Result`。
- 多参数 safety/PK 表按实际目的选择 Parameter 或 Visit 最高层级，并在审查记录中说明。
- 治疗组、comparison、Overall 和 expansion 列按信息语义独立。

### 完成标准

- [x] 所有标题含 by visit/timepoint 的 Table 均有明确最高层级判定。
- [x] 单一连续性 endpoint 不把 Visit 放在治疗组或 statistic 之下。
- [x] 不新增无 protocol/SAP 依据的统计量。
- [x] 同构表族测试通过。

### 边界

- 不强制多参数 lab/vital 表使用单一通用层级。
- 不改变 Figure renderer。

## P3：输出与视觉验收

### 输入条件

- Product Catalog 和布局回归通过。

### 产出

- 全表审查 XLSX。
- 更新后的 DOCX/XLSX/SOP 实际输出。
- 代表性 Word→PDF 视觉检查和完整 OOXML/工作簿结构检查。

### 完成标准

- [x] 审查工作簿行数与审查基线一致，筛选、冻结窗格、列宽和换行可用。
- [x] DOCX 标题、页眉、表头、脚注和书签结构通过。
- [x] 代表性 AE、by-visit、lab、PK 表 PDF 视觉检查通过。
- [x] Product 范围回归通过。

### 边界

- 不覆盖被 Word 占用的文件；必要时使用新 REVIEW 文件名。

## P4：Skill 同步与发布

### 输入条件

- P3 Product 输出验收通过。

### 产出

- Skill 规则、contract、catalog subset、manifest 和验证 helper 与 Product 一致。
- Skill 包与全仓测试通过。
- 受控 commit、push 和 draft PR。

### 完成标准

- [x] Skill 明确包含本轮分类审查、AE、by-visit、脚注唯一性和 Listing 规则。
- [x] `catalog_subset.json` 保持元数据摘要，不承载完整表结构。
- [x] Skill baseline/package/output validation 通过。
- [x] 全套 pytest 通过或仅有已解释且不在范围内的外部阻断。
- [x] 仅相关文件被 staged，提交推送成功并创建 draft PR。

### 边界

- 不新增独立于 Product 的 Skill 工具模块。
- 不把 Skill 改造成独立软件包。

## 执行中发现

- 初始 140 张 Table 中保留 131 张，退役 9 张 AE 表；最终 catalog 为 197 TFL（131 Table / 28 Figure / 38 Listing）。
- 旧 layout 归一化在显式 `Statistic`/`Visit`/`Timepoint` 列前直接 padding，可能把结果 placeholder 静默移入语义列；已在 padding 前展开 `Visit — Statistic` 复合标签。
- 完整 Word→PDF 为 207 页，无空白或低文本页；代表性 T14.3.1.3 和 T14.4.5 视觉检查通过。
- 审核交付物为 `output/TFL_Table_Layout_Audit_R3.xlsx`（140 条）及对应 2 页总结报告。
- 全套分组回归为 93 passed / 2 contract 同步失败；更新旧断言并重生成默认输出后，2 项定向回归通过。

## 关键决策记录

- 2026-08-14：用户批准按表格分类逐表审查，并在 Product 验收后同步 Skill 和远端。
- 2026-08-14：AE cycle、full-frequency PT 和 relationship × grade 不作为通用独立表保留。
