---
name: literature-reading-notes
description: Use when reading a paper, textbook, lecture slides (PDF/PPT), or code to understand it and capture thorough study notes, especially when complete step-by-step derivations and physical intuition are wanted. Triggers on 读论文, 做笔记, 讲义, 看代码, "read this paper", "take notes", "explain this derivation", "understand this code".
---

# Literature Reading → Notes (Read mode)

## Overview
Produce standalone notes that let you reconstruct the physics without the source open. The notes are
the deliverable, not a summary. Default output language: the user's (Chinese); math in `$...$` /
`$$...$$`, rendered by Obsidian.

## Depth standard (every note)
- **Derive every step, no jumps.** Show the algebra — integration by parts, perturbation sums,
  operator manipulations. State what each symbol is. **Prove** claims (e.g. a symmetry, a conservation law, a bound); don't assert.
- **Physical picture beside the math:** intuition, meaning, significance, limiting cases.
- **Number key equations** (`\tag{}`) so later notes and how-tos can cite them.
- End with a short summary (本讲小结) and a one-line pointer to the next topic.

Write for a reader who knows the prerequisites but has *not* seen this specific material — spell out
what the source skips.

## Workflow
1. Skim the structure first (sections, key results): know the destination before deriving.
2. For each core result, re-derive it in the notes, filling every gap the source glosses over.
3. Add a physical-picture paragraph per result: what it means, why it matters, what breaks it.
4. Record the source's conventions (units, sign/transform conventions, index order) in a small table — see
   `convention-table`.
5. Save into the vault; keep the area index in sync if one exists. Never edit source PDFs.

## Formatting
**REQUIRED:** follow `obsidian-safe-markdown` (no raw `|` inside `$...$`, no blank lines inside
`$$…$$`, long unwrapped lines, MathJax-only). Template: `templates/NOTE-TEMPLATE.md`.

## Common mistakes
- Copying boxed results without the derivation — the derivation *is* the note.
- Omitting physical meaning: a wall of algebra you can't interpret next month.
- Silent convention switches (source's Fourier sign ≠ the one your later code assumes).
