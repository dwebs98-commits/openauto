# Development workflow

## Local setup
Use Python 3.10+ and a project virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest -v
python -m streamlit run app.py
```

An existing working environment may be reused. Keep an existing app server running; use `--server.port 8502` if a second instance is needed.

## Codex project
Add the existing OpenAuto folder as a local project in Codex and select it for future work. Repository guidance lives in AGENTS.md. Adding the folder to the app sidebar is a separate step from Git setup.

## Version control
Git is initialized on main. The public repository is https://github.com/dwebs98-commits/openauto.
Only reviewed source, tests, MIT license, README and development guidance belong in Git. Local environments, watchlist exports, caches, credentials and .agents content are excluded. Use a GitHub no-reply email for commits if you prefer to keep your email private.

## Daily work
Create a feature branch, describe the intended change to Codex, review its diff, run relevant checks, then commit. Push and open a pull request when ready. Start with VEHICLE_COMPARISON_PLAN.md.

## Verification
The initial setup passed all four calculation tests and a Streamlit AppTest covering rendering, adding a scenario and clearing the watchlist. For future smoke checks, use a 30-second AppTest timeout and assert that exception lists are empty.
