# Syllabus — N2/K1 Top-Tier (Age 4, Singapore Curriculum)

## Learner Profile: Avyaan

- **Age:** 4 years
- **Numbers:** Knows 1–100, addition/subtraction foundations
- **Letters:** Knows A–Z and a–z, can write his name
- **Communication:** Strong verbal communicator in English
- **Reading/Writing:** Building sight words, CVC blending, early phonics
- **Target level:** Top-performing 4-year-old at elite Singapore preschool (N2/K1)

## Framework Context

Based on the MOE **Nurturing Early Learners (NEL)** framework and curriculum standards
from top Singapore preschools (MindChamps, Mulberry Learning, EtonHouse, MOE Kindergartens).
Questions target the **upper end** of N2/K1 expectations — what the best students excel at.

Approach follows Singapore's **Concrete → Pictorial → Abstract (CPA)** method:
emoji visuals (pictorial) paired with number/word choices (abstract), with strategy hints
that teach the method, not just the answer.

---

## Numeracy (286 questions in `math.json`)

| Topic | Count | Scope | Question Types |
|---|---|---|---|
| Addition (1-digit) | 24 | Sums within 18 with strategy hints (count on, make 10, number bonds, doubles) | `addition` |
| Addition (three addends) | 6 | **a + b + c within 20** — add in any order, hunting for the pair that makes 10 first (3 + 7 + 2) | `addition` |
| Addition (near doubles) | 5 | **Doubles ±1** (6 + 7, 8 + 9) — lean on a known double, then adjust by one | `addition` |
| Addition (2-digit, no regroup) | 22 | **Two-digit addition within 100, no regrouping**: 2-digit + 1-digit, adding tens, and 2-digit + 2-digit. Taught with the mental "tens & ones" decompose strategy and the long-form column algorithm | `addition` |
| Addition (crossing a ten) | 8 | **2-digit + 1-digit that cross a ten** (28+5, 47+6) — the near-10 / make-the-next-ten mental method: fill the bigger number up to the next ten using a number bond, then add the leftover | `addition` |
| Addition (2-digit, with regroup / carry) | 8 | **2-digit + 2-digit that regroup**, sums within 100 (27+15, 48+39) — the written column algorithm *with carrying*: add the ones, write the ones digit, carry 1 ten into the tens column. The next rung above the no-carry column | `addition` |
| Subtraction | 26 | Differences within 10 and 20, with strategy hints (count back, bridge 10, number bonds, doubles) | `subtraction` |
| Subtraction (2-digit, no regroup) | 5 | **35 − 12, 60 − 30** — split into tens and ones and subtract each column | `subtraction` |
| Patterns | 54 | Skip counting (+1 through +6, +9, +10, +11), doubling and **halving**, countdown (−2, −3, −5, −10), sequences that cross a ten, plus a **structure tier**: growing jumps (+1, +2, +3…), triangular and square numbers, zig-zag (+2, −1), Fibonacci (add the last two), repeating blocks (1, 2, 3, 1, 2, 3…) and interleaved pairs (1, 10, 2, 20…) | `pattern` |
| Word problems (bar model) | 22 | **Singapore bar-model stories**: part-whole, missing part, comparison ("how many *more*"), and two-step (win 5, give 3 away) | `word_problem` |
| Missing number | 18 | **Algebraic thinking**: missing addend (7 + ⬜ = 10), missing whole (⬜ − 3 = 6), and **equation balance** (4 + 3 = 5 + ⬜) | `missing_number` |
| Number riddles | 16 | **Deduction over numbers**: multi-clue constraints ("bigger than 5, even, NOT 8"), place value, inverse relations, "which number does a 2-jump frog never land on" | `number_riddle` |
| Shapes | 20 | 2D (triangle, circle, square, rectangle, oval, diamond) + 3D (sphere, cube, cylinder, cone) | `shape` |
| Number ordering | 8 | Before/after/between numbers 1–20 | `number_order` |
| Comparison | 8 | Which number is bigger, comparing within 20 | `bigger` |
| More/Less | 6 | Compare groups visually (emoji groups) | `more_less` |
| Sorting | 6 | Odd one out — spot the different item | `sorting` |
| Measurement | 8 | Longer/shorter, taller/shorter, heavier/lighter, bigger/smaller | `measurement` |
| Positional words | 6 | Next to, above, on top of, under, between | `positional` |
| Time | 5 | Morning/afternoon/night, daily routines | `time` |
| Money | 5 | US coins (penny, nickel, dime, quarter), value comparison | `money` |

### Addition/Subtraction Strategy Hints

Every arithmetic question includes a **method hint** showing HOW to solve it:

| Strategy | When Used | Example |
|---|---|---|
| **Count on** | Small addends (1–5) | "Start at 8, count up 5: 9, 10, 11, 12, 13!" |
| **Count back** | Small subtrahends (1–6) | "Start at 10, count back 3: 9, 8, 7!" |
| **Make 10** | When one number is close to 10 | "8 + 5: take 2 from 5 to make 10, then add 3 = 13" |
| **Number bonds** | When numbers pair to 10 | "7 + 3 = 10, so 7 + 5 = 10 + 2 = 12" |
| **Bridge 10** | Subtraction crossing 10 | "13 − 5: 13 − 3 = 10, then 10 − 2 = 8" |
| **Doubles** | Same number added/subtracted | "6 + 6 = 12 (double 6!)" |
| **Split tens & ones** | Two-digit addition (mental) | "23 + 14: tens 20 + 10 = 30, ones 3 + 4 = 7, together 37" |
| **Add tens** | Adding whole tens | "20 + 30: 2 tens + 3 tens = 5 tens = 50" |
| **Near 10 (make the next ten)** | 2-digit + 1-digit crossing a ten | "28 + 5: 28 needs 2 to reach 30, split 5 into 2 and 3, then 30 + 3 = 33" |
| **Column (long-form)** | Two-digit addition (written) | "Stack them, add the ones column first, then the tens column" |
| **Carry the ten** | 2-digit + 2-digit that regroups (written) | "27 + 15: ones 7 + 5 = 12, write 2 carry 1; tens 1 + 2 + 1 = 4 → 42" |
| **Make ten first** | Three addends | "4 + 7 + 6: 4 + 6 = 10 first, then 10 + 7 = 17" |
| **Near doubles** | Two neighbours (n and n+1) | "7 + 8: double 7 is 14, one more is 15" |
| **Split tens (subtraction)** | 2-digit − 2-digit, no borrowing | "48 − 25: tens 40 − 20 = 20, ones 8 − 5 = 3 → 23" |

### Two-Digit Addition Progression (Primary-1 reach for strong K1/K2)

Follows the Singapore CPA path — mental decomposition first, the written column algorithm second.
All two-digit problems are **no-regrouping** (the ones column never exceeds 9), so the column method stays clean before carrying is introduced.

1. **2-digit + 1-digit, no regroup** (e.g. 21 + 4) — `split_tens`
2. **Adding whole tens** (e.g. 20 + 30) — `add_tens`
3. **2-digit + 2-digit, no regroup** (e.g. 23 + 14) — `two_digit`: a single "Two Ways!" explainer that shows **both** techniques in sequence — the mental tens-&-ones method first (Singapore's emphasis), then the written column/stack method — reinforcing that the algorithm is just the written form of the mental strategy.
4. **2-digit + 1-digit, crossing a ten** (e.g. 28 + 5, 47 + 6) — `near_10`: the make-the-next-ten mental method. This is the child's count-on instinct formalized — these *are* regrouping problems, done mentally (fill to the next ten, then add the leftover) rather than by a carried column.
5. **2-digit + 2-digit, with regrouping** (e.g. 27 + 15, 48 + 39) — `carry`: the written column algorithm *with carrying*. Builds directly on step 3's no-carry column — the only new idea is that when the ones sum exceeds 9, you write the ones digit and carry 1 ten into the tens column.

> **Pedagogical note:** Singapore math deliberately teaches mental calculation (number bonds, make-ten, decompose into tens & ones) *before* and *as the basis for* the standard column algorithm. The two-digit explainer mirrors this: head first, paper second.

---

### Reasoning Inside Math (word problems, missing numbers, riddles, structure patterns)

Arithmetic fluency alone is a weak signal. These four sets keep the Singapore
curriculum but push the *thinking* load, and each has its own chalkboard explainer.

| Set | Models | What it trains |
|---|---|---|
| `word_problem` | `part_whole`, `missing_part`, `comparison`, `two_step` | Turning a story into a **bar model** before computing — Singapore's signature move. Comparison ("how many more") and two-step stories are the hard rungs |
| `missing_number` | `bond`, `inverse_whole`, `balance` | Pre-algebra: an unknown in any position, and `=` as a **balance**, not "the answer comes next" — the single most common early misconception |
| `number_riddle` | — | Holding 2–3 constraints at once and eliminating candidates ("bigger than 5, even, NOT 8") |
| `pattern` (structure tier) | — | Rules beyond a constant step: growing jumps, halving, Fibonacci, repeating blocks, two interleaved sequences |

The bar model is drawn on the chalkboard as proportional bars — parts side by side
with the whole braced beneath, or two bars lined up so the **gap** is visibly the
answer. Missing-number items reuse the number-bond circles (with a hole in them)
and a two-pan balance.

---

## Logic & Reasoning (35 questions in `logic.json`) — the "Logic" mode

A separate **🧩 Logic** mode (`GET /api/questions/logic`), built to exercise the
*reasoning* muscles — abstraction, structure, deduction — rather than calculation.
The rationale: arithmetic fluency is the most-coachable slice of math and a weak
predictor of higher-order mathematical talent; pattern/structure recognition,
transitive reasoning, and "sit with a hard problem" disposition track far better
to olympiad-style problem solving. This mode deliberately targets that gap.

| Type | Count | Skill exercised | Example |
|---|---|---|---|
| `visual_pattern` | 8 | Structural pattern recognition (AB, AAB, ABC repeats) | 🔴🔵🔴🔵🔴 → ? |
| `analogy` | 8 | Relational mapping (A is to B as C is to ?) | Sock→Foot, Glove→? (Hand) |
| `odd_one_out` | 7 | Categorization by a *hidden* rule (living/non-living, even/odd, flies/swims) | 🌳 🌷 🌻 🪨 → 🪨 |
| `deduction` | 7 | Constraint logic, transitive reasoning, likelihood | "Tom > Sam > Ben — who's tallest?" |
| `sequence_logic` | 5 | Ordering by size / time / life-cycle | 🐭 → 🐱 → 🐶 → ? (🐘) |

Each item carries a spoken `hint` that *talks through the reasoning* (the lesson is
the why, not the answer). All types reuse a single generic chalkboard explainer
(`buildTutorialLogic`). Surface-level recall (naming a fruit) is avoided in favour
of items with a rule to *infer* — especially the even/odd, living/non-living,
transitive-height, and likelihood items, which are the most reasoning-loaded.

---

## Literacy (140 questions in `verbal.json`) — a tiered reading engine

The **Words** section is served as a **tier progression** that fuses **Erik Hoel's
"Teaching (very) early reading" game plan** (Parts 1–5) with the **NEL** literacy
approach. The child climbs the ladder; the parent voices the precise sounds.
Each question type maps to a tier (`TIER_BY_TYPE` in `main.py`), served via
`GET /api/questions/verbal?tier=N`.

### Hoel's principles applied
- **Loving & grokking** — optimise for reading *for pleasure*, not "reading level."
- **Skip blending; use "double reading"** — the **Tier 2 sound-it-out game** lays out a
  word's letters as tappable tiles inside a context sentence; the child taps each to hear
  its succinct sound, then says the whole word and confirms with a picture. We never drill
  smooth blending.
- **Letter → *sounds*, kept succinct** — the new `letter_sound` type and the spoken audio
  follow "say /b/, not 'buh'." (Note: the older `phonics` MCQs still use 'buh/duh' option
  text; the new sound-first types model the succinct form.)
- **Context is confidence** — every sound-it-out word sits in a kid-relevant sentence.

### Tier map (Hoel × NEL)

| Tier | Name | Types | Skill |
|---|---|---|---|
| 0 | Warm-Up | `sound`, `opposite`, `color`, `word` | Oral language / vocabulary |
| 1 | Letter Sounds | `letter_sound` (new, audio), `phonics` | Map letters to *sounds* |
| 2 | Sound It Out | `sound_it_out` (new, interactive) | **Double reading** — the core engine |
| 3 | Words & Phrases | `sight_word`, `phrase` (new), `spelling`, `sentence` | Sight words, phrases, sentences |
| 4 | Letter Teams | `digraph`, `magic_e` (new), `word_family` (new), `rhyme` | Phonics rules: sh/ch/th, magic-E, families |
| 5 | Reading Take-Off | `story`, `tricky_word` (new) | Comprehension + irregular words |

Audio uses the browser's `speechSynthesis` (no assets/keys). TTS can't perfectly isolate
stop consonants without a faint vowel, so the on-screen text shows the succinct form and
the parent voices it (Hoel's parent-led 1:1 model).

### Per-type counts

| Topic | Count | Scope | Question Types |
|---|---|---|---|
| Letter sounds (new) | 14 | Sound-first letters (SATPIN +), spoken, succinct | `letter_sound` |
| Sound it out (new) | 10 | Interactive double-reading CVC game with context sentence | `sound_it_out` |
| Phrases (new) | 5 | Read a 2–3 word phrase, match the picture | `phrase` |
| Magic E (new) | 5 | Silent-E changes the vowel (kit→kite, cap→cape) | `magic_e` |
| Word families (new) | 5 | -at, -ig, -op, -all, -ar | `word_family` |
| Tricky words (new) | 4 | Irregular sight words (said, was, you, are) | `tricky_word` |
| Phonics | 15 | 10 letter sounds (b, d, f, g, k, m, n, p, s, t) + 5 CVC blending | `phonics` |
| Sight words | 15 | Common high-frequency words (I, a, the, is, my, it, on, up, go, see, can, we, he, she, no) | `sight_word` |
| Spelling | 12 | CVC words (cat, dog, sun, hat, bed, pig, cup, bus) + CCVC/CVCC (frog, jump, stop, clap) | `spelling` |
| Sentence completion | 8 | Complete simple sentences with context clues and emoji | `sentence` |
| Word-picture | 8 | Match words to pictures / concepts | `word` |
| Rhyming | 7 | Identify rhyming word pairs | `rhyme` |
| Opposites | 8 | Basic opposite pairs (big/small, hot/cold, long/short, hard/soft) | `opposite` |
| Animal sounds | 6 | Identify sounds animals make | `sound` |
| Colors | 6 | Name colors of common objects | `color` |
| Digraphs | 6 | Two-letter sounds: sh, ch, th (2 each) | `digraph` |
| Story comprehension | 6 | Simple 2–3 sentence passages with who/what/where questions | `story` |

### Retired (mastered)
- `letter` — basic uppercase letter recognition (knows A–Z and a–z)

---

## Not Yet Covered

- **Positional words expansion** — beside, around, through
- **Simple reading passages** — longer 4–5 sentence stories
- **Writing practice** — letter/word tracing (needs different UI)
- **Social-emotional** — identifying feelings, sharing, turn-taking
- **Bilingual** — Mandarin vocabulary and characters
- **Regrouping into the hundreds** — written carry is now covered for 2-digit + 2-digit sums *within 100* (the `carry` set, e.g. 27 + 15, 48 + 39). Still not covered: sums that cross 100 (e.g. 68 + 57), and subtraction with regrouping (borrowing)
- **Multiplication foundations** — groups of (2 groups of 3)
- **Three-step word problems** and bar models with unequal parts (fractions of a bar)
- **Analog clock** — telling time to the hour
