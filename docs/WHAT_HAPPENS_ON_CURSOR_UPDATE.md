# ⚠️ What Happens When Cursor Updates | Cursor 更新后会发生什么

**English** | [中文](#中文说明)

---

## 🎯 Quick Answer | 快速回答

**When Cursor updates, some modifications may be reset.**

**当 Cursor 更新时，某些修改可能会被重置。**

---

# English Documentation

## What Gets Reset on Update | 更新时会重置什么

### ✅ Safe (Won't Be Reset) | 安全（不会被重置）

1. **Machine ID Changes** ✅
   - `storage.json` modifications
   - `state.vscdb` database changes
   - System-level machine IDs
   - **Why:** These are user data files, not application files

2. **Disabled Auto-Update Settings** ✅ (Partially)
   - Blocking files we created
   - Registry changes (Windows)
   - **Why:** These prevent updates from happening

3. **Configuration Files** ✅
   - `.cursor-free-vip/config.ini`
   - User preferences
   - **Why:** Stored in user's Documents folder

### ⚠️ May Be Reset | 可能被重置

1. **Token Limit Bypass** ⚠️
   - `workbench.desktop.main.js` modifications
   - **Why:** This file is part of the application and gets replaced during updates
   - **Solution:** Re-run bypass after update

2. **Version Bypass** ⚠️
   - `product.json` modifications
   - **Why:** Application file, gets overwritten
   - **Solution:** Re-run bypass after update

3. **UI Modifications** ⚠️
   - Button text changes
   - Theme modifications
   - **Why:** Part of application code
   - **Solution:** Re-apply modifications

---

## 🔄 Update Scenarios | 更新场景

### Scenario 1: Auto-Update Disabled Successfully | 场景1：成功禁用自动更新

**What happens:**
```
✅ Cursor won't auto-update
✅ Your modifications stay intact
✅ You control when to update
```

**Recommendation:**
- Keep auto-update disabled
- Only update when necessary
- Re-apply modifications after manual updates

### Scenario 2: Auto-Update Occurs | 场景2：发生自动更新

**What happens:**
```
⚠️ Cursor downloads and installs new version
⚠️ Application files get replaced
⚠️ Token limit bypass is reset
⚠️ Version bypass is reset
✅ Machine ID changes remain
✅ User data intact
```

**What to do:**
1. Close Cursor
2. Re-run the tool
3. Re-apply bypasses:
   - Select "5. Bypass Token Limit"
   - Select "6. Bypass Version Check"
   - Select "7. Disable Auto-Update" (again)
4. Restart Cursor

### Scenario 3: Manual Update | 场景3：手动更新

**Before updating manually:**
```bash
# 1. Backup your modifications (optional)
# The tool creates automatic backups, but you can create your own:

# Backup workbench file
copy "C:\Program Files\cursor\resources\app\out\vs\workbench\workbench.desktop.main.js" "C:\backup\workbench.backup.js"

# Backup product.json
copy "C:\Program Files\cursor\resources\app\product.json" "C:\backup\product.backup.json"
```

**After updating:**
1. Install the new version
2. Run cursor-free-vip again
3. Re-apply all modifications
4. Restart Cursor

---

## 🛡️ Protection Strategies | 保护策略

### Strategy 1: Disable Auto-Update (Recommended) | 策略1：禁用自动更新（推荐）

**How:**
```bash
# Run the tool
python main.py

# Select: 7. Disable Auto-Update
# This creates blocking files that prevent updates
```

**Effectiveness:**
- ✅ Prevents unwanted updates
- ✅ Keeps your modifications safe
- ✅ You control update timing

**Maintenance:**
```bash
# Check if auto-update is still disabled
# Windows:
dir "C:\Users\YourName\AppData\Local\cursor-updater"
# Should be a file (blocking), not a directory

# If it became a directory again, re-run disable auto-update
```

### Strategy 2: Version Pinning | 策略2：版本锁定

**How:**
```bash
# After finding a stable version:
# 1. Disable auto-update
# 2. Note the version number
# 3. Don't manually update unless necessary
```

**Benefits:**
- Stable environment
- No surprise breaking changes
- Modifications stay intact

### Strategy 3: Automated Re-Application | 策略3：自动重新应用

**Create a script:**

**Windows (PowerShell):**
```powershell
# save as: reapply-modifications.ps1

# Activate virtual environment
& ".\venv\Scripts\Activate.ps1"

# Close Cursor
taskkill /F /IM Cursor.exe /T

# Wait a moment
Start-Sleep -Seconds 2

# Re-apply modifications
python -c "from bypass_token_limit import run; from main import translator; run(translator)"
python -c "from bypass_version import bypass_version; from main import translator; bypass_version(translator)"

# Restart Cursor
Start-Process "C:\Program Files\cursor\Cursor.exe"

Write-Host "✅ Modifications re-applied successfully!"
```

**Usage:**
```powershell
# After any update:
.\reapply-modifications.ps1
```

### Strategy 4: Monitoring | 策略4：监控

**Check if modifications are still active:**

```python
# save as: check-modifications.py

import os
import json
from cursor_path_detector import find_cursor_installation

cursor_path = find_cursor_installation()

# Check workbench modification
workbench_path = os.path.join(cursor_path, "out", "vs", "workbench", "workbench.desktop.main.js")
with open(workbench_path, 'r', encoding='utf-8') as f:
    content = f.read()
    if 'yeongpin GitHub' in content:
        print("✅ Token limit bypass: ACTIVE")
    else:
        print("⚠️ Token limit bypass: INACTIVE - Need to re-apply")

# Check version modification
product_path = os.path.join(cursor_path, "product.json")
with open(product_path, 'r', encoding='utf-8') as f:
    product = json.load(f)
    version = product.get('version', '0.0.0')
    if version >= "0.46.0":
        print(f"✅ Version bypass: ACTIVE (v{version})")
    else:
        print(f"⚠️ Version bypass: INACTIVE - Need to re-apply")
```

**Usage:**
```bash
python check-modifications.py
```

---

## 📊 Update Impact Analysis | 更新影响分析

### Files Modified by cursor-free-vip | cursor-free-vip 修改的文件

| File | Location | Impact on Update | Recovery |
|------|----------|------------------|----------|
| `storage.json` | `%APPDATA%\Cursor\User\globalStorage\` | ✅ Safe | No action needed |
| `state.vscdb` | `%APPDATA%\Cursor\User\globalStorage\` | ✅ Safe | No action needed |
| `machineId` | `%APPDATA%\Cursor\` | ✅ Safe | No action needed |
| `workbench.desktop.main.js` | `Cursor\resources\app\out\vs\workbench\` | ⚠️ Reset | Re-run bypass |
| `product.json` | `Cursor\resources\app\` | ⚠️ Reset | Re-run bypass |
| `app-update.yml` | `Cursor\resources\` | ⚠️ May reset | Re-disable auto-update |
| `cursor-updater` | `%LOCALAPPDATA%\` | ✅ Blocked | Stays blocked |

### Update Types and Their Impact | 更新类型及其影响

#### Minor Updates (0.42.1 → 0.42.2)
```
Expected Impact: Low
- May not reset modifications
- Usually just bug fixes
- Workbench file might stay intact
```

#### Major Updates (0.42.x → 0.43.0)
```
Expected Impact: Medium
- Likely resets workbench modifications
- May change product.json format
- Recommend re-applying bypasses
```

#### Major Version Updates (0.42.x → 0.50.x)
```
Expected Impact: High
- Definitely resets all modifications
- May change file structure
- May require updates to cursor-free-vip
- Full re-application needed
```

---

## 🔧 Recovery Procedures | 恢复程序

### Quick Recovery (5 minutes) | 快速恢复（5分钟）

```bash
# 1. Close Cursor
# 2. Run tool
python main.py

# 3. Re-apply bypasses in order:
#    - Select 5: Bypass Token Limit
#    - Select 6: Bypass Version Check
#    - Select 7: Disable Auto-Update

# 4. Restart Cursor
```

### Full Recovery (10 minutes) | 完全恢复（10分钟）

```bash
# 1. Close Cursor completely
taskkill /F /IM Cursor.exe /T

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Update cursor-free-vip (if needed)
git pull origin main
pip install -r requirements.txt

# 4. Run comprehensive reset
python main.py
# Select: 1. Reset Machine ID (Totally Reset)
# This does everything at once

# 5. Restart Cursor
```

### If Tool Doesn't Work After Update | 如果更新后工具无法工作

**Possible reasons:**
1. Cursor changed file structure
2. New version incompatible
3. New protection mechanisms

**What to do:**
```bash
# 1. Check for tool updates
cd cursor-free-vip
git pull origin main

# 2. Check GitHub issues
# Visit: https://github.com/yeongpin/cursor-free-vip/issues
# Search for your Cursor version

# 3. Report issue if not found
# Include:
# - Cursor version (Help → About)
# - Error message
# - Tool version
# - Operating system
```

---

## 📝 Best Practices | 最佳实践

### 1. Regular Backups | 定期备份

```bash
# Create backup script: backup-cursor.ps1

$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$backupDir = "$HOME\cursor-backups\$timestamp"
New-Item -ItemType Directory -Path $backupDir

# Backup application files
Copy-Item "C:\Program Files\cursor\resources\app\out\vs\workbench\workbench.desktop.main.js" "$backupDir\"
Copy-Item "C:\Program Files\cursor\resources\app\product.json" "$backupDir\"

# Backup user data
Copy-Item "$env:APPDATA\Cursor\User\globalStorage\storage.json" "$backupDir\"
Copy-Item "$env:APPDATA\Cursor\User\globalStorage\state.vscdb" "$backupDir\"

Write-Host "✅ Backup created: $backupDir"
```

**Run before any update:**
```powershell
.\backup-cursor.ps1
```

### 2. Version Tracking | 版本跟踪

```bash
# save as: check-cursor-version.py

import json
from cursor_path_detector import find_cursor_installation
import os

cursor_path = find_cursor_installation()
package_json = os.path.join(cursor_path, "package.json")

with open(package_json, 'r') as f:
    data = json.load(f)
    version = data.get('version', 'Unknown')
    print(f"Current Cursor Version: {version}")
    
    # Save to file for tracking
    with open('cursor-version-history.txt', 'a') as log:
        from datetime import datetime
        log.write(f"{datetime.now()}: v{version}\n")
```

### 3. Update Log | 更新日志

Create `cursor-update-log.txt`:
```
Date: 2025-11-10
Old Version: 0.42.5
New Version: 0.43.0
Modifications Reset: Yes
Re-applied: Yes
Notes: Major update, workbench structure changed
Status: ✅ Working

Date: 2025-11-15
Old Version: 0.43.0
New Version: 0.43.1
Modifications Reset: No
Notes: Minor patch, no re-application needed
Status: ✅ Working
```

### 4. Test Before Using | 使用前测试

After update and re-application:
```bash
# Test each feature:
# 1. Check token limit - try to use AI features
# 2. Check version - should show 0.48.7 or higher
# 3. Check auto-update - should be disabled
# 4. Check machine ID - should be new
```

---

## 🚨 Emergency Situations | 紧急情况

### Cursor Won't Start After Modification | 修改后 Cursor 无法启动

**Solution 1: Restore from backup**
```bash
# Find backup file (created automatically by tool)
# Located in same directory as modified file
# Example: workbench.desktop.main.js.backup.20251110120000

# Restore it
copy "C:\Program Files\cursor\resources\app\out\vs\workbench\workbench.desktop.main.js.backup.20251110120000" "C:\Program Files\cursor\resources\app\out\vs\workbench\workbench.desktop.main.js"
```

**Solution 2: Reinstall Cursor**
```bash
# 1. Uninstall Cursor
# 2. Delete remaining files:
rmdir /S "C:\Program Files\cursor"
rmdir /S "%LOCALAPPDATA%\Programs\Cursor"

# 3. Reinstall from https://cursor.sh
# 4. Re-apply modifications carefully
```

### Tool Shows "Path Not Found" After Update | 更新后工具显示"找不到路径"

**Reason:** Cursor might have changed installation location

**Solution:**
```bash
# 1. Check where Cursor is installed
Get-Process cursor | Select-Object Path

# 2. If path changed, update config
python main.py
# Select: 4. Change Language → Configure Paths
# Enter new path

# 3. Or rely on auto-detection
# Auto-detection should find it automatically
```

---

## ❓ FAQ | 常见问题

### Q: How often does Cursor update?

**A:** Cursor typically updates:
- Minor patches: Every 1-2 weeks
- Major updates: Every 1-2 months
- Critical fixes: As needed

### Q: Will I lose my work if Cursor updates?

**A:** No! Your code and projects are safe:
- ✅ Your code files are separate from Cursor
- ✅ Workspace settings are preserved
- ⚠️ Only tool modifications are reset

### Q: Should I disable auto-update permanently?

**A:** Recommended approach:
- ✅ Disable auto-update for stability
- ✅ Check for updates manually monthly
- ✅ Update when necessary for security
- ✅ Re-apply modifications after updates

### Q: Can I update Cursor safely?

**A:** Yes, but:
1. Backup your modifications
2. Note your current version
3. Update Cursor
4. Re-run cursor-free-vip
5. Test all features

### Q: What if new Cursor version breaks the tool?

**A:** 
1. Check GitHub for tool updates
2. Downgrade Cursor to previous version
3. Wait for tool to be updated
4. Report issue on GitHub

---

# 中文说明

## Cursor 更新时会发生什么

### ✅ 安全（不会被重置）

1. **机器 ID 更改** - 用户数据文件
2. **禁用的自动更新设置** - 阻止文件保留
3. **配置文件** - 存储在用户文档文件夹中

### ⚠️ 可能被重置

1. **Token 限制绕过** - 应用程序文件会被替换
2. **版本绕过** - 会被覆盖
3. **UI 修改** - 应用程序代码的一部分

## 更新后该做什么

```bash
# 1. 关闭 Cursor
# 2. 运行工具
python main.py

# 3. 重新应用绕过：
#    - 选择 5: 绕过 Token 限制
#    - 选择 6: 绕过版本检查
#    - 选择 7: 禁用自动更新

# 4. 重启 Cursor
```

## 保护策略

1. **禁用自动更新**（推荐）
2. **版本锁定** - 找到稳定版本后不更新
3. **自动重新应用** - 创建脚本自动重新应用修改
4. **监控** - 定期检查修改是否仍然有效

## 最佳实践

- ✅ 定期备份
- ✅ 跟踪版本
- ✅ 记录更新日志
- ✅ 更新后测试

---

<div align="center">

**⚠️ Remember: Always re-apply modifications after Cursor updates**

**记住：Cursor 更新后始终重新应用修改**

**The tool makes this easy - just run it again!**

**工具让这变得简单 - 只需再次运行它！**

</div>
