# 项目指南

## 1. 文档目的

本文档用于说明 `TFLshell` 项目的当前定位、边界、交付物分类与推荐阅读顺序。

本项目的核心目标不是生成最终统计结果，而是维护一个受控的 TFL shell 主库、
参考生成能力与相关产品化资产。

## 2. 项目定位

`TFLshell` 当前应被理解为 `TFLs-Shell Product` 的维护仓库。

它主要承担以下职责：

- 维护受控 TFL shell 主库
- 维护 DOCX / XLSX / SOP 生成器
- 维护格式契约与输出基线
- 维护推荐与生成相关实现资产
- 作为 `TFLs-Shell SKILL` 的主要参考 source

## 3. 四层边界

请始终区分以下四层：

### 3.1 `TFLs-Shell SKILL`

位于 `.trae/skills/` 下的可复用应用层 Skill 包。

它负责定义：

- 何时调用
- 接收什么输入
- 如何理解与推荐
- 如何生成与说明
- 输出契约与风险提示

### 3.2 `TFLs-Shell Product`

本仓库中的产品化实现层。

它负责维护：

- shell catalog
- 推荐逻辑
- 生成器
- 格式契约
- 测试基线
- 项目规范与设计材料

### 3.3 `Governance Docs`

项目中的规范、设计稿、测试契约、开发约束等文档。

### 3.4 `Formal Outputs`

由 Product 生成的正式业务输出，例如：

- `TFL_Shell_Template_v<version>.docx`
- `TFL_TOC_v<version>.xlsx`
- `TFL_Shell_SOP_v<version>.docx`

## 4. 当前交付物

本仓库当前维护的主要交付物包括：

- CSR 面向的 DOCX shell 模板
- XLSX TFL catalog 与使用工作簿
- SOP DOCX
- `TFLs-Shell SKILL` 的参考文档与支撑资产
- 设计文档、测试契约与规范文档

## 5. 目录说明

- `src/tflshell/`：Product 代码实现，包括模型、catalog、生成器与推荐支持逻辑
- `.trae/skills/`：可复用 Skill 包
- `scripts/`：Skill 包维护脚本与轻量校验脚本
- `docs/superpowers/specs/`：设计与治理收口文档
- `docs/superpowers/`：Product 层交付说明与历史材料
- `tests/`：回归与契约测试
- `output/`：正式业务输出，不是规范真值源

## 6. 当前治理范围

当前受控范围包括：

- `14.1` Demographics and Baseline Characteristics
- `14.2` Efficacy
- `14.3` Safety
- `14.4` Special Assessments
- `16.2` Patient Data Listings

当前不包括：

- `16.1`
- 最终统计结果
- 最终 study-specific SAP 决策
- 绕过治理约束的任意模板编辑

## 7. Product 与 SKILL 的关系

当前正式口径如下：

- `TFLs-Shell SKILL` 是可复用的应用层工作流包
- `TFLs-Shell Product` 是仓库内的产品化实现与维护主 source

Product 不等于 SKILL，但它应作为 SKILL 的高保真参考基线，使调用 SKILL 后
产出的东西尽可能接近本项目中维护的正式生成物。

## 8. 推荐阅读顺序

建议按以下顺序阅读：

1. `PROJECT_GUIDE.md`
2. `PROJECT_SPEC.md`
3. `CODE_STYLE.md`
4. `test_guide.md`
5. `.trae/skills/tfls-shell/`
6. `docs/superpowers/specs/`
7. `src/tflshell/`

## 9. 工作原则

- `shell-first`：shell 是结构模板，不是最终结果包
- `governance-first`：规则优先于局部实现便利
- `product-as-source`：Product 是格式与行为的主要维护源
- `skill-for-reuse`：SKILL 是复用入口，不是仓库实现别名
- `cross-output-alignment`：DOCX、XLSX、SOP 与文档口径保持一致

## 10. 已知问题与方向

当前仍需持续收敛的点包括：

- 非肿瘤领域覆盖仍需继续扩展
- phase/domain 选择逻辑仍需继续结构化
- Product 与 SKILL 的引用关系仍可进一步规范
- 输出格式回归与文档术语一致性仍可进一步自动化

当前已完成的近期收敛包括：

- `TFLs-Shell SKILL` 的 `recommend_then_generate` 已返回 schema-first 的 `validation_results`
- `xlsx` 主表最小内容级一致性检查已覆盖 TFL ID、Display Label、Section、Shell Family、Applicability 与行数
- `xlsx` 主表现已进一步覆盖 Type、Study Phase Scope、Coverage Summary、Population 等治理字段
- `docx` 主模板现已进一步覆盖 header block 的 `Display Label / Title / Analysis Set` 顺序以及 `Protocol / Sponsor` 行存在性
- `sop` 现已进一步覆盖头表关键标签、`CONFIDENTIAL` 分类值、关键 Heading 结构与 Appendix heading
- 上述细节 contract 已开始从入口脚本中抽离到独立 helper，并可通过结构化字段声明本次实际引用内容
- `TFLs-Shell SKILL` 包内已开始补齐最小自包含资产，包括 contract registry、catalog 子集、最小依赖清单与样例请求
- `TFLs-Shell SKILL` 包内已新增最小 runtime 层，包括 catalog loader、registry loader、三类输出 wrapper 与受控导出脚本
- 上述检查已同步进入测试契约，作为当前 Skill 输出对齐的最小基线

## 11. 风险提示

- `技术风险`：如果 SKILL 与 Product 边界再次混淆，输出格式将逐步漂移
- `维护风险`：如果项目文档与实现不同步，后续会形成双重真值
- `项目风险`：如果没有明确 Product 是主 source，SKILL 的可靠性会下降

## 12. 优化建议

### 12.1 立即可做

- 继续统一术语为 `TFLs-Shell SKILL / TFLs-Shell Product`
- 保持文档、实现、测试同步更新
- 以 Product 输出为 SKILL 高保真参考基线
- 使用 `scripts/validate_skill_package.py` 对正式 Skill 包做基础结构校验
- 继续把 `validation_results` 向更细粒度的跨输出 contract 扩展，而不只停留在最小内容级校验
- 优先抽离可复用的 contract helper，避免 Skill 入口脚本持续堆积格式感知逻辑
- 优先把稳定细节做成可声明引用的 helper/注册表，而不是散落在单个脚本中
- 优先把跨项目复用必需的最小资产封进 Skill 包，而不是默认依赖当前仓库环境补齐
- 优先让入口脚本走包内 runtime 层，再逐步减少对 `src/tflshell` 的直接暴露

### 12.2 中长期

- 为 SKILL 增加样例、术语映射与引用资产
- 为 Product 增加更稳定的格式回归与输出基线
- 逐步建立 SKILL 与 Product 的更明确接口关系
