# 🚀 Quick Reference Card

## Daily Workflow Commands

### Start Working
```powershell
cd c:\Users\akash\upwork\cursor-free-vip
.\venv\Scripts\Activate.ps1
```

### Run Application
```powershell
python main.py
```

### Run Tests
```powershell
pytest                              # All tests
pytest tests/test_utils.py         # Specific file
pytest -v                          # Verbose
pytest --cov=.                     # With coverage
```

### Code Quality
```powershell
black .                            # Format code
flake8 .                           # Lint code
```

### Git Workflow
```powershell
git status                         # Check status
git checkout -b feature/name       # New branch
git add .                          # Stage all
git commit -m "message"            # Commit
git push origin branch-name        # Push
```

### End Working
```powershell
deactivate                         # Deactivate venv
```

---

## 📁 Important Files

| File | Purpose |
|------|---------|
| `SETUP_COMPLETE.md` | Setup summary |
| `QUICKSTART.md` | Quick start guide |
| `CONTRIBUTION_IDEAS.md` | Contribution ideas |
| `PROJECT_ANALYSIS.md` | Project analysis |
| `docs/TESTING.md` | Testing guide |
| `pyproject.toml` | Project config |

---

## 🎯 Quick Tasks (Pick One!)

### Beginner
- [ ] Add type hints to `utils.py`
- [ ] Improve docstrings
- [ ] Fix typos in comments
- [ ] Add tests for one function

### Intermediate
- [ ] Write tests for `config.py`
- [ ] Refactor a long function
- [ ] Add input validation
- [ ] Improve error messages

### Advanced
- [ ] Increase test coverage by 10%
- [ ] Add new feature
- [ ] Performance optimization
- [ ] Security improvements

---

## 📊 Your Environment

✅ Python: 3.14.0  
✅ Virtual Env: Active  
✅ Dependencies: Installed  
✅ Tests: 30/32 passing  
✅ Coverage: 43.9% (utils.py)  
✅ Status: Ready to contribute!

---

## 🆘 Quick Help

**Virtual env not activating?**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Tests failing?**
```powershell
pip install -r requirements.txt
pip install pytest pytest-cov
```

**Import errors?**
Make sure venv is activated!

---

## 🔗 Links

- **GitHub:** https://github.com/yeongpin/cursor-free-vip
- **Issues:** https://github.com/yeongpin/cursor-free-vip/issues
- **Python Docs:** https://docs.python.org/3/
- **Pytest Docs:** https://docs.pytest.org/

---

*Keep this file open for quick reference!*
