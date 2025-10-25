# XBot
七牛云1024节参赛项目

## 宗旨
在有限时间内交付最有价值的成果

## 快速开始

### 一键安装（推荐）

XBot 提供了一键安装脚本，支持 Linux 和 macOS 系统，无需手动配置环境。

```bash
curl -fsSL https://raw.githubusercontent.com/ShaoLongFei/XBot/main/install.sh | bash
```

或者下载后执行：

```bash
wget https://raw.githubusercontent.com/ShaoLongFei/XBot/main/install.sh
chmod +x install.sh
./install.sh
```

安装脚本会自动完成以下操作：
- 检测并安装 Git（如未安装）
- 检测并安装 Python 3.10+（如未安装）
- 克隆项目代码
- 创建 Python 虚拟环境
- 安装 Python 依赖
- 自动安装 Dashboard 前端依赖（如果存在）
- 创建必要的数据目录

### 运行项目

```bash
cd XBot
source venv/bin/activate
python main.py
```

首次运行会自动下载管理面板文件，请确保网络连接正常。

### 配置说明

项目配置文件位于 `data/config/cmd_config.json`，首次运行会自动生成。主要配置项包括：

- `platform`: 平台适配器配置（QQ、微信、Telegram 等）
- `provider`: LLM 服务商配置（OpenAI、Claude、Gemini 等）
- `dashboard_config`: Web 管理界面设置
- `admins_id`: 管理员 ID 列表
- `wake_prefix`: 唤醒前缀

详细配置说明请参考 [CLAUDE.md](CLAUDE.md)。
