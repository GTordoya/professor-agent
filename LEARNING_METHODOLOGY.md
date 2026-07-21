# Learning Methodology

This project uses a specific method for rebuilding technical skills from first
principles. The method matters as much as the artifact, so it is documented
here in plain terms. The full rulebook lives in `TEACHING_CONSTITUTION.md`;
this is the readable summary.

## Build-as-curriculum

There is no separate course. The curriculum is the act of building an AI
"professor agent," and each concept is introduced at the moment the build
requires it. Shells and paths come first because you cannot work without
them; Git and reproducible Python come next because the project needs version
control and a stable environment; programming fundamentals, HTTP and APIs,
reliability, and deployment follow as the agent grows into them. Learning in
the order the work demands keeps every topic motivated by a real need rather
than by a syllabus.

## The learner writes the implementation

The single most important rule is that the learner writes all of the
implementation code. The AI acts as a professor: it explains concepts, assigns
one small task at a time, reviews what the learner wrote, and helps the learner
correct it. It does not scaffold files or paste finished solutions, because the
goal is not working code — working code is easy to obtain. The goal is the
understanding and judgment that let a person supervise, extend, and debug code,
including code they did not write.

When the learner is stuck, help is given as a ladder rather than an answer:
restate the goal, point to the relevant concept, narrow to the specific line,
and only as a last resort show the answer — after which the learner re-derives
it independently in a fresh variation.

## Evidence-based progress

Progress is measured by evidence, not by whether a program runs. A topic is
considered learned only when the learner can do five different things with it:
**recall** it, **construct** with it, **modify** existing work that uses it,
**diagnose** a failure involving it, and **explain** it clearly. A program that
runs demonstrates none of these on its own. This standard is deliberately
higher than "it worked," because working output is exactly the thing that hides
gaps in understanding.

The target of all this is judgment rather than encyclopedic coverage. Nobody
understands an entire technology stack. The useful standard is enough depth to
descend one level when something breaks — to know what to ask, to recognize
output that is subtly wrong, and to know which layer to investigate. Depth is
pursued in service of that judgment, not collected for its own sake.

## Working habits

A few concrete habits run through every session:

- **Predict before running.** Before executing a command or a program, the
  learner states the expected result, then compares. A surprise is a learning
  opportunity; a confirmed prediction is evidence of a working mental model.
- **Read output before reacting.** The learner interprets command output and
  error messages first, treating each error as a specimen to be read — its
  type, message, and location — rather than an obstacle to clear away.
- **Review the staged diff before committing.** Every change is reviewed and
  explained, file by file, before it enters version control. Nothing is
  committed that the learner cannot narrate.
- **Verify controls instead of trusting them.** After changing a safeguard —
  a permission rule, an ignore rule — the learner confirms it works by
  attempting the thing it should prevent and observing the block.

## Independent review

Periodically, a separate AI model that did not teach the recent material runs
a short independent review. It receives a neutral briefing — the topics
covered and the exercises attempted, but not the explanations or expected
answers — and then asks the learner to recall, explain, predict, apply, and
diagnose. The point is calibration: a model that just taught a concept cannot
help filling in gaps unconsciously, while a fresh one with limited context
cannot. Findings feed back into future sessions and the backlog. Using a
different model, ideally from a different provider, keeps the review genuinely
independent.

## Security as a continuous concern

Security is treated as cross-cutting rather than as a single phase. At each new
feature, the same questions are asked: what are the assets, what are the
untrusted inputs, where are the trust boundaries, what could go wrong, and what
limits the damage when it does. Secrets are kept out of version control from
the start, and safeguards are verified rather than assumed.

## Public notes versus private records

Two kinds of record are kept, on purpose. A detailed instructional log and the
learner's personal reflections are private: they contain candid, in-the-moment
detail that is useful for teaching but not meant for publication. A curated set
of public notes (`LEARNER_NOTES.md`) summarizes, in the learner's own words,
the concepts explored, the work completed, the verification performed, and the
direction of the project. The public notes are reviewed for accuracy; they are
a readable account of progress, not a complete assessment record.

## Why early governance was necessary, and what comes next

The first stage of the project is heavier on structure than on application
code — the constitution, the curriculum, the review process, and the
safeguards all had to exist before meaningful building could begin, and they
are themselves part of the professor-agent's design. That balance is expected
to shift. As the project progresses, the repository will increasingly emphasize
learner-written software: functions and modules, input and output, validation
and error handling, tests, interfaces, HTTP and model APIs, persistence,
reliability, and eventually deployment. The methodology stays the same; what it
produces moves steadily toward a conventional, demonstrable software portfolio.
