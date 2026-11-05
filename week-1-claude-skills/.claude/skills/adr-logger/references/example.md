# Example ADR

A filled-in example, using a real decision from this project. Note how the
Options section includes the choice that was *not* picked, and how the Decision
explains *why*, not just *what*.

```markdown
# ADR-0004: Build a native app with React Native, not a Next.js web app

## Date and status
November 5, 2026. Accepted.

## Context
Patiencents is a budgeting app for adults with ADHD. Its core promise is that
the app comes to the user through notifications (a morning budget, an afternoon
breakdown, and Patience Pot milestones) rather than relying on the user to
remember to open it. We need to choose the kind of app to build. A course
template suggested a Next.js web app with Material UI.

## Options
- Next.js web app (mobile-friendly / PWA):
  - Good: One of the stacks the course expects; fast to deploy on Vercel at a
    public URL; one language for screens and server code.
  - Bad: On iOS, web apps can only send push notifications if the user manually
    adds the app to their home screen, and delivery is unreliable. For an ADHD
    audience whose core struggle is "out of sight, out of mind," that setup
    step defeats the product's whole point.
- React Native (Expo) native app with a Vercel backend:
  - Good: Reliable push notifications on iOS and Android from install, which is
    the product's entire engagement model; one codebase for both platforms.
  - Bad: More to build; app distribution uses an install link (Expo/TestFlight)
    instead of a plain web URL; the design system is React Native Paper rather
    than Material UI.

## Decision
Build a React Native (Expo) native app with the backend/API on Vercel, because
notifications are the engagement model and native is the only way they work
reliably. The instructor approved deviating from the web-app template as long
as the change is reasonable and documented.

## Consequences
Push notifications work from install, so the core loop is testable.
The design system becomes React Native Paper (still Material Design) instead of
Material UI — see ADR-0005. "Live and reachable" is met by a public Vercel
backend plus an install link rather than a single web URL — see ADR-0006.
Next steps: set up the Expo project, wire Supabase Auth, and configure Expo
push to Apple's APNs and Google's FCM.
```
