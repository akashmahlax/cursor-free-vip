"""
Comprehensive functionality test for cursor-free-vip
Tests all major features to ensure they work correctly
"""
import os
import sys
from colorama import Fore, Style, init

init()

def print_test(name, status, message=""):
    """Print test result"""
    if status:
        print(f"{Fore.GREEN}✅ {name}{Style.RESET_ALL} {message}")
    else:
        print(f"{Fore.RED}❌ {name}{Style.RESET_ALL} {message}")
    return status

def test_imports():
    """Test that all modules can be imported"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"Testing Module Imports")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    modules = [
        'config',
        'utils', 
        'logo',
        'bypass_token_limit',
        'bypass_version',
        'quit_cursor',
        'disable_auto_update',
        'cursor_acc_info',
    ]
    
    results = []
    for module in modules:
        try:
            __import__(module)
            results.append(print_test(f"Import {module}", True))
        except Exception as e:
            results.append(print_test(f"Import {module}", False, f"- Error: {e}"))
    
    return all(results)

def test_config():
    """Test configuration"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"Testing Configuration")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    try:
        from config import get_config
        from utils import get_user_documents_path
        
        results = []
        
        # Test config loading
        config = get_config()
        results.append(print_test("Load configuration", config is not None))
        
        # Test required sections
        required_sections = ['Browser', 'Timing', 'Utils', 'WindowsPaths']
        for section in required_sections:
            has_section = config.has_section(section)
            results.append(print_test(f"Config section [{section}]", has_section))
        
        # Test cursor path
        cursor_path = config.get('WindowsPaths', 'cursor_path')
        path_correct = r'C:\Program Files\cursor' in cursor_path
        results.append(print_test("Cursor path configured", path_correct, f"- {cursor_path}"))
        
        # Check if workbench file exists
        workbench_path = os.path.join(cursor_path, 'out', 'vs', 'workbench', 'workbench.desktop.main.js')
        exists = os.path.exists(workbench_path)
        results.append(print_test("Workbench file exists", exists, f"- {workbench_path}"))
        
        return all(results)
        
    except Exception as e:
        print_test("Configuration test", False, f"- Error: {e}")
        return False

def test_utils():
    """Test utility functions"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"Testing Utility Functions")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    try:
        from utils import (
            get_user_documents_path,
            get_default_browser_path,
            get_default_driver_path,
        )
        
        results = []
        
        # Test documents path
        docs_path = get_user_documents_path()
        results.append(print_test("Get documents path", 
                                 docs_path and len(docs_path) > 0,
                                 f"- {docs_path}"))
        
        # Test browser paths
        browsers = ['chrome', 'firefox', 'edge', 'brave', 'opera']
        for browser in browsers:
            path = get_default_browser_path(browser)
            results.append(print_test(f"Get {browser} path", 
                                     path and len(path) > 0))
        
        # Test driver paths
        for browser in ['chrome', 'firefox', 'edge']:
            path = get_default_driver_path(browser)
            results.append(print_test(f"Get {browser} driver path", 
                                     path and len(path) > 0))
        
        return all(results)
        
    except Exception as e:
        print_test("Utility functions test", False, f"- Error: {e}")
        return False

def test_cursor_detection():
    """Test Cursor detection"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"Testing Cursor Detection")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    try:
        import psutil
        
        # Check if Cursor is running
        cursor_running = any('cursor' in p.name().lower() for p in psutil.process_iter(['name']))
        print_test("Cursor process detected", cursor_running)
        
        # Check Cursor installation
        cursor_path = r'C:\Program Files\cursor\Cursor.exe'
        cursor_installed = os.path.exists(cursor_path)
        print_test("Cursor executable found", cursor_installed, f"- {cursor_path}")
        
        return cursor_installed
        
    except Exception as e:
        print_test("Cursor detection test", False, f"- Error: {e}")
        return False

def test_bypass_token_limit():
    """Test bypass token limit functionality"""
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"Testing Bypass Token Limit")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    try:
        from config import get_config
        config = get_config()
        
        results = []
        
        # Check workbench file
        cursor_path = config.get('WindowsPaths', 'cursor_path')
        workbench_path = os.path.join(cursor_path, 'out', 'vs', 'workbench', 'workbench.desktop.main.js')
        
        file_exists = os.path.exists(workbench_path)
        results.append(print_test("Workbench file accessible", file_exists))
        
        # Check for backup
        backup_dir = os.path.dirname(workbench_path)
        backup_files = [f for f in os.listdir(backup_dir) if 'backup' in f and 'workbench' in f]
        has_backup = len(backup_files) > 0
        results.append(print_test("Backup file exists", has_backup, 
                                 f"- {backup_files[0] if backup_files else 'None'}"))
        
        # Check file size (modified file should be different)
        if file_exists:
            file_size = os.path.getsize(workbench_path)
            results.append(print_test("Workbench file readable", file_size > 0,
                                     f"- Size: {file_size:,} bytes"))
        
        return all(results)
        
    except Exception as e:
        print_test("Bypass token limit test", False, f"- Error: {e}")
        return False

def main():
    """Run all tests"""
    print(f"\n{Fore.YELLOW}{'='*60}")
    print(f"🧪 Cursor Free VIP - Functionality Test Suite")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    results = {
        'Imports': test_imports(),
        'Configuration': test_config(),
        'Utilities': test_utils(),
        'Cursor Detection': test_cursor_detection(),
        'Bypass Token Limit': test_bypass_token_limit(),
    }
    
    # Summary
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"📊 Test Summary")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    total = len(results)
    passed = sum(1 for v in results.values() if v)
    failed = total - passed
    
    for name, status in results.items():
        status_icon = "✅" if status else "❌"
        status_text = "PASSED" if status else "FAILED"
        color = Fore.GREEN if status else Fore.RED
        print(f"{status_icon} {name}: {color}{status_text}{Style.RESET_ALL}")
    
    print(f"\n{Fore.YELLOW}{'='*60}")
    print(f"Total: {total} | Passed: {Fore.GREEN}{passed}{Fore.YELLOW} | Failed: {Fore.RED}{failed}{Fore.YELLOW}")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    if passed == total:
        print(f"{Fore.GREEN}🎉 All tests passed! Everything is working correctly!{Style.RESET_ALL}\n")
        return 0
    else:
        print(f"{Fore.YELLOW}⚠️  Some tests failed. Please check the issues above.{Style.RESET_ALL}\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
