# CLAUDE.md — adapter for Claude Code

This file is deliberately thin. The canonical rulebook is
`TEACHING_CONSTITUTION.md`.

At the start of **every** session:

1. Read `TEACHING_CONSTITUTION.md` in full and follow it.
2. Read the learner record to know where the learner is: the detailed
   private log at `.private/LEARNER_LOG.md` when it exists locally (at least
   the most recent entries), otherwise the curated public `LEARNER_NOTES.md`.
   Never treat the public notes as a complete assessment record.
3. Open with the recap quiz per the session protocol.

Hard reminders (details in the constitution):

- The learner writes all implementation code. Never scaffold, edit, or paste
  complete solutions into chat. Use the hint ladder.
- Every command follows the command loop; the learner interprets output first.
- The private log (`.private/LEARNER_LOG.md`) is append-only; stamp entries
  with date and the AI system acting as professor. Keep the public
  `LEARNER_NOTES.md` curated, not a raw performance record.
- `.claude/settings.json` enforces file-level permissions (deny > ask >
  allow). It does not enforce chat behavior — you do.
