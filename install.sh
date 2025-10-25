#!/bin/bash

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

REPO_SSH_URL="git@github.com:ShaoLongFei/XBot.git"
PROJECT_DIR="XBot"
PYTHON_MIN_VERSION="3.10"

print_message() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

check_command() {
    if command -v "$1" &> /dev/null; then
        return 0
    else
        return 1
    fi
}

detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
        if check_command apt-get; then
            PKG_MANAGER="apt-get"
        elif check_command yum; then
            PKG_MANAGER="yum"
        elif check_command dnf; then
            PKG_MANAGER="dnf"
        elif check_command pacman; then
            PKG_MANAGER="pacman"
        else
            print_message "$RED" "错误: 无法检测到支持的包管理器"
            exit 1
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="mac"
        PKG_MANAGER="brew"
    else
        print_message "$RED" "错误: 不支持的操作系统 $OSTYPE"
        exit 1
    fi
    print_message "$GREEN" "检测到操作系统: $OS"
}

check_python_version() {
    if ! check_command python3; then
        print_message "$RED" "错误: 未找到 Python3"
        return 1
    fi
    
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [ "$PYTHON_MAJOR" -lt 3 ] || { [ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 10 ]; }; then
        print_message "$RED" "错误: 需要 Python $PYTHON_MIN_VERSION 或更高版本，当前版本: $PYTHON_VERSION"
        return 1
    fi
    
    print_message "$GREEN" "Python 版本检查通过: $PYTHON_VERSION"
    return 0
}

install_python() {
    print_message "$BLUE" "正在安装 Python3..."
    
    case $PKG_MANAGER in
        apt-get)
            sudo apt-get update
            sudo apt-get install -y python3 python3-pip python3-venv
            ;;
        yum)
            sudo yum install -y python3 python3-pip
            ;;
        dnf)
            sudo dnf install -y python3 python3-pip
            ;;
        pacman)
            sudo pacman -S --noconfirm python python-pip
            ;;
        brew)
            brew install python@3.11
            ;;
    esac
}

install_git() {
    print_message "$BLUE" "正在安装 Git..."
    
    case $PKG_MANAGER in
        apt-get)
            sudo apt-get update
            sudo apt-get install -y git
            ;;
        yum)
            sudo yum install -y git
            ;;
        dnf)
            sudo dnf install -y git
            ;;
        pacman)
            sudo pacman -S --noconfirm git
            ;;
        brew)
            brew install git
            ;;
    esac
}

clone_repository() {
    if [ -d "$PROJECT_DIR" ]; then
        print_message "$YELLOW" "目录 $PROJECT_DIR 已存在，跳过克隆..."
        cd "$PROJECT_DIR"
        git pull origin main || print_message "$YELLOW" "警告: 更新失败，使用现有代码"
    else
        print_message "$BLUE" "正在克隆项目..."
        git clone "$REPO_SSH_URL" "$PROJECT_DIR"
        cd "$PROJECT_DIR"
    fi
}

setup_python_environment() {
    print_message "$BLUE" "正在设置 Python 虚拟环境..."
    
    if ! check_command uv; then
        print_message "$YELLOW" "未检测到 uv，正在安装..."
        curl -LsSf https://astral.sh/uv/install.sh | sh
        export PATH="$HOME/.local/bin:$PATH"
        
        if ! check_command uv; then
            print_message "$RED" "uv 安装失败"
            exit 1
        fi
        print_message "$GREEN" "uv 安装成功"
    else
        print_message "$GREEN" "uv 已安装"
    fi
    
    if [ ! -d ".venv" ]; then
        uv venv --python $PYTHON_MIN_VERSION
        print_message "$GREEN" "虚拟环境创建成功"
    else
        print_message "$YELLOW" "虚拟环境已存在"
    fi
    
    print_message "$BLUE" "同步项目依赖..."
    uv sync
    
    print_message "$GREEN" "Python 依赖安装完成"
}

install_dashboard_dependencies() {
    print_message "$BLUE" "检查是否需要安装 Dashboard 依赖..."
    
    if [ -f "dashboard/package.json" ]; then
        print_message "$BLUE" "检测到 Dashboard，自动安装前端依赖..."
        if ! check_command node; then
            print_message "$YELLOW" "未检测到 Node.js，正在安装..."
            case $PKG_MANAGER in
                apt-get)
                    curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
                    sudo apt-get install -y nodejs
                    ;;
                yum|dnf)
                    curl -fsSL https://rpm.nodesource.com/setup_lts.x | sudo bash -
                    sudo $PKG_MANAGER install -y nodejs
                    ;;
                pacman)
                    sudo pacman -S --noconfirm nodejs npm
                    ;;
                brew)
                    brew install node
                    ;;
            esac
        fi
        
        cd dashboard
        npm install
        cd ..
        print_message "$GREEN" "Dashboard 依赖安装完成"
    fi
}

create_directories() {
    print_message "$BLUE" "创建必要的目录..."
    mkdir -p data/config
    mkdir -p data/plugins
    mkdir -p data/temp
    print_message "$GREEN" "目录创建完成"
}

print_success() {
    echo ""
    print_message "$GREEN" "=========================================="
    print_message "$GREEN" "        XBot 安装成功！"
    print_message "$GREEN" "=========================================="
    echo ""
    print_message "$BLUE" "运行项目: cd $PROJECT_DIR && source .venv/bin/activate && python main.py"
    echo ""
}

main() {
    print_message "$BLUE" "=========================================="
    print_message "$BLUE" "     XBot 一键安装脚本"
    print_message "$BLUE" "=========================================="
    echo ""
    
    detect_os
    
    if ! check_command git; then
        print_message "$YELLOW" "未检测到 Git，正在安装..."
        install_git
    else
        print_message "$GREEN" "Git 已安装"
    fi
    
    if ! check_python_version; then
        print_message "$YELLOW" "正在安装 Python..."
        install_python
        if ! check_python_version; then
            print_message "$RED" "Python 安装或版本检查失败"
            exit 1
        fi
    fi
    
    CURRENT_DIR=$(pwd)
    clone_repository
    create_directories
    setup_python_environment
    install_dashboard_dependencies
    
    cd "$CURRENT_DIR/$PROJECT_DIR"
    print_success
}

main "$@"
