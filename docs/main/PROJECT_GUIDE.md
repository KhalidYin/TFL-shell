# 项目指南

## 1. 文档目的

本文档用于说明 `TFLshell` 项目的当前定位、边界、交付物分类与推荐阅读顺序。

本项目的核心目标不是生成最终统计结果，而是维护一个受控的 TFL shell 主库、
参考生成能力与相关产品化资产。

## 2. 项目定位

`TFLshell` 当前应被理解为两层资产的维护仓库：

- `TFLs-Shell Product`：落地级 TFL shell 主库与正式输出生成层
- `TFLs-Shell SKILL`：从 Product 流程中抽出的固定、可复现、可安装 Skill 包

它主要承担以下职责：

- 维护受控 TFL shell 主库
- 维护 DOCX / XLSX / SOP 生成器
- 维护格式契约与输出基线
- 维护推荐与生成相关实现资产
- 维护 `Skill/tfls-shell/` 作为可复用 Skill 源目录
- 提供脚本将 Skill 快速安装到 agent 环境

## 3. 四层边界

请始终区分以下四层：

### 3.1 `TFLs-Shell SKILL`

位于 `Skill/tfls-shell/` 下的可复用应用层 Skill 包。

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
- `Skill/tfls-shell/`：正式可复用 Skill 源目录
- `Skill/tfl-governed-shell-workflow/`：历史 workflow skill 归档，不是当前正式交付
- `scripts/`：仓库级维护脚本，包括 Skill 校验、回归基线校验与安装脚本
- `docs/main/`：项目长期规范文档，包含架构、范围、代码风格与测试契约
- `docs/dep/`：开发记录与任务检查点
- `docs/deploy/`：发布与回滚说明
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

- 最终统计结果
- 最终 study-specific SAP 决策
- 绕过治理约束的任意模板编辑

## 7. Product 与 SKILL 的关系

当前正式口径如下：

- `TFLs-Shell SKILL` 是可复用的应用层工作流包
- `TFLs-Shell Product` 是仓库内的产品化实现与维护主 source

Product 不等于 SKILL，但它应作为 SKILL 的高保真参考基线，使调用 SKILL 后
产出的东西尽可能接近本项目中维护的正式生成物。

当前固定流程是：

1. Product 负责维护落地级 TFL shell catalog、DOCX、XLSX 与 SOP 输出。
2. Skill 从 Product 的稳定流程、契约、样例和验证 helper 中抽取可复现工作流。
3. `scripts/install_skill_to_agents.py` 将 `Skill/tfls-shell/` 安装到 agent skills 目录。

## 8. 推荐阅读顺序

建议按以下顺序阅读：

1. `docs/main/PROJECT_GUIDE.md`
2. `docs/main/PROJECT_SPEC.md`
3. `docs/main/CODE_STYLE.md`
4. `docs/main/TEST_GUIDE.md`
5. `Skill/tfls-shell/`
6. `src/tflshell/`

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
- `TFLs-Shell SKILL` 包内已开始收纳 Product 产生细节 contract，包括 DOCX / XLSX / SOP 契约文档、`output_manifest.json`、`export_product_contracts.py` 与 `validate_outputs.py`
- `TFLs-Shell SKILL` 已从历史 `.trae` 目录迁移到仓库根目录 `Skill/`
- 仓库已新增 `scripts/install_skill_to_agents.py`，用于快速安装 `Skill/tfls-shell/`
- 仓库已新增 `scripts/validate_skill_baseline.py`，用于把 `output_manifest.json`、`contract_registry.json` 与生成脚本清单作为回归基线校验
- 长期规范文档已按 personal-assistant 结构迁移到 `docs/main/`，头脑风暴设计草稿不再作为项目规范保留
- 上述检查已同步进入测试契约，作为当前 Skill 输出对齐的最小基线

## 11. 风险提示

- `技术风险`：如果 SKILL 与 Product 边界再次混淆，输出格式将逐步漂移
- `维护风险`：如果项目文档与实现不同步，后续会形成双重真值
- `项目风险`：如果没有明确 Product 是主 source，SKILL 的可靠性会下降

## 12. 边界守卫：SKILL 不是软件包

`TFLs-Shell SKILL` 的定位是 **AI 调用的规范文档 + 参考资产**，不是需要独立运行的程序包。
此边界是整个项目架构的基石，混淆此边界属于根本性错误。

### 12.1 SKILL 是什么

| 层级 | 形式 | 作用 |
|------|------|------|
| `SKILL.md` | Markdown 规范 | AI 读取的工作流和规则说明 |
| `docs/` | 契约文档 | AI 参考的格式规则和输出约束 |
| `package_assets/` | JSON / TXT | AI 做推荐时的元数据参考 |
| `examples/` | JSON 请求 | AI 学习的输入输出样例 |
| `scripts/` | Python 辅助工具 | AI 调用的自动化入口（依赖 Product） |
| `runtime/` | 薄 Python 封装 | 统一 Product 生成器的调用接口 |

### 12.2 绝对禁止

- 在 SKILL 包内创建独立于 Product 的工具模块（如独立的命名、版本、模式检测）
- 以"让 SKILL 脱离仓库也能运行"为目的复制 Product 代码到 SKILL 包内
- 在 `catalog_subset.json` 中膨胀全量 shell 结构数据（`shell_rows` 等属于 Product `definitions.py`）
- 在 SKILL 包内建立独立的依赖管理（`setup.py`、`pyproject.toml`）
- 让 SKILL 脚本尝试在没有 `tflshell` 的环境下"降级运行"

### 12.3 SKILL 对 Product 的依赖是设计如此

脚本中的 `from tflshell import ...` 和 `_bootstrap_repo_imports()` 是**正确的架构模式**，
不是待解决的耦合。SKILL 跨项目复用 = 安装或复制 `Skill/tfls-shell/` + AI 读取规范。
如果新环境需要实际生成文件，正确做法是安装 Product 运行依赖，例如 `pip install tflshell`。

### 12.4 自包含的正确含义

- ✅ 参考资产随包携带：catalog 子集、contract 文档、示例请求
- ✅ AI 拿到 SKILL 包就能做推荐和判断
- ❌ 脚本脱离 Product 仍能独立运行
- ❌ 在 SKILL 包内复制一份 Product 代码

## 13. 优化建议

### 13.1 立即可做

- 继续统一术语为 `TFLs-Shell SKILL / TFLs-Shell Product`
- 保持文档、实现、测试同步更新
- 以 Product 输出为 SKILL 高保真参考基线
- 使用 `scripts/validate_skill_package.py` 对正式 Skill 包做基础结构校验
- 使用 `scripts/validate_skill_baseline.py` 校验 Skill 包资产与 Product 当前导出是否一致
- 继续把 `validation_results` 向更细粒度的跨输出 contract 扩展，而不只停留在最小内容级校验
- 优先抽离可复用的 contract helper，避免 Skill 入口脚本持续堆积格式感知逻辑
- 优先把稳定细节做成可声明引用的 helper/注册表，而不是散落在单个脚本中
- 优先把跨项目复用所需的参考资产（contract 文档、catalog 子集、示例）封进 Skill 包
- 优先把 Product 已稳定实现的输出细节沉淀进 Skill 包内 contract 文档与验证 helper
- 使用 `python scripts/install_skill_to_agents.py --force` 将当前 Skill 安装到默认项目本地 `.agent/skills`
- 使用 `python scripts/validate_skill_baseline.py` 防止 Product 与 Skill 的 manifest / registry / 生成脚本清单漂移

### 13.2 中长期

- 为 SKILL 增加样例、术语映射与引用资产
- 为 Product 增加更稳定的格式回归与输出基线
- 逐步建立 SKILL 与 Product 的更明确接口关系
- 继续把 `output_manifest.json`、`contract_registry.json` 与生成器实现纳入同一维护闭环
- 后续如需要当前用户全局 agent 目录，可使用 `--target-root $HOME/.agents` 安装到全局 `.agents/skills`
