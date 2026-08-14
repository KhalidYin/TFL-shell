# Dev Log

---

## 2026-06-17

### Round 1 [14:53]

#### Done
- 将项目长期规范文档迁移到 `docs/main/`，并新增 `USAGE.md`、`docs/main/memory/` 与 `docs/deploy/DEPLOY_GUIDE.md`，对齐 personal-assistant 文档结构。
- 删除 `docs/superpowers/` 下头脑风暴、设计草稿和历史交付说明，避免作为长期规范继续漂移。
- 将正式 Skill 源目录从 `.trae/skills/` 迁移到 `Skill/`，并删除 `.trae` 源目录。
- 新增 `scripts/install_skill_to_agents.py`，默认仅安装到项目本地 `.agent/skills/tfls-shell`；本轮只执行 `--dry-run`，未安装 Skill。
- 新增 `scripts/validate_skill_baseline.py`，把 `output_manifest.json`、`contract_registry.json` 和 Skill 生成/验证脚本清单纳入 Product 对齐回归基线。
- 补强 `scripts/validate_skill_package.py`，要求 Skill 包包含完整生成入口脚本。
- 新增安装脚本与 baseline 校验测试，并同步更新 Skill 包说明、开发规则、项目规范和测试指南。
- 验证通过：`python scripts\validate_skill_package.py`、`python scripts\validate_skill_baseline.py`、`python scripts\install_skill_to_agents.py --dry-run`、`python -m tflshell validate`。
- 全量测试通过：`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q`，结果为 `59 passed, 24 warnings`。

#### Issues / Blockers
- 本机 pytest 自动加载的第三方插件与 pytest 版本存在兼容问题，测试需设置 `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`。
- 仍有 Python 3.14 下 openpyxl 的 `datetime.utcnow()` 弃用警告，当前不影响本轮改动。

#### Next
1. Done — no next steps

#### Files Changed / Commits
- `Skill/`（新增/迁移/修改）— (uncommitted)
- `.trae/`（删除）— (uncommitted)
- `docs/main/`（新增/迁移/修改）— (uncommitted)
- `docs/dep/DEVLOG.md`（新增）— (uncommitted)
- `docs/deploy/DEPLOY_GUIDE.md`（新增）— (uncommitted)
- `docs/superpowers/`（删除）— (uncommitted)
- `USAGE.md`（新增）— (uncommitted)
- `scripts/install_skill_to_agents.py`（新增）— (uncommitted)
- `scripts/validate_skill_baseline.py`（新增）— (uncommitted)
- `scripts/validate_skill_package.py`（修改）— (uncommitted)
- `src/tflshell/skill.py`（修改）— (uncommitted)
- `tests/unit/`（新增/修改）— (uncommitted)

---

### Round 2 [15:57]

#### Done
- 将 catalog 定义拆成 `src/tflshell/data/common.py` 与 `src/tflshell/data/sections/*.py`，`definitions.py` 只保留治理归一化、source listing 映射和 `build_catalog()` 编排。
- 修正 14.1 实践边界：`T14.1.1` 限定为通用人口学/体格基线表，移除 ECOG、疾病分期、组织学等肿瘤特异内容；`T14.1.2` 改为 `Summary of Baseline Oncology Disease Characteristics` 并标记为 `Oncology only`。
- 新增 `src/tflshell/figures/registry.py`，集中维护 figure renderer、mock data factory 与 PNG buffer 生成；`DocxShellGenerator` 改为调用 registry。
- 保留 `src/tflshell/generators/figure_engine.py` 为向后兼容入口，避免既有调用方断裂。
- 新增测试覆盖 catalog 模块结构、14.1 实践边界、figure registry 支持类型、代表性 PNG buffer 生成与 DOCX 嵌图。
- 重新导出 `Skill/tfls-shell/package_assets/catalog_subset.json` 与 `output_manifest.json`，并重新生成 DOCX / XLSX / SOP 正式输出。
- 验证正式 DOCX 当前包含 28 个 inline figure image，`Skill/tfls-shell/scripts/validate_outputs.py` 对重新生成的 DOCX/XLSX/SOP 通过。
- 全量测试通过：`PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q`，结果为 `66 passed, 24 warnings`。

#### Issues / Blockers
- 部分 figure 仍是语义近似 renderer，例如 CDF 复用 longitudinal、eDISH/heatmap 复用 box plot；本轮已通过 registry 集中管理，但尚未新增专门 renderer。
- 14.1 的 shell family 仍较粗，后续可继续细分 disposition、protocol deviation、exposure、medical history、medication 等子家族。
- openpyxl 在 Python 3.14 下仍有 `datetime.utcnow()` 弃用警告。

#### Next
1. 为 CDF、eDISH、heatmap、PK overlay 增加语义专用 renderer 或显式 renderer profile。
2. 为 14.1 增加更细的 shell family / denominator / sorting metadata，并考虑在 XLSX 增加 row/column 审阅视图。

#### Files Changed / Commits
- `src/tflshell/data/common.py`（新增）— (uncommitted)
- `src/tflshell/data/sections/`（新增）— (uncommitted)
- `src/tflshell/data/definitions.py`（重构）— (uncommitted)
- `src/tflshell/figures/registry.py`（新增）— (uncommitted)
- `src/tflshell/generators/docx_shell.py`（修改）— (uncommitted)
- `src/tflshell/generators/figure_engine.py`（修改）— (uncommitted)
- `tests/unit/test_catalog_module_structure.py`（新增）— (uncommitted)
- `tests/unit/test_figure_shell_rendering.py`（新增）— (uncommitted)
- `tests/unit/test_section_14_1_practice.py`（新增）— (uncommitted)
- `Skill/tfls-shell/package_assets/`（更新）— (uncommitted)
- `output/`（重新生成）— (uncommitted)
- `docs/main/`、`USAGE.md`、`docs/main/memory/`（更新）— (uncommitted)
