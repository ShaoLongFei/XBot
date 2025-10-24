# AstrBot 核心模块速查

本文档帮助开发者快速了解 AstrBot 项目的核心架构和关键模块。

## 项目启动流程

```
main.py → InitialLoader → AstrBotCoreLifecycle + AstrBotDashboard
```

1. **InitialLoader** (`astrbot/core/initial_loader.py`) - 启动器，初始化核心生命周期和仪表板
2. **AstrBotCoreLifecycle** (`astrbot/core/core_lifecycle.py`) - 核心生命周期管理，初始化和协调所有组件
3. **AstrBotDashboard** (`astrbot/dashboard/server.py`) - Web 管理界面（基于 Quart，默认端口 6185）

## 核心管理器

### PlatformManager (`astrbot/core/platform/`)
- 管理多平台适配器（QQ、微信、Telegram、Discord 等）
- 接收和分发消息事件到事件队列
- 支持的平台：aiocqhttp、qq_official、telegram、discord、wechatpadpro 等

### ProviderManager (`astrbot/core/provider/`)
- 管理 LLM 服务提供商（OpenAI、Claude、Gemini 等）
- 支持语音转文字（STT）、文字转语音（TTS）
- 提供 Embedding 和 Rerank 能力
- 支持多提供商实例和会话隔离

### PluginManager (`astrbot/core/star/star_manager.py`)
- 插件加载、卸载、热重载
- 插件配置管理和依赖安装
- 插件事件处理和工具注册

### PipelineScheduler (`astrbot/core/pipeline/scheduler.py`)
- 消息处理管道调度器
- 实现洋葱模型：前置处理 → 业务逻辑 → 后置处理
- 管道阶段：白名单检查 → 唤醒检查 → 预处理 → 核心处理 → 结果装饰 → 响应

## 核心模块目录

```
astrbot/
├── core/                    # 核心模块
│   ├── initial_loader.py    # 启动器
│   ├── core_lifecycle.py    # 生命周期管理
│   ├── config/              # 配置管理（AstrBotConfig、default.py）
│   ├── platform/            # 平台适配器
│   ├── provider/            # LLM 提供商
│   ├── star/                # 插件系统
│   ├── pipeline/            # 消息处理管道
│   ├── agent/               # Agent 和工具执行
│   ├── db/                  # 数据库层（SQLite）
│   ├── log.py               # 日志系统（LogManager、LogBroker）
│   └── utils/               # 工具类（路径、下载、命令解析等）
├── dashboard/               # Web 管理界面
│   ├── server.py            # Quart 服务器
│   └── routes/              # API 路由（auth、plugin、config 等）
├── api/                     # 插件开发 API
└── cli/                     # 命令行工具
    └── commands/            # init、run、plug 等命令
```

## 数据存储

```
data/
├── config/                  # 配置文件
│   └── cmd_config.json      # 主配置（自动生成）
├── plugins/                 # 用户插件
├── temp/                    # 临时文件
├── dist/                    # WebUI 静态文件（自动下载）
└── data_v4.db               # SQLite 数据库
```

## 关键配置

### data/cmd_config.json
- `platform`: 平台适配器配置
- `provider`: LLM 服务商配置
- `dashboard_config`: Web 界面设置
- `admins_id`: 管理员 ID 列表
- `wake_prefix`: 唤醒前缀
- `platform_settings.unique_session`: 会话隔离设置

## 消息处理流程

```
平台消息 → 事件队列 → PipelineScheduler → 插件处理 → Provider 生成响应 → 平台发送
```

1. 平台适配器接收消息，封装为 `AstrMessageEvent`
2. 事件进入队列，`PipelineScheduler` 按阶段处理
3. 插件系统匹配并执行相应插件
4. Provider 调用 LLM 生成回复
5. 响应通过平台适配器发送

## 开发入口

- **插件开发**: `astrbot/api/` 提供插件 API，参考 `astrbot/core/star/`
- **平台适配**: 实现 `astrbot/core/platform/platform.py` 的 Platform 接口
- **LLM 提供商**: 实现 `astrbot/core/provider/provider.py` 的 Provider 接口
- **Dashboard 路由**: 在 `astrbot/dashboard/routes/` 添加新路由

## 常用工具类

- `astrbot.core.utils.astrbot_path` - 路径管理
- `astrbot.core.utils.io` - 文件下载和管理
- `astrbot.core.utils.command_parser` - 命令解析
- `astrbot.core.log` - 日志管理
