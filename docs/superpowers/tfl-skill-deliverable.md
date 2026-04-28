# TFLs-Shell Product 交付说明

## 1. 文档定位

本文件不再描述“正式 Skill 交付物”，而是描述当前仓库中
`TFLs-Shell Product` 的交付与作用。

它用于说明：

- Product 是什么
- Product 不是什么
- Product 与 `TFLs-Shell SKILL` 的关系
- Product 当前维护哪些资产

## 2. 当前口径

当前正式口径为：

- `TFLs-Shell SKILL`：可复用应用层 Skill 包
- `TFLs-Shell Product`：仓库内产品化实现与维护主 source

因此，之前形成的 recommend / generate 相关实现、设计稿、测试与说明，
现在统一归类为 `Product` 资产，而不是“无效输出”。

## 3. Product 当前包含

- 设计与契约文档
- shell catalog
- 生成器
- 推荐支持逻辑
- 测试基线
- 示例输出与格式约束

## 4. Product 的价值

Product 的主要价值在于：

- 为 `TFLs-Shell SKILL` 提供高保真参考
- 持续维护格式与结构的稳定性
- 作为后续规则与输出演进的主要 source

## 5. Product 与 SKILL 的关系

应理解为：

- SKILL 负责复用与调用
- Product 负责维护与高保真实现

调用 SKILL 后，如需产出尽量接近本项目正式生成物的内容，应尽量参考 Product。

## 6. 当前 Product 资产示例

- `src/tflshell/` 下的 Product 实现代码
- `tests/` 下的回归与契约测试
- `docs/superpowers/specs/` 下的设计与治理文档
- `output/` 下的正式业务输出样式参考

## 7. 风险提示

- `技术风险`：若 Product 不再被视为主 source，SKILL 输出会逐渐偏离正式格式
- `维护风险`：若历史资产不重新归类，团队会持续混淆 SKILL 与 Product
- `项目风险`：若对外描述仍把 Product 叫作 SKILL，实现与交付边界会再次失控

## 8. 优化建议

### 8.1 立即可做

- 继续把历史“项目级 skill”口径统一改称 `Product`
- 用 Product 作为 SKILL 的高保真参考基线

### 8.2 中长期

- 持续沉淀 Product 的格式契约、输出样例与测试基线
- 逐步建立 SKILL 对 Product 的稳定引用关系
