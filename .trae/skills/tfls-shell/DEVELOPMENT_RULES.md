# TFLs-Shell SKILL 开发规则

## 1. 目标

本文件用于约束后续 `TFLs-Shell SKILL` 的制定与开发方向，确保后续所有扩展都
围绕“可复用应用层 Skill 包”这一目标展开。

## 2. 默认定义

后续凡提到 `TFLs-Shell SKILL`，默认指：

- 一个可复用的应用层 Skill 包
- 至少包含 `SKILL.md`
- 可附带补充文档、样例、辅助脚本或参考资产

后续凡提到“上游项目”，默认指：

- 当前仓库内的产品化支撑层
- 包含代码、文档、测试、生成器、设计稿与输出基线
- 仅作为 Skill 提炼阶段的上游经验来源之一

## 3. 开发顺序

后续开发时，应坚持以下顺序：

1. 先定义 SKILL 的应用层目的、触发条件、边界与输出契约
2. 再决定需要哪些包内补充文档、样例、脚本或资产
3. 最后再决定是否需要从上游项目中提炼可复用子集

不要再从某个项目实现反推 Skill 定义。

## 4. 允许加入的内容

为了提高调用可靠性，可以加入：

- 输入解释规则
- 输出字段说明
- 风险提示模板
- 术语映射
- 典型样例
- 质量检查清单
- 辅助脚本
- 精选的上游经验摘要
- 最小运行依赖清单
- 可执行样例请求
- 受控 catalog 子集
- contract registry
- output manifest
- Product 对齐契约文档
- 输出结构验证脚本

如果某类细节已经在上游项目中反复稳定出现，例如：

- workbook 字段 contract
- workbook sheet 数量、名称与顺序
- docx header block 规则
- docx 页面设置、heading 层级与 table layout
- sop 关键 heading 与治理文案
- placeholder / quality gate / 命名规则

应优先把它们整理成独立 helper 或细节注册表，而不是继续内联堆在入口脚本中。

如果目标是让 Skill 包可以直接迁移到其他项目中使用，则这些稳定子集还应尽量随包封装，
并通过结构化字段暴露“当前包是否已经自包含可运行”。

当前最先内收的运行子集应优先包括：

- catalog loader
- registry loader
- `docx / xlsx / sop` wrapper
- Product -> Skill 的 catalog 受控导出脚本
- Product -> Skill 的输出契约受控导出脚本
- Skill 包内输出契约验证脚本

当前优先级最高的脚本类型是：

- 直接提升“输出一致性”的生成脚本
- 能稳定复现项目命名与输出结构的辅助脚本
- 能把 recommend 与 generate 串成单条调用路径的脚本

## 5. 必须避免的偏差

以下情况都应视为错误：

- 把某个仓库里的 `skill.py` 或 CLI 子命令当成 Skill 包本体
- 把整个上游项目当成 Skill 运行时依赖
- 只写一份 `SKILL.md`，却不给必要的可靠性支撑文档
- 先写实现，再让定义被实现绑架
- 不区分“可复用子集”和“完整项目资产”

## 6. 变更要求

当 Skill 包发生实质变化时，至少应检查：

- `SKILL.md` 是否仍清楚描述触发条件与边界
- 包内补充文档是否仍与主入口一致
- 示例是否仍代表当前应用层工作流
- 如有辅助脚本，其输入输出是否仍与文档一致
- 如有上游提炼资产，是否已裁剪为真正可复用子集
- 如有细节 helper，是否仍只承载稳定可复用 contract，而不是临时实现碎片
- 如脚本声明引用了细节 contract，`declared_references` 是否仍与实际 helper 保持一致
- 如目标是跨项目复用，最小自包含资产是否齐备并可被脚本发现
- 如已引入 runtime 层，入口脚本是否优先走包内 loader / wrapper
- 如已引入导出脚本，`catalog_subset.json` 是否仍由受控同步入口生成
- 如已引入输出契约，`output_manifest.json` 与 `contract_registry.json` 是否仍由受控同步入口生成
- 如已生成正式输出，是否可通过 `scripts/validate_outputs.py` 校验

## 7. 推荐扩展方向

优先扩展：

- 更清晰的输入归一规则
- 更稳定的输出契约
- 更具体的风险与歧义处理
- 更高价值的样例和映射资产
- 更稳定的可复用 workflow 资产

谨慎扩展：

- 与某个仓库强耦合的命令行细节
- 过度依赖局部目录结构的说明
- 尚未稳定的实现策略

## 8. 审阅清单

每次审阅本 Skill，至少确认：

- 这是 SKILL 包，而不是 Product 实现说明
- 是否已明确区分 SKILL、上游项目资产、规范文档与业务输出
- 是否加入了足够的可靠性支撑材料
- 是否只纳入了真正值得复用的精选子集
- 是否仍适合作为可复用应用层交付物

## 9. 维护口径

未来继续扩展本 Skill 时，应坚持：

- skill-first
- package-first
- subset-curated
- reliability-first
