# Backlog

Topics deliberately deferred until the Phase 4 exit criteria in
`CURRICULUM.md` are met. Order is a working hypothesis, not a commitment.
(Learner: paste your longer list below — it will be merged and sequenced in a
session.)

- Telegram bot via long polling — first real users (me, on my phone)
- FastAPI + webhooks — from polling to being called
- Concurrency — async/await, threads vs. processes, queues; why the
  agent can't block while waiting
- JSON file state — persistence without a database
- SQLite + skill graph — real storage, modeling what the learner knows
- SQL depth + data modeling — indexing, transactions, normalization,
  query plans (financial-reporting-flavored examples)
- Pedagogy engine — spaced repetition, mastery tracking as code
- Data structures & algorithms refresher — complexity, the workhorse
  structures; light pass, degree knowledge reactivated not relearned
- Repository archaeology — a repeatable method for onboarding to an
  unfamiliar codebase: purpose and architecture from README/docs/config,
  entry points, module map, dependencies, data flows, tracing a feature,
  locating the code behind an issue; practiced on real open-source repos of
  increasing size and different languages; AI assistant as exploration
  instrument, never as substitute for the mental model. Prereq: Phase 4 done
  plus own multi-module project built.
- Open-source contribution — collaboration mechanics on a real project:
  branching workflows, forks, pull requests, code review etiquette,
  contribution guides, choosing an appropriately small first change;
  capstone: a merged PR. Builds on repository archaeology.
- RAG over my own learning history — embeddings, chunking, vector
  search against the learning log and lesson notes
- launchd — running the agent as a service on macOS
- Docker — packaging and reproducible deployment
- Evals + observability — measuring whether the professor actually teaches
- Networking deep dive — routing, subnets, NAT, how packets actually
  move; consolidates the applied networking from Phases 3+
- Frontend fundamentals — enough HTML/CSS/JS to give the professor a UI
- Local models via Ollama / MLX — inference, quantization, on Apple Silicon
- AI/ML fundamentals track — neural nets (Karpathy Zero to Hero as
  companion), embeddings, fine-tuning, agent design patterns, MCP
- Cloud deployment — off the desk, onto the internet
- System design capstone — caching, load balancing, consistency,
  scaling patterns; the destination the whole arc points at

Security is **not** on this list because it is not a phase — it is applied at
every feature (see `TEACHING_CONSTITUTION.md` §8).
