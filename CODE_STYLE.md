# 代码与文档规范

## 1. 文档目的

本文档定义 `TFLshell` 仓库的代码、文档与治理同步规则。

它主要服务于 `TFLs-Shell Product` 的持续维护，并间接为
`TFLs-Shell SKILL` 提供稳定参考基线。

## 2. 通用原则

- 优先做小而明确、可读性强的改动
- 规则变化必须同步到文档
- shell metadata 视为受控项目数据，而不是随意文本
- 优先使用轻量、可自动化的检查方式

## 3. 目录职责

- `src/tflshell/data/`：shell 定义与受控内容源
- `src/tflshell/models/`：领域模型与共享语义
- `src/tflshell/generators/`：DOCX、XLSX、Figure 等生成器
- `src/tflshell/`：Product 支撑逻辑，例如推荐、验证与工具方法
- `scripts/`：仓库级辅助脚本，优先放置 Skill 包校验与轻量提炼工具
- `.trae/skills/`：可复用 Skill 包
- `docs/`：设计、规范与交付说明
- `tests/`：回归与契约测试

## 4. 命名规则

### 4.1 Python

- 模块：`snake_case`
- 函数：`snake_case`
- 类：`PascalCase`
- 常量：`UPPER_SNAKE_CASE`

### 4.2 Clinical Shell Domain

- TFL ID 保持受控格式，如 `T14.3.1`
- reviewer-facing label 从 ID 稳定派生
- section 术语使用受控 CSR section 编号
- applicability 仅使用受控集合

### 4.3 文件名

正式输出文件保持稳定命名，例如：

- `TFL_Shell_Template_v<version>.docx`
- `TFL_TOC_v<version>.xlsx`
- `TFL_Shell_SOP_v<version>.docx`

## 5. 文档同步规则

任何影响以下内容的改动，都必须同步检查文档：

- 范围边界
- section coverage
- applicability wording
- metadata 字段
- 输出字段名
- shell family 解释
- phase / domain coverage
- `TFLs-Shell SKILL` 的触发条件、输出契约或配套规则

## 6. Skill 与 Product 口径

后续一律采用：

- `TFLs-Shell SKILL`：可复用应用层包
- `TFLs-Shell Product`：仓库内产品化实现层

不要再把某个 `skill.py` 或 CLI 子命令写成 Skill 本体。

## 7. 编辑标准

- 项目文档统一使用 Markdown
- 文档统一使用中文
- 注释保持简洁且有必要
- 已批准的规范文档中不要留下 `TBD`、`TODO`

## 8. 变更纪律

### 8.1 小改动

- 更新最近相关文档
- 说明受影响规则
- 避免无关重构

### 8.2 结构性改动

如涉及新 shell family、新 metadata 或输出规则变化：

- 文档与代码必须同一轮更新
- 如行为有明显变化，需同步更新设计稿
- 同步更新测试或测试说明

### 8.3 规范变更

规范文档（`PROJECT_SPEC.md` / `PROJECT_GUIDE.md` / `CODE_STYLE.md` / `test_guide.md`）
中任何受控规则的修改，必须在同一轮 commit 中完成对应的代码变更和测试更新。

禁止行为：

- 规范文档改了但代码没改（"先改文档，代码以后补"）
- 代码变了但规范文档没变（"实现先行，文档以后追"）
- commit message 只说"更新规范"但实际没有代码变更（空规范变更）

规范变更的完整同步要求见 `PROJECT_SPEC.md` §13。

## 9. 推荐工具链

- `black`
- `ruff`
- `pre-commit`
- `pytest`

## 10. 风险提示

- `技术风险`：版本或元数据漂移会破坏输出可信度
- `维护风险`：不受控自由文本会增加未来清理成本
- `项目风险`：代码变了文档不变，会造成对外口径冲突

## 11. 优化建议

### 11.1 立即可做

- 继续集中管理版本与命名
- 减少重复指导文案

### 11.2 中长期

- 增强 metadata 完整性自动校验
- 增强 cross-output 规则检查

### 11.3 工具链

- 增加 Markdown 术语一致性检查
- 增加版本字符串漂移检查
