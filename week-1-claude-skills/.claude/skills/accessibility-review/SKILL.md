---
name: accessibility-review
description: >-
  Accessibility (a11y) standards and a review checklist for building
  enterprise-ready user interfaces, targeting WCAG 2.2 AA. Use this skill
  WHENEVER you create, edit, or review any user-facing interface — web pages,
  React/Vue/HTML components, forms, buttons, modals, menus, navigation, tables,
  or any markup a person will see or interact with — EVEN IF the user does not
  say the word "accessibility." Also apply it when the user mentions WCAG,
  screen readers, keyboard navigation, ARIA, color contrast, focus, or inclusive
  design, and when auditing existing UI for compliance. Default to applying
  these standards on any front-end work rather than waiting to be asked.
---

# Accessibility Review

Build and review interfaces so they are usable by people relying on keyboards,
screen readers, magnification, and other assistive technology. Target standard
is **WCAG 2.2 Level AA** unless the user specifies otherwise.

## How to apply this skill

- When **writing new UI**, follow the checklist below as you go — don't bolt
  accessibility on afterward.
- When **reviewing existing UI**, walk the checklist top to bottom and report
  findings grouped by severity: **Blocker** (keyboard trap, unusable with a
  screen reader), **Major** (fails a WCAG AA criterion), **Minor** (works but
  degrades the experience). For each finding give the location, the problem, the
  specific WCAG criterion if relevant, and a concrete fix.

## Checklist

### 1. Semantic HTML first
- Use the right element for the job: `<button>` for actions, `<a href>` for
  navigation, `<nav>`, `<main>`, `<header>`, `<footer>`, `<ul>`/`<ol>` for lists.
- One `<h1>` per page; headings nest in order (no skipping levels).
- Never rebuild a native control out of `<div>`s when a real element exists —
  native elements come with keyboard and screen-reader behavior for free.

### 2. Keyboard operability
- Every interactive element must be reachable and operable with Tab, Shift+Tab,
  Enter, and Space (and arrow keys for composite widgets like menus/tabs).
- Tab order follows visual/reading order; no positive `tabindex` values.
- No keyboard traps — focus can always move away from a component.

### 3. Focus management
- A **visible focus indicator** on every focusable element — never
  `outline: none` without a clear replacement.
- When opening a modal/dialog, move focus into it and trap focus inside until
  it closes; on close, return focus to the triggering element.

### 4. Color and contrast
- Text contrast ≥ **4.5:1** (≥ 3:1 for large text, ≥ 18.66px bold or 24px).
- UI components and meaningful graphics ≥ **3:1** against adjacent colors.
- Never use color as the *only* way to convey meaning (add text, icon, or
  pattern — e.g. errors need more than red).

### 5. Images and media
- Informative images need descriptive `alt` text; decorative images use
  `alt=""` so screen readers skip them.
- Video needs captions; audio needs a transcript.

### 6. Forms
- Every input has a programmatically associated `<label>` (via `for`/`id` or
  wrapping).
- Group related fields with `<fieldset>`/`<legend>`.
- Errors are announced and tied to their field (e.g. `aria-describedby`), not
  signaled by color alone; keep instructions visible, not placeholder-only.

### 7. ARIA — only when needed
- Prefer native HTML. Reach for ARIA only to fill gaps native elements can't.
- Follow the first rule of ARIA: *don't use ARIA if a native element does it.*
- Give icon-only controls an accessible name (`aria-label`).

### 8. Dynamic content
- Announce async updates (toasts, validation, loading results) with an
  appropriate live region (`aria-live="polite"` for most, `"assertive"` for
  urgent).
- Respect `prefers-reduced-motion` for animation.

## Quick verification
- Tab through the whole interface using only the keyboard — can you reach and
  operate everything, and is focus always visible?
- Check text contrast with a contrast tool against WCAG AA.
- Run an automated pass (e.g. axe) to catch mechanical issues, then confirm the
  human-judgment items above by hand — automated tools catch only a fraction.
