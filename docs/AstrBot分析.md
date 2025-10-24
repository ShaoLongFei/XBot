# AstrBot 项目分析

本文档整理了 AstrBot 项目的核心架构和运行环境要求。

## 核心模块结构

### astrbot/core/ 目录

- `initial_loader.py` - 初始化加载器
- `core_lifecycle.py` - 核心生命周期管理
- `db_helper.py` / `db/` - 数据库层
- `log.py` - 日志系统(LogManager, LogBroker)
- `config/` - 配置管理
  - `default.py` - 默认配置和元数据
  - `AstrBotConfig` - 配置类
- `platform/` - 平台适配器
- `provider/` - LLM服务提供商
- `star/` - 插件系统
- `utils/` - 工具类
  - `io.py` - 下载管理面板文件
  - `astrbot_path.py` - 路径管理

### astrbot/dashboard/ 目录

- `server.py` - WebUI服务器(AstrBotDashboard类)
- 前端资源(需要下载或构建)

## 运行时目录结构

项目运行时会自动创建以下目录:

```
data/
├── config/       # 配置文件存储
├── plugins/      # 插件目录
├── temp/         # 临时文件
├── dist/         # WebUI静态文件(自动下载)
└── data_v4.db    # SQLite数据库
```

## 配置文件

### 主配置文件

- `data/cmd_config.json` - 运行时配置(自动生成)

### 配置内容包括

- **平台适配器配置** - 支持多种消息平台(QQ、微信、Telegram、Discord等)
- **LLM服务商配置** - 集成多种AI服务(OpenAI、Claude、Gemini等)
- **Dashboard配置** - Web管理界面设置(默认端口6185)
- **管理员ID** - 机器人管理员权限配置
- **唤醒前缀** - 触发机器人的关键词设置
- **其他功能配置** - 插件、知识库、安全审核等

---

> 本文档提取自 AstrBot 项目分析报告，用于快速了解项目核心架构。
