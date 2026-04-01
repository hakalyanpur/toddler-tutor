# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A toddler quiz app ("Avyaan's Tutor" / "QuizSprout") for math, verbal, and chess questions, targeting a 3.5-year-old at advanced N1/pre-N2 Singapore curriculum level. Built with FastAPI + SQLite backend and a single-page HTML/JS/CSS frontend.

## Commands

```bash
# Run locally (auto-reloads on changes)
uvicorn main:app --reload --port 8000

# Install dependencies
pip install -r requirements.txt

# Deploy (Fly.io)
fly deploy
```

There are no tests, linters, or build steps configured.

## Architecture

- **`main.py`** — FastAPI app. Loads question banks from JSON at import time, serves the SPA, and exposes REST API endpoints (`/api/questions/{mode}`, `/api/answer`, `/api/progress/{name}`, `/api/leaderboard`). Smart question selection in `_pick_questions()` prioritizes unseen → incorrect → mastered questions per player.
- **`database.py`** — SQLite helper. Single `answers` table stores all player responses. DB auto-creates at `db/tutor.db` on first run.
- **`static/index.html`** — Entire frontend in one file (HTML + CSS + JS). No framework, no bundler.
- **`questions/`** — JSON question banks (`math.json`, `verbal.json`, `chess.json`). Each question has an `id`, `type`, `answer`, and display fields. Math questions include `method` and `hint` fields for teaching strategies.
- **`questions/syllabus.md`** — Curriculum reference explaining topic scope, mastery strategies, and what's not yet covered.

## Key Design Details

- Question modes: `math`, `verbal`, `chess` — each backed by a separate JSON file and API endpoint.
- The `mode` field in `AnswerPayload` accepts `"math"`, `"verbal"`, or `"chess"`.
- Deployed on Fly.io (`quizsprout` app, `sjc` region) with a persistent volume mounted at `/data`. The Dockerfile uses port 8080.
- The SQLite DB path is relative to `database.py` (`db/tutor.db`), not the Fly volume — this may need alignment for production persistence.
