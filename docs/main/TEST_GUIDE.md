# 测试指南

## 1. 文档目的

本文档定义 `TFLshell` 仓库当前有效的测试契约。

它主要服务于 `TFLs-Shell Product` 的回归保障，并为 `TFLs-Shell SKILL`
提供稳定参考基线。

## 2. 测试原则

- 测试应验证治理行为，而不只是实现细节
- cross-output consistency 是一等要求
- 测试应轻量、聚焦、可本地运行
- 新功能或行为变化应配套新增或更新测试
- `tests/` 是唯一规范测试根目录

## 3. 目录约定

规范测试根目录：

`tests/`

建议结构：

```text
tests/
  unit/
    models/
    utils/
    data/
    generators/
  integration/
    catalog/
    outputs/
    consistency/
  fixtures/
    catalog/
    output_samples/
```

## 4. 最小回归集合

### 4.1 Catalog Integrity

- TFL ID 唯一
- 非 figure shell 保持 placeholder 列
- 非 figure shell 保持 shell rows
- 每个 shell 保留 dataset source 等关键元数据

### 4.2 Scope Control

- 仅出现受控 section
- applicability 标签保持在受控集合内

### 4.3 Output Structure

- DOCX shell 输出包含 TOC field
- SOP 输出包含 TOC field
- workbook sheet 与字段符合治理模型
- 生成输出保持受控标题与标签
- DOCX figure shell 在默认生成时应嵌入模拟 PNG image，而不只是文本占位

### 4.4 Cross-Output Consistency

- ID 与 display label 在 DOCX、XLSX、SOP 中一致
- section naming 一致
- applicability wording 一致
- workbook 字段与项目规范一致

## 5. 何时加测试

出现以下变化时，应新增或更新测试：

- 新 shell family
- 范围边界变化
- applicability 或编号规则变化
- workbook 字段变化
- 生成器文案或结构变化
- recommendation 逻辑或输出契约变化
- `TFLs-Shell SKILL` 的触发条件、示例或输出契约变化
- Product 的格式契约或输出基线变化
- catalog section builder 拆分或迁移
- figure renderer registry 或 mock data factory 变化

## 6. 不要过度测试什么

避免低价值测试，例如：

- 机械重复每条硬编码字符串
- 脆弱的逐行文档快照
- 会因无关文案变化而大面积失败的测试

## 7. 工具建议

- `pytest`
- fixture-based unit tests
- DOCX / XLSX 结构读取工具
- `pre-commit`
- CI 中执行 `generate`、`validate` 与 `pytest`

## 8. Skill 与 Product 的测试口径

当前测试重点仍在 `TFLs-Shell Product`。

如果后续需要测试 `TFLs-Shell SKILL`，应重点关注：

- 触发条件
- 输入解释
- 中间状态 schema
- 输出契约
- validation 摘要
- 与 Product 的对齐结果

当前最小内容级对齐检查应至少覆盖：

- `xlsx` 主表中的 TFL ID 与 catalog 一致
- `xlsx` 主表中的 Display Label 与 catalog 一致
- `xlsx` 主表中的 Type 与 catalog 一致
- `xlsx` 主表中的 Section 与 catalog 一致
- `xlsx` 主表中的 Shell Family 与 catalog 一致
- `xlsx` 主表中的 Study Phase Scope 与 catalog 一致
- `xlsx` 主表中的 Coverage Summary 与 catalog 一致
- `xlsx` 主表中的 Population 与 catalog 一致
- `xlsx` 主表中的 Applicability 与 catalog 一致
- `xlsx` 主表行数与推荐后的 shell 数量一致
- `docx` 中 Heading 4 的 `Display Label + Title` 顺序与 catalog 一致
- `docx` 中 shell heading 数量与推荐后的 shell 数量一致
- `docx` 中推荐涉及的顶层 section heading 已出现
- `docx` 中 header block 的 `Display Label / Title / Analysis Set` 顺序与 catalog 一致
- `docx` 中每个 shell 的 `Protocol:` 与 `Sponsor:` 行已出现
- `sop` 中标准标题与受控 scope 文案存在
- `sop` 中三类正式输出的对齐要求文案存在
- `sop` 中 generation、catalog validation、regression tests 的 quality gate 文案存在
- `sop` 中头表关键标签与 `Classification = CONFIDENTIAL` 存在
- `sop` 中关键 Heading 结构与 Appendix heading 存在
- `validation_results.declared_references` 已声明当前脚本实际引用的细节 helper 与字段集合
- 顶层 `package_bundle` 已声明当前 Skill 包是否具备 contract registry、catalog 子集、最小运行依赖与样例请求
- 顶层 `runtime_summary` 已声明当前是否优先走 Skill 包内 runtime，以及 catalog / registry / wrapper 来源
- `package_assets/output_manifest.json` 已声明当前 Product 版本下 DOCX / XLSX / SOP 的可观察输出结构
- `xlsx_workbook` contract 已覆盖 workbook sheet 名、catalog sheet 字段、section sheet 行数、Field_Definitions、Usage_Guide 与 Change_Log
- `docx_layout` contract 已覆盖主模板页面设置、Introduction 文案、Heading 层级、table/listing body table 数量与受控组别表头
- `scripts/validate_outputs.py` 可用于验证生成物是否符合包内 Product 对齐契约

不要把某个仓库内临时 CLI 原型误当成 Skill 官方测试面。

当前已增加基础校验脚本：

- `scripts/validate_skill_package.py`
- `scripts/validate_skill_baseline.py`
- `scripts/install_skill_to_agents.py`

其测试重点应包括：

- Skill 包目录结构
- `SKILL.md` frontmatter
- 必需配套文件
- 最小自包含资产
- runtime loader / wrapper 与导出脚本
- `output_manifest.json`、`contract_registry.json` 与 Product 当前导出一致
- 生成/验证脚本清单完整
- 明显的错误绑定表述
- 安装脚本能将 `Skill/tfls-shell/` 安装到目标 `skills` 目录，且目标已存在时需要显式 `--force`

## 9. 风险提示

- `技术风险`：无测试时，文档与输出行为会静默漂移
- `维护风险`：shell 扩张但无验证，会提高未来维护成本
- `项目风险`：覆盖声明可能超出真实实现

## 10. 优化建议

### 10.1 立即可做

- 保持测试与 `docs/main/PROJECT_SPEC.md` 同步
- 优先验证治理不变量
- 保持 Product 输出结构的稳定回归

### 10.2 中长期

- 增加 oncology / non-oncology 代表性 fixture
- 增加 phase-aware metadata checks

### 10.3 工具链

- 在 CI 中保留 `pytest`
- 增加关键输出格式回归
- 增加 SKILL 包结构与术语一致性检查
