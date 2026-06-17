# 使用指南

## 项目用途

`TFLshell` 用于维护落地级 TFL shell 主库、正式 DOCX / XLSX / SOP 生成能力，
并从稳定 Product 流程中抽取可复现的 `TFLs-Shell SKILL`。

## 常用命令

生成当前 Product 输出：

```powershell
python -m tflshell generate
```

默认生成会把可支持的 figure shell 渲染为模拟 PNG 并嵌入 DOCX。仅在需要跳过图形时使用：

```powershell
python -m tflshell generate --no-figures
```

校验 catalog：

```powershell
python -m tflshell validate
```

校验 Skill 包结构：

```powershell
python scripts\validate_skill_package.py
```

校验 Skill 回归基线是否与 Product 当前实现一致：

```powershell
python scripts\validate_skill_baseline.py
```

预览 Skill 安装路径，不写入文件：

```powershell
python scripts\install_skill_to_agents.py --dry-run
```

运行测试：

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q
```

## 文档入口

- `docs/main/PROJECT_GUIDE.md`：项目架构与边界
- `docs/main/PROJECT_SPEC.md`：受控规则与质量门
- `docs/main/CODE_STYLE.md`：编辑、命名与同步规则
- `docs/main/TEST_GUIDE.md`：测试契约
- `docs/dep/DEVLOG.md`：开发记录

## 注意事项

- 不要把 `output/` 作为规范真值源；它是生成结果。
- 不要保留新的头脑风暴草稿作为项目规范；稳定规则必须进入 `docs/main/` 或 Skill 包内契约文档。
- 未经明确要求，不要安装 Skill；可先使用 `--dry-run` 预览。
