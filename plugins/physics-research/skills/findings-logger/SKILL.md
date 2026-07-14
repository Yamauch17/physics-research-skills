---
name: findings-logger
description: Use when recording the result of a quick exploration so it stays traceable — the one mandatory output of exploration mode. Triggers on FINDINGS, 记录发现, 记一下, 记下来, 存个结论, log this, "log the finding", "note the result", "record what we found", "write it down", "jot down", one-line log, exploration result.
---

# Findings Logger

## Overview
The single mandatory output of `exploration-mode`. One append-only line makes a throwaway probe
recoverable tomorrow — without it, exploration is wasted.

## The format
Append to `FINDINGS.md`, one line per finding:

```
- 2026-07-13 — response saturates above g≈1; slope matches the linear-theory estimate. → scratch/response_vs_g_g0.3_T10.png
```

Three parts: **date** · **one-sentence conclusion** · **path to the figure** (which encodes its
parameters in the filename).

## Rules
- One line. If it needs a paragraph, it is probably `production-mode` work now.
- Always link a saved figure; a conclusion with no artifact is not traceable.
- Append, never rewrite history — the log is a timeline.

## Common mistakes
- Batching findings "to write up later" — write the line the moment the plot is saved.
- A conclusion with no figure path, or a figure whose filename omits its parameters.
