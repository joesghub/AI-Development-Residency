---
name: skill-distiller
description: >-
  Turn the work of the current session into a reusable skill (a SKILL.md file),
  in a consistent house format. Use this skill WHENEVER the user asks to "turn
  this into a skill," "make a skill out of this," "capture how I want this done,"
  "save this workflow," "so we don't redo this every time," or signals they want
  to repeat a process reliably in future sessions — EVEN IF they don't say the
  word "skill." Also use it at the end of a session where the same task was done
  repeatedly or the user kept correcting the same thing, to offer to capture it.
  This skill both extracts the workflow from the conversation AND writes the new
  SKILL.md so that every generated skill comes out in the same shape.
---

# Skill Distiller

Capture a repeatable workflow from the current session and emit a new, well-formed
`SKILL.md`. The goal is twofold: (1) distill what actually happened into reusable
instructions, and (2) enforce a consistent format so every skill triggers and
reads the same way.

## Process

### 1. Distill the session (the summary step)
Scan the conversation and extract:
- **What was done** — the task that repeated, or the thing the user wants to lock in.
- **The sequence** — the concrete steps, in order.
- **Corrections** — anything the user had to fix or restate; these are the rules
  they care about most, so they belong in the skill.
- **Inputs and outputs** — formats, file types, naming conventions observed.
- **Success criteria** — how the user judged a good result.

A reusable prompt that produces this:
> "We just did <TASK> several times, and I kept steering you toward <CORRECTIONS>.
> Distill that into a SKILL.md that captures how I want this done next time —
> triggers, steps, and what 'done well' looks like."

### 2. Confirm before writing
Show the user the extracted intent (what it does, when it should trigger, expected
output) and let them fill gaps or correct it. Do not write the file until the user
confirms — the session is a draft of their intent, not the final word.

## House format for every generated skill

Write the new skill to `.claude/skills/<name>/SKILL.md`. Follow this shape exactly
so output stays consistent:

### Frontmatter
- `name`: kebab-case identifier that **matches the folder name**.
- `description`: this is the ONLY thing Claude uses to decide whether to fire the
  skill, and skills tend to *under*-trigger. So make it deliberately **pushy**:
  - state what the skill does AND the specific contexts/phrases that should trigger it,
  - list concrete triggers (file types, component kinds, user phrasings),
  - include an explicit "EVEN IF the user doesn't say '<keyword>'" clause,
  - tell Claude to apply it by default rather than wait to be asked.

### Body
- Open with a short **"How to apply"** section (when to use it inline vs. as a review).
- Then the substance as an **actionable checklist, steps, or decision tree** — not
  prose to be interpreted.
- One skill = one job. If it's sprawling, split it.
- Keep it under ~500 lines; if longer, move detail into `references/` files and
  point to them from the body.

## Quality bar before declaring done
- Would this description fire on a realistic request *without* the keyword in it?
- Is the body something Claude can follow step-by-step, or is it vague?
- Does the folder name match the `name`?
- Output the final file path and show the draft to the user for a last look.

## Note on scope
This is session-end distillation triggered on request — not a background process
that silently watches and emits skills on its own. The trigger is the user asking
(or an obvious end-of-session opportunity you offer to capture).
