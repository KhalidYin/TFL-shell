# Table Layout 契约

## 1. Shell-First 规则

Tables 与 listings 只保留 layout structure，不包含最终统计结果或伪造 subject-level records。

第一列保留结构性行标签。非结构性单元格使用 placeholder。

## 2. 先确定信息层级，再确定组别位置

不要把所有表机械套成 `Group 1 / Group 2 / ... / Overall`。先判断表格的医学审阅目的、统计结果类型和可编程结构：

- 治疗组可以在列、行或 grouped subheader 中出现。
- 第一列或左侧结构区承载真正的分类维度、row group、visit、parameter、statistic 等键。
- 模型治疗估计与 treatment comparison 必须通过独立列组或 subheader 识别；治疗组按行时，comparison 值可以放在对应非参考组行，但不能混入 observed 或 within-group 结果列。
- `...` 仅表示可扩展的额外治疗组，不得与 `Overall`、`Total`、HR 或其他 analytic column 合并。

## 3. By-Visit 与连续终点

对于单一 by-visit endpoint：

- `Visit` 为最高行层级。
- 多参数时使用 `Visit > Parameter > Treatment Group`；单参数时省略 Parameter 层级。
- `Baseline` 单独作为列；observed at visit、within-group difference 与 between-group difference 分开显示。
- `Within-Group Difference` 和 `Between-Group Difference` 使用 grouped subheader，具体 estimate、SE、CI、p-value 仅按 SAP 需要选择。
- 参考组行显示 `Reference`；每个非参考治疗组的差值、比值、OR、HR 或其他比较估计放在该治疗组行的 between-group 列中，不为同一比较重复增加独立行。
- 若 contrast 无法映射到单一治疗组，例如非参考组之间的比较或联合 contrast，才使用独立 comparison 行。

对于多参数安全性、PK/PD 综述，使用 `Parameter > Visit/Timepoint > Statistic` 的缩进行层级。编程数据可以继续保留 parameter、visit/timepoint、statistic、treatment、value 等 long-form keys，但最终表格不应把 `Statistic` 机械打印为独立重复列。

不得仅因为表名含 `by visit` 就硬塞 LS mean、p-value 或其他模型指标；是否展示由 protocol/SAP 决定。

## 4. AE 表

- AE 主体按事件日期记录；通用 AE 不按 cycle 汇总。
- DLT 观察期、输注次序、PK/PD sampling cycle 等有明确方案依据的场景不受上述禁令机械限制。
- SOC/PT 是常用医学层级；maximum CTCAE grade 在 SOC/PT 下按行分组，不作为结果列。
- subject incidence、event count、relatedness、seriousness、grade 和 outcome 不得混成不可比较的交叉列。
- AESI、IRR、late-onset、onset window 与 follow-up 表仅在 protocol/SAP 明确定义概念、窗口和 denominator 时保留。
- 不保留与既有 SOC/PT 表重复的所谓 full-frequency listing；patient-level detail 应进入真正的 listing。

## 5. 脚注与统计定义

- 表内出现缩写时，使用一条受控 `Abbreviations:` footnote 解释。
- 只有展示需要定义的统计量时才增加 `Statistical definitions:`，不得向所有表机械灌入模型说明。
- 同一表内 MedDRA/CTCAE dictionary/version 只出现一次；推荐使用一条 coding/grading footnote。
- denominator、time origin、event/censoring、model、missing data 和 multiplicity 仅在相关表中说明，并保持 SAP-controlled。

## 6. Placeholder 样式

允许的 placeholder 示例包括：

- `XX`
- `xx`
- `xx (xx.x)`
- `x.xxx`
- `(xx.x, xx.x)`
- `xx.x (xx.x, xx.x)`

placeholder 样式必须匹配目标展示模式。

## 7. 三线表与对齐规则

生成的 DOCX tables 使用 Product 三线表约定：

- top border
- header separator
- bottom border
- structural first-column headers and body labels left-aligned
- numeric/result headers and result cells centered unless a study standard explicitly requires another alignment
- auto-fit to page width

表头可以使用 grouped subheaders。层级行可使用兼容式 `indent_level` 表达两级以上关系。不得通过静默补空或截断掩盖 `Visit`、`Timepoint`、`Statistic` 与结果列之间的语义错位。

## 8. Listing 规则

Listings 保留变量列、排序说明与关键展示字段，不得包含伪造 subject-level rows。
