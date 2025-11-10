"""
Pytest configuration and fixtures
"""
import pytest
import os
import tempfile
import shutil
from pathlib import Path


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files"""
    temp_path = tempfile.mkdtemp()
    yield temp_path
    # Cleanup after test
    shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def mock_config_file(temp_dir):
    """Create a mock configuration file"""
    config_content = """
[Browser]
default_browser = chrome

[Timing]
min_random_time = 0.1
max_random_time = 0.5

[Utils]
enabled_update_check = False
enabled_account_info = False
"""
    config_path = os.path.join(temp_dir, "config.ini")
    with open(config_path, 'w') as f:
        f.write(config_content)
    
    return config_path


@pytest.fixture
def mock_translator():
    """Create a mock translator for testing"""
    class MockTranslator:
        def get(self, key, **kwargs):
            # Return the key itself for testing
            return key.format(**kwargs) if kwargs else key
    
    return MockTranslator()


@pytest.fixture(autouse=True)
def reset_environment():
    """Reset environment variables before each test"""
    # Store original environment
    original_env = os.environ.copy()
    
    yield
    
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)
