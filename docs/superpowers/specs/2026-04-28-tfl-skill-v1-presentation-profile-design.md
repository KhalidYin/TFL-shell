# TFL Skill V1 格式契约与 Presentation Profile 设计（中文版）

> 当前术语说明：本文中的格式契约设计，在现行口径下主要归属于
> `TFLs-Shell Product`，用于支撑 `TFLs-Shell SKILL` 产出更接近正式项目
> 格式的结果。

日期：2026-04-28  
主题：TFL Skill V1 中格式策略、版式契约与 DOCX 渲染边界设计  
状态：V1，presentation profile 最小实现已接入主 DOCX 生成链路，供 review

## 1. 文档目的

本文档用于回答一个在 Skill V1 设计中必须尽早明确的问题：

- TFL shell 的版式细节是否应由 Skill 控制
- 如果需要控制，应控制到哪一层
- 哪些排版细节继续留在 generator / renderer 层更合适

这里的“格式细节”包括但不限于：

- 行间距
- 区块之间的隔行或段前距
- 缩进层级
- 表格与脚注间距
- 标题与正文间距
- 表格宽度自适应页面
- 单页优先呈现

本文档不讨论 study-specific 内容生成，而只讨论“内容如何以受控版式落成文档”。

## 2. 核心结论

我建议采用“三层分工”：

- `Skill` 控制格式策略与交付意图
- `Generator` 控制文档级布局编排
- `Renderer` 控制具体 Word 排版参数

也就是说：

- Skill 可以决定“采用哪一种受控版式 profile”
- 但 Skill 不应直接暴露“段前 6pt、段后 1pt、缩进 4 空格”这种微参数

这是为了让 Skill 保持面向用户语义，而不是退化成 Word 微调面板。

## 3. 为什么不能把细节都塞进 Skill

如果把所有版式参数都暴露给 Skill，会出现三个问题：

- Skill 接口会迅速膨胀，后续难以解释和维护
- generator 内部重构时，很容易打破 Skill 的细粒度契约
- 用户会把 Skill 理解为“任意文档排版器”，偏离 TFL 治理目标

因此，Skill 需要控制“策略”，而不是直接控制“每个 Word 参数”。

## 4. 当前仓库中的版式控制现状

当前版式细节已经分散存在于多个实现层。

### 4.1 表格行与区块格式

当前 `three_line_table.py` 已经体现出基础版式逻辑：

- `bold` 行作为区块头时，额外增加段前距
- `indent` 行使用更紧凑的组内 spacing
- 普通行使用标准紧凑 spacing
- 首列通过受控缩进表现层级结构
- 表格整体启用页面宽度自适应

这说明：

- 表格细节控制已经存在
- 但尚未被抽象为统一的 profile 机制

### 4.2 文档标题、脚注与图注格式

当前 `docx_shell.py` 与 `styles.py` 已控制：

- Heading 样式
- 脚注段前段后距
- 图注与图形间距
- 段落 keep-with-next
- 封面和章节标题间距

这说明：

- 文档层布局也已有受控规则
- 但这些规则目前主要通过散落常量和局部代码体现

### 4.3 底层单元格文本格式

当前 `xml_helpers.py` 中 `set_cell_text()` 已控制：

- cell paragraph 的段前段后距
- 固定 line spacing
- 表格单元格字体大小和加粗

这说明底层 renderer 层也已经承担了部分具体排版参数。

## 5. 建议的三层边界

### 5.1 Skill 层

Skill 应负责：

- 识别当前交付场景
- 决定采用何种 presentation profile
- 决定是否偏重审阅、归档或继续编辑
- 将 profile 作为结构化字段传递给 generate 工作流

Skill 不应负责：

- 直接给出每个段前段后的 pt 数值
- 直接决定某个 cell 使用几个空格缩进
- 直接拼接 Word 原生格式控制

### 5.2 Generator 层

Generator 应负责：

- 根据 profile 选择章节级和对象级布局策略
- 决定表、图、listing、脚注各自采用哪组版式子策略
- 把统一策略分发到实际渲染函数

Generator 是“版式编排层”，不是“具体排版参数库”。

### 5.3 Renderer 层

Renderer 应负责：

- 具体段前段后距
- 行距
- 缩进实现
- keep-with-next
- autofit
- border、shading、alignment 等 Word 细节

这一层应尽量以 profile 配置驱动，而不是把数值散落在条件分支中。

## 6. Presentation Profile 的设计目标

首版 profile 设计应满足以下目标：

- 能表达不同交付场景
- 不暴露过细参数
- 能稳定映射到当前 generator / renderer
- 后续可兼容 MCP

首版不追求覆盖所有排版风格，而只覆盖当前 TFL shell 项目真正需要的三种主要使用场景。

## 7. V1 建议支持的三个 Profile

### 7.1 `csr_standard`

用途：

- 作为默认正式 shell 交付样式

适用场景：

- 主 DOCX 模板输出
- 常规审阅与治理留档

期望效果：

- 标题、表格、脚注之间层次清晰
- 区块头与子项有稳定间隔
- 缩进清楚但不过度压缩
- 表格尽量在页面内自然适配

### 7.2 `compact_review`

用途：

- 作为快速审阅或对比阅读样式

适用场景：

- 需要在单页内尽量容纳更多 shell 结构信息
- 强调紧凑阅读而不是正式交付

期望效果：

- 行距更紧凑
- 区块间距收缩
- 图注和脚注更节省空间
- 仍保留层级和可读性

### 7.3 `authoring_shell`

用途：

- 作为后续 study-specific 编辑与衍生模板的工作样式

适用场景：

- 内容仍会被继续编辑
- 需要更清晰的区块分层和人工修改空间

期望效果：

- 标题与区块之间留白更明显
- 缩进和分组更突出
- 脚注与说明更容易被编辑者识别

## 8. V1 建议暴露给 Skill 的格式字段

首版 Skill 不建议暴露大量格式参数，只建议暴露少量受控字段。

### 8.1 `presentation_profile`

建议枚举：

- `csr_standard`
- `compact_review`
- `authoring_shell`

作用：

- 决定整体文档的版式基线

### 8.2 `table_layout_policy`

建议枚举：

- `grouped_standard`
- `grouped_compact`
- `flat_compact`

作用：

- 控制区块头、子项、缩进和行间距策略

### 8.3 `listing_layout_policy`

建议枚举：

- `traceability_standard`
- `compact_listing`

作用：

- 控制 listing 的层级和留白密度

### 8.4 `footnote_layout_policy`

建议枚举：

- `standard_footnote`
- `compact_footnote`

作用：

- 控制脚注段前段后距和连续脚注呈现方式

## 9. V1 不建议暴露给 Skill 的细粒度参数

以下参数不应直接出现在 Skill 输入中：

- `space_before_pt`
- `space_after_pt`
- `line_spacing_pt`
- `left_indent_pt`
- `first_line_indent_pt`
- `table_width_pct`
- `footnote_spacing_pt`

这些参数应在 generator / renderer 内由 profile 统一映射。

## 10. Profile 到实现层的映射建议

建议增加一层轻量“格式契约对象”，由 generator 读取。

### 10.1 Skill 输出层

Skill 只产出：

- `presentation_profile`
- 可选的对象级 layout policy

### 10.2 Generator 映射层

Generator 负责把 profile 映射为：

- heading spacing 策略
- table row spacing 策略
- listing spacing 策略
- footnote spacing 策略
- figure caption spacing 策略

### 10.3 Renderer 执行层

Renderer 再把这些策略转成实际参数：

- `space_before`
- `space_after`
- `line_spacing`
- `keep_with_next`
- `autofit`
- `indent implementation`

## 11. 建议新增的格式契约对象

建议未来在实现层引入类似如下的受控对象：

- `PresentationProfileConfig`
- `TableLayoutConfig`
- `ListingLayoutConfig`
- `FootnoteLayoutConfig`

这些对象用于：

- 集中管理格式策略
- 减少散落的 magic numbers
- 让 Skill generate 更容易解释“为什么这样排版”

## 12. 表格细节的建议控制方式

你提到的三个重点都应纳入受控格式策略：

### 12.1 行间距

建议由 `table_layout_policy` 控制，而不是让 Skill 输入具体 pt。

### 12.2 区块之间隔行或段前距

建议由“区块头行策略”控制：

- `grouped_standard` 下区块头有更明显分隔
- `grouped_compact` 下分隔保留但收缩

### 12.3 缩进

建议保留为受控层级语义：

- 是否缩进
- 哪类行应缩进

而不要让 Skill 直接指定缩进宽度。

## 13. Figure 和 Listing 的位置

虽然当前问题主要来自 table shell，但首版 profile 不应只覆盖 table。

至少还应考虑：

- figure caption spacing
- listing subject-structure indentation
- 脚注和 source listing 引用的留白

否则同一 profile 会只在 table 看起来统一，而文档整体仍不协调。

## 14. Skill V1 中的推荐边界

在 Skill V1 中，格式策略建议作为可选输入，而不是强制输入。

推荐顺序应是：

1. 如果用户明确说明交付意图，则尊重指定 profile
2. 如果用户未说明，则默认使用 `csr_standard`
3. 只有在明确强调紧凑审阅或继续编辑时，才切换到其他 profile

这样可以避免首版接口过重。

## 15. 对 `recommend -> generate` 的影响

在继续实现 `generate` 之前，最好先把 profile 作为 generate 的正式输入之一。

建议 `generate` 阶段至少支持：

- `presentation_profile`
- `include_figures`
- `include_listings`

这样生成结果就不只是“生成了什么”，而是“以什么受控格式生成”。

## 16. 对 MCP 化的意义

如果未来做 MCP，profile 也是非常适合暴露的输入层，而微参数不是。

MCP 更适合暴露：

- `presentation_profile`
- `layout_policy`
- `generate_mode`

不适合暴露：

- Word 级 paragraph micro-tuning 参数

这会让接口更稳定，也更符合产品化边界。

## 17. 建议的实施顺序

建议按以下顺序推进：

### 17.1 第一步

先补格式契约对象和三个受控 profile 的设计实现。

### 17.2 第二步

把当前 `docx_shell.py`、`three_line_table.py`、`xml_helpers.py` 中散落的 spacing / indent / autofit 规则收敛到 profile 驱动。

### 17.3 第三步

再把 `presentation_profile` 正式接入 Skill generate 输入。

这样可以避免在 generate 已经对外暴露后，再回头改接口。

## 18. 总体判断

关于你提出的问题，我的结论是：

- `需要控制`
- `但不应该直接由 Skill 控制到微参数`
- `应由 Skill 管格式策略，由 generator / renderer 落具体实现`

这是当前最稳的边界。

## 19. 风险提示

- 技术风险：如果继续让 spacing、indent、autofit 等规则散落在多个文件中，后续 Skill generate 的格式行为会难以解释和复用。
- 维护风险：如果把每个 Word 微参数都开放给 Skill，接口会迅速膨胀且难以稳定。
- 项目风险：临床统计与监管审阅对文档呈现较敏感，若格式策略不受控，生成结果即使内容正确，也可能显得不专业或不一致。

## 20. 优化建议

### 20.1 立即可做

- 保持当前 `presentation_profile` 最小实现只覆盖主 DOCX 生成链路
- 以 `csr_standard` 作为默认 profile
- 保持 Skill 不直接暴露微参数

### 20.2 中长期

- 为 table、figure、listing、footnote 建立统一的 profile 映射对象
- 逐步减少散落在 renderer 中的 magic numbers
- 将格式契约纳入 Skill 与未来 MCP 的共享 schema

### 20.3 工具链

- 增加结构化版式测试，验证 profile 是否正确映射到表格 spacing、缩进和 autofit
- 为不同 profile 准备代表性生成 fixture
- 在 CI 中加入 profile 级回归检查
