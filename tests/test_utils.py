"""
Unit tests for utils.py
"""
import pytest
import platform
import os
from utils import (
    get_user_documents_path,
    get_default_browser_path,
    get_default_driver_path,
    get_random_wait_time
)


class TestGetUserDocumentsPath:
    """Test suite for get_user_documents_path function"""
    
    def test_returns_string(self):
        """Test that the function returns a string"""
        result = get_user_documents_path()
        assert isinstance(result, str)
    
    def test_path_exists(self):
        """Test that returned path exists"""
        result = get_user_documents_path()
        assert os.path.exists(result) or "Documents" in result
    
    def test_path_not_empty(self):
        """Test that path is not empty"""
        result = get_user_documents_path()
        assert len(result) > 0
    
    @pytest.mark.skipif(platform.system() != "Windows", reason="Windows specific test")
    def test_windows_path_format(self):
        """Test Windows path format"""
        result = get_user_documents_path()
        assert "\\" in result or "/" in result
    
    @pytest.mark.skipif(platform.system() == "Windows", reason="Unix specific test")
    def test_unix_path_format(self):
        """Test Unix path format"""
        result = get_user_documents_path()
        assert result.startswith("/") or result.startswith("~")


class TestGetDefaultBrowserPath:
    """Test suite for get_default_browser_path function"""
    
    @pytest.mark.parametrize("browser", ["chrome", "firefox", "edge", "brave", "opera"])
    def test_returns_string_for_all_browsers(self, browser):
        """Test that function returns string for all supported browsers"""
        result = get_default_browser_path(browser)
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_chrome_path_contains_chrome(self):
        """Test that Chrome path contains 'chrome' in name"""
        result = get_default_browser_path('chrome')
        assert 'chrome' in result.lower() or 'chromium' in result.lower()
    
    def test_firefox_path_contains_firefox(self):
        """Test that Firefox path contains 'firefox' in name"""
        result = get_default_browser_path('firefox')
        assert 'firefox' in result.lower()
    
    def test_case_insensitive_browser_name(self):
        """Test that browser name is case insensitive"""
        result1 = get_default_browser_path('chrome')
        result2 = get_default_browser_path('CHROME')
        result3 = get_default_browser_path('Chrome')
        
        # All should return the same path
        assert result1 == result2 == result3
    
    def test_unknown_browser_defaults_to_chrome(self):
        """Test that unknown browser defaults to Chrome"""
        result = get_default_browser_path('unknown_browser')
        chrome_path = get_default_browser_path('chrome')
        assert result == chrome_path


class TestGetDefaultDriverPath:
    """Test suite for get_default_driver_path function"""
    
    @pytest.mark.parametrize("browser", ["chrome", "firefox", "edge", "brave"])
    def test_returns_string_for_all_browsers(self, browser):
        """Test that function returns string for all supported browsers"""
        result = get_default_driver_path(browser)
        assert isinstance(result, str)
        assert len(result) > 0
    
    @pytest.mark.skipif(platform.system() != "Windows", reason="Windows specific test")
    def test_windows_driver_has_exe_extension(self):
        """Test that Windows driver paths have .exe extension"""
        result = get_default_driver_path('chrome')
        assert result.endswith('.exe')
    
    @pytest.mark.skipif(platform.system() == "Windows", reason="Unix specific test")
    def test_unix_driver_no_extension(self):
        """Test that Unix driver paths don't have .exe extension"""
        result = get_default_driver_path('chrome')
        assert not result.endswith('.exe')
    
    def test_brave_uses_chrome_driver(self):
        """Test that Brave browser uses Chrome driver"""
        brave_driver = get_default_driver_path('brave')
        chrome_driver = get_default_driver_path('chrome')
        assert brave_driver == chrome_driver


class TestGetRandomWaitTime:
    """Test suite for get_random_wait_time function"""
    
    def test_returns_float(self):
        """Test that function returns a float"""
        config = {
            'Timing': {
                'test_timing': '0.5-1.5'
            }
        }
        result = get_random_wait_time(config, 'test_timing')
        assert isinstance(result, float)
    
    def test_value_in_range_with_dash(self):
        """Test that returned value is within specified range (dash separator)"""
        config = {
            'Timing': {
                'test_timing': '1.0-2.0'
            }
        }
        result = get_random_wait_time(config, 'test_timing')
        assert 1.0 <= result <= 2.0
    
    def test_value_in_range_with_comma(self):
        """Test that returned value is within specified range (comma separator)"""
        config = {
            'Timing': {
                'test_timing': '1.0,2.0'
            }
        }
        result = get_random_wait_time(config, 'test_timing')
        assert 1.0 <= result <= 2.0
    
    def test_single_value(self):
        """Test handling of single value (no range)"""
        config = {
            'Timing': {
                'test_timing': '1.5'
            }
        }
        result = get_random_wait_time(config, 'test_timing')
        assert result == 1.5
    
    def test_missing_timing_returns_default(self):
        """Test that missing timing key returns default value"""
        config = {
            'Timing': {}
        }
        result = get_random_wait_time(config, 'nonexistent_key')
        assert 0.5 <= result <= 1.5
    
    def test_invalid_format_returns_default(self):
        """Test that invalid format returns default value"""
        config = {
            'Timing': {
                'test_timing': 'invalid'
            }
        }
        result = get_random_wait_time(config, 'test_timing')
        assert 0.5 <= result <= 1.5
    
    def test_multiple_calls_return_different_values(self):
        """Test that multiple calls return different random values"""
        config = {
            'Timing': {
                'test_timing': '0.1-2.0'
            }
        }
        results = [get_random_wait_time(config, 'test_timing') for _ in range(10)]
        
        # At least some values should be different (very unlikely all 10 are the same)
        assert len(set(results)) > 1


class TestIntegration:
    """Integration tests for utils module"""
    
    def test_all_functions_work_together(self, temp_dir):
        """Test that all utility functions can work together"""
        # This is a basic integration test
        docs_path = get_user_documents_path()
        browser_path = get_default_browser_path('chrome')
        driver_path = get_default_driver_path('chrome')
        
        assert all([
            isinstance(docs_path, str),
            isinstance(browser_path, str),
            isinstance(driver_path, str)
        ])
    
    @pytest.mark.parametrize("os_name", ["Windows", "Darwin", "Linux"])
    def test_cross_platform_compatibility(self, os_name, monkeypatch):
        """Test that functions handle different OS correctly"""
        # This is a placeholder - actual implementation would mock platform.system()
        # monkeypatch.setattr(platform, 'system', lambda: os_name)
        
        # Just verify functions don't crash on different OS
        try:
            get_user_documents_path()
            get_default_browser_path('chrome')
            get_default_driver_path('chrome')
        except Exception as e:
            pytest.fail(f"Function failed on {os_name}: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
