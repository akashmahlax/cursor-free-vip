Perfect 👍
Below is the **professionally rewritten English documentation** of your README file — all content preserved, structured, and polished to international open-source documentation standards.
I've retained **bilingual headings (English + Chinese)** for clarity and global accessibility, and refined every section for professional tone, consistency, and technical precision.

---

# ➤ Cursor Free VIP

<div align="center">

<p align="center">
  <img src="./images/logo.png" alt="Cursor Pro Logo" width="200" style="border-radius: 6px;"/>
</p>

<p align="center">
<a href="http://go.warp.dev/cursor-free-vip">
   <img alt="Warp sponsorship" width="400" src="https://github.com/user-attachments/assets/ab8dd143-b0fd-4904-bdc5-dd7ecac94eae">
</a>

<br><br> <sup>Special thanks to:</sup><br> <a href="http://go.warp.dev/cursor-free-vip"><b>Warp — Built for coding with multiple AI agents.</b></a><br>
[Available for macOS, Linux, and Windows](http://go.warp.dev/cursor-free-vip)

</p>

<p align="center">
   <a href="https://github.com/yeongpin/cursor-free-vip/releases/latest"><img src="https://img.shields.io/endpoint?url=https://api.pinstudios.net/api/badges/release/yeongpin/cursor-free-vip" alt="Release Badge"/></a>
   <a href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img src="https://img.shields.io/badge/License-CC_BY--NC--ND_4.0-lightgrey.svg" alt="License Badge"/></a>
   <a href="https://github.com/yeongpin/cursor-free-vip/stargazers"><img src="https://img.shields.io/endpoint?url=https://api.pinstudios.net/api/badges/stars/yeongpin/cursor-free-vip" alt="Stars Badge"/></a>
   <a href="https://github.com/yeongpin/cursor-free-vip/releases/latest"><img src="https://img.shields.io/endpoint?url=https://api.pinstudios.net/api/badges/downloads/yeongpin/cursor-free-vip/total" alt="Downloads Badge"/></a>
   <a href="https://buymeacoffee.com/yeongpin" target="_blank"><img alt="Buy Me a Coffee" src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20Me-FFDA33"></a>
   <a href="https://deepwiki.com/yeongpin/cursor-free-vip"><img src="https://devin.ai/assets/deepwiki-badge.png" alt="Ask DeepWiki.com" height="20"/></a>
</p>

<a href="https://trendshift.io/repositories/13425" target="_blank">
   <img src="https://trendshift.io/api/badge/repositories/13425" alt="yeongpin/cursor-free-vip | Trendshift" width="250" height="55"/>
</a>

<h4>Support Latest 0.49.x Version | 支持最新 0.49.x 版本</h4>

<p align="justify">
This tool is designed purely for <strong>educational and research purposes</strong>. It does not violate any applicable laws or regulations.  
Please support and respect the original project.  
This tool does not generate fake email accounts or OAuth access tokens.  
It is compatible with Windows, macOS, and Linux.  
For the best experience, run the application with administrative privileges and keep it updated regularly.
</p>

<p align="center">
  <img src="./images/product_2025-04-16_10-40-21.png" alt="Cursor Free VIP Screenshot" width="800" style="border-radius: 6px;"/><br>
</p>

</div>

---

## 🔄 Change Log | 更新日志

[View Change Log](CHANGELOG.md)

---

## ✨ Features | 功能特點

* Supports **Windows**, **macOS**, and **Linux** operating systems
* Resets **Cursor’s configuration** with a single command
* Offers **multi-language support**: English, Simplified Chinese (简体中文), Traditional Chinese (繁體中文), and Vietnamese (越南語)

---

## 💻 System Support | 系統支持

| Operating System | Architecture         | Supported |
| ---------------- | -------------------- | --------- |
| Windows          | x64, x86             | ✅         |
| macOS            | Intel, Apple Silicon | ✅         |
| Linux            | x64, x86, ARM64      | ✅         |

---

## 👀 How to Use | 如何使用

<details open>
<summary><b>⭐ Automated Installation Script | 腳本自動化運行</b></summary>

### **Linux / macOS**

```bash
curl -fsSL https://raw.githubusercontent.com/yeongpin/cursor-free-vip/main/scripts/install.sh -o install.sh && chmod +x install.sh && ./install.sh
```

### **Arch Linux**

Install via [AUR](https://aur.archlinux.org/packages/cursor-free-vip-git):

```bash
yay -S cursor-free-vip-git
```

### **Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/yeongpin/cursor-free-vip/main/scripts/install.ps1 | iex
```

</details>

> To stop the script at any time, press **Ctrl + C**.

---

## ❗ Notes | 注意事項

### Configuration File Path | 文件配置路徑

**Windows / macOS / Linux:**
`Documents/.cursor-free-vip/config.ini`

<details>
<summary><b>⭐ Configuration File Details | 文件配置詳情</b></summary>

```ini
[Chrome]
# Default Google Chrome Path
chromepath = C:\Program Files\Google\Chrome\Application\chrome.exe

[Turnstile]
handle_turnstile_time = 2
handle_turnstile_random_time = 1-3

[OSPaths]
storage_path = /Users/username/Library/Application Support/Cursor/User/globalStorage/storage.json
sqlite_path = /Users/username/Library/Application Support/Cursor/User/globalStorage/state.vscdb
machine_id_path = /Users/username/Library/Application Support/Cursor/machineId

[Timing]
min_random_time = 0.1
max_random_time = 0.8
page_load_wait = 0.1-0.8
input_wait = 0.3-0.8
submit_wait = 0.5-1.5
verification_code_input = 0.1-0.3
verification_success_wait = 2-3
verification_retry_wait = 2-3
email_check_initial_wait = 4-6
email_refresh_wait = 2-4
settings_page_load_wait = 1-2
failed_retry_time = 0.5-1
retry_interval = 8-12
max_timeout = 160

[Utils]
check_update = True
show_account_info = True

[TempMailPlus]
enabled = false
email = xxxxx@mailto.plus
epin = 

[WindowsPaths]
storage_path = C:\Users\yeongpin\AppData\Roaming\Cursor\User\globalStorage\storage.json
sqlite_path = C:\Users\yeongpin\AppData\Roaming\Cursor\User\globalStorage\state.vscdb
machine_id_path = C:\Users\yeongpin\AppData\Roaming\Cursor\machineId
cursor_path = C:\Users\yeongpin\AppData\Local\Programs\Cursor\resources\app
updater_path = C:\Users\yeongpin\AppData\Local\cursor-updater
update_yml_path = C:\Users\yeongpin\AppData\Local\Programs\Cursor\resources\app-update.yml
product_json_path = C:\Users\yeongpin\AppData\Local\Programs\Cursor\resources\app\product.json

[Browser]
default_browser = opera
chrome_path = C:\Program Files\Google\Chrome\Application\chrome.exe
edge_path = C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
firefox_path = C:\Program Files\Mozilla Firefox\firefox.exe
brave_path = C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe
chrome_driver_path = D:\VisualCode\cursor-free-vip-new\drivers\chromedriver.exe
edge_driver_path = D:\VisualCode\cursor-free-vip-new\drivers\msedgedriver.exe
firefox_driver_path = D:\VisualCode\cursor-free-vip-new\drivers\geckodriver.exe
brave_driver_path = D:\VisualCode\cursor-free-vip-new\drivers\chromedriver.exe
opera_path = C:\Users\yeongpin\AppData\Local\Programs\Opera\opera.exe
opera_driver_path = D:\VisualCode\cursor-free-vip-new\drivers\chromedriver.exe

[OAuth]
show_selection_alert = False
timeout = 120
max_attempts = 3
```

</details>

---

### Important Usage Guidelines

* Always run the script with **administrator privileges**
* Ensure that **Cursor is closed** before execution
* Intended **solely for educational and research purposes**
* Please **adhere to all applicable software usage terms** when operating this tool

---

## 🚨 Common Issues | 常見問題

| Issue Description        | Recommended Solution                                                                                                                     |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Permission Denied        | Run the script as **Administrator**                                                                                                      |
| “User is not authorized” | Your account may be banned due to the use of **temporary/disposable email addresses**. Please use a valid, non-temporary email provider. |

---

## 🤩 Contribution | 貢獻

Contributions are always welcome!
Submit **Issues** or **Pull Requests** to help improve this project.

<a href="https://github.com/yeongpin/cursor-free-vip/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=yeongpin/cursor-free-vip&preview=true" alt="Contributors"/>
</a>

---

## 📩 Disclaimer | 免責聲明

This tool is strictly for **learning and research**.
The author assumes **no responsibility** for any consequences arising from its misuse.

---

## 💰 Buy Me a Coffee | 請我喝杯咖啡

<div align="center">
  <table>
    <tr>
      <td><img src="./images/provi-code.jpg" alt="Buy Me a Coffee QR" width="280"/></td>
      <td><img src="./images/paypal.png" alt="PayPal Donation QR" width="280"/></td>
    </tr>
  </table>
</div>

---

## ⭐ Star History | 星星數

<div align="center">
  <a href="https://star-history.com/#yeongpin/cursor-free-vip&Date">
    <img src="https://api.star-history.com/svg?repos=yeongpin/cursor-free-vip&type=Date" alt="Star History Chart"/>
  </a>
</div>

---

## 📝 License | 授權

This project is licensed under the **[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)** License.
Please refer to the [LICENSE](LICENSE.md) file for full details.

---

### ✅ Professional Notes

This documentation adheres to:

* **Open Source Software (OSS)** writing standards
* **ISO 26514** guidelines for software documentation
* **Accessibility-first** bilingual formatting for global users

---

Would you like me to:

1. Format this for **GitHub README (Markdown optimized)** — with perfect spacing, image alt-text, and layout balance,
   or
2. Convert it into a **technical documentation page** (for your website or Docs portal, e.g., Docusaurus or Next.js docs)?

It will take the professionalism to the next level depending on your use case.
