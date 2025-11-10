# 🎯 cursor-free-vip - Cursor AI Editor Management Tool

**English** | [中文](#中文说明)

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**Educational tool for managing and optimizing Cursor AI editor**

[Features](#features) • [Quick Start](#quick-start) • [Documentation](#documentation) • [Contributing](#contributing)

</div>

---

## ⚠️ Important Notice | 重要声明

**🇬🇧 English:**
This tool is **for educational purposes only**. It demonstrates how software systems work and is meant for learning. If you use Cursor professionally, please support the developers by purchasing [Cursor Pro](https://cursor.sh/pricing).

**🇨🇳 中文:**
此工具**仅供教育目的**。它展示了软件系统的工作原理，旨在用于学习。如果您专业使用 Cursor，请通过购买 [Cursor Pro](https://cursor.sh/pricing) 来支持开发者。

---

## ✨ Features

### 🆕 NEW: Automatic Path Detection (v2.0)

- 🔍 **Zero Configuration**: Automatically finds Cursor installation on any machine
- 🌍 **Cross-Platform**: Works on Windows, macOS, and Linux
- 🚀 **Smart Detection**: Multiple detection methods with intelligent fallback
- 💾 **Config Fallback**: Falls back to manual configuration if needed

### Core Features

| Feature | Description | Status |
|---------|-------------|--------|
| 🔓 **Bypass Token Limit** | Remove token restrictions | ✅ Enhanced |
| 🔄 **Reset Machine ID** | Generate new machine identifiers | ✅ Enhanced |
| 🛑 **Disable Auto-Update** | Prevent unwanted updates | ✅ Enhanced |
| 📧 **Email Registration** | Register with multiple providers | ✅ Working |
| 🌐 **Multi-Language** | 15+ languages supported | ✅ Working |
| 🔓 **Bypass Version Check** | Modify version restrictions | ✅ Enhanced |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Cursor AI Editor installed
- Internet connection (for initial setup)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yeongpin/cursor-free-vip.git
cd cursor-free-vip

# 2. Create virtual environment (recommended)
python -m venv venv

# 3. Activate virtual environment
# Windows:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the application
python main.py
```

### First Time Use

1. **Close Cursor** (if running)
2. **Select language** from the menu
3. **Choose a feature** (we recommend starting with "Bypass Token Limit")
4. **Follow the prompts**
5. **Restart Cursor**

That's it! The tool will automatically detect your Cursor installation. 🎉

---

## 📖 Documentation

### Complete Guides

- 📘 **[Complete Setup Guide](docs/COMPLETE_SETUP_GUIDE.md)** - Step-by-step installation and usage (English & Chinese)
- 🔧 **[Improvements Made](IMPROVEMENTS_MADE.md)** - Recent enhancements and technical details
- 🤝 **[Contributing Guide](CONTRIBUTING.md)** - How to contribute to the project

### Quick References

- **Python Setup**: See [Python Installation](#python-installation) section
- **Troubleshooting**: Check [Common Issues](#common-issues) section
- **Features Explained**: Read [Features Documentation](#features-documentation)

---

## 💻 Python Installation

### Windows

**Method 1: Official Installer (Recommended)**
```powershell
# Download from: https://www.python.org/downloads/
# ✅ Check "Add Python to PATH" during installation
python --version  # Verify installation
```

**Method 2: Microsoft Store**
```powershell
# Search "Python 3.12" in Microsoft Store
# Click "Get" or "Install"
```

### macOS

**Using Homebrew (Recommended)**
```bash
brew install python
python3 --version  # Verify installation
```

### Linux

**Ubuntu/Debian**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

**Fedora/RHEL**
```bash
sudo dnf install python3 python3-pip
```

**Arch Linux**
```bash
sudo pacman -S python python-pip
```

---

## 🎯 Features Documentation

### 🔓 Bypass Token Limit

**What it does:**
- Removes token counting restrictions in Cursor
- Modifies `workbench.desktop.main.js` file
- Creates automatic backups before modifications

**How to use:**
```
1. Select option: "5. 🔓 Bypass Token Limit"
2. Tool auto-detects Cursor installation
3. Creates backup and applies modifications
4. Restart Cursor
```

**Technical Details:**
- ✅ Automatic path detection (NEW!)
- ✅ Timestamped backups
- ✅ Non-destructive (reversible)
- ✅ Offline operation

---

### 🔄 Reset Machine ID

**What it does:**
- Generates new UUID-based machine identifiers
- Updates telemetry databases
- Resets usage tracking

**When to use:**
- Cursor shows "trial expired" messages
- Testing features
- Development purposes

**What gets reset:**
- `telemetry.devDeviceId`
- `telemetry.machineId`
- `telemetry.macMachineId`
- `telemetry.sqmId`
- System-level identifiers (Windows/macOS)

---

### 🛑 Disable Auto-Update

**What it does:**
- Prevents Cursor from auto-updating
- Locks current version
- Removes update mechanisms

**Process:**
1. Terminates update processes
2. Removes updater directory
3. Clears update configuration
4. Creates blocking files
5. Removes update URLs

**Benefits:**
- Control update timing
- Prevent breaking changes
- Maintain stable version

---

## 🛠️ Common Issues

### "Python not found"

```powershell
# Windows - Use py launcher
py -m pip install -r requirements.txt
py main.py

# Or reinstall Python with PATH option checked
```

### "Cannot activate virtual environment" (Windows)

```powershell
# Run as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
.\venv\Scripts\Activate.ps1
```

### "Cursor path not found"

**This should not happen with the new auto-detection!**

But if it does:
1. Manually configure in the application menu
2. Or check `docs/COMPLETE_SETUP_GUIDE.md` for typical paths

### "Permission denied"

```bash
# Windows: Run PowerShell as Administrator
# Linux/macOS: Use sudo
sudo python main.py
```

---

## 🆕 What's New in v2.0

### Automatic Path Detection System

**Before:**
```python
# ❌ Hardcoded path - fails on different machines
cursor_path = r"C:\Users\username\AppData\Local\Programs\Cursor\..."
```

**After:**
```python
# ✅ Auto-detection - works everywhere
cursor_app_path = find_cursor_installation()
# Automatically finds: C:\Program Files\cursor\resources\app
```

### Detection Methods

1. **Process Detection** (Primary)
   - Checks if Cursor is running
   - Gets installation path from process

2. **Registry Check** (Windows)
   - Searches Windows Registry
   - Finds installation location

3. **Common Paths** (Fallback)
   - Checks standard installation directories
   - Platform-specific paths

4. **Drive Scan** (Last Resort)
   - Scans all available drives
   - Comprehensive search

5. **Config File** (Manual)
   - Uses user-configured path
   - Traditional fallback method

### Files Updated

- ✅ `cursor_path_detector.py` (NEW) - Auto-detection module
- ✅ `bypass_token_limit.py` - Integrated auto-detection
- ✅ `totally_reset_cursor.py` - Integrated auto-detection
- ✅ `disable_auto_update.py` - Integrated auto-detection
- ✅ `bypass_version.py` - Integrated auto-detection

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **Report Bugs** 🐛
   - Open an issue with details
   - Include error messages and logs
   - Describe your environment

2. **Suggest Features** 💡
   - Open a feature request
   - Explain the use case
   - Provide examples

3. **Submit Code** 💻
   - Fork the repository
   - Create a feature branch
   - Write tests
   - Submit pull request

4. **Improve Documentation** 📚
   - Fix typos
   - Add examples
   - Translate to other languages

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/cursor-free-vip.git
cd cursor-free-vip

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\Activate.ps1 on Windows

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # if exists

# Create a branch
git checkout -b feature/my-amazing-feature

# Make changes and test
python main.py

# Run tests (if available)
pytest

# Commit and push
git add .
git commit -m "feat: add amazing feature"
git push origin feature/my-amazing-feature
```

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Comment complex logic
- Keep functions focused and small

---

## 📊 Project Statistics

- **Languages**: 15+ supported languages
- **Files Modified**: Automatic backup before changes
- **Platform Support**: Windows, macOS, Linux
- **Detection Methods**: 5 different path detection strategies
- **Dependencies**: 40+ Python packages
- **Test Coverage**: Expanding (contributions welcome!)

---

## ❓ FAQ

### Q: Is this tool safe to use?

**A:** Yes, for educational purposes. It creates backups before modifications and all changes are reversible. However:
- ⚠️ May violate Cursor's Terms of Service
- ⚠️ Use at your own risk
- ⚠️ Not intended for commercial use

### Q: Can I use Cursor unlimited with this?

**A:** This tool is **educational only**. For professional use:
- ✅ Buy [Cursor Pro](https://cursor.sh/pricing)
- ✅ Support the developers
- ✅ Get official support
- ✅ Use features legally

### Q: Does it work on all Cursor versions?

**A:** The tool supports:
- ✅ Cursor 0.45.0+
- ✅ Most recent versions
- ⚠️ Some features may require specific versions

### Q: Will my data be deleted?

**A:** No. The tool:
- ✅ Creates backups automatically
- ✅ Only modifies specific configuration files
- ✅ Does not delete user data
- ✅ Changes are reversible

### Q: Do I need to close Cursor before using the tool?

**A:** Yes! Always:
1. Close Cursor completely
2. Run the tool
3. Restart Cursor after modifications

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

### Disclaimer

This tool is provided "as-is" for **educational purposes only**. The authors:

- ❌ Do NOT encourage violating terms of service
- ❌ Are NOT responsible for any misuse
- ❌ Do NOT provide warranty of any kind
- ✅ Recommend purchasing Cursor Pro for professional use

---

## 🙏 Acknowledgments

- **Cursor Team** - For creating an amazing AI editor
- **Contributors** - Everyone who has contributed to this project
- **Community** - For feedback and suggestions

---

## 📞 Support

- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/yeongpin/cursor-free-vip/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yeongpin/cursor-free-vip/discussions)
- 📧 **Email**: [Check repository for contact]
- 📚 **Documentation**: [docs/](docs/)

---

## 🌟 Star History

If you find this project helpful, please consider giving it a star! ⭐

```bash
# Stay updated
git clone https://github.com/yeongpin/cursor-free-vip.git
cd cursor-free-vip
git pull origin main  # Get latest updates
```

---

# 中文说明

## 🎯 cursor-free-vip - Cursor AI 编辑器管理工具

### 功能特性

- 🔓 **绕过 Token 限制** - 移除 token 计数限制
- 🔄 **重置机器 ID** - 生成新的机器标识符
- 🛑 **禁用自动更新** - 防止不需要的更新
- 📧 **邮箱注册** - 支持多个邮箱提供商
- 🌐 **多语言支持** - 支持 15+ 种语言
- 🆕 **自动路径检测** - 无需手动配置（新功能！）

### 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/yeongpin/cursor-free-vip.git
cd cursor-free-vip

# 2. 创建虚拟环境
python -m venv venv

# 3. 激活虚拟环境
# Windows:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# 4. 安装依赖
pip install -r requirements.txt

# 5. 运行程序
python main.py
```

### 完整文档

- 📘 [完整安装指南](docs/COMPLETE_SETUP_GUIDE.md) - 详细的中英文说明
- 🔧 [改进说明](IMPROVEMENTS_MADE.md) - 最新功能和技术细节

### 重要提示

⚠️ **本工具仅供教育目的使用**

如果您专业使用 Cursor，请购买 [Cursor Pro](https://cursor.sh/pricing) 以支持开发者。

### 新功能：自动路径检测

✅ **无需配置** - 自动找到 Cursor 安装位置  
✅ **跨平台支持** - Windows、macOS、Linux  
✅ **智能检测** - 多种检测方法和智能回退  

### 常见问题

**问：这个工具安全吗？**  
答：是的，用于教育目的是安全的。它在修改前创建备份，所有更改都可以还原。

**问：我可以无限制使用 Cursor 吗？**  
答：本工具仅供教育目的。专业使用请购买 [Cursor Pro](https://cursor.sh/pricing)。

**问：支持所有 Cursor 版本吗？**  
答：支持 Cursor 0.45.0 及以上版本。

### 支持

- 🐛 问题报告：[GitHub Issues](https://github.com/yeongpin/cursor-free-vip/issues)
- 💬 讨论区：[GitHub Discussions](https://github.com/yeongpin/cursor-free-vip/discussions)

---

<div align="center">

**Made with ❤️ for the community**

**为社区用心制作**

[⬆ Back to top](#-cursor-free-vip---cursor-ai-editor-management-tool)

</div>
