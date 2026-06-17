---
name: project-catalog-structure
description: Catalog 按 CSR section 模块化维护，figure shell 由 registry 统一渲染。
type: project
---

Catalog 定义按 CSR section 拆分：

- `src/tflshell/data/common.py` 放共享 section/type/header/ellipsis 常量。
- `src/tflshell/data/sections/` 放各 section 的 `build_*_items()`。
- `src/tflshell/data/definitions.py` 只保留治理归一化、source listing 映射和 `build_catalog()` 编排。

Figure shell 由 `src/tflshell/figures/registry.py` 维护 renderer 映射与 mock data factory，
DOCX 生成器只调用 registry，并在默认生成时嵌入模拟 PNG。

**Why:** 用户明确指出大量表格集中在单一脚本难以维护，并要求 figure shell 从代码层面模拟真实图形放入 shell。

**How to apply:** 新增或修改 TFL 时优先编辑对应 section builder；新增 figure 类型时先注册 renderer 和 mock data，再更新 DOCX/测试/Skill 基线。
