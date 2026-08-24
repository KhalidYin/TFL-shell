---
name: TFL layout 复核标准
description: 用户确认的临床统计报告、编程实现与信息直观度联合审查规则
type: feedback
---

TFL shell layout 必须联合判断临床/统计报告实践、编程实现性和信息直观度，不应机械统一 treatment group 或硬塞统计指标。

**Why:** 表格既是医学/统计审阅界面，也是编程规格；只展示模型结果或只追求统一外观都会产生误导。

**How to apply:** 单一 by-visit endpoint 以 Visit 为最高层级。多参数连续终点采用 Visit > Parameter > Treatment Group，Baseline 单独成列，组内差异和组间差异使用独立 subheader；参考组标记 Reference，比较值放在非参考组行。多参数 safety/PK/PD 使用 Parameter > Visit/Timepoint > Statistic 的缩进行层级，不把 long-form Statistic 机械打印成独立重复列。通用 AE 不按 cycle 汇总，maximum grade 在 SOC/PT 下作为行层级。同表缩写、统计定义和 MedDRA/CTCAE version 受控且不重复。
