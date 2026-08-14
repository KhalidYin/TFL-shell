# Dev Log — R001-R040

---

## 2026-08-12

### R001 [17:58] [P1-tfl-shell-layout-refactor] P1-P5: TFL shell 临床实践与布局重构

#### Done
- 建立兼容式 layout contract，支持多级表头、跨页重复表头、列语义对齐、comparison 位置与 listing 排序/分母说明。
- 重构代表性 14.2 model comparison、14.3 汇总/受试者级边界、14.4 PK period comparison 与 16.2 宽 listing；未为布局形式硬塞指标。
- 增加 CDF、eDISH、laboratory heatmap、concentration-QTcF 与 PK profile 专用 renderer，并给 mock 图体增加 illustrative 标识。
- 修正 source listing 显式优先、Hy's Law/代谢/PK/lab 已知映射，移除 food-effect/crossover 的无依据 Non-Oncology 限定，收敛 specialised coverage 和固定结果值。
- XLSX 增加 Layout Profile、Comparison Position、Sorting Note、Denominator Note；SOP 改为按列语义对齐；DOCX 修复 figure 孤立续页与空白尾页。
- 更新 Product 主文档与使用说明，生成 `_REVIEW` DOCX/XLSX/SOP 实际输出。
- 验证：`tflshell validate` 通过（206 TFL）；相关回归 38 passed；Product 范围回归 81 passed、3 deselected；Ruff 通过；Word→PDF 224 页，空白页 0、低文本页 0。

#### Issues / Blockers
- 固定正式 DOCX 被 Word 锁定，无法安全覆盖；新版保存在 `output/*_REVIEW.*`。未强制关闭用户 Word 进程。
- 全套 pytest 为 80 passed / 3 failed。失败均来自本轮明确冻结的 `Skill/` 衍生 manifest/contract 仍期待旧 XLSX 表头、适用性计数和正式文件；按用户边界留待实际输出审核通过后同步。
- openpyxl 在 Python 3.14 下产生 `datetime.utcnow()` 弃用警告，不影响输出。
- `tmp/` 审阅中间件清理被环境递归删除安全策略拦截；未绕过安全策略，正式输出不受影响。

#### Next
1. 用户审核 `output/*_REVIEW.*` 实际输出。
2. 审核通过后，关闭占用正式 DOCX/SOP 的 Word 文档并将 REVIEW 文件替换为正式文件名。
3. 另起任务同步 `Skill/tfls-shell/` contract、manifest 与相关测试。

#### Files Changed / Commits
- `src/tflshell/models/`, `src/tflshell/docx_utils/`, `src/tflshell/generators/`, `src/tflshell/figures/`, `src/tflshell/data/`（modified/added）— (uncommitted)
- `tests/unit/`, `tests/integration/`（modified/added）— (uncommitted)
- `docs/main/`, `USAGE.md`, `docs/dep/`（modified/added）— (uncommitted)
- `output/TFL_Shell_Template_v2.1.0_REVIEW.docx`, `output/TFL_TOC_v2.1.0_REVIEW.xlsx`, `output/TFL_Shell_SOP_v2.1.0_REVIEW.docx`（generated）— (uncommitted)

---

## 2026-08-14

### R002 [14:29] [P1-tfl-shell-layout-refactor] 用户复核问题修正与 REVIEW_R2 输出

#### Done
- DOCX 每个 shell 仅保留一条黑色粗体 `Display Label + Title`；Heading 4 和书签锚定同一段，移除重复可见标题。
- Sponsor 与 Word `Page X of Y` 字段位于同一行，页码通过右对齐 tab 放置；Protocol 独占下一行。
- flat/multilevel 表头默认首个结构列左对齐，其余列和数据遵循声明式 alignment。
- Listing 强制清空 `source_listing`，患者明细输出不再出现 `Source Listing` 脚注。
- 对 140 张 Table 按实际标题、表头、行标签和既有脚注扫描受控缩写，并按百分比、n/N、模型、描述统计和时间事件语义补充统计定义；未向无关表格统一填充模型指标。
- `T14.3.1.3/.16/.18/.21/.22` 将 AE 最大 Grade 改为 SOC/PT 或 Cycle 下的层级行；实验室 shift 的 Grade 维度保持原语义。
- 修正 `T14.1.4/.9` 误复用 SOC/PT 首列表头的问题，分别使用 ATC Level 3/2 + Preferred Name。
- 更新 Product 规范与测试；未修改或同步 `Skill/`。
- 生成 `output/*_REVIEW_R2.*` 三份实际输出。代表性 Word→PDF 人工检查通过；完整输出结构验收为 206 headings/bookmarks、206 Sponsor/Page 行、206 XLSX 主表行。
- 验证：catalog 206 items / 0 warnings；针对性测试 31 passed；Product 范围完整回归 64 passed；`git diff --check` 与可独立 lint 的变更模块 Ruff 通过。

#### Issues / Blockers
- 原 `output/TFL_Shell_Template_v2.1.0_REVIEW.docx` 仍被 Word 占用，覆盖时触发 `PermissionError [Errno 13]`；为不强制关闭用户进程，改用 `TFL_Shell_Template_v2.1.0_REVIEW_R2.docx`，旧文件未改动。
- Python 3.14 下 pytest-asyncio 与 openpyxl 仍产生弃用警告，不影响生成和验证结果。
- `Skill/` 衍生快照仍按用户边界冻结，未运行本轮同步；需待实际输出审核通过后另起任务处理。

#### Next
1. 用户审核 `output/*_REVIEW_R2.*`。
2. 审核通过且关闭 Word 占用后，再决定是否替换正式文件名。
3. 经用户明确批准后另起任务同步 `Skill/tfls-shell/`。

#### Files Changed / Commits
- `src/tflshell/docx_utils/header_block.py`, `src/tflshell/docx_utils/three_line_table.py`, `src/tflshell/generators/docx_shell.py`, `src/tflshell/models/tfl_item.py`（modified）— (uncommitted)
- `src/tflshell/data/definitions.py`, `src/tflshell/data/sections/section_14_1.py`, `src/tflshell/data/sections/section_14_3.py`（modified）— (uncommitted)
- `tests/unit/test_docx_header_contract.py`, `tests/unit/test_table_layout_contract.py`, `tests/unit/test_clinical_layout_practice.py`（added/modified）— (uncommitted)
- `docs/main/PROJECT_SPEC.md`, `docs/main/CODE_STYLE.md`, `docs/main/TEST_GUIDE.md`, `docs/dep/`（modified）— (uncommitted)
- `output/TFL_Shell_Template_v2.1.0_REVIEW_R2.docx`, `output/TFL_TOC_v2.1.0_REVIEW_R2.xlsx`, `output/TFL_Shell_SOP_v2.1.0_REVIEW_R2.docx`（generated）— (uncommitted)

---

### R003 [16:20] [P2-table-layout-audit-skill-sync] P1-P4: 全表审查、R3 输出与 Skill 发布

#### Done
- 复核初始 140 张 Table，生成逐表审核矩阵与总结报告；当前保留 131 张，退役 9 张重复/非常规 AE 表。
- `T14.3.1.3` 合并为全治疗组 SOC/PT/maximum-grade 行层级；移除通用 AE by-cycle、重复 full-frequency PT、relationship × grade 和组别专属重复表。
- AE onset/duration/outcome 改为左侧统计/结局层级与治疗组列；IRR、late-onset、onset-window、follow-up 使用 protocol/SAP-defined 口径。
- 单一 by-visit endpoint 以 Visit 为最高层级；T14.4.5 将 treatment estimate 与 comparison 分为独立列组；多参数 safety 保留 Parameter > Visit > Statistic。
- 在 placeholder padding 前展开 legacy `Visit — Statistic` / `Timepoint — Statistic` 标签，修复语义列静默错位。
- 同表 MedDRA/CTCAE version 收敛为一条 coding/grading footnote；缩写与统计定义继续按实际可见内容受控生成。
- 生成 `_REVIEW_R3` DOCX/XLSX/SOP、140 行审核 XLSX 和 2 页审核报告，并重生成默认正式输出。
- 同步 `Skill/tfls-shell/` 的 SKILL 规则、DOCX/XLSX/table-layout contract、helper、catalog subset、manifest 和 registry。
- 验证：catalog 197 items / 0 warning；Skill output/baseline/package/install dry-run 通过；Word→PDF 207 页且 0 空白/低文本页；回归 93 passed，修正 2 个旧 contract/输出同步失败后定向 2 passed。

#### Issues / Blockers
- 首次 PDF 命令找不到 LibreOffice；改用本机 Word/Excel COM 后完成 PDF round-trip。根因是环境缺少 `soffice`，不是文档生成失败。
- 全套 pytest 首次因 125 秒命令上限被终止；提高上限并分组后完成。两项失败均为旧 Skill key 与旧默认输出，已修复。
- openpyxl 在 Python 3.14 下仍有 `datetime.utcnow()` 弃用警告，不影响输出内容。

#### Next
1. 在 study-specific 使用时补齐 protocol/SAP-defined visit、window、denominator、model 与 multiplicity 规则。
2. 如需纸质打印逐表审核矩阵，可另生成分页型窄表报告；当前 XLSX 以交互筛选审阅为主。
3. 远端 draft PR 供用户最终审核与合并。

#### Files Changed / Commits
- `src/tflshell/`, `tests/`, `docs/main/`, `Skill/tfls-shell/`, `scripts/generate_layout_audit.py`（modified/added）— release commit
- `output/*_REVIEW_R3.*`, `output/TFL_Table_Layout_Audit_R3.xlsx`, `output/TFL_Table_Layout_Audit_Report_R3.docx`（generated, ignored）
