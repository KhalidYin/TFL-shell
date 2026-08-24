---
phase_index: 3
status: done
created: 2026-08-14
updated: 2026-08-24
priority: 1
estimated_rounds: 1-2
depends_on:
  - P2-table-layout-audit-skill-sync.md
tags:
  - tfl
  - table-layout
  - efficacy
  - safety
syncs_to:
  - PROJECT_SPEC.md
  - PROJECT_GUIDE.md
  - TEST_GUIDE.md
  - CODE_STYLE.md
---

# 连续终点与汇总表层级布局重构

## 目标

把数据集字段式的 Table shell 改为面向临床统计审阅的层级布局，同时保持 long-form 编程键可实现。

## 背景

- 当前状态：部分 14.3/14.4 表把 `Visit`、`Timepoint`、`Statistic` 直接打印为并列列，视觉上接近 listing；部分 14.2 连续终点把治疗组横向扩展，不利于多组、多访视和多指标审阅。
- 约束：最小修改现有声明式 layout contract；不新增统计指标；不改变真实 study-specific SAP 决策边界。
- 方案来源：用户对实际 R3 输出的复核与轻量讨论。
- 头脑风暴记录：2026-08-14 用户确认治疗组按行、Baseline 独立列、组内差异和组间差异作为子表头；参考组比较值不另起行。

## 涉及范围

- **包含**：14.2 连续终点代表性/同类 shell；14.3/14.4 重复 `Statistic` 的汇总 shell；布局契约、测试、Skill 同步资产和 R4 实际输出。
- **不包含**：分类终点、shift table、subject listing 的机械转置；新增模型、指标或 study-specific 统计规则。

## 主文档影响

- `PROJECT_SPEC.md`：更新 Shell 构造规则中的层级汇总及组内/组间差异规则。
- `PROJECT_GUIDE.md`：更新近期 layout contract 能力说明。
- `TEST_GUIDE.md`：增加代表性层级布局、参考组行内比较和重复 Statistic 列回归。
- `CODE_STYLE.md`：更新声明式层级行及组内/组间列组约定。

---

## Phase 总览

| Phase | 目标 | 预估轮次 | 依赖 | 状态 |
|-------|------|----------|------|------|
| P1 | 重构 14.2、14.3、14.4 catalog 布局与测试 | R004 | - | done |
| P2 | 同步契约、生成 R4 并完成视觉/回归验证 | R004 | P1 | done |

---

## P1: Catalog 与布局契约重构

### 输入条件

- R3 实际输出和用户确认的布局规则可用。
- Catalog、声明式多级表头和行占位机制测试通过。

### 产出

- 14.2 连续终点使用治疗组行及组内/组间差异列组。
- 14.3/14.4 汇总表使用 Parameter/Visit/Statistic 缩进行层级。
- 代表性 contract 测试覆盖新规则。

### 完成标准

- [x] Baseline 为独立列，组内差异与组间差异为可识别子表头。
- [x] 参考组行不产生冗余独立比较行；非参考组行承载相对参考组的估计值。
- [x] 代表性 14.3/14.4 汇总表不再以独立 `Statistic` 列重复展示层级。
- [x] 相关单元测试通过。

### 边界（本 Phase 明确不做）

- 不把所有两组、单访视表机械转换为同一格式。
- 不改变分类、时间事件、shift 或 listing 的业务语义。

### 涉及文件

| 文件 | 操作 | 预计行数 |
|------|------|----------|
| `src/tflshell/data/sections/section_14_2.py` | 修改 | ~120 |
| `src/tflshell/data/sections/section_14_3.py` | 修改 | ~160 |
| `src/tflshell/data/sections/section_14_4.py` | 修改 | ~80 |
| `tests/unit/test_table_layout_contract.py` | 修改 | ~100 |
| `tests/unit/test_clinical_layout_practice.py` | 修改 | ~80 |

### 关键决策

- 编程层继续保留 long-form keys，输出层用缩进和多级表头表达层级，避免把数据集列直接当出版表列。
- 通用多治疗组连续终点以共同参考组映射比较值；只有不可映射的非参考组比较才允许单独比较行。

---

## P2: 契约同步与实际输出验证

### 输入条件

- P1 完成且相关单元测试通过。

### 产出

- Product 主文档和 Skill table-layout contract 同步。
- R4 DOCX/XLSX/SOP 与 PDF 抽查证据。
- 全量回归、Skill 基线和输出验证结果。

### 完成标准

- [x] 主文档、Skill contract 和导出资产与 Product 行为一致。
- [x] Catalog validate、pytest、Skill/package/output 验证通过。
- [x] R4 代表页视觉抽查确认层级、列宽和比较位置合理。
- [x] 未引入无关 output 或工作树变更。

### 边界（本 Phase 明确不做）

- 不替用户合并 PR。
- 不修改或删除既有 `tmp/` 和 `__pycache__` 用户/环境文件。

### 涉及文件

| 文件 | 操作 | 预计行数 |
|------|------|----------|
| `docs/main/*.md` | 修改 | ~40 |
| `docs/main/memory/tfl-layout-review-standards.md` | 修改 | ~15 |
| `Skill/tfls-shell/` | 同步 | 按导出差异 |
| `output/*_REVIEW_R4.*` | 生成 | 二进制输出 |

### 关键决策

- 先以代表性高风险表验证，再执行全目录回归和实际 PDF 视觉检查。

---

## 执行中发现

| ID | 描述 | 发现于 | 类型 | 处理 |
|----|------|--------|------|------|

## 关键决策记录

| 日期 | 决策 | 选项 | 选择 | 理由 |
|------|------|------|------|------|
| 2026-08-14 | 多治疗组比较展示 | 独立比较行 / 映射到治疗组行 | 映射到非参考组行 | 减少冗余并保持一行对应一个治疗组；共同参考组语义直观 |
| 2026-08-14 | Baseline 与差异展示 | 混在行标签 / 独立列组 | Baseline 独立列，差异为子表头 | 便于同一治疗组内横向读取基线、组内变化和组间比较 |

## 同步记录

| 日期 | 已同步到 | 说明 |
|------|----------|------|
| 2026-08-24 | PROJECT_SPEC / PROJECT_GUIDE / TEST_GUIDE / CODE_STYLE / memory / Skill | 同步治疗组行内比较、组内/组间子表头、14.3/14.4 层级汇总与验证契约 |
