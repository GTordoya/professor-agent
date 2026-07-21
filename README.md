# professor-agent

Learning technical skills from first principles by building my AI professor —
build-as-curriculum, follow along.

## The premise

I'm rebuilding and extending my technical fluency from first principles by
building an AI "professor agent." Rather than following a standalone course,
the project introduces concepts when the implementation requires them. Every
topic (shells, Git, Python, HTTP, APIs, reliability, deployment) is taught at
the moment the build needs it, by an AI professor operating under strict rules.

## The rules that make it real

- **I write all the implementation code.** The AI professor teaches, assigns,
  reviews, and quizzes — it never scaffolds files or pastes solutions. The
  rulebook is [TEACHING_CONSTITUTION.md](TEACHING_CONSTITUTION.md), and
  file-level permissions in `.claude/settings.json` enforce what they can.
- **Progress requires evidence.** Topics advance only when I can recall,
  construct, modify, diagnose, and explain — never because "it runs." See
  [CURRICULUM.md](CURRICULUM.md) for phases and exit criteria.
- **Understanding is checked, not assumed.** Public learning notes summarize
  the concepts explored, implementation progress, verification performed, and
  major lessons from each stage. Periodic independent reviews test whether
  documented understanding can be recalled, explained, modified, and applied.
  Detailed instructional records and personal reflections remain private.

## Where the project is now

The first stage deliberately established the learning environment, safeguards,
curriculum, and review process. These foundations are part of the
professor-agent design. As the project progresses, the repository will
increasingly emphasize learner-written application code, tests, interfaces,
reliability, and deployment.

## Following along

1. This README
2. [LEARNING_METHODOLOGY.md](LEARNING_METHODOLOGY.md) — how the project works
3. [CURRICULUM.md](CURRICULUM.md) — phases and exit criteria
4. [LEARNER_NOTES.md](LEARNER_NOTES.md) — curated progress notes
5. The implementation and commit history

## License

MIT — see [LICENSE](LICENSE).
