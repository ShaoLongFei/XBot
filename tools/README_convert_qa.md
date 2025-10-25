# 客服问答数据转换工具

将客服问答 JSON 数据转换为 AstrBot 知识库可导入的 Markdown 格式（策略1：整合完整对话）。

## 功能说明

本工具将包含多轮对话的客服工单 JSON 数据转换为完整对话格式，保留问题诊断的完整上下文。

**转换示例：**

输入 JSON 格式：
```json
{
  "id": 397413,
  "title": "SSL证书验证问题",
  "description": "证书验证不通过",
  "category": "对象存储｜其他类咨询",
  "replies": [
    {
      "content": "<p>详细问题描述...</p>",
      "owner": "customer"
    },
    {
      "content": "<p>解决方案...</p>",
      "owner": "agent"
    }
  ]
}
```

输出 Markdown 格式：
```markdown
## SSL证书验证问题

**分类**：对象存储｜其他类咨询

### 问题描述

证书验证不通过

### 对话过程

**客户**：详细问题描述...

**客服**：解决方案...
```

## 使用方法

### 基本用法

```bash
python convert_customer_qa_to_kb.py <输入JSON文件>
```

这将生成一个 `<原文件名>_converted.md` Markdown 文件。

### 指定输出文件和格式

```bash
# 输出为 Markdown 文件（默认）
python convert_customer_qa_to_kb.py customer_qa.json -o converted.md -f md

# 输出为文本文件
python convert_customer_qa_to_kb.py customer_qa.json -o converted.txt -f txt

# 输出为 JSON 文件（包含转换后的文本）
python convert_customer_qa_to_kb.py customer_qa.json -o converted.json -f json
```

### 参数说明

- `input`: （必需）输入 JSON 文件路径
- `-o, --output`: （可选）输出文件路径
- `-f, --format`: （可选）输出格式，可选 `md`、`txt` 或 `json`，默认 `md`

## 输出格式说明

### Markdown 格式（默认推荐）
使用 Markdown 标记，便于阅读和导入知识库：
```markdown
## 问题标题

**分类**：问题分类

### 问题描述

...

### 对话过程

**客户**：...

**客服**：...

---

## 下一个问题标题
...
```

### TXT 格式
每条记录之间用分隔线分隔，适合直接阅读和查看：
```
================================================================================
标题：问题标题
分类：问题分类

问题描述：
...

对话过程：
客户：...
客服：...
================================================================================
```

### JSON 格式
结构化数据，方便进一步处理：
```json
[
  {
    "id": 397413,
    "title": "问题标题",
    "category": "问题分类",
    "content": "## 问题标题\n\n**分类**：...\n\n### 对话过程\n..."
  }
]
```

## 特性

- ✅ 自动清理 HTML 标签
- ✅ 将 `<img>` 标签转换为 `[图片]`
- ✅ 保留完整对话上下文
- ✅ 区分客户和客服发言
- ✅ 支持批量处理
- ✅ 错误处理：单条记录失败不影响其他记录

## 后续步骤

转换完成后，您可以：

1. **查看转换结果**：打开生成的 txt 或 json 文件确认格式正确
2. **导入知识库**：使用转换后的数据导入到 AstrBot 知识库

如需将转换后的数据直接导入 AstrBot 知识库，请参考项目文档中的知识库导入方法。

## 示例

```bash
# 处理客服数据
python convert_customer_qa_to_kb.py /path/to/customer_service_data.json

# 输出结果
📖 读取文件: /path/to/customer_service_data.json
📊 共找到 500 条客服记录
✓ 已处理 100/500 条记录...
✓ 已处理 200/500 条记录...
✓ 已处理 300/500 条记录...
✓ 已处理 400/500 条记录...
✓ 已处理 500/500 条记录...
💾 保存为 Markdown 格式: /path/to/customer_service_data_converted.md

✅ 转换完成！
   成功转换: 500/500 条记录
   输出文件: /path/to/customer_service_data_converted.md
```

## 常见问题

**Q: 如果 JSON 文件很大会怎样？**
A: 脚本会每处理 100 条记录显示一次进度，大文件也能正常处理。

**Q: 如果某条记录转换失败怎么办？**
A: 脚本会跳过失败的记录并继续处理，最后会显示成功转换的数量。

**Q: 转换后如何导入知识库？**
A: 请参考 AstrBot 知识库文档中的批量导入方法。
