# Complete Setup Guide | 完整安装指南

**English** | [中文](#中文指南)

---

## 📖 Table of Contents | 目录

### English
- [What is cursor-free-vip?](#what-is-cursor-free-vip)
- [Features](#features)
- [Python Installation](#python-installation)
- [Project Setup](#project-setup)
- [How to Use](#how-to-use)
- [Features Explained](#features-explained)
- [Troubleshooting](#troubleshooting)
- [Can I Use Cursor Unlimited?](#can-i-use-cursor-unlimited)

### 中文
- [什么是 cursor-free-vip？](#什么是-cursor-free-vip)
- [功能特性](#功能特性)
- [Python 安装](#python-安装)
- [项目设置](#项目设置)
- [如何使用](#如何使用)
- [功能详解](#功能详解)
- [故障排除](#故障排除)
- [我可以无限制使用 Cursor 吗？](#我可以无限制使用-cursor-吗)

---

# English Guide

## What is cursor-free-vip?

**cursor-free-vip** is an educational open-source tool designed to help you manage and optimize your Cursor AI editor experience. It provides various utilities to:

- ✅ Bypass token limits
- ✅ Manage machine IDs
- ✅ Disable auto-updates
- ✅ Register with multiple email providers
- ✅ Reset Cursor settings completely

> ⚠️ **Educational Purpose Only**: This tool is for learning and understanding how software systems work. Please support the official Cursor Pro subscription if you use Cursor professionally.

---

## Features

### 🎯 Main Features

1. **Automatic Path Detection** (NEW!)
   - No manual configuration needed
   - Works on any machine with Cursor installed
   - Supports Windows, macOS, and Linux

2. **Bypass Token Limit**
   - Modify Cursor to remove token restrictions
   - Automatic backup before modifications
   - Works across different Cursor versions

3. **Machine ID Reset**
   - Generate new machine IDs
   - Reset telemetry data
   - Support for multiple resets

4. **Auto-Update Control**
   - Disable Cursor auto-updates
   - Prevent unwanted version changes
   - Lock update configuration files

5. **Multi-Language Support**
   - 15+ languages supported
   - Easy language switching
   - Complete UI translations

---

## Python Installation

### Windows

#### Method 1: Official Python Installer (Recommended)

1. **Download Python**
   - Go to https://www.python.org/downloads/
   - Download Python 3.8 or higher (3.10+ recommended)
   - Click "Download Python 3.x.x"

2. **Install Python**
   ```
   ✅ Check "Add Python to PATH" (VERY IMPORTANT!)
   ✅ Check "Install pip"
   Click "Install Now"
   ```

3. **Verify Installation**
   ```powershell
   # Open PowerShell and run:
   python --version
   pip --version
   ```

#### Method 2: Microsoft Store

1. Open Microsoft Store
2. Search "Python 3.12" or "Python 3.11"
3. Click "Get" or "Install"
4. Verify: `python --version`

### macOS

#### Method 1: Official Installer

1. Download from https://www.python.org/downloads/macos/
2. Open the `.pkg` file
3. Follow installation wizard
4. Verify: `python3 --version`

#### Method 2: Homebrew (Recommended)

```bash
# Install Homebrew if you don't have it
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python

# Verify
python3 --version
pip3 --version
```

### Linux

#### Ubuntu/Debian

```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Verify
python3 --version
pip3 --version
```

#### Fedora/CentOS/RHEL

```bash
# Install Python
sudo dnf install python3 python3-pip

# Verify
python3 --version
pip3 --version
```

#### Arch Linux

```bash
# Install Python
sudo pacman -S python python-pip

# Verify
python --version
pip --version
```

---

## Project Setup

### Step 1: Download the Project

#### Option A: Using Git (Recommended)

```bash
# Clone the repository
git clone https://github.com/yeongpin/cursor-free-vip.git

# Navigate to the project
cd cursor-free-vip
```

#### Option B: Download ZIP

1. Go to https://github.com/yeongpin/cursor-free-vip
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal/command prompt in the extracted folder

### Step 2: Create Virtual Environment

**Why use a virtual environment?**
- Isolated dependencies (no conflicts with other projects)
- Professional best practice
- Easy to clean up
- Reproducible environment

#### Windows (PowerShell)

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get an error about execution policy:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again
.\venv\Scripts\Activate.ps1
```

#### macOS/Linux

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

**You'll know it's activated when you see `(venv)` at the beginning of your command prompt.**

### Step 3: Install Dependencies

```bash
# Upgrade pip first (recommended)
python -m pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

This will install:
- `colorama` - Colored terminal output
- `selenium` - Browser automation
- `DrissionPage` - Advanced page automation
- `faker` - Test data generation
- `requests` - HTTP library
- And 40+ other dependencies

**Installation may take 2-5 minutes depending on your internet speed.**

---

## How to Use

### Starting the Application

```bash
# Make sure virtual environment is activated (you should see (venv))
# If not, activate it first:
#   Windows: .\venv\Scripts\Activate.ps1
#   macOS/Linux: source venv/bin/activate

# Run the main program
python main.py
```

### Main Menu

You'll see a colorful menu with options:

```
==================================================
🎯 Cursor Free VIP Tool
==================================================
1. 🔄 Reset Machine ID (Totally Reset)
2. 📧 Register with Email
3. ❌ Close Cursor
4. 🌐 Change Language
5. 🔓 Bypass Token Limit
6. 🔓 Bypass Version Check
7. 🛑 Disable Auto-Update
8. ... and more options
==================================================
```

### Common Use Cases

#### Use Case 1: First Time Setup - Bypass Token Limit

This is the most popular feature!

1. **Close Cursor** (Option 3)
   ```
   Select: 3
   ```

2. **Bypass Token Limit** (Option 5)
   ```
   Select: 5
   
   ✅ Auto-detecting Cursor installation...
   ✅ Found Cursor at: C:\Program Files\cursor\resources\app
   ✅ Backup Created
   ✅ File Modified
   ```

3. **Restart Cursor**
   - Open Cursor normally
   - Token limit is now bypassed!

#### Use Case 2: Reset Machine ID

When Cursor detects repeated use:

1. **Close Cursor** (Option 3)

2. **Reset Machine ID** (Option 1)
   ```
   Select: 1
   
   ℹ️ Auto-detecting Cursor installation...
   ✅ Found Cursor at: C:\Program Files\cursor\
   🔄 Generating new IDs...
   ✅ SQLite database updated
   ✅ System IDs updated
   ✅ Reset completed successfully!
   ```

3. **Restart Cursor**
   - Your machine ID is now fresh
   - Cursor treats it as a new installation

#### Use Case 3: Disable Auto-Update

To prevent Cursor from auto-updating:

1. **Disable Auto-Update** (Option 7)
   ```
   Select: 7
   
   🔄 Ending Cursor processes...
   ✅ Cursor processes ended
   📁 Removing updater directory...
   ✅ Updater directory removed
   📄 Creating block files...
   ✅ Block files created
   ✅ Auto-update disabled successfully!
   ```

2. **Result**
   - Cursor will no longer auto-update
   - Your current version is locked
   - You control when to update

---

## Features Explained

### 🔓 Bypass Token Limit

**What it does:**
- Modifies `workbench.desktop.main.js` file
- Removes token count restrictions
- Changes "Upgrade to Pro" button to "GitHub" link

**How it works:**
1. Auto-detects your Cursor installation
2. Creates timestamped backup of workbench file
3. Applies pattern replacements to remove limits
4. Preserves file permissions and ownership

**Safety:**
- ✅ Creates backup automatically
- ✅ Non-destructive (can be reversed)
- ✅ Works offline

### 🔄 Reset Machine ID

**What it does:**
- Generates new UUID-based machine IDs
- Updates `storage.json` database
- Updates `state.vscdb` SQLite database
- Modifies system-level identifiers (Windows/macOS)

**When to use:**
- Cursor shows "trial expired" messages
- Want to reset usage tracking
- Testing Cursor features

**Technical details:**
- Generates 4 different ID types:
  - `telemetry.devDeviceId` (UUID)
  - `telemetry.machineId` (SHA-256 hash)
  - `telemetry.macMachineId` (SHA-512 hash)
  - `telemetry.sqmId` (Windows SQM ID)

### 🛑 Disable Auto-Update

**What it does:**
- Kills Cursor update processes
- Deletes `cursor-updater` directory
- Clears `app-update.yml` configuration
- Creates read-only blocking files
- Removes update URLs from `product.json`

**Benefits:**
- Prevents breaking changes
- Keeps stable version
- Avoids unwanted features
- Controls update timing

---

## Troubleshooting

### Problem: "Python not found" or "python is not recognized"

**Solution:**
```powershell
# Windows - Reinstall Python with PATH checked
# OR use this workaround:
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py main.py
```

### Problem: "Cannot activate virtual environment" (Windows)

**Error:**
```
.\venv\Scripts\Activate.ps1 : cannot be loaded because running scripts is disabled
```

**Solution:**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then try activating again
.\venv\Scripts\Activate.ps1
```

### Problem: "Cursor path not found"

**Solution:**
The new auto-detection should handle this! But if it still fails:

1. **Manually configure path:**
   ```
   Select language → Configure Paths → Enter Cursor path
   ```

2. **Windows typical paths:**
   - `C:\Program Files\cursor\resources\app`
   - `C:\Users\YourName\AppData\Local\Programs\Cursor\resources\app`

3. **macOS typical path:**
   - `/Applications/Cursor.app/Contents/Resources/app`

4. **Linux typical paths:**
   - `/opt/Cursor/resources/app`
   - `/usr/share/cursor/resources/app`

### Problem: "Permission denied" errors

**Windows:**
```powershell
# Run PowerShell as Administrator
# Right-click PowerShell → "Run as Administrator"
# Then run the script
```

**macOS/Linux:**
```bash
# Use sudo for system-level operations
sudo python main.py

# Or change file ownership
sudo chown -R $USER:$USER ~/.config/cursor
```

### Problem: Dependencies installation fails

**Solution:**
```bash
# Upgrade pip first
python -m pip install --upgrade pip setuptools wheel

# Try installing dependencies one by one
pip install colorama
pip install selenium
pip install DrissionPage
# ... etc

# Or install with no-cache
pip install --no-cache-dir -r requirements.txt
```

---

## Can I Use Cursor Unlimited?

### ⚠️ Important Legal & Ethical Considerations

**Short Answer:** This tool is for **educational purposes only**.

**Long Answer:**

1. **Ethically:**
   - Cursor is developed by a small team
   - They provide an excellent product
   - Using bypasses denies them fair compensation
   - If you use Cursor professionally, **please buy a Pro subscription**

2. **Legally:**
   - Using this tool may violate Cursor's Terms of Service
   - Could result in account suspension
   - May void any support agreements
   - Use at your own risk

3. **Technically:**
   - This tool demonstrates how software protections work
   - Helps understand application structure
   - Educational value for developers
   - Not intended for production use

### Recommended Usage

**✅ Appropriate Use:**
- Testing and learning
- Understanding Cursor's architecture
- Temporary evaluation before purchase
- Educational projects
- Development and debugging

**❌ Inappropriate Use:**
- Commercial/business projects
- Long-term daily use without license
- Distributing bypassed versions
- Violating terms of service

### Support the Developers!

If you find Cursor useful:

1. **Buy Cursor Pro** 💰
   - Visit https://cursor.sh/pricing
   - Support continued development
   - Get official support
   - Access all features legally

2. **Alternatives if Budget Limited:**
   - Use free tier responsibly
   - Contribute to open-source alternatives
   - Support through GitHub sponsors
   - Recommend Cursor to others

---

## Contributing

Want to help improve cursor-free-vip?

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

See `IMPROVEMENTS_MADE.md` for recent contributions!

---

## License

This project is open-source under the MIT License.

**Disclaimer:** This tool is provided "as-is" for educational purposes. The authors are not responsible for any misuse or violations of terms of service.

---

# 中文指南

## 什么是 cursor-free-vip？

**cursor-free-vip** 是一个教育性开源工具，旨在帮助您管理和优化 Cursor AI 编辑器体验。它提供各种实用功能：

- ✅ 绕过 token 限制
- ✅ 管理机器 ID
- ✅ 禁用自动更新
- ✅ 使用多个邮箱提供商注册
- ✅ 完全重置 Cursor 设置

> ⚠️ **仅供教育目的**：此工具用于学习和了解软件系统的工作原理。如果您专业使用 Cursor，请支持官方 Cursor Pro 订阅。

---

## 功能特性

### 🎯 主要功能

1. **自动路径检测**（新功能！）
   - 无需手动配置
   - 适用于任何安装了 Cursor 的机器
   - 支持 Windows、macOS 和 Linux

2. **绕过 Token 限制**
   - 修改 Cursor 以移除 token 限制
   - 修改前自动备份
   - 适用于不同 Cursor 版本

3. **机器 ID 重置**
   - 生成新的机器 ID
   - 重置遥测数据
   - 支持多次重置

4. **自动更新控制**
   - 禁用 Cursor 自动更新
   - 防止不需要的版本更改
   - 锁定更新配置文件

5. **多语言支持**
   - 支持 15+ 种语言
   - 轻松切换语言
   - 完整的 UI 翻译

---

## Python 安装

### Windows

#### 方法 1：官方 Python 安装程序（推荐）

1. **下载 Python**
   - 访问 https://www.python.org/downloads/
   - 下载 Python 3.8 或更高版本（推荐 3.10+）
   - 点击 "Download Python 3.x.x"

2. **安装 Python**
   ```
   ✅ 勾选 "Add Python to PATH"（非常重要！）
   ✅ 勾选 "Install pip"
   点击 "Install Now"
   ```

3. **验证安装**
   ```powershell
   # 打开 PowerShell 并运行：
   python --version
   pip --version
   ```

#### 方法 2：Microsoft Store

1. 打开 Microsoft Store
2. 搜索 "Python 3.12" 或 "Python 3.11"
3. 点击 "获取" 或 "安装"
4. 验证：`python --version`

### macOS

#### 方法 1：官方安装程序

1. 从 https://www.python.org/downloads/macos/ 下载
2. 打开 `.pkg` 文件
3. 按照安装向导操作
4. 验证：`python3 --version`

#### 方法 2：Homebrew（推荐）

```bash
# 如果没有 Homebrew，先安装它
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 安装 Python
brew install python

# 验证
python3 --version
pip3 --version
```

### Linux

#### Ubuntu/Debian

```bash
# 更新包列表
sudo apt update

# 安装 Python 和 pip
sudo apt install python3 python3-pip python3-venv

# 验证
python3 --version
pip3 --version
```

#### Fedora/CentOS/RHEL

```bash
# 安装 Python
sudo dnf install python3 python3-pip

# 验证
python3 --version
pip3 --version
```

#### Arch Linux

```bash
# 安装 Python
sudo pacman -S python python-pip

# 验证
python --version
pip --version
```

---

## 项目设置

### 步骤 1：下载项目

#### 选项 A：使用 Git（推荐）

```bash
# 克隆仓库
git clone https://github.com/yeongpin/cursor-free-vip.git

# 进入项目目录
cd cursor-free-vip
```

#### 选项 B：下载 ZIP

1. 访问 https://github.com/yeongpin/cursor-free-vip
2. 点击 "Code" → "Download ZIP"
3. 解压 ZIP 文件
4. 在解压的文件夹中打开终端/命令提示符

### 步骤 2：创建虚拟环境

**为什么使用虚拟环境？**
- 隔离依赖（不与其他项目冲突）
- 专业最佳实践
- 易于清理
- 可重现的环境

#### Windows (PowerShell)

```powershell
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
.\venv\Scripts\Activate.ps1

# 如果遇到执行策略错误：
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 然后再次尝试激活
.\venv\Scripts\Activate.ps1
```

#### macOS/Linux

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate
```

**当您在命令提示符开头看到 `(venv)` 时，说明已激活成功。**

### 步骤 3：安装依赖

```bash
# 先升级 pip（推荐）
python -m pip install --upgrade pip

# 安装所有必需的包
pip install -r requirements.txt
```

这将安装：
- `colorama` - 彩色终端输出
- `selenium` - 浏览器自动化
- `DrissionPage` - 高级页面自动化
- `faker` - 测试数据生成
- `requests` - HTTP 库
- 以及 40+ 个其他依赖项

**安装可能需要 2-5 分钟，具体取决于您的网速。**

---

## 如何使用

### 启动应用程序

```bash
# 确保虚拟环境已激活（您应该看到 (venv)）
# 如果没有，先激活它：
#   Windows: .\venv\Scripts\Activate.ps1
#   macOS/Linux: source venv/bin/activate

# 运行主程序
python main.py
```

### 主菜单

您将看到一个彩色菜单，包含以下选项：

```
==================================================
🎯 Cursor Free VIP 工具
==================================================
1. 🔄 重置机器 ID（完全重置）
2. 📧 使用邮箱注册
3. ❌ 关闭 Cursor
4. 🌐 更改语言
5. 🔓 绕过 Token 限制
6. 🔓 绕过版本检查
7. 🛑 禁用自动更新
8. ... 更多选项
==================================================
```

### 常见使用场景

#### 场景 1：首次设置 - 绕过 Token 限制

这是最受欢迎的功能！

1. **关闭 Cursor**（选项 3）
   ```
   选择：3
   ```

2. **绕过 Token 限制**（选项 5）
   ```
   选择：5
   
   ✅ 正在自动检测 Cursor 安装...
   ✅ 找到 Cursor：C:\Program Files\cursor\resources\app
   ✅ 已创建备份
   ✅ 文件已修改
   ```

3. **重启 Cursor**
   - 正常打开 Cursor
   - Token 限制现已绕过！

#### 场景 2：重置机器 ID

当 Cursor 检测到重复使用时：

1. **关闭 Cursor**（选项 3）

2. **重置机器 ID**（选项 1）
   ```
   选择：1
   
   ℹ️ 正在自动检测 Cursor 安装...
   ✅ 找到 Cursor：C:\Program Files\cursor\
   🔄 正在生成新 ID...
   ✅ SQLite 数据库已更新
   ✅ 系统 ID 已更新
   ✅ 重置成功完成！
   ```

3. **重启 Cursor**
   - 您的机器 ID 现在是全新的
   - Cursor 将其视为新安装

#### 场景 3：禁用自动更新

防止 Cursor 自动更新：

1. **禁用自动更新**（选项 7）
   ```
   选择：7
   
   🔄 正在结束 Cursor 进程...
   ✅ Cursor 进程已结束
   📁 正在删除更新程序目录...
   ✅ 更新程序目录已删除
   📄 正在创建阻止文件...
   ✅ 阻止文件已创建
   ✅ 自动更新已成功禁用！
   ```

2. **结果**
   - Cursor 将不再自动更新
   - 您的当前版本已锁定
   - 您可以控制何时更新

---

## 功能详解

### 🔓 绕过 Token 限制

**功能说明：**
- 修改 `workbench.desktop.main.js` 文件
- 移除 token 计数限制
- 将 "升级到 Pro" 按钮更改为 "GitHub" 链接

**工作原理：**
1. 自动检测您的 Cursor 安装位置
2. 创建工作台文件的时间戳备份
3. 应用模式替换以移除限制
4. 保留文件权限和所有权

**安全性：**
- ✅ 自动创建备份
- ✅ 非破坏性（可以还原）
- ✅ 离线工作

### 🔄 重置机器 ID

**功能说明：**
- 生成基于 UUID 的新机器 ID
- 更新 `storage.json` 数据库
- 更新 `state.vscdb` SQLite 数据库
- 修改系统级标识符（Windows/macOS）

**何时使用：**
- Cursor 显示 "试用已过期" 消息
- 想要重置使用跟踪
- 测试 Cursor 功能

**技术细节：**
- 生成 4 种不同的 ID 类型：
  - `telemetry.devDeviceId`（UUID）
  - `telemetry.machineId`（SHA-256 哈希）
  - `telemetry.macMachineId`（SHA-512 哈希）
  - `telemetry.sqmId`（Windows SQM ID）

### 🛑 禁用自动更新

**功能说明：**
- 终止 Cursor 更新进程
- 删除 `cursor-updater` 目录
- 清空 `app-update.yml` 配置
- 创建只读阻止文件
- 从 `product.json` 中删除更新 URL

**优势：**
- 防止破坏性更改
- 保持稳定版本
- 避免不需要的功能
- 控制更新时间

---

## 故障排除

### 问题："Python not found" 或 "python is not recognized"

**解决方案：**
```powershell
# Windows - 重新安装 Python 并勾选 PATH
# 或使用此变通方法：
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py main.py
```

### 问题："Cannot activate virtual environment"（Windows）

**错误：**
```
.\venv\Scripts\Activate.ps1 : 无法加载，因为禁止运行脚本
```

**解决方案：**
```powershell
# 以管理员身份运行 PowerShell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 然后再次尝试激活
.\venv\Scripts\Activate.ps1
```

### 问题："Cursor path not found"

**解决方案：**
新的自动检测应该能处理这个问题！但如果仍然失败：

1. **手动配置路径：**
   ```
   选择语言 → 配置路径 → 输入 Cursor 路径
   ```

2. **Windows 典型路径：**
   - `C:\Program Files\cursor\resources\app`
   - `C:\Users\您的用户名\AppData\Local\Programs\Cursor\resources\app`

3. **macOS 典型路径：**
   - `/Applications/Cursor.app/Contents/Resources/app`

4. **Linux 典型路径：**
   - `/opt/Cursor/resources/app`
   - `/usr/share/cursor/resources/app`

### 问题："Permission denied" 错误

**Windows：**
```powershell
# 以管理员身份运行 PowerShell
# 右键点击 PowerShell → "以管理员身份运行"
# 然后运行脚本
```

**macOS/Linux：**
```bash
# 对系统级操作使用 sudo
sudo python main.py

# 或更改文件所有权
sudo chown -R $USER:$USER ~/.config/cursor
```

### 问题：依赖项安装失败

**解决方案：**
```bash
# 先升级 pip
python -m pip install --upgrade pip setuptools wheel

# 尝试逐个安装依赖项
pip install colorama
pip install selenium
pip install DrissionPage
# ... 等等

# 或使用 no-cache 安装
pip install --no-cache-dir -r requirements.txt
```

---

## 我可以无限制使用 Cursor 吗？

### ⚠️ 重要的法律和道德考虑

**简短回答：** 此工具**仅供教育目的**。

**详细回答：**

1. **道德方面：**
   - Cursor 由一个小团队开发
   - 他们提供了优秀的产品
   - 使用绕过工具会剥夺他们应得的报酬
   - 如果您专业使用 Cursor，**请购买 Pro 订阅**

2. **法律方面：**
   - 使用此工具可能违反 Cursor 的服务条款
   - 可能导致账户被暂停
   - 可能使任何支持协议失效
   - 使用风险自负

3. **技术方面：**
   - 此工具展示了软件保护的工作原理
   - 帮助理解应用程序结构
   - 对开发者有教育价值
   - 不适用于生产环境

### 推荐使用方式

**✅ 适当使用：**
- 测试和学习
- 了解 Cursor 的架构
- 购买前的临时评估
- 教育项目
- 开发和调试

**❌ 不当使用：**
- 商业/业务项目
- 无许可证的长期日常使用
- 分发绕过版本
- 违反服务条款

### 支持开发者！

如果您觉得 Cursor 有用：

1. **购买 Cursor Pro** 💰
   - 访问 https://cursor.sh/pricing
   - 支持持续开发
   - 获得官方支持
   - 合法访问所有功能

2. **预算有限的替代方案：**
   - 负责任地使用免费版本
   - 为开源替代品做贡献
   - 通过 GitHub 赞助商支持
   - 向他人推荐 Cursor

---

## 贡献

想帮助改进 cursor-free-vip？

1. **Fork 仓库**
2. **创建功能分支**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **进行更改**
4. **彻底测试**
5. **提交 pull request**

查看 `IMPROVEMENTS_MADE.md` 了解最近的贡献！

---

## 许可证

本项目在 MIT 许可证下开源。

**免责声明：** 此工具按 "原样" 提供，仅供教育目的。作者不对任何滥用或违反服务条款的行为负责。

---

## 📞 Support | 支持

**English:**
- GitHub Issues: https://github.com/yeongpin/cursor-free-vip/issues
- Discussions: https://github.com/yeongpin/cursor-free-vip/discussions

**中文：**
- GitHub 问题：https://github.com/yeongpin/cursor-free-vip/issues
- 讨论区：https://github.com/yeongpin/cursor-free-vip/discussions

---

**Made with ❤️ for the community | 为社区用心制作**
