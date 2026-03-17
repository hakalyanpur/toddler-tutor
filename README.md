# 🦄 Avyaan's Tutor

A local math + verbal tutor app for kids, built with FastAPI + SQLite.

## Quick Start

```bash
# 1. Go into the project folder
cd avyaan-tutor

# 2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate      # Mac/Linux
# .venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn main:app --reload --port 8000

# 5. Open in browser
open http://localhost:8000
```

## Project Structure

```
avyaan-tutor/
├── main.py          ← FastAPI routes + question banks
├── database.py      ← SQLite init + helpers
├── requirements.txt
├── db/
│   └── tutor.db     ← auto-created on first run
└── static/
    └── index.html   ← full frontend (HTML + CSS + JS)
```

## API Endpoints

| Method | Path                        | Description              |
|--------|-----------------------------|--------------------------|
| GET    | /                           | Serve the frontend       |
| GET    | /api/questions/math         | 5 random math questions  |
| GET    | /api/questions/verbal       | 5 random verbal questions|
| POST   | /api/answer                 | Submit an answer         |
| GET    | /api/progress/{name}        | Personal progress        |
| GET    | /api/leaderboard            | Top 10 scores            |
| GET    | /docs                       | Auto Swagger UI          |

## Extending with Claude Code

Once you want to add AI hints, just run:
```
claude
```
Then ask it to: "Add a /api/hint endpoint that takes a question_id and
returns an age-appropriate hint using the anthropic SDK"
