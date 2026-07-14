---
name: checkpoint-and-resume
description: Use during any multi-step task that could be interrupted by a token limit, lost charge, or session end — persist each finished unit immediately and keep a resume protocol so nothing done is ever lost. Triggers on 断点续传, 断点, 续跑, 接着做, 中断恢复, 上次做到哪, checkpoint, resume, "pick up where we left off", "continue the task", "don't lose work", "save state", save progress, long task, token limit, "in case it stops", batch of files.
---

# Checkpoint & Resume

## Overview
Finished work must survive a sudden stop (token cutoff, dead battery, crash). The rule: **the moment a
unit is done, it is on disk and recorded** — never held only in memory or "to be written at the end".

## Practice
1. **Write each finished unit to disk immediately** (one file per unit, not a big end-of-run dump).
2. **Maintain a manifest** — `PROGRESS.md` / `BUILD-PROGRESS.md` — with one checkbox per unit. Tick it
   as each unit lands. **First unchecked box = the next task.**
3. **Put a "Resume protocol" header** at the top of the repo's `CLAUDE.md`: what to read first, how to
   find the next task, the sanity check to run. Any fresh session recovers from it.
4. **Commit per unit** at natural boundaries (see `phased-git-workflow`) so the recoverable state is
   also in git history.

## Red flags — STOP
- Holding several finished files unwritten "to save round-trips" — write them now.
- "I'll update the progress file at the end" — update it per unit; the end may never come.
- No resume protocol, so an interrupted task restarts from zero.

## Common mistakes
- A manifest that is updated in bulk after the fact — it no longer reflects the true recoverable point.
- Finished results kept only in the conversation, lost when the session ends.
