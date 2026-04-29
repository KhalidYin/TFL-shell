# TFLs-Shell SKILL 收纳 Product 产生细节契约设计

日期：2026-04-29  
主题：将 Product 已稳定实现的输出结构、layout 规则与验证 helper 收纳进 `TFLs-Shell SKILL` 包  
状态：Approved for implementation

## 1. 文档目的

本文档定义本轮路线调整：`TFLs-Shell SKILL` 不再只收纳最小 runtime 子集，而是进一步收纳 Product 已稳定实现的可观察产生细节。

目标是让 Skill 包迁移到其他项目后，仍能按包内契约生成与当前 Product contract-level 一致的 DOCX / XLSX / SOP 输出，并通过包内 helper 检查漂移。

## 2. 设计结论

本轮采用：

`Product-aligned Skill package full capture`

其含义是：

- 收纳 Product 的稳定输出契约
- 收纳 DOCX / XLSX / SOP 的结构约束
- 收纳 table layout 与 placeholder 规则
- 收纳 machine-readable output manifest
- 收纳输出验证 helper

不采用：

- 将整个 `src/tflshell` 原样复制进 Skill 包
- 追求生成文件字节级完全一致
- 暴露 Word XML 等低层实现细节给最终用户

## 3. 新增 Skill 包资产

本轮新增或强化以下包内资产：

- `docs/product_alignment_contract.md`
- `docs/catalog_schema_contract.md`
- `docs/docx_shell_contract.md`
- `docs/xlsx_workbook_contract.md`
- `docs/sop_contract.md`
- `docs/table_layout_contract.md`
- `package_assets/output_manifest.json`
- `scripts/export_product_contracts.py`
- `scripts/validate_outputs.py`

并扩展：

- `package_assets/contract_registry.json`
- `scripts/alignment_contracts.py`
- `scripts/package_bundle.py`
- `scripts/recommend_then_generate.py`

## 4. 输出契约范围

### 4.1 DOCX

DOCX contract 覆盖：

- landscape letter 页面设置
- margin
- Introduction heading 与使用说明
- governed section heading
- TFL shell Heading 4
- shell header block
- table/listing body table 数量
- `Group 1 / Group 2 / ...` 受控组别语义

### 4.2 XLSX

XLSX contract 覆盖：

- 9 个 workbook sheet 的名称与顺序
- 16 个 catalog 主字段
- section sheet 行数与 catalog 一致
- `Field_Definitions`
- `Usage_Guide`
- `Change_Log`

### 4.3 SOP

SOP contract 覆盖：

- 头表标签
- `CONFIDENTIAL` 分类值
- 受控 scope 文案
- cross-output alignment 文案
- quality gate 文案
- required headings
- Appendix A / B

## 5. 防漂移闭环

当 Product 生成细节变化时，维护者应执行：

1. 更新 Product 实现或 catalog
2. 运行 `.trae/skills/tfls-shell/scripts/export_catalog_subset.py`
3. 运行 `.trae/skills/tfls-shell/scripts/export_product_contracts.py`
4. 生成正式输出
5. 运行 `.trae/skills/tfls-shell/scripts/validate_outputs.py`
6. 运行 `pytest`

## 6. 成功标准

本轮完成后应满足：

- Skill 包内存在人类可读 contract 文档
- Skill 包内存在机器可读 output manifest
- contract registry 能声明 `xlsx_workbook` 与 `docx_layout`
- recommend -> generate 的 validation_results 能返回扩展 contract 检查
- 独立 validate_outputs 脚本能验证当前 Product 输出
- 测试覆盖新增导出、manifest 与验证入口

## 7. 风险提示

- 技术风险：如果 contract 文档只描述理想状态而不接 helper，仍会漂移。
- 维护风险：如果 Product 改动后不重新导出 manifest，Skill 包会形成旧真值。
- 项目风险：如果把完整 Product 镜像进 Skill 包，会扩大维护面并削弱包的可复用性。

## 8. 后续建议

- 继续把 source listing 和 shell family registry 结构化。
- 继续减少入口脚本对 `src/tflshell` 的直接暴露。
- 后续如做 MCP，应优先复用本轮形成的 contract docs、manifest 与 validation helper。
