# 部署指南

本项目当前没有独立服务部署流程。

## 环境

- 本地 Python 环境
- 仓库依赖见 `requirements.txt` 与 `pyproject.toml`

## 发布前检查

```powershell
python -m tflshell validate
python scripts\validate_skill_package.py
python scripts\validate_skill_baseline.py
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q
```

## 回滚

如果生成输出或 Skill 基线出现非预期漂移，回滚对应代码、`Skill/tfls-shell/package_assets/`
和相关契约文档后重新运行发布前检查。
