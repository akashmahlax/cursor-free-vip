# 🚀 Professional Setup Guide for cursor-free-vip

## Prerequisites

### 1. Install Python

**Download Python 3.10 or higher:**
- Go to https://www.python.org/downloads/
- Download Python 3.10+ (recommended: Python 3.11 or 3.12)
- **IMPORTANT:** During installation, check "Add Python to PATH"

**Verify Installation:**
```powershell
python --version
# Should show: Python 3.x.x
```

## 2. Professional Setup Steps

### Step 1: Create Virtual Environment

```powershell
# Navigate to project directory
cd c:\Users\akash\upwork\cursor-free-vip

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 2: Install Dependencies

```powershell
# Ensure pip is up to date
python -m pip install --upgrade pip

# Install all project dependencies
pip install -r requirements.txt
```

### Step 3: Run the Application

```powershell
# With virtual environment activated
python main.py
```

## 3. Deactivate Virtual Environment (when done)

```powershell
deactivate
```

## 4. Best Practices for Development

### Always Activate Virtual Environment First
```powershell
cd c:\Users\akash\upwork\cursor-free-vip
.\venv\Scripts\Activate.ps1
```

### Install New Packages (within venv)
```powershell
pip install package-name
pip freeze > requirements.txt  # Update requirements
```

### Run Tests
```powershell
python main.py
```

## 5. Project Structure

```
cursor-free-vip/
├── venv/                    # Virtual environment (you'll create this)
├── main.py                  # Main entry point
├── config.py                # Configuration management
├── utils.py                 # Utility functions
├── requirements.txt         # Python dependencies
├── locales/                 # Translation files
├── scripts/                 # Installation scripts
└── email_tabs/              # Email automation modules
```

## 6. Common Issues & Solutions

### Issue: "Execution Policy" Error
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: pip not recognized
```powershell
python -m pip install --upgrade pip
```

### Issue: Module not found
```powershell
# Make sure venv is activated and reinstall
pip install -r requirements.txt
```

## 7. Git Workflow (For Contributing)

### First Time Setup
```powershell
# Fork the repository on GitHub first, then:
git clone https://github.com/YOUR-USERNAME/cursor-free-vip.git
cd cursor-free-vip
git remote add upstream https://github.com/yeongpin/cursor-free-vip.git
```

### Making Changes
```powershell
# Create a new branch
git checkout -b feature/your-feature-name

# Make your changes, then:
git add .
git commit -m "Description of changes"
git push origin feature/your-feature-name
```

### Keeping Your Fork Updated
```powershell
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

## 8. Testing Your Changes

Before submitting a PR:
1. Test all menu options
2. Verify configuration files are created correctly
3. Check multi-language support
4. Ensure no errors in console
5. Test on clean environment

## 9. Code Quality Tools (Recommended)

```powershell
# Install development tools
pip install black flake8 mypy pylint

# Format code
black .

# Check for issues
flake8 .
pylint *.py
mypy .
```

## 10. Documentation

When contributing, ensure:
- Update CHANGELOG.md with your changes
- Add docstrings to new functions
- Update README.md if adding new features
- Add translations for new strings in all locale files
