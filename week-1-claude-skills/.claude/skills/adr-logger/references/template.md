# ADR Template

Copy everything in the code block into a new file `docs/adr/NNNN-title.md`,
replacing `NNNN` with the next sequential number and filling in each section.
Keep every heading. Do not remove the Options section.

```markdown
# ADR-NNNN: [The decision, in a few words]

## Date and status
[Date]. [Proposed, Accepted, or Replaced by ADR-NNNN]

## Context
What is happening? What problem pushed you to make a choice?

## Options
What choices did you look at? Write the good and bad parts of each one.

- Option 1:
  - Good:
  - Bad:
- Option 2:
  - Good:
  - Bad:

## Decision
What did you choose, and why?

## Consequences
What happens because of this choice? What gets easier? What gets harder?
What do you need to do next?
```

## Rules

- **One decision per ADR.** Split multiple decisions into multiple files.
- **Number sequentially**, zero-padded to four digits: `0001`, `0002`, …
- **Status**: `Proposed` (still deciding), `Accepted` (acting on it now), or
  `Replaced by ADR-NNNN` (superseded by a later ADR).
- **Say why, not just what.** The reasoning is the point.
- **Include the option you did NOT pick**, with its honest trade-offs.
- **Date things that can change** (costs, limits, versions).

## This project is based on the Michael Nygard ADR template
(Title, Status, Context, Decision, Consequences), extended with an Options
section so the alternatives that were not chosen are written down too.
