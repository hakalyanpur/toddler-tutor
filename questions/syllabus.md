# Syllabus — N2/K1 Top-Tier (Age 4, Singapore Curriculum)

## Learner Profile: Avyaan

- **Age:** 4 years
- **Numbers:** Knows 1–100, addition/subtraction foundations
- **Letters:** Knows A–Z and a–z, can write his name
- **Communication:** Strong verbal communicator in English
- **Reading/Writing:** Building sight words, CVC blending, early phonics
- **Target level:** Top-performing 4-year-old at elite Singapore preschool (N2/K1)

## Framework Context

Two official documents define the ladder. Both were read directly; the placement
table below cites their own numbering.

- **[NEL Framework 2022 / Educators' Guide for Numeracy](https://isomer-user-content.by.gov.sg/57/c079b912-2898-42e2-b32d-ff3ab7cfbec4/Nurturing%20Early%20Learners%202022%20Educators%20Guide%20Numeracy_new.pdf)** — the preschool band, ages 4–6 (N2 through K2).
- **[MOE 2021 Primary Mathematics Syllabus P1–P6](https://www.moe.gov.sg/api/media/92bff26d-b2b4-4535-b868-b8415c744b91/2021-Primary-Mathematics-Syllabus-P1-to-P6-Updated-October-2025.pdf)** (updated Oct 2025) — P1 onwards, ages 6–7 and up.

### What the preschool band actually asks for

NEL's numeracy learning goals cap out well below this app. Verbatim:

- LG 3.1 "Rote count to at least 20"; 3.2 "Count reliably to at least 10 things"
- LG 3.7 compare two sets "of up to 10 things each" using same as / more than / fewer than
- LG 3.8 "Name the parts that form the whole in a quantity of up to 10 (e.g., 5 is made up of 2 and 3, and 1 and 4)" — number bonds within 10, the ceiling of preschool arithmetic
- LG 2.3 "Recognise, extend and create patterns (e.g., ABABAB, ABCABCABC)" — repeats only, no number sequences
- LG 4.1 the four basic shapes: circle, square, rectangle, triangle

There is **no symbolic addition or subtraction anywhere in the preschool goals**. The
guide frames part-whole work as preparation "with addition and subtraction in their
future learning."

So: only the `more_less`, `sorting`, `positional`, some `bigger`, and the bonds-within-10
items sit inside the Singapore preschool band. **Everything else in `math.json` is
Primary-1 content or above** — deliberately, but it should be called what it is. The
"top-tier N2/K1" title is aspiration, not placement.

Approach follows Singapore's **Concrete → Pictorial → Abstract (CPA)** method:
emoji visuals (pictorial) paired with number/word choices (abstract), with strategy hints
that teach the method, not just the answer.

### Curriculum placement (against the MOE content lists)

| App content | Level | Syllabus reference |
|---|---|---|
| Bonds within 10, compare sets to 10, ABAB patterns, 4 basic shapes | Preschool | NEL LG 2.3, 3.7, 3.8, 4.1 |
| Numbers to 100, place value, comparing/ordering | P1 (6–7) | P1 Whole Numbers 1.1–1.5 |
| `pattern` (number sequences) | P1 → P4 | "patterns in number sequences": P1 1.6, P2 1.5, P3 1.5, P4 1.4 |
| `missing_number` (inverse, missing addend) | P1 | Add/Sub 2.3 "relationship between addition and subtraction" |
| `missing_number` (balance, `4 + 3 = 5 + ⬜`) | P1 topic, Big Idea | Add/Sub 2.2 "use of +, – and ="; syllabus Big Ideas → Equivalence |
| Three addends (`a25`–`a30`) | P1 | Add/Sub 2.4 "adding more than two 1-digit numbers" |
| 2-digit addition and subtraction, incl. carrying | P1 | Add/Sub 2.5 "adding and subtracting within 100" + 2.6 "using algorithms" |
| `split_tens`, `near_10`, mental strategies | P1 | Add/Sub 2.7 (within 20; 2-digit and ones without renaming; 2-digit and tens) |
| Odd/even reasoning (`nr13`, logic `oo4`) | P2 (7–8) | P2 Whole Numbers 1.6 "odd and even numbers" |
| 3D shapes (cube, cylinder, cone) | P2 | P2 Geometry 2.1 (cube, cuboid, cone, cylinder) |
| `time` (parts of the day) | below P1 | P1 Time 2.1 is "telling time to 5 minutes" — the app is easier, not harder |

### Deviations, deliberate and otherwise

- **Bar models are not in the MOE content lists at all.** They are pedagogy carried by
  the textbooks, not syllabus items, so no level can be cited for part-whole vs
  comparison vs two-step. The progression used here (part-whole first, comparison
  later, two-step last) follows textbook practice, not a sourced MOE ordering.
- **Money uses US coins**, not the syllabus's cents-to-$1 and dollars-to-$100. Deliberate.
- **Shapes**: `oval` and `diamond` are not MOE shapes at any level, and P1's list
  includes half circle and quarter circle, which the app lacks. `sphere` is not in the
  P2 3D list (cube, cuboid, cone, cylinder).
- **Named sequence structures** — triangular, square, Fibonacci, interleaved — are not
  spelled out anywhere in P1–P4. They sit under the "patterns in number sequences"
  heading in spirit, at its enrichment end. Treat them as olympiad-flavoured, not
  curriculum.
- **P1 also contains multiplication within 40 and division within 20**, which this app
  does not cover at all.

---

## Numeracy (302 questions in `math.json`)

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
| Place value (tens & bundles) | 16 | **Unitizing**: ten loose straws become one bundle, and back again. Bundles are drawn as ten visible sticks under a tie, never as a pre-formed block, so ten-as-one is something to see rather than accept. `pv11` (1 bundle + 12 loose) is carrying, before any column | `place_value` |
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

### Level progression (how math is served)

`math.json` spans preschool to P2, so serving it flat meant a session could mix
"which is bigger, 3 or 5?" with `48 − 25`. Every question now carries a `level`
and a `strand`, and the Math button opens a level picker, mirroring how Words is
served as reading tiers.

| Level | Name | Contents | Count |
|---|---|---|---|
| 1 | Counting & Comparing | more/less, sorting, positional, 2D shapes, small comparisons | 58 |
| 2 | Facts to 20 | count on, make ten, doubles, bonds, constant-step patterns, number order | 102 |
| 3 | Structure & Stories | structure patterns, missing number, word problems, riddles, 3D shapes | 83 |
| 4 | Tens & Bundles | place value, split tens, add tens, near-10 | 39 |
| 5 | On Paper | column method, carrying, 2-digit subtraction | 20 |

**Level 4 sits deliberately below level 5.** Carrying is meaningless without
ten-as-a-unit: the whole move is "ten ones become one ten". A child who has the
column algorithm but not the bundle is performing a ritual. The ordering puts
that in the data rather than leaving it to memory.

`strand` (number, operations, patterns, reasoning, shapes, measures) is the
second axis, for topic selection and per-strand progress. `GET /api/questions/math`
accepts `?level=` and `?strand=`, both optional; with neither, it behaves as before.

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
- **Analog clock** — P1 expects telling time to 5 minutes (P1 Time 2.1); the app only covers parts of the day
- **Multiplication and division** — both are P1 content in the 2021 syllabus (within 40 and within 20 respectively), entirely absent here
