# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A toddler quiz app ("Avyaan's Tutor" / "QuizSprout") for math, reading and logic questions, targeting a 4-year-old. Most content is Singapore Primary-1 level or above; see `questions/syllabus.md` for the sourced curriculum placement. Built with FastAPI + SQLite backend and a single-page HTML/JS/CSS frontend.

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
- **`questions/`** — JSON question banks (`math.json`, `verbal.json`, `logic.json`). Each question has an `id`, `type`, `answer`, and display fields. Math questions also carry `level` (1–5, the difficulty progression) and `strand` (topic), plus `method` and `hint` on arithmetic items.
- **`questions/syllabus.md`** — Curriculum reference explaining topic scope, mastery strategies, and what's not yet covered.

## Key Design Details

- Question modes: `math`, `verbal`, `logic` — each backed by a separate JSON file and API endpoint.
- The `mode` field in `AnswerPayload` accepts `"math"`, `"verbal"`, or `"logic"`.
- Math and Words are both served as progressions: `/api/questions/math?level=N` (levels live on each question, plus an optional `&strand=`) and `/api/questions/verbal?tier=N` (tiers live in `TIER_BY_TYPE`). Both are picked from the home screen before a session starts.
- Every question type needs three things or it will silently render blank: a branch in `renderQuestion()`, an entry in `tutorialBuilders`, and a prompt field (`display`/`question`/`story`).
- Deployed on Fly.io (`quizsprout` app, `sjc` region) with a persistent volume mounted at `/data`. The Dockerfile uses port 8080.
- The SQLite DB path is relative to `database.py` (`db/tutor.db`), not the Fly volume — this may need alignment for production persistence.
