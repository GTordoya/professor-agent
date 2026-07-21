# Curriculum

Build-as-curriculum: each phase exists because the professor agent needs it.
A phase is complete only when **every exit criterion** is met with evidence
recorded in the learner record (recall, construction, modification,
diagnosis, explanation — per the mastery rules in
`TEACHING_CONSTITUTION.md`). Topics beyond Phase 4 live in `BACKLOG.md` until
scheduled.

## Phase 0 — Workstation

**Topics**: terminal vs shell, filesystem paths, cwd, environment variables,
PATH and command resolution, processes, package managers (Homebrew), install
provenance, Unix permissions.

**Exit criteria — the learner can:**
- Explain the difference between the terminal emulator and the shell, and
  name which shell is running.
- Trace, step by step, how the shell resolves a typed command name to an
  executable (PATH order, first match wins), and use `which`/`type` to verify.
- Explain what an environment variable is, inspect one, and set one for a
  single command vs. a whole session.
- Explain where Homebrew installs binaries on Apple Silicon and why that
  location must be on PATH.
- Explain what a process is and inspect a running one.
- State, for any installed tool: where it came from, who publishes it, and
  how to remove it.

## Phase 1 — Git + reproducible Python

**Topics**: working tree / staging area / commits / branches / remotes;
public GitHub repo; `uv`; virtual environments; `pyproject.toml`; lockfiles;
first learner-written programs; staged-diff review habit; secrets hygiene
(`.env` + `.gitignore`).

**Exit criteria — the learner can:**
- Draw or narrate the three-area model (working tree → staging → history) and
  predict what `git status` will show after a given action.
- Stage selectively, review `git diff --staged`, and narrate every change
  before committing — demonstrated on every commit, not once.
- Explain what a branch and a remote are; push to and pull from GitHub.
- Explain global vs. project Python, why virtual environments exist, and
  create/activate one with `uv`.
- Explain the roles of `pyproject.toml` vs. a lockfile, and what
  "reproducible" means concretely.
- Write, from scratch, a small working Python script (financial-flavored)
  with no scaffolding.
- Show that `.env` is gitignored by demonstrating it can't be staged.

## Phase 2 — Model-free professor CLI

**Topics**: variables, strings, I/O, conditionals, loops, functions,
collections (list/dict/set/tuple), modules and imports, exceptions, type
hints.

**Build**: a command-line quiz/professor program with no AI model behind it —
question banks, scoring, review scheduling as plain data and logic.

**Exit criteria — the learner can:**
- Choose the right collection for a problem and justify it.
- Write and call functions with typed signatures; explain what the hints
  promise and what they don't (no runtime enforcement).
- Raise and handle exceptions deliberately; explain the difference between
  expected failure and a bug.
- Split the program into modules and explain the import system.
- Modify the program live under observation (e.g., "add a category filter")
  without hints, and diagnose a seeded bug from its traceback.

## Phase 3 — HTTP, JSON, APIs, auth

**Topics**: client-server model, DNS, ports, TCP, TLS, request/response,
methods, status codes, headers, JSON serialization, API keys, bearer auth,
first real model API call, provider+model as configuration.

**Exit criteria — the learner can:**
- Narrate the full journey of an HTTPS request (name → address → connection
  → encryption → request → response) at the concept level.
- Predict the meaning of status code classes (2xx/4xx/5xx) and inspect
  headers to debug a failing call.
- Make an authenticated API call to a model provider with the key loaded from
  `.env` — no credentials hardcoded anywhere, verified by staged-diff review.
- Serialize/deserialize JSON to and from Python structures and explain the
  type mapping.
- Swap provider or model via configuration without touching call-site logic.
- Answer the five security questions (assets, untrusted inputs, trust
  boundaries, failure modes, damage limits) for the API-calling feature.

## Phase 4 — Reliability

**Topics**: input validation, exception design, reading stack traces,
logging, tests (pytest), timeouts, retries with backoff, rate limits,
refactoring under a test safety net.

**Exit criteria — the learner can:**
- Read an unfamiliar stack trace bottom-up and locate the fault.
- Write tests first for a bug fix, watch them fail, then pass.
- Explain why timeouts are mandatory on network calls and set them.
- Implement retry-with-backoff and explain why naive retries make outages
  worse.
- Add structured logging and use it to diagnose a seeded failure.
- Refactor a module with the test suite proving behavior is unchanged.

## Milestone — First Real User (target: before 2026-09-14)

**Not a phase.** Phases are knowledge-gated; this is gated by *behavior in
the world*, which is a different kind of thing and teaches what no phase
can: the gap between "works on my machine" and "something depends on it."

**Definition**: the professor agent is reachable from the learner's phone,
used daily for at least one week, surviving real use by its first real user
(the learner).

**Exit criteria — demonstrated, not asserted:**
- It runs without the learner babysitting it, and restarts after a crash or
  a reboot.
- It fails *safely*: bad input, network failure, or a model/API error
  produces a handled error, not a silent wrong answer and not data loss.
- Secrets live in `.env`, never in history — verified by staged-diff review
  and probe, not by memory.
- The learner finds and fixes at least one real bug in something already
  shipped, diagnosed from logs or a traceback rather than by guessing.
- Someone else could install and run it from the repo: README instructions
  are sufficient, and the environment rebuilds from committed recipe files.
- The learner can narrate the full request path end to end — phone →
  network → their code → model API → response → phone.

**Scheduling rule**: backlog items genuinely required to reach this
milestone (Telegram polling, JSON state, launchd) are pulled forward as
soon as Phase 4 permits. Everything else in `BACKLOG.md` stays parked. A
milestone without a date is a wish; this one has a date.

## Beyond Phase 4 and the milestone

See `BACKLOG.md`. Nothing there is scheduled until Phase 4 exit criteria are
met, except items pulled forward by the First Real User milestone above.
