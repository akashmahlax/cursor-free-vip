"""
Automatic Cursor Installation Path Detection
Detects Cursor installation across different machines and operating systems
"""
import os
import sys
import platform
import subprocess
import winreg
from pathlib import Path
from typing import Optional, List


def find_cursor_windows() -> Optional[str]:
    """
    Find Cursor installation on Windows by checking multiple locations
    Returns the resources/app path if found
    """
    possible_paths = []
    
    # Method 1: Check if Cursor process is running and get its path
    try:
        result = subprocess.run(
            ['powershell', '-Command', 
             "Get-Process cursor -ErrorAction SilentlyContinue | Select-Object -First 1 | ForEach-Object { $_.Path }"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.stdout.strip():
            cursor_exe = result.stdout.strip()
            # Extract base directory
            cursor_dir = os.path.dirname(cursor_exe)
            app_path = os.path.join(cursor_dir, "resources", "app")
            if os.path.exists(app_path):
                return app_path
    except Exception as e:
        pass
    
    # Method 2: Check registry for installation path
    try:
        # Check HKEY_CURRENT_USER
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Cursor") as key:
            install_path = winreg.QueryValueEx(key, "InstallLocation")[0]
            app_path = os.path.join(install_path, "resources", "app")
            if os.path.exists(app_path):
                return app_path
    except Exception:
        pass
    
    try:
        # Check HKEY_LOCAL_MACHINE
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Cursor") as key:
            install_path = winreg.QueryValueEx(key, "InstallLocation")[0]
            app_path = os.path.join(install_path, "resources", "app")
            if os.path.exists(app_path):
                return app_path
    except Exception:
        pass
    
    # Method 3: Check common installation directories
    username = os.getenv('USERNAME', '')
    program_files = os.getenv('PROGRAMFILES', 'C:\\Program Files')
    program_files_x86 = os.getenv('PROGRAMFILES(X86)', 'C:\\Program Files (x86)')
    local_appdata = os.getenv('LOCALAPPDATA', f'C:\\Users\\{username}\\AppData\\Local')
    appdata = os.getenv('APPDATA', f'C:\\Users\\{username}\\AppData\\Roaming')
    
    possible_paths = [
        # User-specific installations
        os.path.join(local_appdata, "Programs", "Cursor", "resources", "app"),
        os.path.join(appdata, "Cursor", "resources", "app"),
        
        # System-wide installations
        os.path.join(program_files, "cursor", "resources", "app"),
        os.path.join(program_files, "Cursor", "resources", "app"),
        os.path.join(program_files_x86, "cursor", "resources", "app"),
        os.path.join(program_files_x86, "Cursor", "resources", "app"),
        
        # Portable installations
        "C:\\cursor\\resources\\app",
        "C:\\Cursor\\resources\\app",
        os.path.join("D:\\", "cursor", "resources", "app"),
        os.path.join("D:\\", "Cursor", "resources", "app"),
    ]
    
    # Method 4: Search all drives for Cursor
    try:
        import string
        drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]
        for drive in drives[:3]:  # Check first 3 drives only (usually C, D, E)
            possible_paths.extend([
                os.path.join(drive, "Program Files", "cursor", "resources", "app"),
                os.path.join(drive, "Program Files", "Cursor", "resources", "app"),
                os.path.join(drive, "cursor", "resources", "app"),
                os.path.join(drive, "Cursor", "resources", "app"),
            ])
    except Exception:
        pass
    
    # Check all possible paths
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None


def find_cursor_macos() -> Optional[str]:
    """Find Cursor installation on macOS"""
    possible_paths = [
        "/Applications/Cursor.app/Contents/Resources/app",
        os.path.expanduser("~/Applications/Cursor.app/Contents/Resources/app"),
    ]
    
    # Check if Cursor process is running
    try:
        result = subprocess.run(
            ['ps', 'aux'],
            capture_output=True,
            text=True,
            timeout=5
        )
        for line in result.stdout.split('\n'):
            if 'Cursor.app' in line:
                # Extract path from process info
                parts = line.split()
                for part in parts:
                    if 'Cursor.app' in part:
                        app_bundle = part.split('Cursor.app')[0] + 'Cursor.app'
                        resources_path = os.path.join(app_bundle, 'Contents', 'Resources', 'app')
                        if os.path.exists(resources_path):
                            return resources_path
    except Exception:
        pass
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None


def find_cursor_linux() -> Optional[str]:
    """Find Cursor installation on Linux"""
    possible_paths = [
        "/opt/Cursor/resources/app",
        "/opt/cursor/resources/app",
        "/usr/share/cursor/resources/app",
        "/usr/lib/cursor/resources/app",
        "/usr/local/share/cursor/resources/app",
        "/usr/local/lib/cursor/resources/app",
        os.path.expanduser("~/.local/share/cursor/resources/app"),
        os.path.expanduser("~/cursor/resources/app"),
        os.path.expanduser("~/squashfs-root/usr/share/cursor/resources/app"),  # AppImage
    ]
    
    # Check if Cursor process is running
    try:
        result = subprocess.run(
            ['ps', 'aux'],
            capture_output=True,
            text=True,
            timeout=5
        )
        for line in result.stdout.split('\n'):
            if 'cursor' in line.lower():
                parts = line.split()
                for part in parts:
                    if 'cursor' in part.lower() and os.path.isfile(part):
                        cursor_dir = os.path.dirname(part)
                        resources_path = os.path.join(cursor_dir, 'resources', 'app')
                        if os.path.exists(resources_path):
                            return resources_path
    except Exception:
        pass
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None


def find_cursor_installation() -> Optional[str]:
    """
    Automatically detect Cursor installation path across different operating systems
    Returns the path to resources/app directory
    """
    system = platform.system()
    
    if system == "Windows":
        return find_cursor_windows()
    elif system == "Darwin":
        return find_cursor_macos()
    elif system == "Linux":
        return find_cursor_linux()
    else:
        return None


def get_workbench_path(cursor_app_path: str) -> str:
    """
    Get the workbench.desktop.main.js path from cursor app path
    """
    system = platform.system()
    
    if system == "Windows":
        return os.path.join(cursor_app_path, "out", "vs", "workbench", "workbench.desktop.main.js")
    else:  # macOS and Linux use forward slashes
        return os.path.join(cursor_app_path, "out/vs/workbench/workbench.desktop.main.js")


def verify_cursor_installation() -> dict:
    """
    Verify Cursor installation and return installation details
    Returns dict with: found, app_path, workbench_path, version (if available)
    """
    result = {
        "found": False,
        "app_path": None,
        "workbench_path": None,
        "system": platform.system(),
        "error": None
    }
    
    try:
        app_path = find_cursor_installation()
        
        if app_path is None:
            result["error"] = "Cursor installation not found"
            return result
        
        if not os.path.exists(app_path):
            result["error"] = f"Path exists but not accessible: {app_path}"
            return result
        
        workbench_path = get_workbench_path(app_path)
        
        if not os.path.exists(workbench_path):
            result["error"] = f"Workbench file not found: {workbench_path}"
            return result
        
        result["found"] = True
        result["app_path"] = app_path
        result["workbench_path"] = workbench_path
        
        # Try to get version info
        try:
            package_json = os.path.join(os.path.dirname(app_path), "package.json")
            if os.path.exists(package_json):
                import json
                with open(package_json, 'r') as f:
                    data = json.load(f)
                    result["version"] = data.get("version", "unknown")
        except Exception:
            result["version"] = "unknown"
        
        return result
        
    except Exception as e:
        result["error"] = str(e)
        return result


if __name__ == "__main__":
    """Test the detection"""
    print("🔍 Detecting Cursor installation...")
    print(f"Operating System: {platform.system()}")
    print("-" * 50)
    
    info = verify_cursor_installation()
    
    if info["found"]:
        print("✅ Cursor installation found!")
        print(f"📁 App Path: {info['app_path']}")
        print(f"📄 Workbench Path: {info['workbench_path']}")
        if "version" in info:
            print(f"🔢 Version: {info['version']}")
    else:
        print("❌ Cursor installation not found")
        print(f"Error: {info.get('error', 'Unknown error')}")
        print("\nPlease make sure Cursor is installed on your system.")
