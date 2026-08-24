# DOCX Shell 契约

## 1. 输出

Product 对齐的 DOCX shell template 输出为：

- `TFL_Shell_Template_v<version>.docx`

它是 master shell template，不是最终统计结果包。

## 2. 页面设置

主 shell template 使用：

- one Word section
- landscape letter page setup
- page width: `11.0` inches
- page height: `8.5` inches
- margins: `0.75` inches

## 3. 必需前置内容

文档必须包含：

- cover page
- Word-native Table of Contents field
- Introduction and Usage Notes
- table/listing shell convention text
- figure shell explanation

## 4. Heading 契约

shell 文档必须使用：

- `Heading 1` for `Table of Contents` and `1.0  Introduction and Usage Notes`
- `Heading 2` for usage-note subsections and top-level governed sections
- `Heading 3` for TFL type groups or 14.3 safety sub-sections
- `Heading 4` for each TFL shell heading

每个 TFL shell heading 必须为：

`<Display Label>  <Title>`

## 5. Header Block 契约

每个 shell 必须包含 header block，其中包括：

- sponsor 与右对齐的 `Page X of Y`（同一行）
- protocol
- study title / compound name
- 一个合并的粗体 `<Display Label>  <Title>` Heading 4
- analysis set

不得再生成独立的 display-label 行或重复 title 行。验证 helper 会检查合并 Heading 4、无重复标题、`Analysis Set` 顺序，以及每个 shell 的 Sponsor/Page、Protocol 和 study-title 行。

## 6. Body 契约

Tables 与 listings 渲染为 Word tables。

Figures 在启用生成时渲染为模拟 shell 图示，否则使用 figure placeholder fallback。

Footnotes 在可用时包含 source listing 与 dataset/program traceability。缩写、统计定义和 coding/grading version 按 `table_layout_contract.md` 去重并受控生成；listing 本身不显示 `Source Listing:` 自引用。
