---
name: obsidian-safe-markdown
description: Use when writing or editing Markdown notes and theory documents that render in Obsidian with LaTeX math. Triggers on obsidian, 笔记格式, 公式渲染, 公式显示不对, 双美元符, markdown math, LaTeX in markdown, MathJax, "$$", table with math, "renders wrong", "math broke in Obsidian", "equations don't display", writing a theory note.
---

# Obsidian-Safe Markdown

## Overview
Obsidian's Markdown + MathJax has a few sharp edges that silently corrupt math. Follow these rules so
theory docs render correctly and diff cleanly.

## Rules
- **Long, unwrapped lines** — one line per paragraph. Do *not* hand-wrap at ~80 chars; manual wrapping
  breaks list/paragraph rendering and makes diffs noisy.
- **Never a raw `|` inside `$...$` in a table cell.** Obsidian's table auto-formatter splits on `|`
  and corrupts the math. Write `\lvert x \rvert` (or `\mid`), never `|x|`, inside table-cell math.
- **No blank lines inside `$$…$$`** blocks — a blank line ends the math block early.
- **MathJax-compatible LaTeX only** — no packages/macros MathJax lacks. Test-render before committing.
- Do not edit source PDFs the notes derive from.

## Common mistakes
- A `|B|` in a table cell that renders as a broken row + stray dollar signs.
- Hand-wrapped paragraphs that turn into hard line breaks.
- A multi-line aligned block with a blank line in the middle that stops rendering halfway.

Used by `literature-reading-notes` and any theory `.md`.
