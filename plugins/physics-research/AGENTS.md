# physics-research

Auto-activating **Agent Skills** under `./skills/` (open Agent Skills format: each `SKILL.md` has a
`name` + `description`). They activate when a task matches a skill's `description` — no manual command.

Entry point: `research-mode-router`, which routes between **Read** (`literature-reading-notes`),
**Explore** (`exploration-mode`), and **Produce** (`production-mode`, the 7-stage pipeline).

Skill instructions use Claude Code tool names (Read/Write/Edit/Bash/Grep/Glob); use your platform's
equivalents — see the tool-name mapping in the repo README.
