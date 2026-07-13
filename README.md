# Physics Research Skills

Auto-activating [Claude Code](https://claude.com/claude-code) skills for **physics research** — a
subject-agnostic research-process **core** plus **pluggable domain packs**. The first domain pack is
topological insulators; the architecture is built so any physics subject can add its own pack without
touching the core. The skills follow the open [Agent Skills](https://agentskills.io/specification)
format, so they also work in other agents (Codex, Cursor, Copilot CLI, Gemini CLI, …).

Modeled on [`obra/superpowers`](https://github.com/obra/superpowers) (process-skill format + plugin
distribution) and [`K-Dense-AI/scientific-agent-skills`](https://github.com/K-Dense-AI/scientific-agent-skills)
(large SKILL.md library).

> **中文速览:** 面向物理科研的 Claude Code 技能集。核心插件 `physics-research`(24 个技能,**对所有物理学科通用**)
> 把科研分成三种模式——**读**(文献→严谨笔记)、**探索**(低成本、可追溯的快速试探)、**生产**(可信、可发表的
> 七阶段流水线);领域插件 `topological-insulator`(9 个技能)提供拓扑绝缘体的具体方法(紧束缚 H(k)、陈数、Z2、
> 边缘态……)。核心里不出现 H(k) 这类学科专属内容——它们只属于领域插件。技能靠描述里的触发词**自动激活**。
> 安装方法见下方 “Install & use in your agent”(支持 Claude Code / Codex / Cursor / Copilot / Gemini 等)。

## The idea: three research modes

Every task runs in one mode; picking the wrong one is where research time is wasted or trust is lost.
The `research-mode-router` skill routes you:

| Mode | When | Output |
|------|------|--------|
| **Read** | understand a paper / book / slides / code | thorough notes, full derivations |
| **Explore** | probe a question whose answer you can't yet picture | one-line `FINDINGS.md` + a saved plot |
| **Produce** | a result that must be trusted / published / reused | acceptance-gated deliverable |

A hard **firewall** separates them: exploration code tells you *where to look*, never *what the answer
is*. Trusted results are re-derived from scratch through a 7-stage production pipeline.

## Architecture: core + domain packs

```
physics-research-skills/            (this repo = a Claude Code plugin marketplace)
├── plugins/
│   ├── physics-research/           Tier 1 — subject-agnostic core (24 skills)
│   └── topological-insulator/      Tier 2 — domain pack (9 skills)
└── .claude-plugin/marketplace.json
```

The **core** speaks only of "your model / governing equations / structural invariants". Anything a
different subject wouldn't share (a Bloch Hamiltonian `H(k)`, Berry curvature, edge states) lives
**only** in a domain pack. Add a new subject = add a sibling plugin; the core is untouched.

## Install & use in your agent

Each skill is a self-contained folder with a `SKILL.md` (`name` + `description`), per the open
[Agent Skills](https://agentskills.io/specification) spec. Skills **auto-activate** when your task
matches a skill's `description` — you don't invoke them by hand. Pick your agent:

### Claude Code

Marketplace (recommended) — run each line as a **separate** `/plugin` command (don't paste them all at once):
```text
/plugin marketplace add Yamauch17/physics-research-skills
```
```text
/plugin install physics-research@physics-research-skills
```
```text
/plugin install topological-insulator@physics-research-skills
```
The third command (the `topological-insulator` domain pack) is optional. If `marketplace add` rejects the
`owner/repo` form, use the full clone URL instead:
`/plugin marketplace add https://github.com/Yamauch17/physics-research-skills.git`
Or as personal skills, without a marketplace — clone, then install into `~/.claude/skills/`:
```bash
git clone https://github.com/Yamauch17/physics-research-skills.git
pwsh -File physics-research-skills/install-local.ps1
```
On Windows, `install-local.ps1` junctions every skill into `~/.claude/skills`. On macOS/Linux, or to do it
by hand, copy each `plugins/*/skills/<name>` folder into `~/.claude/skills/` instead.

### Codex · Cursor · Gemini CLI · Copilot CLI (native, superpowers-style)

Each plugin ships the **same per-tool manifests as `superpowers`** — `.codex-plugin/plugin.json`,
`.cursor-plugin/plugin.json`, `gemini-extension.json` (+ `GEMINI.md` / `AGENTS.md`) — all pointing at its
`./skills/`. So each plugin installs natively: clone the repo and add the plugin **directory** the same
way you'd add the superpowers plugin.

```bash
git clone https://github.com/Yamauch17/physics-research-skills.git
```
Each plugin directory is a self-contained, multi-tool plugin: `plugins/physics-research/` (core, required)
and `plugins/topological-insulator/` (domain pack, optional).

| Agent | Manifest it reads | How to add |
|-------|-------------------|-----------|
| **Codex CLI** | `.codex-plugin/plugin.json` | add the plugin dir as a plugin (see Codex plugin docs) |
| **Cursor** | `.cursor-plugin/plugin.json` | add the plugin dir in Cursor's plugin settings |
| **Gemini CLI** | `gemini-extension.json` + `GEMINI.md` | install the plugin dir as an extension |
| **GitHub Copilot CLI** | Agent Skills under `skills/` | add the repo as a plugin source; skills are auto-discovered, invoked via the `skill` tool |

Point your tool at `plugins/physics-research` (and optionally `plugins/topological-insulator`) — the same
mechanism you use for superpowers. (Consult each tool's current plugin/skills docs for the exact add step;
the manifest layout is identical to superpowers.)

**Tool-name note.** Skill instructions reference a few Claude Code tool names; every agent has
equivalents and most map them automatically:

| In the skills | Codex | Copilot CLI | Gemini CLI |
|---------------|-------|-------------|------------|
| `Read` / `Write` / `Edit` | native file tools | `view` / `create` / `edit` | `read_file` / `write_file` / `replace` |
| `Bash` | native shell | `bash` | `run_shell_command` |
| `Grep` / `Glob` | native search | `grep` / `glob` | `grep_search` / `glob` |

The skills need only file + shell tools, so they port cleanly.

### Verify
```bash
pwsh -File validate.ps1
```
This checks that all 33 `SKILL.md` files parse and each skill's `name` matches its folder.

## Skills

### `physics-research` — core (24), universal to all physics
**Router + the 3 modes:** `research-mode-router` · `literature-reading-notes` · `exploration-mode` ·
`production-mode`
**Production pipeline (7 stages):** `literature-review-conventions` · `physics-brainstorming` ·
`theory-derivation` · `implementation-planning` · `convention-driven-coding` · `physical-verification` ·
`research-review`
**Rigor & infrastructure:** `convention-table` · `dimensional-analysis` · `numerical-spot-check` ·
`external-anchor-doctrine` · `convergence-study` · `prl-figure-style` · `jupytext-notebook-workflow` ·
`findings-logger` · `phased-git-workflow` · `obsidian-safe-markdown` · `adversarial-review` ·
`research-repo-bootstrap` · `checkpoint-and-resume`

### `topological-insulator` — domain pack (9)
`tight-binding-builder` · `symmetry-analysis` · `berry-curvature-chern` · `wilson-loop-wcc` ·
`z2-invariant` · `edge-states-bulk-boundary` · `kp-effective-model` · `topological-phase-diagram` ·
`numerical-tb-backend`

Runnable self-tests ship with the code skills: `numerical-spot-check/scripts/spot_check.py`,
`prl-figure-style/scripts/figstyle.py`, `berry-curvature-chern/scripts/chern_fhs.py` (FHS Chern with a
massive-Dirac sign anchor).

## Add your own domain pack

1. Copy `plugins/topological-insulator/` to `plugins/<your-subject>/`.
2. Edit `.claude-plugin/plugin.json` (name, description, keywords).
3. Add skills under `skills/<name>/SKILL.md`. Keep subject-specific symbols here, not in the core; make
   each skill **reference** core skills (`theory-derivation`, `physical-verification`, …) rather than
   duplicate them.
4. List the plugin in `.claude-plugin/marketplace.json`.
5. `pwsh -File validate.ps1`, then reinstall.

## How auto-activation works

Each `SKILL.md` has a `description` written as pure *triggering conditions* ("Use when …") packed with
English + Chinese keywords. The agent reads descriptions and loads a skill when the task matches — no
manual command needed. Descriptions never summarize the workflow (that would let the agent shortcut the
skill body).

## Credits & license

Method conventions distilled from real research repos (phased-git, PRL figures, external-anchor
doctrine, adversarial review). Format inspired by `superpowers` and `scientific-agent-skills`.
**MIT** — see `LICENSE`.
