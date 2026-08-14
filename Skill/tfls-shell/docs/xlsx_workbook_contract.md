# XLSX Workbook 契约

## 1. 输出

Product 对齐的 workbook 输出为：

- `TFL_TOC_v<version>.xlsx`

该 workbook 是受控 catalog 视图，不是项目追踪工作簿。

## 2. Sheet 契约

workbook 必须按顺序包含以下 9 个 sheet：

1. `TOC_Master`
2. `14.1_Demographics`
3. `14.2_Efficacy`
4. `14.3_Safety`
5. `14.4_Special`
6. `16.2_Listings`
7. `Field_Definitions`
8. `Usage_Guide`
9. `Change_Log`

## 3. Catalog Sheet 字段

`TOC_Master` 与每个 section sheet 必须使用同一组 20 个 catalog 字段：

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
- `Layout Profile`
- `Comparison Position`
- `Sorting Note`
- `Denominator Note`
- `Footnotes`
- `Remarks`

## 4. 支撑 Sheet

`Field_Definitions` 必须解释 catalog 字段。

`Usage_Guide` 必须包含以下主题说明：

- workbook purpose
- scope
- coverage metadata
- applicability
- placeholder convention
- layout review
- figures
- ordering
- Word TOC
- change management

`Change_Log` 必须包含：

- `Date`
- `Version`
- `Scope`
- `Change Description`
- `Author`

## 5. Layout 与 Placeholder 指引

Usage Guide 必须说明：treatment group 可按分析目的放在列、行或 grouped subheader；结构维度保留在左侧；model estimate 与 treatment comparison 保持独立可识别。`Layout Profile`、`Comparison Position`、`Sorting Note` 与 `Denominator Note` 用于解释可实现的展示结构，不是 workflow 状态字段。
