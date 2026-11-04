# OpenAuto development

OpenAuto is a local-first Streamlit auction scenario analyzer.
- UI: app.py. Calculation source of truth: calculator.py (Deal).
- Preserve existing user work. Inspect changes before editing.
- Run `python -m unittest -v` for calculation changes.
- Run `python -m streamlit run app.py` to launch.
- Use a project .venv; install requirements.txt. An existing working environment may be used until the project environment is prepared.
- Smoke-check the UI with streamlit.testing.v1.AppTest and a 30-second timeout; check exception lists and affected interactions.
- Keep calculation logic independent of Streamlit; add meaningful tests for new behavior.
- Work in small feature branches; review the diff and checks before committing.
- Never commit secrets, private watchlists, local databases or environments.
- Ask before public publishing. Do not scrape auction listings or introduce paid services without authorization.
- See DEVELOPMENT.md and VEHICLE_COMPARISON_PLAN.md.
