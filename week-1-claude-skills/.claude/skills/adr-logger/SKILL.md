---
name: adr-logger
description: >-
  Capture Architecture Decision Records (ADRs) in docs/adr. Use this skill
  WHENEVER an architectural or technical decision is made, discussed, or
  changed while building this project — choosing a framework, database,
  hosting provider, auth approach, external service, data model, folder
  structure, or any choice that would be costly to reverse later. Trigger it
  proactively, even when the user does not say the word "ADR": phrases like
  "let's use X instead of Y", "we decided to", "I'll go with", "should we use
  A or B", "switch from X to Y", or any time the build commits to one option
  over others. Also use it at the start of work to read existing ADRs before
  making changes, and when a past decision is being reversed or superseded.
  Do NOT use it for tiny, easily-reversible choices (variable names, a single
  CSS value, which line to edit).
---

# ADR Logger

This skill captures **Architecture Decision Records**: short documents that
record one important technical choice and why it was made. It keeps them
correctly numbered, correctly formatted, and correctly superseded, so the
project ends with a complete, honest history of its architecture instead of a
pile of undocumented decisions.

An ADR records a decision that is **hard to change later** — which framework,
database, host, auth method, external API, or data model to use. It does NOT
record small reversible choices.

## Before making changes: read first

At the start of a work session, or before making any architectural change,
**read every file in `docs/adr`** so current decisions and their rationale are
known. A new decision must be consistent with accepted ADRs, or must formally
supersede one (see "When a decision changes").

## When to write a new ADR

Write one as soon as a significant decision is settled. Signals that a decision
is ADR-worthy:

- A framework, library ecosystem, or language is chosen (e.g. React Native vs.
  Next.js; a design-system library).
- A database, hosting provider, or external service is chosen (e.g. Supabase,
  Vercel, Plaid).
- An auth, security, or data-isolation approach is decided (e.g. row-level
  security).
- A data model, schema shape, or key workflow is settled (e.g. how a core
  calculation works; how background jobs run).
- A previous decision is being reversed or replaced.

If unsure whether something qualifies, ask: *"Would a new developer be confused
or make a mistake if they didn't know we chose this, and why?"* If yes, write
the ADR.

**One ADR = one decision.** If a conversation settles three decisions, write
three ADRs.

## How to write it

1. **Find the next number.** List `docs/adr`. Numbers are zero-padded and
   sequential: `0001`, `0002`, …. The next ADR is the highest existing number
   plus one. If `docs/adr` does not exist yet, create it, and start at `0001`.
2. **Name the file** `NNNN-short-kebab-case-title.md`, e.g.
   `0004-use-react-native-paper.md`. The title is the decision in a few words.
3. **Fill the template** (`references/template.md`) exactly. Keep every section
   heading. Do not invent sections or drop the Options section.
4. **Write the reasoning, not just the outcome.** The Context explains what
   forced the choice; Options lists the real alternatives with honest Good/Bad
   for each (including the option NOT chosen); Decision states the pick and
   *why*; Consequences states what gets easier, what gets harder, and the next
   steps.
5. **Date anything that can change** (costs, free-tier limits, version numbers)
   so a future reader knows it may be stale.
6. **Status** starts as `Accepted` for a decision being acted on now, or
   `Proposed` if it is still under discussion.

See `references/template.md` for the exact format and
`references/example.md` for a filled-in example.

## When a decision changes

Never delete or rewrite an old ADR. Instead:

1. Write a **new** ADR describing the new decision, with the next number.
2. In the new ADR's Context, note which ADR it replaces.
3. Edit the **old** ADR's "Date and status" line to
   `Replaced by ADR-NNNN` (the new number), leaving everything else intact.

This preserves the history: the project shows both what was decided before and
why it changed.

## After writing

- Save the ADR under `docs/adr/`.
- Commit and push it **together with the code the decision affects**, so the
  decision and its implementation travel together.
- Tell the user, in one line, which ADR number was created and its title.

## Keeping CLAUDE.md wired up

This skill works best when the project's `CLAUDE.md` tells every session to use
it. If `CLAUDE.md` does not already contain an instruction to read and write
ADRs, add this line:

> Read every ADR in `docs/adr` before making changes, and write a new ADR
> (using the adr-logger skill) for every big architectural decision.
