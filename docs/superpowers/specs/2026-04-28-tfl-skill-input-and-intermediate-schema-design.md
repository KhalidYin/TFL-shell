# TFL Skill V1 输入与中间状态 Schema 设计（中文版）

> 当前术语说明：本文中的 `Skill` 输入与中间状态 schema，在现行口径下主要
> 服务于 `TFLs-Shell Product` 的实现与对齐；正式可复用交付物请以
> `.trae/skills/tfls-shell/` 下的 `TFLs-Shell SKILL` 为准。

日期：2026-04-28\
主题：面向 TFL mock shell 生成与治理审阅的 Skill V1 输入、处理中间状态与输出 schema\
状态：V1，供 review

## 1. 文档目的

本文档用于补充 `TFL Mock Shell 生成规范与产品化设计（中文版 V1）`，聚焦定义后续 TFL Skill 的三类核心契约：

- 输入 schema：Skill 如何接收用户材料、上下文和偏好
- 中间状态 schema：Skill 如何在解析、映射、推荐和生成过程中保留可解释状态
- 输出 schema：Skill 最终如何返回推荐、生成结果、风险和验证信息

本文档的目标不是定义最终代码接口，而是先建立一个对人类用户友好、对后续 MCP 兼容、对治理规则可追溯的 V1 数据模型。

## 2. 设计目标

Skill V1 的 schema 设计应满足以下目标：

- 支持非结构化输入优先，而不是要求用户先整理成固定字段
- 能同时容纳 protocol、SAP、文章、统计需求清单和临时说明
- 中间过程必须可解释，便于 review 和后续审计
- 与当前 catalog 元数据规则对齐
- 后续可向 MCP 的结构化 tool 参数平滑收敛

## 3. 设计原则

### 3.1 输入以业务材料为中心

用户在真实工作中通常不会先给出干净的 JSON 参数，而更可能给出：

- protocol 或方案段落
- SAP 或统计分析计划
- 文章中的 endpoint / method 描述
- 统计需求列表
- study-specific 的补充说明

因此，Skill V1 必须先支持“材料驱动输入”，而不是只支持“字段驱动输入”。

### 3.2 中间状态必须可解释

Skill 不能只返回结果，还必须能解释：

- 它从哪些材料里提取了哪些关键信息
- 哪些字段是直接给出的，哪些是推断的
- 哪些推荐是基础必选，哪些是可选扩展
- 哪些结论带有不确定性或依赖假设

### 3.3 治理字段与推断字段分层

Skill 的处理中，必须区分两类字段：

- 治理字段：对应当前项目的受控字段，如 `Section`、`Applicability`、`Shell Family`
- 推断字段：从自由材料中抽出的研究语义，如 `indication`、`primary endpoint intent`

二者不能混成一个自由文本对象，否则后续验证和产品化都会失控。

### 3.4 先适配 Skill，再兼容 MCP

Skill V1 的 schema 首先面向人类协作体验，但字段命名和边界应尽量结构化，以便后续迁移到 MCP tool 参数时无需整体推翻。

## 4. Skill 工作流总览

建议将 Skill V1 拆为六个逻辑阶段：

1. 输入接收
2. 内容抽取
3. 语义归一化
4. shell 映射与推荐
5. 生成与校验计划
6. 结果输出

每个阶段都应产生一个可追踪的中间状态对象，而不是只在内存里隐式流转。

## 5. 输入 Schema V1

### 5.1 顶层输入对象

建议 Skill V1 使用如下顶层输入对象：

```json
{
  "request_id": "optional-string",
  "task_mode": "generate|review|recommend|compare|extend",
  "input_bundle": {},
  "execution_preferences": {},
  "user_overrides": {}
}
```

### 5.2 `task_mode`

建议支持以下任务模式：

- `generate`：直接生成 DOCX / XLSX / SOP 或其子集
- `review`：审阅已有 shell 方案、输入材料或治理匹配度
- `recommend`：推荐适用 shell family 或 TFL 包
- `compare`：比较两个方案、两套输入材料或两组 shell 选择策略
- `extend`：在现有基础上建议应增加的 shell 或治理补充

V1 版本不建议支持过多模式；上述五种已覆盖大多数高价值场景。

### 5.3 `input_bundle`

`input_bundle` 用于承载用户给出的所有输入材料。建议结构如下：

```json
{
  "sources": [
    {
      "source_id": "src-001",
      "source_type": "user_prompt|protocol|sap|article|stat_request|study_note",
      "title": "optional",
      "content_text": "raw text if available",
      "file_path": "optional local path",
      "language": "zh|en|mixed",
      "priority": "primary|secondary",
      "notes": "optional"
    }
  ]
}
```

### 5.4 `source_type` 受控枚举

建议 V1 受控支持以下类型：

- `user_prompt`
- `protocol`
- `sap`
- `article`
- `stat_request`
- `study_note`

后续如需要支持 `email`、`meeting_note`、`csr_excerpt`，应在 V2 以后扩展。

### 5.5 输入最小要求

Skill V1 的最小输入要求建议非常宽松，只需满足以下之一：

- 至少一条 `sources`
- 或者显式提供一组结构化偏好参数

Skill 不应要求用户同时提交 protocol、SAP 和统计需求；这些应视为增强信息，而非强制前置条件。

### 5.6 `execution_preferences`

`execution_preferences` 用于定义本轮运行偏好，而不是研究本身的业务事实。建议包括：

```json
{
  "desired_outputs": ["docx_shell", "xlsx_toc", "docx_sop"],
  "section_scope": ["14.1", "14.2", "14.3", "14.4", "16.2"],
  "therapeutic_area_hint": "oncology|non-oncology|all|unknown",
  "study_phase_hint": "phase-i|phase-ii|phase-iii|mixed|unknown",
  "include_figures": true,
  "include_listings": true,
  "run_validation": true,
  "output_dir": "optional-path"
}
```

### 5.7 `user_overrides`

`user_overrides` 用于处理“用户明确指定”的条件，优先级应高于自动推断。建议包括：

```json
{
  "sponsor": "optional",
  "protocol_id": "optional",
  "force_sections": ["optional"],
  "exclude_sections": ["optional"],
  "force_shell_ids": ["optional"],
  "exclude_shell_ids": ["optional"],
  "naming_style": "group-1-style",
  "notes": "optional"
}
```

V1 不建议支持任意自由格式的结构改写，例如直接覆写表头列结构。

## 6. 中间状态 Schema V1

Skill V1 的核心价值在于“把复杂输入材料转成治理可解释的推荐过程”。建议保留以下五类中间状态。

### 6.1 `ingestion_state`

用于记录输入接收和初步解析结果。

```json
{
  "recognized_sources": [
    {
      "source_id": "src-001",
      "source_type": "sap",
      "usable": true,
      "language": "en",
      "has_structured_signal": true,
      "issues": []
    }
  ],
  "unreadable_sources": [],
  "input_warnings": []
}
```

主要作用：

- 记录哪些材料成功读取
- 记录哪些材料格式不清或信息不足
- 避免 Skill 直接跳到推荐阶段而不说明输入质量

### 6.2 `extraction_state`

用于记录从材料中抽出的业务语义。建议字段如下：

```json
{
  "study_context": {
    "study_phase": "Phase II",
    "therapeutic_area": "Non-Oncology",
    "indication": "example",
    "development_intent": "confirmatory|exploratory|dose-escalation|unknown"
  },
  "analysis_context": {
    "primary_endpoints": ["example"],
    "secondary_endpoints": ["example"],
    "analysis_populations": ["Safety Population", "FAS"],
    "key_time_to_event": true,
    "key_responder": false,
    "key_safety_focus": ["AE", "labs", "ECG"]
  },
  "traceability_context": {
    "expects_patient_listings": true,
    "expects_program_refs": true,
    "expects_dictionary_traceability": true
  }
}
```

这些字段不是要求每次都提满，而是为后续映射提供结构化容器。

### 6.3 `normalization_state`

用于记录如何把自由文本语义映射到当前项目的治理字段。

```json
{
  "mapped_governance_fields": {
    "section_scope": ["14.1", "14.2", "14.3", "16.2"],
    "applicability_hint": "Non-Oncology only",
    "shell_family_candidates": [
      "General Efficacy",
      "Non-Oncology Efficacy",
      "Safety"
    ],
    "study_phase_scope_hint": "Phase II-III"
  },
  "mapping_rationale": [
    "Primary endpoint implies efficacy package",
    "Non-oncology language suggests domain-specific efficacy families",
    "Safety review remains core"
  ]
}
```

这一层是 Skill 与 MCP 后续复用的关键，因为它已经从自由输入转换到治理语言。

### 6.4 `ambiguity_state`

用于显式记录不确定性和冲突，避免 Skill 假装自己知道所有答案。

```json
{
  "missing_fields": ["study_phase"],
  "conflicts": [
    {
      "field": "therapeutic_area",
      "source_a": "protocol",
      "value_a": "oncology-like endpoint language",
      "source_b": "user_prompt",
      "value_b": "non-oncology"
    }
  ],
  "assumptions": [
    "Treat study as Phase II-III unless user overrides"
  ],
  "needs_user_confirmation": false
}
```

V1 中，Skill 可以在低风险情况下带着假设继续，但必须把假设说清楚。

### 6.5 `recommendation_state`

用于记录推荐包、可选扩展和排除项。

```json
{
  "base_package": {
    "sections": ["14.1", "14.2", "14.3", "16.2"],
    "shell_ids": ["T14.1.1", "T14.2.1"],
    "shell_families": ["Demographics and Baseline", "Safety"]
  },
  "optional_expansions": [
    {
      "family": "Non-Oncology Efficacy",
      "reason": "time-to-event endpoint detected"
    }
  ],
  "excluded_items": [
    {
      "target": "14.4",
      "reason": "no clear special-assessment signal in inputs"
    }
  ],
  "governance_warnings": [
    "source listing specificity should be reviewed for selected efficacy shells"
  ],
  "gap_notes": []
}
```

### 6.6 `generation_plan_state`

用于描述本轮是否进入正式生成，以及生成什么。

```json
{
  "should_generate": true,
  "planned_outputs": ["docx_shell", "xlsx_toc", "docx_sop"],
  "filters": {
    "therapeutic_area": "non-oncology",
    "section_scope": ["14.1", "14.2", "14.3", "16.2"]
  },
  "overrides": {
    "sponsor": "optional",
    "protocol_id": "optional"
  },
  "validation_plan": {
    "run_catalog_validation": true,
    "run_cross_output_checks": true
  }
}
```

## 7. 输出 Schema V1

建议 Skill V1 的顶层输出结构如下：

```json
{
  "request_summary": {},
  "interpreted_context": {},
  "recommendations": {},
  "generation_results": {},
  "validation_results": {},
  "risk_notes": [],
  "optimization_suggestions": {}
}
```

### 7.1 `request_summary`

用于说明本轮 Skill 实际理解到的任务，例如：

- 用户给了哪些来源
- 当前任务模式是什么
- 是偏生成、偏审阅，还是偏推荐

### 7.2 `interpreted_context`

用于返回 Skill 对研究语境的理解，例如：

- 研究阶段
- 治疗领域
- endpoint 类型
- analysis population
- 是否倾向保留 figures 或 listings

### 7.3 `recommendations`

建议包括：

- 推荐 sections
- 推荐 shell families
- 可选扩展
- 排除建议
- 理由摘要

### 7.4 `generation_results`

如进入生成阶段，应返回：

- 是否实际生成
- 产物路径
- 文件名
- 使用的过滤条件
- 版本信息

### 7.5 `validation_results`

建议返回：

- catalog validation 结果
- cross-output consistency 结果
- rule violations
- warnings

### 7.6 `risk_notes`

必须保留：

- 假设带来的风险
- 输入材料不全带来的风险
- traceability 或 coverage 可能不完整的风险

### 7.7 `optimization_suggestions`

建议拆分为：

- 立即可做
- 中长期
- 工具链

这样与当前项目文档中的风险提示和优化建议格式保持一致。

## 8. 与当前项目对象的映射关系

Skill V1 schema 不应重新发明一套对象，而应尽量映射到当前仓库对象。

### 8.1 与 `TFLItem` 的映射

当前 `TFLItem` 已覆盖以下核心治理字段：

- `id`
- `title`
- `tfl_type`
- `section`
- `population`
- `dataset_source`
- `program_ref`
- `source_listing`
- `placeholder_style`
- `shell_family`
- `study_phase_scope`
- `coverage_summary`
- `shell_rows`
- `placeholder_columns`

因此，Skill 输出中的推荐 shell 和生成计划最终都应落到 `TFLItem` 或 `TFLCatalog` 可表达的范围内。

### 8.2 与 `TFLCatalog` 的映射

当前 `TFLCatalog` 已具备：

- `all`
- `by_section`
- `by_type`
- `by_therapeutic_area`
- `get`
- `summary_stats`
- `section_summary`
- `validate`

因此，Skill V1 的推荐层和校验层，优先应复用 catalog 现有能力，而不是另起一套平行逻辑。

## 9. MCP 兼容性设计

为了后续迁移到 MCP，建议 Skill schema 在命名上尽量向结构化参数靠拢，但保留 Skill 所需的非结构化输入容器。

### 9.1 适合迁移到 MCP 的字段

- `task_mode`
- `section_scope`
- `therapeutic_area_hint`
- `study_phase_hint`
- `desired_outputs`
- `run_validation`
- `output_dir`
- `force_shell_ids`
- `exclude_shell_ids`

### 9.2 暂不适合直接迁移到 MCP 的字段

- 大段自由文本材料本体
- 未清洗的 article 或 protocol 原文
- 仅用于对话解释的自然语言中间备注

这些内容更适合作为 Skill 的上层输入，再由 Skill 清洗后调用 MCP。

## 10. V1 示例

### 10.1 示例一：用户提供 SAP 片段并要求生成基础包

```json
{
  "task_mode": "generate",
  "input_bundle": {
    "sources": [
      {
        "source_id": "src-001",
        "source_type": "sap",
        "title": "SAP excerpt",
        "content_text": "Primary endpoint is time to first exacerbation..."
      }
    ]
  },
  "execution_preferences": {
    "desired_outputs": ["docx_shell", "xlsx_toc"],
    "therapeutic_area_hint": "non-oncology",
    "run_validation": true
  },
  "user_overrides": {
    "naming_style": "group-1-style"
  }
}
```

### 10.2 示例二：用户给出文章和统计需求，先做推荐不生成

```json
{
  "task_mode": "recommend",
  "input_bundle": {
    "sources": [
      {
        "source_id": "src-001",
        "source_type": "article",
        "content_text": "Kaplan-Meier analysis of progression-free survival..."
      },
      {
        "source_id": "src-002",
        "source_type": "stat_request",
        "content_text": "Need baseline package, primary efficacy tables, forest plot, and traceable listings."
      }
    ]
  },
  "execution_preferences": {
    "desired_outputs": [],
    "run_validation": false
  }
}
```

## 11. V1 明确不做的内容

以下内容不建议纳入 Skill V1 schema：

- 任意自定义表格列结构编辑
- 任意改写受控命名标准
- 用户直接上传所有原始 Office 文件并要求 Skill 在 V1 全自动反向抽取复杂结构
- 基于自由文本自动输出最终监管级 study-specific 结论

V1 应专注于“受控推荐 + 受控生成 + 可解释中间状态”，而不是追求全能。

## 12. 风险提示

- 技术风险：如果中间状态定义不清，后续 Skill 实现会把关键信息藏在 prompt 或临时变量里，难以测试和复用。
- 维护风险：如果治理字段与推断字段混用，后续很难判断某条推荐是规则要求还是模型推断。
- 项目风险：如果 V1 试图支持过多自由编辑能力，容易破坏当前 TFL 库的治理边界。

## 13. 优化建议

### 13.1 立即可做

- 以本文档为基础，进一步确定 `task_mode` 和 `input_bundle` 的最小实现集合
- 在主设计稿中补充对本 schema 文档的引用
- 以 `docs/superpowers/specs/2026-04-28-tfl-skill-v1-workflow-and-minimum-implementation-plan.md` 作为后续实现顺序和最小闭环的执行基线
- 以 `docs/superpowers/specs/2026-04-28-tfl-skill-v1-recommend-slice-design.md` 作为首个可落地切片的具体实现参考
- 以 `docs/superpowers/specs/2026-04-28-tfl-skill-v1-presentation-profile-design.md` 作为 generate 阶段格式字段和版式契约的设计参考
- 后续实现时先把 `ingestion_state`、`extraction_state`、`recommendation_state` 三层做出来

### 13.2 中长期

- 将 `study_context` 与 `analysis_context` 进一步标准化
- 为 endpoint intent、analysis class、regulatory criticality 增加受控枚举
- 将 traceability 关系提升为更稳定的对象模型

### 13.3 工具链

- 为 Skill 增加 schema-level contract tests
- 为中间状态对象增加样例 fixture
- 在 Skill 和未来 MCP 间建立共享 schema 校验层
