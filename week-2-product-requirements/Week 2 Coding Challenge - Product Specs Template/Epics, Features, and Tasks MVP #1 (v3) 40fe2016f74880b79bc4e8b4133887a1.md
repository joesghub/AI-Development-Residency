# Epics, Features, and Tasks: MVP #1 (v3)

# Epic 0: Platform Foundation (v3)

> 🔄 **What changed and why (v2 → v3)**
> 
> - **Feature 0.4 changed from "Home Screen App and Notifications" (a web PWA) to "Native App Install and Push Notifications."** The app is now React Native + Expo, so this feature sets up the app on the phone and wires push through Expo to APNs and FCM, instead of a service worker and "add to home screen."
> - **Feature 0.1 changed from deploying a web app to deploying a native app + a Vercel backend.** It now sets up the Expo app and its build/distribution alongside the backend deploys.
> - **Feature 0.5 gains the notification cap and log,** so the app never sends more than 3–4 notifications a day and records which Pot milestones already fired.
> - **Features 0.2 (User Accounts) and 0.3 (Data Security) are nearly unchanged,** with small native additions: secure token storage on the device.
> - **Task count for Epic 0: 33 → 36.**

**Outcome:** A secure, installable native app with user accounts, data protection, push notifications, scheduled jobs, and KPI tracking.

**Build phase:** Phase 0

## Feature 0.1: Project Setup and Deployment Pipeline

**Priority:** Must · *Updated for native + backend.*

**Feature-Level User Story:**

As the product team, we want the app and its backend to build and deploy automatically and safely, so that features reach beta testers quickly without breaking anything.

**Feature-Level Use Case Scenarios:**

- **Main:** A developer opens a pull request; the Vercel backend gets a preview deploy, and a test build of the app can be shared through Expo; after review, merging to `main` deploys the backend to production.
- **Alternate:** A build fails; the pull request can't be merged until it's fixed.
- **Edge:** A developer tries to push directly to `main`; branch protection blocks it.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E0-F1-T1 | Create the React Native app with Expo and TypeScript in the GitHub repo | Setup | ✏️ Updated |
| E0-F1-T2 | Set up the Next.js backend project and connect the repo to Vercel (preview deploys for pull requests, production from `main`) | Setup | ✏️ Updated |
| E0-F1-T3 | Create Supabase projects for test and production, with the command-line tools for migrations | Setup | — |
| E0-F1-T4 | Add environment variables in Vercel and Expo for each environment | Setup | ✏️ Updated |
| E0-F1-T5 | Enable branch protection on `main` and require pull request reviews | Setup | — |
| E0-F1-T6 | Turn on GitHub secret scanning and Dependabot alerts | Security | — |
| E0-F1-T7 | Add a GitHub Actions workflow that runs linting and tests on each pull request | Testing | — |
| E0-F1-T8 | Set up Expo's build service and a way to share test builds with the team | Setup | 🆕 |

## Feature 0.2: User Accounts

**Priority:** Must · *Small native addition.*

**Feature-Level User Story:**

As a user, I want to create an account and log in securely on my phone, so that my financial information stays private and available only to me.

**Feature-Level Use Case Scenarios:**

- **Main:** A user signs up with an email and password, confirms their email, and lands on onboarding.
- **Alternate:** A user chooses a magic link and logs in from their email.
- **Alternate:** A user forgets their password and resets it by email.
- **Edge:** A logged-out user opens the app and is taken to login.
- **Edge:** A user deletes their account, and all their data is permanently removed.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E0-F2-T1 | Design sign-up, login, and password reset screens (mobile-first, calm, minimal fields) | Design | — |
| E0-F2-T2 | Build sign-up, login, and magic link login with Supabase Auth in the app | Frontend | ✏️ Updated |
| E0-F2-T3 | Build the password reset flow | Frontend | — |
| E0-F2-T4 | Keep the user logged in between sessions using the phone's secure storage | Frontend | ✏️ Updated |
| E0-F2-T5 | Create the `profiles` table, created automatically when a user signs up | Database | — |
| E0-F2-T6 | Build account deletion that removes all of the user's data and disconnects their bank | Backend | — |
| E0-F2-T7 | Add sign out, clearing the secure token from the device | Frontend | ✏️ Updated |

## Feature 0.3: Data Security

**Priority:** Must · *One native addition.*

**Feature-Level User Story:**

As a user, I want my financial data protected and my progress accurate, so that I can trust the app with my bank information and trust the numbers it shows.

**Feature-Level Use Case Scenarios:**

- **Main:** A logged-in user requests their data and receives only their own.
- **Edge:** Someone tries to request another user's data and receives nothing.
- **Edge:** A user tries to write to their own Pot directly; the request is rejected, because only the server can.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E0-F3-T1 | Write row-level security policies for every table | Security | — |
| E0-F3-T2 | Write automated tests confirming one user can't read or change another user's data | Testing | — |
| E0-F3-T3 | Restrict the Supabase admin key and Plaid secrets to the Vercel backend only | Security | — |
| E0-F3-T4 | Set up encrypted storage for Plaid access tokens, readable only by the server | Security | — |
| E0-F3-T5 | Add secret-key validation to all scheduled job endpoints | Security | — |
| E0-F3-T6 | Write the privacy policy page explaining what data is stored and why | Design | — |
| E0-F3-T7 | Make `pot_ledger` and `daily_results` read-only for users, so only the server can write to them | Security | — |
| E0-F3-T8 | Store the login token in the phone's secure storage (Keychain/Keystore) and require HTTPS for all backend calls | Security | 🆕 |

## Feature 0.4: Native App Install and Push Notifications

**Priority:** Must · *Rewritten from the web PWA version.*

**Feature-Level User Story:**

As a user, I want to install the app and get its notifications, so that it reminds me instead of relying on me to remember it.

**Feature-Level Use Case Scenarios:**

- **Main:** A new user installs the app, and early in onboarding is asked to allow notifications, with a short line on why they matter.
- **Alternate:** A user declines notifications; the app still works, and the same information is visible on its screens, with a gentle reminder that notifications are how the app helps most.
- **Edge:** A user changes their mind later and turns notifications on (or off) in settings.
- **Edge:** A user installs on a second device; both receive notifications.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E0-F4-T1 | Set up the app icon, splash screen, and app name for iOS and Android | Setup | ✏️ Updated |
| E0-F4-T2 | Add Expo push notifications and request a push token on the device | Frontend | ✏️ Updated |
| E0-F4-T3 | Connect Expo Push to Apple's APNs and Google's FCM | Setup | 🆕 |
| E0-F4-T4 | Build the notification permission request, shown after the user sees value, with a plain reason | Frontend | ✏️ Updated |
| E0-F4-T5 | Create the `device_tokens` table and save each device's push token | Database | ✏️ Updated |
| E0-F4-T6 | Build a backend function that sends a notification to a user's devices through Expo Push | Backend | ✏️ Updated |
| E0-F4-T7 | Build deep links so tapping a notification opens the right screen (home or breakdown) | Frontend | 🆕 |
| E0-F4-T8 | Build notification settings: turn each type on or off, and set the morning time | Frontend | ✏️ Updated |

## Feature 0.5: Scheduled Jobs, Notification Rules, and KPI Tracking

**Priority:** Must · *Gains the daily cap and milestone log.*

**Feature-Level User Story:**

As the product team, we want time-based actions to run automatically, notifications to stay within a gentle daily limit, and key actions to be recorded, so that the app engages users without overwhelming them and we can measure whether the MVP works.

**Feature-Level Use Case Scenarios:**

- **Main:** Every hour, the scheduler triggers a backend function that runs whatever is due for each user's time zone: the morning budget, the ~2pm breakdown, confirmations, and milestone checks.
- **Main:** When a user parks a wishlist item or crosses a Pot milestone, an event is recorded.
- **Edge:** Several notifications would fire on the same day; the daily cap keeps it to 3–4, and lower-priority ones wait.
- **Edge:** A job fails; the error is logged and the next hourly run picks up any missed work.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E0-F5-T1 | Set up an hourly Supabase scheduled job that calls a secure Vercel function | Setup | — |
| E0-F5-T2 | Build the scheduled job handler that runs each user's due jobs based on their time zone | Backend | — |
| E0-F5-T3 | Add logging for scheduled job runs and failures | Backend | — |
| E0-F5-T4 | Create the `events` table and a helper to record key actions | Database | — |
| E0-F5-T5 | Create the `notification_log` table and enforce the daily cap of 3–4, recording which Pot milestones already fired | Backend | 🆕 |
| E0-F5-T6 | Build saved database queries (views) for each MVP KPI: activation, retention, comeback rate, days under budget, Pot growth, wishlist adoption, Buy Day outcomes, notification open and opt-out rates | Database | ✏️ Updated |

# Epic 1: Effortless Money Tracking (v3)

> 🔄 **What changed and why (v2 → v3)**
> 
> - **New Feature 1.8: Budget Breakdown.** A screen, always available, that explains how today's budget was calculated from recent settled transactions, plus a ~2pm notification that points to it. This is the "teaching" feature, replacing the same-day nudge idea. It works from day one because it explains the *inputs* to today's number, not today's fresh purchases.
> - **Feature 1.6 (Morning Notification) gains a deep link** so tapping it opens the home screen, and a small wording note to distinguish it from the new 2pm notification.
> - **Everything else in Epic 1 is unchanged from v2** (onboarding, Plaid, CSV, three buckets, Today's Budget, Usuals insights), apart from "web" becoming "app" where a screen is built.
> - **Task count for Epic 1: 39 → 44.**

**Outcome:** Users see what they can spend today, and understand where that number comes from, with almost no effort.

**Pain points:** P1, P2, P6 · **Build phase:** Phase 1

## Feature 1.1: Quick Onboarding

**Priority:** Must · *Unchanged from v2 (tasks E1-F1-T1 to T5).*

**Feature-Level User Story:** As a chronic abandoner, I want setup to take less than five minutes, so that I see value before I lose interest.

## Feature 1.2: Bank Connection (Plaid)

**Priority:** Must · *Unchanged from v2 (tasks E1-F2-T1 to T9).* The Plaid secure login now opens in the native app's in-app browser rather than a web page.

**Feature-Level User Story:** As a user, I want to connect my bank securely, so that my spending is tracked automatically without manual entry.

## Feature 1.3: CSV Import

**Priority:** Must (beta fallback) · *Unchanged from v2 (tasks E1-F3-T1 to T5).* On a phone, the user picks the file through the device's file picker.

**Feature-Level User Story:** As a user who can't or won't link my bank, I want to upload my bank's transaction file, so that I can still use the app.

## Feature 1.4: Three Buckets

**Priority:** Must · *Unchanged from v2 (tasks E1-F4-T1 to T6).*

**Feature-Level User Story:** As a user, I want my spending sorted automatically into Bills, Essentials, and Usuals, so that I never have to categorize anything myself.

## Feature 1.5: Today's Budget

**Priority:** Must · *Unchanged from v2 (tasks E1-F5-T1 to T6).* (Renamed from "Today's Number" in the deck; the documents use "Today's Budget" from here on.)

**Feature-Level User Story:** As a user with time blindness, I want one daily number for my Usuals, so that I can decide at a glance without thinking about the whole month.

## Feature 1.6: Morning Notification

**Priority:** Must · *Updated: deep link + wording.*

**Feature-Level User Story:** As a user who forgets to check apps, I want Today's Budget and my next Buy Day sent to me each morning, so that I know my number and stay excited about what's coming.

**Feature-Level Use Case Scenarios:**

- **Main:** At the user's chosen morning time: "Today's Budget: $28. Headphones Buy Day: 12 days 🎧" Tapping it opens the home screen.
- **Alternate:** The user has no wishlist items; the notification shows only Today's Budget, with an occasional gentle prompt to add one.
- **Edge:** Notifications are off; the number is on the home screen when the app opens.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E1-F6-T1 | Add the morning notification to the scheduled jobs, with Today's Budget and the next Buy Day countdown | Backend | — |
| E1-F6-T2 | Write friendly text with rotating variations, worded as the "here's your number" push (distinct from the 2pm breakdown) | Design | ✏️ Updated |
| E1-F6-T3 | Build the morning notification time setting | Frontend | — |
| E1-F6-T4 | Deep link the morning notification to the home screen | Frontend | 🆕 |
| E1-F6-T5 | Track the events "morning notification sent" and "opened" | Backend | — |

## Feature 1.7: Usuals Insights

**Priority:** Should · *Unchanged from v2 (tasks E1-F7-T1 to T4).*

**Feature-Level User Story:** As a newly diagnosed adult, I want to see what I usually spend money on, so that I understand my patterns without reviewing every transaction.

## Feature 1.8: Budget Breakdown 🆕

**Priority:** Must

**Feature-Level User Story:**

As someone who finds budgets abstract, I want to see how my recent spending shaped today's budget, so that I learn what moves my number instead of just being told what it is.

**Feature-Level Use Case Scenarios:**

- **Main:** The user opens the Budget Breakdown screen and sees the plain math behind today's number: income this pay period, minus Bills set aside, minus Essentials set aside, minus Usuals already spent, divided by days until payday, equals Today's Budget. Every line is built from recent settled transactions.
- **Main:** Around 2pm, after the daily sync, a notification arrives: "Here's how your spending shaped today's budget." Tapping it opens the breakdown screen.
- **Alternate:** It's the user's first day; the breakdown still works, built from the 30–90 days of history Plaid imported on connection.
- **Alternate:** The user turns the 2pm notification off in settings; the screen is still available anytime.
- **Edge:** A line has little data yet (for example, Essentials estimated from a short history); it's labeled "estimated" rather than shown as exact.
- **Edge:** The user tapped in from the morning notification; the breakdown is reachable from the home screen too, not only from its own notification.

| ID | Task | Type |
| --- | --- | --- |
| E1-F8-T1 | Build the breakdown calculation: return each line of the Today's Budget math (income, Bills, Essentials, Usuals spent, days to payday) from recent settled transactions | Backend |
| E1-F8-T2 | Label lines built from limited history as "estimated" | Backend |
| E1-F8-T3 | Design the Budget Breakdown screen: one clear line per step, calm, no red, plain language | Design |
| E1-F8-T4 | Build the Budget Breakdown screen and link to it from the home screen | Frontend |
| E1-F8-T5 | Add the ~2pm breakdown notification to the scheduled jobs, after the daily sync, respecting the daily cap | Backend |
| E1-F8-T6 | Write the breakdown notification text and deep link it to the breakdown screen | Design |
| E1-F8-T7 | Add a setting to turn the breakdown notification on or off | Frontend |
| E1-F8-T8 | Track the events "breakdown viewed" and "breakdown notification opened" | Backend |

# Epic 2: Patience Pot and Wishlist (v3)

> 🔄 **What changed and why (v2 → v3)**
> 
> - **New Feature 2.6: Patience Pot Milestone Notifications.** As the Pot grows toward the next wishlist item, notifications celebrate crossing 25%, 50%, and 75%. This replaces the plain Buy Day reminder with a progress story, rewarding patience along the way, not just at the finish.
> - **Feature 2.4 (Buy Day Check-In) keeps the 100% Buy Day notification,** now framed as the final milestone after 25/50/75.
> - **Everything else in Epic 2 is unchanged from v2** (Daily Close and Pot, Wishlist, Buy Day Scheduling, Matching, Kept Your Patience), apart from "screen" being a native screen.
> - **Task count for Epic 2: 44 → 50.**

**Outcome:** Daily patience visibly funds the things users want, celebrated at every step.

**Pain points:** P3, P4, P6 · **Build phase:** Phase 2

## Feature 2.1: Daily Close and Patience Pot

**Priority:** Must · *Unchanged from v2 (tasks E2-F1-T1 to T10).*

**Feature-Level User Story:** As someone who needs to see progress, I want the money I don't spend each day to go into a Pot, confirmed by my bank, so that patience feels real and rewarding.

## Feature 2.2: Wishlist

**Priority:** Must · *Unchanged from v2 (tasks E2-F2-T1 to T9).*

**Feature-Level User Story:** As someone who buys on impulse, I want a quick way to save things I want for later, so that I can say later instead of now.

## Feature 2.3: Buy Day Scheduling

**Priority:** Must · *Unchanged from v2 (tasks E2-F3-T1 to T7).*

**Feature-Level User Story:** As someone with time blindness, I want each wishlist item to have a real date when I can afford it, so that waiting feels concrete and exciting instead of endless.

## Feature 2.4: Buy Day Check-In and Matching

**Priority:** Must · *Unchanged from v2 (tasks E2-F4-T1 to T12).* The Buy Day notification is now the 100% point of the milestone series in Feature 2.6.

**Feature-Level User Story:** As a user, I want Buy Day to feel like a celebration and my purchase to be recognized automatically, so that buying on purpose feels like a win, not a slip.

## Feature 2.5: Kept Your Patience

**Priority:** Must · *Unchanged from v2 (tasks E2-F5-T1 to T6).*

**Feature-Level User Story:** As a chronic abandoner, I want missed Buy Days to count as a win instead of a to-do, so that stepping away never creates a backlog.

## Feature 2.6: Patience Pot Milestone Notifications 🆕

**Priority:** Must

**Feature-Level User Story:**

As someone who needs encouragement along the way, I want to hear when I'm getting closer to something on my wishlist, so that saving feels rewarding before I even buy it.

**Feature-Level Use Case Scenarios:**

- **Main:** As the Pot grows toward the top wishlist item, a notification fires at each quarter: "You're a quarter of the way to your headphones! $30 of $120 saved," then halfway, then "Almost! Just $30 to go." At 100%, the Buy Day notification takes over.
- **Alternate:** The user adds a new item to the top of the list; milestones now track that item.
- **Edge:** An item is added when the Pot is already past 50%; the 25% and 50% notifications don't fire retroactively, and the next one is 75%.
- **Edge:** The Pot dips below a milestone and crosses it again later; the notification doesn't repeat, because each milestone fires once per item.
- **Edge:** A milestone and the 2pm breakdown would land the same day; both can go (a "3 notifications" day), but the daily cap still holds.

| ID | Task | Type |
| --- | --- | --- |
| E2-F6-T1 | Build the milestone check: compare the Pot balance against 25/50/75% of the top wishlist item's cost | Backend |
| E2-F6-T2 | Record fired milestones per item (in `notification_log`) so each fires once and dips don't re-trigger | Backend |
| E2-F6-T3 | Handle items added when the Pot is already past a milestone (skip the passed ones) | Backend |
| E2-F6-T4 | Add the milestone check to the scheduled jobs, after confirmations and Pot changes, respecting the daily cap | Backend |
| E2-F6-T5 | Write the milestone notification text for 25/50/75%, celebratory and specific | Design |
| E2-F6-T6 | Deep link milestone notifications to the Pot / wishlist screen | Frontend |
| E2-F6-T7 | Track the event "milestone notification sent," with the level | Backend |

---

# Epic 3: Bill Reminders — Removed in v3

> 🔄 **What changed and why (v2 → v3)**
> 
> 
> Epic 3 (Bill Detection and Bill Reminders) is **removed from the MVP.** Bill reminders were cut, and with them the reminder feature. **Bill detection survives**, but it moved into the Today's Budget calculation, where it belongs: the budget must set money aside for recurring bills to be honest, even with no reminders.
> 
> - **Where detection lives now:** the `bills` table and recurring-payment detection are part of the Build Plan (v3) data model and feed Feature 1.5 (Today's Budget) and Feature 1.8 (Budget Breakdown). No new tasks are needed, since Today's Budget already subtracts detected bills.
> - **What's gone:** the bill reminder notification and the "mark as paid" flow (v2 tasks E3-F2-T1 to T4 and the reminder parts of E3-F1).
> - **Returns in:** the MMP, as a bill reminder feature, if validated.

*The epic numbering is kept (Epic 4 stays Epic 4) so task IDs from v2 don't shift.*

# Epic 4: Guilt-Free Comebacks (v3)

> 🔄 **What changed and why (v2 → v3)**
> 
> - **Nearly unchanged from v2.** The welcome-back summary, money stress check-in, and monthly recap all carry over.
> - **Two small updates:** the welcome-back summary can now mention Pot milestones reached while the user was away, and the monthly recap and welcome-back notifications are wired to the native deep-link and daily-cap system from Epic 0.
> - **Task count for Epic 4: 15 → 15** (no new tasks; two revised).

**Outcome:** Users return after a lapse without a backlog or shame.

**Pain point:** P4 · **Build phase:** Phase 3

## Feature 4.1: Welcome-Back Summary

**Priority:** Must · *Updated: can surface milestones reached while away.*

**Feature-Level User Story:**

As a chronic abandoner, I want returning after time away to be quick and judgment-free, so that one missed week doesn't make me quit.

**Feature-Level Use Case Scenarios:**

- **Main:** The user returns after 7+ days: "Your Pot grew $46 while you were away. You passed the halfway mark on your headphones. Today's Budget: $31." Then straight to the home screen.
- **Alternate:** A Buy Day passed while away: "You kept your patience on the jacket. Want it back on your wishlist?"
- **Alternate:** A shorter break (under 7 days); no summary is shown.
- **Edge:** A lot happened while away; the summary still shows at most three items.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E4-F1-T1 | Update "last active date" in `profiles` each time the app is opened | Backend | — |
| E4-F1-T2 | Build the summary generator, choosing the three most useful items: Pot growth, milestones reached, kept-patience items, and Today's Budget | Backend | ✏️ Updated |
| E4-F1-T3 | Design the welcome-back screen: warm wording, no red, no overdue language | Design | — |
| E4-F1-T4 | Build the welcome-back screen | Frontend | — |
| E4-F1-T5 | Write welcome-back message variations | Design | — |
| E4-F1-T6 | Track the event "returned after lapse" | Backend | — |
| E4-F1-T7 | Review all screens to remove streaks, overdue warnings, and guilt-based wording | Testing | — |

## Feature 4.2: Money Stress Check-In

**Priority:** Should · *Unchanged from v2 (tasks E4-F2-T1 to T4).*

**Feature-Level User Story:** As the product team, we want users to rate their money stress at signup and after 30 days, so that we can measure whether the app reduces stress.

## Feature 4.3: Monthly Recap

**Priority:** Could · *Updated: wired to native notifications.*

**Feature-Level User Story:** As a user, I want a short monthly summary of my progress, so that I can see how patience paid off.

**Feature-Level Use Case Scenarios:**

- **Main:** On the first of the month, a notification links to a 30-second recap: Total Kept, items bought on purpose, and items where you kept your patience.
- **Edge:** A quiet month with little activity; the recap stays positive and short.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E4-F3-T1 | Design the recap screen (three cards, 30 seconds to read) | Design | — |
| E4-F3-T2 | Build the recap generator: Total Kept, items bought on purpose, and kept-patience items | Backend | — |
| E4-F3-T3 | Add the monthly recap notification to the scheduled jobs, deep-linked and within the daily cap | Backend | ✏️ Updated |
| E4-F3-T4 | Build the recap screen | Frontend | — |

---

**Epic summary (v3)**

| Epic | Features | Tasks | Change |
| --- | --- | --- | --- |
| Epic 0: Platform Foundation | 5 | 36 | +3 (native + push) |
| Epic 1: Effortless Money Tracking | 8 | 44 | +5 (Budget Breakdown) |
| Epic 2: Patience Pot and Wishlist | 6 | 50 | +6 (milestones) |
| ~~Epic 3: Bill Reminders~~ | 0 | 0 | −9 (removed; detection folded into Today's Budget) |
| Epic 4: Guilt-Free Comebacks | 3 | 15 | 0 |
| **Total** | **22** | **145** | +5 net |