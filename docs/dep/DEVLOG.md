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

