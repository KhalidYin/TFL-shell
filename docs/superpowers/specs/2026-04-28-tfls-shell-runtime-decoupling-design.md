# TFLs-Shell SKILL 运行解耦优先设计

日期：2026-04-28  
主题：将 `TFLs-Shell SKILL` 从当前仓库运行时依赖中进一步解耦，优先形成包内最小运行子集  
状态：V1，待 review

## 1. 文档目的

本文档用于定义 `TFLs-Shell SKILL` 的下一步演进方向：

- 不再只补“文档和静态资产”
- 而是开始补“可运行的包内最小子集”
- 使 Skill 包在迁移到其他项目时，优先依赖包内 runtime，而不是默认依赖 `src/tflshell`

本设计采用“运行解耦优先”路线，不在本轮追求 recommend 逻辑彻底独立，而是先把以下能力稳定封进 Skill 包：

- catalog loader
- registry loader
- xlsx/docx/sop wrapper
- Product -> Skill 的受控导出同步流程

## 2. 目标与非目标

### 2.1 本轮目标

- 让 Skill 包拥有包内 runtime 层，而不是只有脚本层
- 让 `recommend_then_generate.py` 能优先使用包内 runtime 资产
- 让三类正式输出至少通过包内 wrapper 暴露统一调用接口
- 让 `catalog_subset.json` 从“静态快照”升级为“受控导出产物”
- 让测试与校验脚本能识别 Skill 包是否具备最小运行解耦条件

### 2.2 本轮非目标

- 不在本轮完全移除 recommend 对 Product 实现的依赖
- 不在本轮重写 DOCX / XLSX / SOP 生成器内核
- 不在本轮把整个 `src/tflshell` 镜像搬入 Skill 包
- 不在本轮引入新的 MCP 路径

## 3. 为什么选择这条路线

当前 `TFLs-Shell SKILL` 已经具备：

- `SKILL.md`
- 包内脚本
- 细节 contract helper
- `declared_references`
- 最小自包含资产

但仍存在关键问题：

- 运行时仍直接依赖 `src/tflshell`
- `catalog_subset.json` 仍只是一次性导出的静态文件
- 外部项目即使拿到 Skill 包，也还不能优先走包内运行路径

如果直接进入“彻底独立包”路线，会同时引入：

- recommend 逻辑复制
- catalog 规则复制
- 生成器实现复制

这会显著扩大维护面，且与当前“先确保输出尽量和 Product 一致”的目标冲突。

因此，本轮采用“运行解耦优先”：

- 先把包内运行入口和包内资产读写路径稳定下来
- 再决定后续是否继续把 recommend 最小子集内收

## 4. 设计原则

### 4.1 package-first

Skill 包必须优先以自己的目录结构解释自身运行能力，而不是假设调用环境理解当前仓库。

### 4.2 runtime-subset-only

只把稳定、可复用、对外部运行最关键的最小子集放进包内，不复制整个 Product。

### 4.3 wrapper-before-rewrite

先建立包内 wrapper 层，统一调用接口与输出契约；本轮不重写生成器核心实现。

### 4.4 export-as-build-artifact

`catalog_subset.json` 必须开始拥有明确导出来源、导出入口和版本信息，不能长期停留在人工快照状态。

### 4.5 docs-tests-sync

所有运行解耦能力必须同步落到：

- `SKILL.md`
- `PACKAGE_GUIDE.md`
- `DEVELOPMENT_RULES.md`
- `PROJECT_GUIDE.md`
- `test_guide.md`

## 5. 目标结构

建议在 `.trae/skills/tfls-shell/` 下形成如下结构：

```text
.trae/skills/tfls-shell/
  SKILL.md
  PACKAGE_GUIDE.md
  DEVELOPMENT_RULES.md
  examples/
  package_assets/
  runtime/
    __init__.py
    catalog_loader.py
    registry_loader.py
    wrappers/
      __init__.py
      xlsx_wrapper.py
      docx_wrapper.py
      sop_wrapper.py
  scripts/
    alignment_contracts.py
    package_bundle.py
    generate_project_aligned_outputs.py
    recommend_then_generate.py
    export_catalog_subset.py
```

说明：

- `runtime/` 是包内最小运行层
- `scripts/` 仍是可执行入口和维护脚本层
- `package_assets/` 是随包携带的静态/半静态资产层

## 6. 关键模块设计

### 6.1 `runtime/catalog_loader.py`

职责：

- 读取 `package_assets/catalog_subset.json`
- 返回包内可用的 catalog 表示
- 暴露最小查询接口

最小接口建议：

- `load_catalog_subset()`
- `get_item(item_id)`
- `all_items()`
- `items_by_section(section)`

本轮不要求其完全等价于 `TFLCatalog`，但应覆盖当前 Skill 包需要的最小访问路径。

### 6.2 `runtime/registry_loader.py`

职责：

- 读取 `package_assets/contract_registry.json`
- 返回受控 contract 注册信息
- 支持脚本与 helper 查询当前支持的 contract key

最小接口建议：

- `load_contract_registry()`
- `get_contract(name)`
- `list_contracts()`

### 6.3 `runtime/wrappers/xlsx_wrapper.py`

职责：

- 以包内统一接口声明如何生成 `xlsx`
- 封装输出命名、输出路径、参数整理
- 在可用时调用底层生成实现

本轮要求：

- wrapper 对上层统一暴露 `generate(...)`
- 上层不直接知道底层生成器类名

### 6.4 `runtime/wrappers/docx_wrapper.py`

职责：

- 封装 `docx` shell 输出的统一调用接口
- 负责 sponsor、protocol、presentation profile 等参数整形
- 保持输出命名契约不变

### 6.5 `runtime/wrappers/sop_wrapper.py`

职责：

- 封装 `sop` 输出的统一调用接口
- 负责最小参数收口和输出路径规范

### 6.6 `scripts/export_catalog_subset.py`

职责：

- 从 Product 的当前 catalog 受控导出 Skill 包使用的 `catalog_subset.json`
- 写入版本、governed sections、item_count
- 保证导出格式稳定

该脚本是“静态导出升级为受控构建产物”的第一版入口。

## 7. 入口脚本改造

### 7.1 `recommend_then_generate.py`

当前问题：

- 直接导入 `build_catalog`
- 直接导入 Product 生成器
- 无法明确声明当前是否走包内 runtime

改造后应：

1. 优先读取 `package_bundle`
2. 优先走 `runtime/catalog_loader.py`
3. 生成阶段优先走 `runtime/wrappers/*`
4. 在返回结果中新增 runtime 使用摘要，例如：

```json
{
  "runtime_summary": {
    "mode": "skill_runtime_preferred",
    "catalog_source": "package_assets/catalog_subset.json",
    "registry_source": "package_assets/contract_registry.json",
    "wrapper_layer": "runtime/wrappers"
  }
}
```

### 7.2 `generate_project_aligned_outputs.py`

应进行同样收口：

- 不直接暴露底层生成器导入路径
- 优先经由 wrapper 层生成

## 8. Product -> Skill 同步流程

### 8.1 当前问题

`catalog_subset.json` 目前虽然已存在，但本质上仍是人工导出文件。

风险：

- Product 变化后无法确认何时同步
- Skill 包中的 catalog 子集可能落后
- 外部调用者无法理解该子集的版本来源

### 8.2 本轮目标流程

建立如下最小闭环：

1. Product 维护 `build_catalog()`
2. `scripts/export_catalog_subset.py` 从 Product 导出 Skill 需要的最小字段子集
3. 导出结果写入 Skill 包的 `package_assets/catalog_subset.json`
4. 导出结果写入版本元信息
5. 测试验证导出结构稳定

### 8.3 同步要求

每次出现以下变化时，应重新导出：

- shell 新增或移除
- applicability 变化
- shell family 变化
- phase scope 变化
- coverage summary 变化
- source listing 映射变化

## 9. 测试设计

### 9.1 新增单测

- `catalog_loader` 能读取 `catalog_subset.json`
- `registry_loader` 能读取 `contract_registry.json`
- `xlsx/docx/sop wrapper` 均存在统一入口
- `recommend_then_generate.py` 返回 `runtime_summary`
- `validate_skill_package.py` 校验运行解耦资产
- `export_catalog_subset.py` 导出结构稳定

### 9.2 保留回归

继续保留当前：

- `validation_results`
- `declared_references`
- `package_bundle`
- `xlsx/docx/sop` 内容级 contract 检查

### 9.3 暂不做

- 不做离仓全运行集成测试的全量闭环
- 不做 recommend 彻底脱离 Product 的测试

## 10. 风险与取舍

### 10.1 技术风险

如果 wrapper 只是简单转发，但没有统一接口和运行摘要，运行解耦价值会很弱。

### 10.2 维护风险

如果 `catalog_subset.json` 没有受控导出流程，Skill 包中的真值会逐渐漂移。

### 10.3 项目风险

如果本轮顺手把 recommend 全量内收，会明显扩大范围，拖慢当前主目标。

## 11. 实施顺序

建议按以下顺序实现：

1. 新增 `runtime/catalog_loader.py`
2. 新增 `runtime/registry_loader.py`
3. 新增 `runtime/wrappers/`
4. 改造 `recommend_then_generate.py`
5. 改造 `generate_project_aligned_outputs.py`
6. 新增 `scripts/export_catalog_subset.py`
7. 补测试
8. 更新文档

## 12. 成功标准

本轮完成后，应满足：

- Skill 包已具备包内 runtime 层
- 两个入口脚本优先走包内 runtime
- `package_bundle` 与 `runtime_summary` 能说明当前运行来源
- `catalog_subset.json` 已有受控导出入口
- 测试能验证运行解耦资产和导出流程

## 13. 风险提示

- `技术风险`：本轮只是“运行解耦优先”，还不是 recommend 全独立。
- `维护风险`：如果文档与导出脚本不同步，会再次形成双重真值。
- `项目风险`：如果后续继续扩大范围而不分阶段，Skill 包会重新膨胀为 Product 镜像。

## 14. 优化建议

### 14.1 立即可做

- 先实现 runtime 层与 wrapper 层
- 先建立 `catalog_subset.json` 的受控导出入口
- 先让入口脚本返回 `runtime_summary`

### 14.2 中长期

- 再评估是否把 recommend 最小子集继续内收
- 再增加离仓运行验证
- 再引入更细粒度的 registry 版本与来源追踪

### 14.3 工具链

- 为导出脚本增加专门单测
- 为 runtime loader 增加 fixture 测试
- 将 Skill 包运行解耦校验纳入固定回归集合
