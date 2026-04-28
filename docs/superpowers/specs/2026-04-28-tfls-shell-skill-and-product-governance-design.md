# TFLs-Shell SKILL 与 Product 治理收口设计

日期：2026-04-28  
主题：统一 `TFLs-Shell SKILL`、`TFLs-Shell Product`、项目文档与正式输出物的概念边界  
状态：Approved for implementation

## 1. 文档目的

本文档用于解决当前仓库中最关键的一处概念混淆：

- “可复用的应用层 `SKILL`”
- “仓库内的推荐/生成/格式维护实现”

此前两者都曾被称为 “skill”，导致：

- 交付物边界不清
- 文档语义冲突
- 维护方向不稳定
- 用户口径与项目口径不一致

本次收口后，后续一律采用以下术语：

- `TFLs-Shell SKILL`：可复用的应用层 Skill 包
- `TFLs-Shell Product`：仓库内的产品化实现与维护主 source

## 2. 核心结论

### 2.1 `TFLs-Shell SKILL`

`TFLs-Shell SKILL` 是对外可复用的应用层工作流包。

它的职责是：

- 定义何时调用
- 定义接收什么输入
- 定义如何理解 protocol / SAP / 统计需求
- 定义应返回什么推荐、说明、风险与输出指令
- 定义与 `TFLs-Shell Product` 的关系

它至少包含：

- `SKILL.md`

它也可以包含：

- 包说明文档
- 开发规则文档
- 示例
- 术语说明
- 辅助脚本
- 映射资产

因此，`SKILL` 不是“只有一个 `SKILL.md` 文件”，而是“以 `SKILL.md` 为主入口
的可复用包”。

### 2.2 `TFLs-Shell Product`

`TFLs-Shell Product` 是仓库内的产品化实现层。

它的职责是：

- 维护生成器
- 维护格式契约
- 维护示例输出
- 维护推荐与生成逻辑
- 维护测试与项目文档
- 作为 `TFLs-Shell SKILL` 的高保真参考 source

`Product` 不是 `SKILL` 本身，但它是：

- `SKILL` 输出精度的重要支撑层
- `SKILL` 持续演化的维护主 source
- 让 `SKILL` 产物尽量接近正式项目输出的参考基座

### 2.3 二者关系

二者关系应固定为：

- `SKILL` 面向复用和调用
- `Product` 面向维护和高保真实现

建议理解为：

`调用方 -> TFLs-Shell SKILL -> 参考 TFLs-Shell Product -> 生成尽量接近正式项目格式的输出`

## 3. 正式术语替换规则

从本次起，仓库中涉及该主题时，应按以下方式统一命名：

- 原先泛称的“项目集 skill / 项目级 skill / workflow skill”
  - 统一改称：`TFLs-Shell Product`
- 原先泛称的“可复用 Skill / Skill 包 / SKILL”
  - 统一改称：`TFLs-Shell SKILL`

除非明确讨论历史背景，否则不要再单独使用模糊词 `skill` 指代两者之一。

## 4. 四类交付物边界

后续项目中必须始终区分以下四类东西：

### 4.1 `TFLs-Shell SKILL`

位于 `.trae/skills/` 下的可复用应用层 Skill 包。

### 4.2 `TFLs-Shell Product`

位于仓库实现层的代码、文档、测试、生成器、样例产物与设计材料。

### 4.3 `Governance Docs`

描述范围、规则、测试契约、设计决策的治理文档。

### 4.4 `Formal Outputs`

由仓库生成的 DOCX / XLSX / SOP 等正式业务输出物。

## 5. 为什么 Product 必须保留

此前创建的项目级 recommend / generate / 测试 / 设计文档并不是无意义资产。

在新的口径下，它们应被理解为：

- `TFLs-Shell Product` 的组成部分
- `TFLs-Shell SKILL` 的支撑资产
- 用于逼近正式输出格式与行为的参考实现

保留这些资产的原因是：

- `SKILL` 需要高保真的参考基线
- 单靠抽象说明无法稳定逼近项目输出格式
- 生成器、格式契约、测试样例、输出物结构都需要一个长期维护主 source

因此，之前的项目级交付物应被“重新归类”，而不是简单否定。

## 6. 文档治理要求

从本次开始，所有文档遵循以下原则：

- 全部 Markdown 文档统一使用中文
- 所有相关文档都要明确区分 `SKILL` 与 `Product`
- 如需引用历史文件，应显式说明它们当前归属于 `Product` 层
- 不再把仓库实现文件误写成 `SKILL` 本体
- 不再把 `output/` 下业务文件误写成规范真值源

## 7. 对后续开发的约束

后续凡是“制定或开发 Skill”，默认指：

- 先定义 `TFLs-Shell SKILL` 的应用层目的、触发条件、边界与输出契约
- 再决定 `TFLs-Shell Product` 需要提供哪些实现支持

不要再按以下顺序推进：

- 先写仓库实现
- 再把实现反推为 `SKILL` 定义

正确顺序应为：

1. 先定义 `TFLs-Shell SKILL`
2. 再设计 `TFLs-Shell Product` 的支撑能力
3. 最后把输出与测试对齐

## 8. 对当前仓库的直接影响

本次收口后，当前仓库需要完成以下同步：

1. 顶层项目文档改成中文版并使用新术语
2. `.trae/skills/` 下包文档改成中文版并使用 `TFLs-Shell SKILL`
3. `docs/superpowers/` 下设计文档改成中文版并把历史“项目级 skill”
   改写为 `TFLs-Shell Product`
4. `Product` 相关历史材料保留，但口径上重新归类

## 9. 风险提示

- 技术风险：如果 `SKILL` 与 `Product` 边界不清，后续输出格式会逐渐漂移
- 维护风险：如果历史文档仍保留英文和旧术语，仓库会长期存在双重真值
- 项目风险：如果没有把 `Product` 明确为主 source，后续 `SKILL` 的质量会失去稳定参考基线

## 10. 优化建议

### 10.1 立即可做

- 将现有 Markdown 文档全部改为中文版
- 用 `TFLs-Shell SKILL / TFLs-Shell Product` 收口所有相关口径
- 明确保留历史产物，但统一归入 `Product` 层

### 10.2 中长期

- 在 `SKILL` 包中增加示例、术语说明与映射资产
- 在 `Product` 中继续沉淀格式契约、输出样例与测试基线
- 逐步建立 `SKILL` 对 `Product` 的稳定引用关系

### 10.3 工具链

- 增加文档术语一致性检查
- 增加 `.trae/skills/` 结构校验
- 增加对关键输出格式的回归检查
