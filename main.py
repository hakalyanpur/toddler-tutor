from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from starlette.responses import Response
from pydantic import BaseModel
from database import init_db, get_db, close_db
import random, datetime, json, os

app = FastAPI(title="Avyaan's Tutor")

# ── load question banks from JSON ────────────────────────────────────────────
def _load_questions(filename):
    path = os.path.join(os.path.dirname(__file__), "questions", filename)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

MATH_Q = _load_questions("math.json")
VERBAL_Q = _load_questions("verbal.json")


# ── startup / shutdown ────────────────────────────────────────────────────────
@app.on_event("startup")
def startup():
    init_db()

# ── static + root ─────────────────────────────────────────────────────────────
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    resp = FileResponse("static/index.html")
    resp.headers["Cache-Control"] = "no-cache"
    return resp

# ── schemas ───────────────────────────────────────────────────────────────────
class AnswerPayload(BaseModel):
    player_name: str
    mode: str        # "math" | "verbal"
    question_id: str
    correct: bool

class SessionStart(BaseModel):
    player_name: str

# ── smarter question selection ───────────────────────────────────────────────
def _pick_questions(pool, mode, player_name, count=5):
    """Prefer unseen questions, then incorrectly-answered, then recycle."""
    if not player_name:
        return random.sample(pool, min(count, len(pool)))

    db = get_db()
    try:
        # IDs the player answered correctly at least once
        correct_rows = db.execute(
            "SELECT DISTINCT question_id FROM answers WHERE player_name = ? AND mode = ? AND correct = 1",
            (player_name, mode)
        ).fetchall()
        correct_ids = {r["question_id"] for r in correct_rows}

        # IDs the player attempted but never got correct
        attempted_rows = db.execute(
            "SELECT DISTINCT question_id FROM answers WHERE player_name = ? AND mode = ?",
            (player_name, mode)
        ).fetchall()
        attempted_ids = {r["question_id"] for r in attempted_rows}
        wrong_ids = attempted_ids - correct_ids
    finally:
        close_db(db)

    unseen   = [q for q in pool if q["id"] not in attempted_ids]
    wrong    = [q for q in pool if q["id"] in wrong_ids]
    mastered = [q for q in pool if q["id"] in correct_ids]

    # Build result: unseen first, then wrong, then mastered
    result = []
    for bucket in [unseen, wrong, mastered]:
        random.shuffle(bucket)
        result.extend(bucket)
        if len(result) >= count:
            break

    return result[:count]

# ── question endpoints ────────────────────────────────────────────────────────
@app.get("/api/questions/math")
def get_math_questions(player_name: str = Query("")):
    return _pick_questions(MATH_Q, "math", player_name)

@app.get("/api/questions/verbal")
def get_verbal_questions(player_name: str = Query("")):
    return _pick_questions(VERBAL_Q, "verbal", player_name)

# ── answer + progress ─────────────────────────────────────────────────────────
@app.post("/api/answer")
def submit_answer(payload: AnswerPayload):
    db = get_db()
    try:
        db.execute(
            "INSERT INTO answers (player_name, mode, question_id, correct, ts) VALUES (?,?,?,?,?)",
            (payload.player_name, payload.mode, payload.question_id,
             int(payload.correct), datetime.datetime.utcnow().isoformat())
        )
        db.commit()
    finally:
        close_db(db)

    encouragement = random.choice([
        "Amazing! 🎉", "You're SO smart! 🌟", "WOW, yes! 🥳",
        "Great job! 💫", "You did it! 🎊", "Brilliant! ⭐"
    ]) if payload.correct else random.choice([
        "Oops! Try again 😊", "Almost! Count once more 🤗",
        "Keep going! 💪", "So close! 🌈"
    ])
    return {"ok": payload.correct, "message": encouragement}

@app.get("/api/progress/{player_name}")
def get_progress(player_name: str):
    db = get_db()
    try:
        rows = db.execute(
            """SELECT mode,
                      SUM(correct) as correct,
                      COUNT(*) as total
               FROM answers
               WHERE player_name = ?
               GROUP BY mode""",
            (player_name,)
        ).fetchall()
        streak = db.execute(
            """SELECT correct FROM answers
               WHERE player_name = ?
               ORDER BY ts DESC LIMIT 10""",
            (player_name,)
        ).fetchall()
    finally:
        close_db(db)

    # compute current streak
    current_streak = 0
    for r in streak:
        if r["correct"]: current_streak += 1
        else: break

    progress = {r["mode"]: {"correct": r["correct"], "total": r["total"]} for r in rows}
    return {"progress": progress, "streak": current_streak}

@app.get("/api/leaderboard")
def leaderboard():
    db = get_db()
    try:
        rows = db.execute(
            """SELECT player_name,
                      SUM(correct) as score,
                      COUNT(*) as attempts
               FROM answers
               GROUP BY player_name
               ORDER BY score DESC
               LIMIT 10"""
        ).fetchall()
    finally:
        close_db(db)
    return [dict(r) for r in rows]
