# TFL Shell 生成器设计

日期：2026-04-27  
主题：TFL shell 生成器的结构、规则与输出边界设计  
状态：历史设计稿，现归属于 `TFLs-Shell Product` 设计资产

## 1. 设计目的

本文档用于说明 Product 层生成器的核心设计目标：

- 生成受控的 TFL shell 结构
- 保持 DOCX、XLSX、SOP 三类输出的一致性
- 让输出适合临床审阅，而不是伪造最终统计结果

## 2. 生成器定位

生成器属于 `TFLs-Shell Product`，不是 `TFLs-Shell SKILL` 本体。

它的作用是：

- 提供正式输出能力
- 提供格式与结构基线
- 为 SKILL 的高保真生成提供参考

## 3. 核心规则

### 3.1 shell-first

表和 listing 的核心是“结构模板”，而不是结果填充样例。

### 3.2 traceability-first

输出中应保留必要的：

- dataset source
- program reference
- dictionary / standard
- footnote context

### 3.3 cross-output-alignment

DOCX、XLSX、SOP 应共享同一套：

- 编号规则
- 标签规则
- applicability 语义
- section 边界

## 4. SOP 结构要求

SOP 主要用于说明模板集如何被治理与使用。

当前建议的章节结构包括：

1. 目的与范围
2. 定义与缩略语
3. 职责
4. 程序
5. 参考资料
6. 附录

SOP 必须描述真实生成器行为，而不是理想化行为。

## 5. 主要生成规则

### 5.1 元数据以 shell 为中心

catalog 应优先定义：

- 该 TFL 是什么
- 它属于哪个 section
- 适用于哪些研究语境
- 其 shell 结构包含什么
- 展示时应带哪些说明与元数据

### 5.2 Word TOC 是主要目录机制

DOCX 应采用 Word 原生 TOC field，而不是手工目录文本。

### 5.3 placeholder 策略遵循 shell 风格

表和 listing 应保持结构示例，同时确保所有结果相关内容仍是非结果性的
placeholder。

### 5.4 internal ID 与 reviewer-facing label 分离

例如：

- 内部：`T14.2.11`
- 展示：`Table 14.2.11`

该区分应在 DOCX、XLSX、SOP 中保持同步。

### 5.5 applicability 必须显式

每个 TFL 应明确属于：

- `General`
- `Oncology only`
- `Non-Oncology only`

### 5.6 figure 保留模拟图

figure 可以保留模拟图像，用于说明目标图形形式，但不得暗示正式结果。

### 5.7 workbook 保持治理导向

workbook 应帮助用户理解：

- TFL 定位
- applicability
- 元数据字段
- DOCX / catalog 的使用方式

它不应默认演化成 staffing 或 workflow tracker。

## 6. 布局与分页

推荐布局规则：

- 每个 TFL 尽量保持单页
- 超大内容允许自然续页
- figure 的标题、图体、注释尽量保持成组
- 避免无必要分页把一个 shell 打散

这是最佳努力目标，不保证所有极端内容都能完全单页。

## 7. 当前实现基线

当前 Product 已具备的能力包括：

- 统一命名与 label 映射
- Word TOC 插入
- DOCX cover page 与 section 生成
- figure shell 的模拟图渲染
- workbook 的治理型结构
- SOP 结构化内容生成

这些能力构成了 `TFLs-Shell Product` 的高保真输出基线。

## 8. 与 SKILL 的关系

`TFLs-Shell SKILL` 不直接等于生成器，但如果希望生成结果尽量接近正式项目
产物，就应尽量参考 Product 生成器的：

- 结构规则
- 标签规则
- 元数据规则
- 布局与格式策略

## 9. 风险提示

- `技术风险`：生成规则与文档脱节会造成输出行为漂移
- `维护风险`：若生成器被误写成 Skill 本体，会再次混淆边界
- `项目风险`：若格式规则缺少稳定基线，外部复用结果会逐渐偏离正式项目输出

## 10. 优化建议

### 10.1 立即可做

- 保持生成器、规范与输出基线同步
- 持续把高价值规则沉淀到 Product 文档中

### 10.2 中长期

- 继续增强分页与 keep-together 行为
- 继续增强 phase / domain 选择逻辑
- 持续为 SKILL 提供更稳定的高保真参考能力
