# Dev-Stats Dashboard

A small Flask web app that fetches GitHub user data and displays profile stats, repository metrics, and language breakdown.

## Project structure

- `main.py` — Flask app entrypoint and routing
- `db_core.py` — SQLite helpers (initialization, save, fetch)
- `app/api.py` — GitHub API wrappers (`get_user`, `get_repos`)
- `app/calc.py` — statistics helpers (language share, engagement)
- `app/templates/dashboard.html` — frontend UI
- `generate_ppt.py` — (optional) simple script to create a PPTX summary

## Requirements

- Python 3.8+ (project uses a `venv`)
- Recommended packages:
  - `Flask`
  - `requests`

Create a `requirements.txt` with:

```
Flask
requests
python-pptx
```

## Setup (Windows PowerShell)

1. Activate virtual environment:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
& .\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Ensure `db` directory exists:

```powershell
if (-Not (Test-Path .\db)) { New-Item -ItemType Directory -Path .\db }
```

## Run the app

```powershell
python main.py
```

Open http://127.0.0.1:5000 in your browser.

## Import snippets (use these in other scripts)

```python
from app.api import get_user, get_repos
from app.calc import calc_language_stats, calc_engagement, prepare_repo_data
from db_core import init_db, save_user, save_repos, get_saved_users
from main import app  # Flask application instance
```

## Optional: generate PPTX summary

If you installed `python-pptx`, you can run the included generator:

```powershell
python generate_ppt.py
```

This will create `Dev-Stats-Dashboard.pptx` in the project root.

## Troubleshooting

- ModuleNotFoundError: `pip install <missing-package>`
- If port 5000 is in use, change `app.run(port=XXXX)` in `main.py`.
- To run without activating venv, call the venv python directly:

```powershell
& 'c:\APP Project\venv\Scripts\python.exe' main.py
```

---

If you want, I can also create a `requirements.txt` file and add a one-line PowerShell script to set up and run everything. Let me know.