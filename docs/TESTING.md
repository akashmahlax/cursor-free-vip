# Testing Guide for cursor-free-vip

## Overview

This guide explains how to run and write tests for the cursor-free-vip project.

## Prerequisites

```powershell
# Install development dependencies
pip install -r requirements-dev.txt
```

## Running Tests

### Run All Tests
```powershell
pytest
```

### Run Tests with Coverage
```powershell
pytest --cov=. --cov-report=html
# Open htmlcov/index.html to view coverage report
```

### Run Specific Test File
```powershell
pytest tests/test_utils.py
```

### Run Specific Test Function
```powershell
pytest tests/test_utils.py::TestGetUserDocumentsPath::test_returns_string
```

### Run Tests in Parallel
```powershell
pytest -n auto  # Uses all CPU cores
```

### Run Tests with Verbose Output
```powershell
pytest -v
```

### Run Only Fast Tests (skip slow tests)
```powershell
pytest -m "not slow"
```

## Test Structure

```
tests/
├── __init__.py              # Test package initialization
├── conftest.py              # Shared fixtures and configuration
├── test_utils.py            # Tests for utils.py
├── test_config.py           # Tests for config.py (to be created)
├── test_translator.py       # Tests for translator functionality (to be created)
└── test_integration.py      # Integration tests (to be created)
```

## Writing Tests

### Basic Test Structure

```python
import pytest
from your_module import your_function

class TestYourFunction:
    """Test suite for your_function"""
    
    def test_basic_functionality(self):
        """Test basic functionality"""
        result = your_function()
        assert result == expected_value
    
    def test_edge_case(self):
        """Test edge case"""
        result = your_function(edge_case_input)
        assert result is not None
```

### Using Fixtures

```python
def test_with_temp_dir(temp_dir):
    """Test using temporary directory fixture"""
    test_file = os.path.join(temp_dir, "test.txt")
    with open(test_file, 'w') as f:
        f.write("test content")
    assert os.path.exists(test_file)
```

### Parameterized Tests

```python
@pytest.mark.parametrize("input,expected", [
    ("chrome", "/path/to/chrome"),
    ("firefox", "/path/to/firefox"),
    ("edge", "/path/to/edge"),
])
def test_browser_paths(input, expected):
    """Test multiple browser paths"""
    result = get_browser_path(input)
    assert expected in result
```

### Mocking

```python
from unittest.mock import Mock, patch

def test_with_mock():
    """Test using mocks"""
    with patch('platform.system') as mock_system:
        mock_system.return_value = 'Windows'
        result = get_platform_specific_path()
        assert 'C:\\' in result
```

### Testing Exceptions

```python
def test_raises_exception():
    """Test that function raises expected exception"""
    with pytest.raises(ValueError):
        your_function(invalid_input)
```

## Test Coverage

### View Coverage Report
```powershell
pytest --cov=. --cov-report=html
start htmlcov/index.html  # Windows
```

### Coverage Goals
- **Minimum**: 70% overall coverage
- **Target**: 80%+ overall coverage
- **Critical modules**: 90%+ coverage (utils.py, config.py)

## Continuous Integration

Tests are automatically run on:
- Every push to repository
- Every pull request
- Before releases

### GitHub Actions Workflow
See `.github/workflows/test.yml` for CI configuration

## Best Practices

### 1. Test Naming
- Use descriptive names that explain what is being tested
- Follow pattern: `test_<function>_<scenario>_<expected_result>`
```python
def test_get_config_missing_file_creates_default()
def test_translator_invalid_language_falls_back_to_english()
```

### 2. Test Independence
- Each test should be independent
- Don't rely on test execution order
- Clean up after tests using fixtures

### 3. Use Fixtures
- Create reusable fixtures in conftest.py
- Use fixtures for setup/teardown
- Share fixtures across test files

### 4. Test Documentation
- Add docstrings to test functions
- Explain the purpose of the test
- Document expected behavior

### 5. Assertions
- Use clear, specific assertions
- One logical assertion per test (when possible)
- Provide helpful error messages

```python
# Good
assert result == expected, f"Expected {expected}, got {result}"

# Better for complex objects
from pytest import approx
assert result == approx(expected, rel=1e-3)
```

## Debugging Tests

### Run with PDB
```powershell
pytest --pdb  # Drop into debugger on failure
```

### Run with Print Statements
```powershell
pytest -s  # Show print statements
```

### Run Specific Failed Tests
```powershell
pytest --lf  # Run last failed
pytest --ff  # Run failed first
```

## Performance Testing

### Profile Tests
```python
import pytest

@pytest.mark.slow
def test_slow_operation():
    """Mark slow tests"""
    # Long running test
    pass
```

### Skip Tests Conditionally
```python
@pytest.mark.skipif(condition, reason="Skip reason")
def test_conditional():
    pass

@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass
```

## Integration Testing

### Example Integration Test
```python
class TestIntegration:
    """Integration tests for complete workflows"""
    
    def test_full_reset_workflow(self, temp_dir, mock_config):
        """Test complete reset workflow"""
        # 1. Setup
        config = load_config(mock_config)
        
        # 2. Execute
        resetter = MachineIDResetter(config)
        result = resetter.reset_machine_ids()
        
        # 3. Verify
        assert result is True
        assert verify_reset_successful()
```

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```powershell
   # Ensure you're in project root
   cd c:\Users\akash\upwork\cursor-free-vip
   # Run tests
   pytest
   ```

2. **Module Not Found**
   ```powershell
   # Install test dependencies
   pip install -r requirements-dev.txt
   ```

3. **Platform-Specific Failures**
   ```python
   # Skip platform-specific tests
   @pytest.mark.skipif(platform.system() != "Windows", reason="Windows only")
   ```

4. **Fixture Not Found**
   - Check conftest.py location
   - Ensure fixture is properly defined
   - Verify fixture scope

## Resources

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Best Practices](https://docs.pytest.org/en/stable/goodpractices.html)
- [Testing Best Practices](https://docs.python-guide.org/writing/tests/)
- [Coverage.py](https://coverage.readthedocs.io/)

## Contributing Tests

When contributing, please:
1. Add tests for new features
2. Update existing tests when changing functionality
3. Ensure all tests pass before submitting PR
4. Aim for >80% coverage on new code
5. Follow existing test patterns
