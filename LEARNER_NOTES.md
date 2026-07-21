# Learner Notes

Selected public summaries of project progress. These notes document the
concepts explored, the work completed, the verification performed, and the
direction of the project — not every detail of every session.

Detailed instructional records and personal reflections are kept privately.
These notes are derived from AI-assisted session records and reviewed by the
learner for accuracy. The goal is a readable public account of what was
learned and built, in the learner's own voice, rather than a performance log.

Sessions use a consistent shape: what I explored, what I built or changed,
how I verified it, the key takeaway, and next steps.

---

## Session 1 — Workstation, Git, and a first program

### What I explored
The layers underneath a terminal prompt: the difference between the terminal
and the shell, how the shell resolves a typed command by walking `PATH` in
order and stopping at the first match, environment variables, and where a
package manager installs software and how it ends up on `PATH`. Then the
Git model — working tree, staging area, commit history, and remotes.

### What I built or changed
Installed `uv` (Python package/environment manager) via Homebrew after
classifying it as a required tool. Initialized a Git repository, configured
identity, and wrote a small first Python program, `reconcile.py`, that
compares two lists of transaction IDs and reports the differences — a
deliberately finance-flavored exercise.

### How I verified it
Inspected `PATH` and command resolution directly (`echo $PATH`, `type -a`)
and predicted results before running. Reviewed the staged diff and explained
every file before the first commit, then pushed to a public GitHub repo.

### Key takeaway
"It runs" is not evidence. Command resolution, install provenance, and a
clean commit are each things you can inspect and explain, not assume.

### Next steps
Deepen the first program; learn virtual environments and reproducible Python.

---

## Session 2 — Python fundamentals through the first program

### What I explored
Core Python building blocks taught in isolation and then composed: variables,
list literals, `for` loops, the membership operator (`in`), and `print`. The
difference between a string literal and a name, and how to read a traceback
from the bottom up (error type, message, location).

### What I built or changed
Extended `reconcile.py` and exercised it against data I designed myself, so I
always knew the correct answer in advance. Practiced modifying the program
under observation — adding data, introducing a duplicate — and predicting the
effect each time.

### How I verified it
Declared the expected output before every run and compared. Diagnosed a
`NameError` from its traceback and corrected a values-as-names mistake.

### Key takeaway
Designing your own test data means you hold the ground truth — you are
checking output against a known answer, not admiring whatever prints.

### Next steps
Processes and the operating system; sets and more efficient membership.

---

## Session 3 — Processes, sets, and better reconciliation

### What I explored
What a process is versus a program on disk, process identifiers and parent
identifiers, and the chain of processes from a shell up to the first process
started at boot. Then sets and hash-based membership: why checking membership
in a set does not require scanning every element the way a list does.

### What I built or changed
Reworked `reconcile.py` to detect duplicate transaction IDs and report
present-but-unmatched IDs on each side. Building the sets first and then
testing membership against them removed the nested list-scan the earlier
version relied on.

### How I verified it
Traced the program by hand, iteration by iteration, and derived every line of
expected output before running. Reviewed the diff as a story of intent —
which loops changed purpose, which were new.

### Key takeaway
A higher-level operator like `in` does not remove work; it can change the
underlying data structure so the work is cheaper. Choosing the right
structure is a design decision with real performance consequences.

### Next steps
A spaced-review session, then reproducible Python environments.

---

## Session 4 — Spaced review

### What I explored
A mixed review session with no new material: active recall across permissions
and precedence, exit codes, the three Git areas, command resolution, and the
set/dictionary distinction. The purpose was to test what survived a week
without rehearsal.

### What I built or changed
No code changes — a deliberate consolidation session.

### How I verified it
Answered from memory first, then reconstructed corrected explanations for the
few that were imprecise.

### Key takeaway
Understanding that cannot be recalled and re-derived a week later was not yet
understanding. Review is part of the build, not a break from it.

### Next steps
Reproducible Python: virtual environments, project metadata, lockfiles.

---

## Session 5 — Reproducible Python with uv

### What I explored
Why a single machine-wide Python interpreter causes problems — projects share
one package directory, so installing a library for one project can change it
for another, and a system upgrade can shift the interpreter underneath every
project at once. Then the fix: a per-project virtual environment, declared
dependencies in `pyproject.toml`, and a lockfile that pins exact versions.
Also how environment variables are inherited (copied from parent process to
child at creation), which explains why activation applies to a shell rather
than a directory.

### What I built or changed
Created a project virtual environment with `uv`, wrote `pyproject.toml` by
hand (project name, version, required Python), and generated a lockfile with
`uv lock`. Confirmed the environment is regenerable rather than something to
commit.

### How I verified it
Deleted the entire virtual environment and rebuilt it from the committed
`pyproject.toml` and lockfile with `uv sync`, then ran the program through the
rebuilt environment and confirmed identical output. Also confirmed that a
mis-cased table name in `pyproject.toml` was silently ignored — caught by a
warning that contradicted what the file actually contained.

### Key takeaway
Reproducibility means committing the recipe (project metadata and lockfile),
never the built environment. The recipe is portable text; the environment is
disposable and machine-specific.

### Next steps
Close out environment and workflow foundations, then move into functions,
modules, and more substantial learner-written software.

---

## Independent review

An independent review — conducted with a separate model that had not taught
the recent sessions — validated several areas of understanding and identified
a few topics that would benefit from more practice, including precise shell
command-resolution vocabulary and the distinction between staging and pushing
in Git. Those topics were folded into subsequent sessions and the project
backlog. Periodic independent review is part of the methodology (see
`LEARNING_METHODOLOGY.md`).

---

## Where the project is headed

The early stage deliberately established the learning environment, safeguards,
curriculum, and review process — these are part of the professor-agent design.
From here, the center of gravity shifts toward learner-written application
code: functions and modules, input/output, validation and error handling,
tests, HTTP and model APIs, persistent state, and eventually a working
AI-enabled tool that is genuinely useful. A near-term milestone is a first
real user (the learner) reaching the agent from a phone and depending on it
day to day.
