# TFL Skill CLI `recommend + generate` 收口设计

> 历史说明：本文件记录的是一次把 Skill 误收口为“仓库级 CLI workflow”的
> 设计过程。它可作为历史偏差样例保留，但不再代表当前 Skill 正式交付方向。
> 当前正式方向是 `.trae/skills/` 下的可复用应用层 Skill 包。

日期：2026-04-28  
主题：基于现有 `TFLshell` 仓库能力完成 `CLI` 优先的 Skill 闭环设计  
状态：Draft v1，已完成本轮设计确认，待写实现计划

## 1. 文档目的

本文档用于把“先做完 Skill”的本轮目标收敛为一个可实施、可测试、
可继承的设计方案。本文档仅覆盖：

- `CLI` 优先的 Skill 交付入口
- `recommend + generate` 两段工作流闭环
- 与现有 `recommend` 原型、catalog、generator 的复用边界
- 结构化返回、测试契约、文档同步要求

本文档不覆盖：

- 完整 MCP server 实现
- `review`、`compare`、`extend` 等额外模式
- 任意自由编辑 shell 结构的能力

## 2. 本轮目标

本轮 Skill 的完成标准定义为：

- 用户可以通过统一的 `CLI` 入口运行 Skill
- Skill 至少支持 `recommend` 与 `generate` 两种模式
- `recommend` 能输出可解释的结构化推荐结果
- `generate` 能在推荐或推断基础上调用现有生成器产出正式文件
- 两种模式都能返回统一风格的摘要、风险提示和优化建议

本轮不要求：

- 落地真正的 `MCP` tool 或 server
- 一次性完成全部 `task_mode`
- 对底层生成器做大规模重构

## 3. 设计结论

本轮采用“在现有 `CLI` 基础上增量闭环”的方案，而不是先做内部大重构
或直接推进 `MCP`。

结论如下：

- 新增统一命令入口：`tflshell skill`
- 首轮只支持 `--mode recommend` 与 `--mode generate`
- 保留现有 `tflshell recommend` 与 `tflshell generate` 作为兼容入口
- Skill 只做编排，不复制 catalog 或 generator 逻辑
- `recommend` 与 `generate` 共用前半段输入理解与治理映射流程

该方案的核心原则是：优先交付一个可用、可解释、与现有代码兼容的
Skill 闭环，而不是把本轮工作扩成“先重构全部架构”。

## 4. 入口设计

### 4.1 新入口

建议新增如下命令：

```bash
tflshell skill --mode recommend ...
tflshell skill --mode generate ...
```

### 4.2 参数方向

Skill 入口应优先复用现有参数风格，避免引入第二套不兼容命名。
首轮建议支持：

- `--mode recommend|generate`
- `--text`，可重复传入
- `--input-file`，可重复传入
- `--section`
- `--area`
- `--phase`
- `--no-figures`
- `--no-listings`
- `--json`
- `--output-dir`
- `--type` 或等价的期望输出参数
- `--sponsor`
- `--protocol`
- `--presentation-profile`

其中：

- `recommend` 模式不需要实际生成文件
- `generate` 模式需要支持调用现有 DOCX / XLSX / SOP 生成器

### 4.3 兼容性

为了降低迁移风险：

- 现有 `recommend` 子命令继续保留
- 现有 `generate` 子命令继续保留
- 新的 `skill` 入口作为统一编排层逐步成为推荐使用方式

本轮不做破坏式替换。

## 5. 内部职责边界

### 5.1 Skill 层职责

Skill 层负责：

- 收集输入源
- 统一输入读取与规范化
- 复用推荐逻辑提取研究语境
- 把研究语境转换为治理过滤条件
- 决定是否进入生成阶段
- 汇总推荐结果、生成结果、风险、建议
- 以用户摘要或 JSON 形式输出

### 5.2 底层复用边界

Skill 不应重写以下能力，而应直接复用：

- `build_catalog()`：当前受控 catalog 真值入口
- `TFLCatalog`：查询、汇总、校验接口
- `DocxShellGenerator`
- `XlsxTocGenerator`
- `DocxSopGenerator`

### 5.3 不建议做的事

本轮明确不做以下实现方式：

- 在 Skill 内复制一套独立 catalog
- 在 Skill 内重写文件渲染逻辑
- 用单个大函数把解析、推荐、生成全部混在一起
- 为将来 `MCP` 提前暴露低层 Word XML 或内部 helper

## 6. 模式设计

### 6.1 `recommend`

`recommend` 模式负责：

- 接收输入材料
- 识别研究阶段、治疗领域、终点与分析集线索
- 形成治理字段映射
- 输出推荐 sections、shell families、shell IDs、可选扩展
- 返回风险提示和优化建议

该模式不生成文件，但仍应保留结构化状态。

### 6.2 `generate`

`generate` 模式负责：

- 复用 `recommend` 前半段流程完成输入理解
- 在推荐结果或用户约束基础上形成生成过滤条件
- 调用现有 generator 生成一个或多个正式输出
- 汇总产物路径、文件名、过滤条件和版本信息
- 返回风险提示和优化建议

`generate` 的核心要求是“在推荐基础上编排生成”，而不是绕过推荐链路
直接拼接参数。

## 7. 状态模型

本轮不需要一次性完全实现文档中全部理想 schema，但至少应让
`recommend` 与 `generate` 共用以下稳定状态层：

- `request_summary`
- `interpreted_context`
- `ingestion_state`
- `extraction_state`
- `normalization_state`
- `recommendation_state`
- `generation_results`
- `validation_results`
- `risk_notes`
- `optimization_suggestions`

如当前实现尚未完整覆盖，也应保证命名和边界向这一结构收敛，
而不是继续分散增长。

### 7.1 `request_summary`

用于描述本轮任务的外层意图：

- 模式
- 输入源数量
- 用户显式请求的 sections
- area / phase hint
- 期望输出类型

### 7.2 `interpreted_context`

用于返回 Skill 对研究语境的理解：

- study phase
- therapeutic area
- primary endpoint signals
- analysis populations
- include_figures
- include_listings

### 7.3 `recommendation_state`

用于返回：

- 基础包 sections
- 推荐 shell families
- 推荐 shell IDs
- 可选扩展
- 治理 warnings

### 7.4 `generation_results`

仅在 `generate` 模式下填充。至少应包括：

- 是否实际生成
- 生成的产物类别
- 文件路径
- 文件名
- 使用的过滤条件
- 关键统计摘要

### 7.5 `validation_results`

`recommend` 与 `generate` 都应返回结构化校验结果。

首轮最小要求：

- 接入 `TFLCatalog.validate()`
- 返回是否执行
- 返回是否通过
- 返回 warning 数量
- 返回 warning 列表

该字段的目标是先建立统一结果边界，而不是在首轮就覆盖全部未来校验面。

## 8. 数据流设计

本轮 Skill 的推荐数据流如下：

1. 收集 `--text` 与 `--input-file`
2. 构造成统一 source 列表
3. 读取与规范化内容
4. 抽取研究语义
5. 映射治理字段
6. 查询 catalog 并形成推荐结果
7. 输出摘要或 JSON

`generate` 在此基础上继续：

8. 将推荐结果转换为生成过滤条件
9. 调用现有 generator
10. 汇总产物信息
11. 输出统一结果

该设计保证：

- `generate` 不跳过推荐链路
- 同一套输入理解逻辑可被复用
- 后续若抽出 `MCP`，更容易下沉原子能力

## 9. 输出契约

### 9.1 默认摘要输出

终端默认应输出面向用户的可读摘要，至少包括：

- 当前识别到的研究语境
- 推荐的 sections 与 shell families
- 若为 `generate`，则列出已生成的文件
- 风险提示
- 优化建议

### 9.2 JSON 输出

当用户指定 `--json` 时，Skill 应输出结构化 JSON。

首轮 JSON 契约要求如下：

- `recommend` 与 `generate` 顶层结构保持一致
- `generate` 只是额外填充 `generation_results`
- `validation_results` 在两种模式下都存在
- 不允许仅返回文件路径而缺少解释性字段

这一步的目标不是一次性冻结最终外部 API，而是为后续 `MCP` 迁移
建立稳定雏形。

## 10. 文件与模块设计

建议采用最小增量结构：

- 新增 `src/tflshell/skill.py` 或等价模块，负责 Skill 编排
- 保持 `src/tflshell/recommend.py` 继续承载推荐逻辑
- 在 `src/tflshell/main.py` 中增加 `skill` 子命令

### 10.1 `skill.py` 建议职责

- 解析 Skill 模式参数
- 调用推荐层
- 将推荐结果转换为生成计划
- 调用已有 generator
- 整理统一输出对象

### 10.2 `recommend.py` 调整方向

- 保持现有推荐逻辑主体
- 对返回结构做轻量统一
- 避免把生成逻辑直接塞进该文件

### 10.3 `main.py` 调整方向

- 新增 `skill` 子命令
- 复用已有参数模式
- 保持旧入口兼容

## 11. 测试设计

本轮测试只做高价值回归，不做低价值快照。

### 11.1 单元测试

建议至少覆盖：

- `skill --mode recommend` 的结构化返回字段
- `skill --mode generate` 的生成结果结构
- 推荐结果向生成过滤条件的传递
- 稀疏输入下的默认治理行为

### 11.2 CLI 测试

建议至少覆盖：

- `tflshell skill --mode recommend --json`
- `tflshell skill --mode generate --json`
- 与现有 `recommend` / `generate` 入口的关键行为一致性

### 11.3 文档与测试契约同步

如果本轮实现落地：

- `test_guide.md` 需补充 Skill CLI 测试关注点
- 如返回字段发生变化，需同步文档说明

## 12. 与 MCP 的关系

本轮 Skill 完成后，不等于直接完成 `MCP`。

本轮明确分层如下：

- Skill：面向用户语义的工作流编排层
- MCP：后续面向外部 agent 的原子能力接口层

完成本轮 Skill 后，后续更适合下沉为 `MCP` 的能力包括：

- `build_catalog`
- `filter_catalog`
- `summarize_catalog`
- `validate_catalog`
- `generate_outputs`

仍更适合保留在 Skill 上层的能力包括：

- 从非结构化材料抽取研究语义
- 生成面向用户的扩展建议
- 在不确定场景下解释默认假设

## 13. 实施顺序建议

建议按以下顺序实现：

1. 统一 Skill 顶层 CLI 入口
2. 复用当前 `recommend` 结构形成统一输出对象
3. 为 `generate` 模式接通现有 generator
4. 补充 JSON 结果中的 `generation_results`
5. 增加有针对性的单元与 CLI 测试
6. 同步项目文档与测试指南

本轮不建议先进行大规模架构重构。

## 14. 完成标准

本轮可视为“Skill 已做完”的最低标准：

- `tflshell skill` 可运行
- 支持 `--mode recommend`
- 支持 `--mode generate`
- `generate` 能产出至少一个正式文件并返回结果摘要
- `--json` 输出具备统一顶层结构
- 已补充对应测试
- 已同步更新相关文档

## 15. 风险提示

- 技术风险：如果把 `validation`、`MCP` 和大规模内部重构一起纳入本轮，
  Skill 范围会再次失控。
- 维护风险：如果 `recommend` 与 `generate` 继续维持不同返回口径，后续
  很难收敛为稳定 contract。
- 项目风险：如果直接替换旧 CLI 入口而不保留兼容层，可能影响现有脚本
  和使用习惯。

## 16. 优化建议

### 16.1 立即可做

- 按本文档先完成 `CLI` 统一入口
- 让 `recommend` 与 `generate` 共用输入理解链路
- 先实现统一 JSON 顶层结构
- 实现完成后同步更新 `PROJECT_GUIDE.md`、`PROJECT_SPEC.md`、
  `CODE_STYLE.md`、`test_guide.md`

### 16.2 中长期

- 将状态对象进一步收敛为独立 contract 层
- 让 `validation_results` 以可选阶段接入统一输出模型
- 将推荐与生成过滤条件的映射做得更细粒度、更 item-aware

### 16.3 工具链

- 为 Skill CLI 增加 contract tests
- 在 `pytest` 中守护顶层 JSON 结构稳定性
- 为后续 `Skill -> MCP` 下沉预留共享 schema 校验层
