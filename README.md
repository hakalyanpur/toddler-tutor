# QuizSprout — Avyaan's Tutor

A math + verbal tutor app for preschoolers, built with FastAPI + SQLite and aligned to the Singapore N2/K1 curriculum (Nurturing Early Learners framework). Designed for a 3–4 year old who already knows 1–100 and A–Z.

**Live:** https://quizsprout.fly.dev/

## Curriculum Foundation

Based on what top Singapore preschools (MindChamps, Mulberry, EtonHouse, MOE Kindergartens) expect their best 4-year-olds to master, following Singapore's **Concrete → Pictorial → Abstract (CPA)** method.

### Math — 134 questions across 12 types

| Topic | Questions | What It Covers |
|-------|-----------|---------------|
| Addition | 24 | Sums to 15, strategies: count on, doubles, make 10, number bonds |
| Subtraction | 20 | Differences within 20, strategies: count back, bridge 10, number bonds |
| Patterns | 18 | Skip counting (+1 to +10), doubling, countdown, repeating sequences |
| Shapes | 20 | 2D (triangle, circle, square, rectangle, oval, diamond) + 3D (sphere, cube, cylinder, cone) |
| Number Ordering | 8 | Before/after/between numbers 1–20 |
| Comparison | 8 | Which number is bigger, within 20 |
| More/Less | 6 | Compare groups visually |
| Sorting | 6 | Odd one out |
| Measurement | 8 | Longer/shorter, heavier/lighter, taller/shorter |
| Positional Words | 6 | Next to, above, under, between, on top of |
| Time | 5 | Morning/afternoon/night daily routines |
| Money | 5 | US coins: penny, nickel, dime, quarter |

### Verbal — 97 questions across 11 types

| Topic | Questions | What It Covers |
|-------|-----------|---------------|
| Phonics | 15 | 10 Jolly Phonics letter sounds + 5 CVC blending (c-a-t → cat) |
| Sight Words | 15 | High-frequency words: I, a, the, is, my, it, on, up, go, see, can, we, he, she, no |
| Spelling | 12 | CVC (cat, dog, sun) + CCVC/CVCC (frog, jump, stop, clap) |
| Sentence Completion | 8 | Fill-in-the-blank with context clues |
| Word-Picture | 8 | Match words to pictures/concepts |
| Rhyming | 7 | Identify rhyming word pairs and word families |
| Opposites | 8 | big/small, hot/cold, long/short, hard/soft |
| Animal Sounds | 6 | Identify sounds animals make |
| Colors | 6 | Name colors of common objects |
| Digraphs | 6 | Two-letter sounds: sh, ch, th |
| Story Comprehension | 6 | Simple 2–3 sentence passages with who/what/where questions |

### Teaching Method — Chalkboard Tutorials

Every question type has an interactive chalkboard tutorial that teaches **how** to solve it, modeled on Singapore teaching techniques:

- **Arithmetic:** Number line with frog hops, number bond diagrams (part-whole), ten frames, make-10 strategy, bridge-through-10
- **Phonics:** Jolly Phonics physical actions per letter ("Weave your hand like a snake! sssss! 🐍"), CVC blending animation (letters slide together)
- **Literacy:** Word family visualization, letter-by-letter spelling, sight word sentences, rhyme pattern highlighting

Tutorials auto-open on first wrong answer, with chalk dust particles, chalk writing sound effects, and text-to-speech narration at toddler-friendly pace.

## Quick Start

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
open http://localhost:8000
```

## Architecture

- **`main.py`** — FastAPI app. Loads question banks from JSON at startup, serves the SPA, smart question selection (unseen → incorrect → mastered per player).
- **`database.py`** — SQLite. Single `answers` table. DB auto-creates at `db/tutor.db` locally, `/data/tutor.db` on Fly.io.
- **`static/index.html`** — Entire frontend in one file (HTML + CSS + JS). No framework, no bundler. Includes the chalkboard tutorial system (~600 lines).
- **`questions/math.json`** — 134 math questions with strategy method hints.
- **`questions/verbal.json`** — 97 verbal questions with phonics/blending subtypes.
- **`questions/syllabus.md`** — Curriculum reference explaining topic scope and coverage.

## API

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Serve the frontend |
| GET | `/api/questions/math` | 5 smart-selected math questions |
| GET | `/api/questions/verbal` | 5 smart-selected verbal questions |
| POST | `/api/answer` | Submit an answer |
| GET | `/api/progress/{name}` | Personal progress + streak |
| GET | `/api/leaderboard` | Top 10 scores |

## Deployment

Deployed on Fly.io (`quizsprout` app, `sjc` region) with a persistent volume for the SQLite database.

```bash
fly deploy
```

## Updating Questions

Edit the JSON files in `questions/` and redeploy. Questions are loaded at startup. Each question needs a unique `id`, a `type` matching a frontend renderer, an `answer`, and a `hint`. See `questions/syllabus.md` for the full topic breakdown and question schemas.
