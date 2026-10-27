# Epics and Features

# Epics, Features, and Tasks: MVP #1

> 🧩 **Purpose:** Break the MVP #1 scope into buildable work. **Epics** are large outcomes, **features** are user-facing capabilities that deliver them, and **tasks** are the individual work items developers complete. Tasks feed directly into the Notion backlog.
> 

## How This Section Connects to Earlier Work

| Source | What It Provides |
| --- | --- |
| **MVP Release-Level Scope** | One epic per scope row (Epics 1–4) |
| **Feature Prioritization** | MoSCoW priority for each feature |
| **Build Plan** | Epic 0 (Platform Foundation), technical decisions, and build phase order |
| **Pain Points and Use Cases** | Each feature traces to a pain point (P1–P6) and an MVP use case (UC1–UC8) |

## Epic Overview

| Epic | Outcome | Pain Points | Build Phase | Features |
| --- | --- | --- | --- | --- |
| **Epic 0: Platform Foundation** | A secure, deployed app with user accounts and the infrastructure every feature needs | Supports all | Phase 0 | 5 |
| **Epic 1: Effortless Money Tracking** | Users see what they can spend today with almost no effort | P1, P2, P6 | Phase 1 | 6 |
| **Epic 2: Impulse Pause** | Users pause before impulse buys and feel rewarded for skipping them | P3 | Phase 2 | 3 |
| **Epic 3: Bill Reminders** | Users never miss a bill | P5 | Phase 4 | 2 |
| **Epic 4: Guilt-Free Comebacks** | Users return after a lapse without backlog or shame | P4 | Phase 3 | 3 |

**Task types:** Setup · Design · Frontend · Backend · Database · Security · Testing

## Definition of Done

Every task is complete only when it meets all of these:

- Code is merged to `main` through a reviewed pull request.
- It works on a phone screen, on both iPhone and Android browsers.
- Any new table has row-level security, verified so one user can't access another user's data.
- No secrets appear in the code or the browser.
- It follows the five design principles: the app comes to the user, no backlog, no streaks, reward restraint, two minutes a day.
- It's tested in the preview deployment before merging.

---

# Epic 0: Platform Foundation

**Outcome:** A secure, deployed web app with user accounts, data protection, notifications, scheduled jobs, and KPI tracking.

**Why it's first:** Every user-facing feature depends on these foundations.

## Feature 0.1: Project Setup and Deployment Pipeline

**Priority:** Must

**Feature-Level User Story:**

As the product team, we want code changes to deploy automatically and safely, so that features reach beta users quickly without breaking the app.

**Feature-Level Use Case Scenarios:**

- **Main:** A developer opens a pull request; Vercel creates a preview link for testing; after review, the merge to `main` deploys to production.
- **Alternate:** A build fails; the pull request can't be merged until it's fixed.
- **Edge:** A developer tries to push directly to `main`; branch protection blocks it.

| ID | Task | Type |
| --- | --- | --- |
| E0-F1-T1 | Create the Next.js app with TypeScript in the GitHub repo | Setup |
| E0-F1-T2 | Connect the repo to Vercel with preview deployments for pull requests and production deployments from `main` | Setup |
| E0-F1-T3 | Create Supabase projects for test and production, and set up the Supabase command-line tools for database migrations | Setup |
| E0-F1-T4 | Add environment variables in Vercel for each environment (local, preview, production) | Setup |
| E0-F1-T5 | Enable branch protection on `main` and require pull request reviews | Setup |
| E0-F1-T6 | Turn on GitHub secret scanning and Dependabot alerts | Security |
| E0-F1-T7 | Add a GitHub Actions workflow that runs linting and tests on each pull request | Testing |

## Feature 0.2: User Accounts

**Priority:** Must

**Feature-Level User Story:**

As a user, I want to create an account and log in securely, so that my financial information stays private and available only to me.

**Feature-Level Use Case Scenarios:**

- **Main:** A user signs up with an email and password, confirms their email, and lands on onboarding.
- **Alternate:** A user chooses a magic link and logs in from their email without a password.
- **Alternate:** A user forgets their password and resets it by email.
- **Edge:** A logged-out user tries to open a private page and is redirected to login.
- **Edge:** A user deletes their account, and all their data is permanently removed.

| ID | Task | Type |
| --- | --- | --- |
| E0-F2-T1 | Design sign-up, login, and password reset screens (mobile-first, calm, minimal fields) | Design |
| E0-F2-T2 | Build sign-up, login, and magic link login with Supabase Auth | Frontend |
| E0-F2-T3 | Build the password reset flow | Frontend |
| E0-F2-T4 | Protect private pages so only logged-in users can access them | Backend |
| E0-F2-T5 | Create the `profiles` table, created automatically when a user signs up | Database |
| E0-F2-T6 | Build account deletion that removes all of the user's data and disconnects their bank | Backend |
| E0-F2-T7 | Add sign out | Frontend |

## Feature 0.3: Data Security

**Priority:** Must

**Feature-Level User Story:**

As a user, I want my financial data protected from anyone else, so that I can trust the app with my bank information.

**Feature-Level Use Case Scenarios:**

- **Main:** A logged-in user requests their transactions and receives only their own.
- **Edge:** Someone tries to request another user's data and receives nothing.
- **Edge:** Someone tries to trigger a scheduled job without the secret key and is rejected.

| ID | Task | Type |
| --- | --- | --- |
| E0-F3-T1 | Write row-level security policies for every table, limiting access to rows owned by the logged-in user | Security |
| E0-F3-T2 | Write automated tests confirming one user can't read or change another user's data | Testing |
| E0-F3-T3 | Restrict the Supabase admin key and Plaid secrets to server functions only | Security |
| E0-F3-T4 | Set up encrypted storage for Plaid access tokens, readable only by the server | Security |
| E0-F3-T5 | Add secret-key validation to all scheduled job endpoints | Security |
| E0-F3-T6 | Write the privacy policy page explaining what data is stored and why | Design |

## Feature 0.4: Home Screen App and Notifications

**Priority:** Must

**Feature-Level User Story:**

As a user, I want to add the app to my home screen and receive notifications, so that the app reminds me instead of relying on me to remember it.

**Feature-Level Use Case Scenarios:**

- **Main:** A user follows the guided steps to add the app to their home screen and allows notifications.
- **Alternate:** A user on iPhone hasn't added the app to their home screen; the app explains that this is needed for notifications.
- **Edge:** A user declines notifications; the same information appears in the app when they open it.

| ID | Task | Type |
| --- | --- | --- |
| E0-F4-T1 | Add the web app manifest, app icons, and splash screen | Setup |
| E0-F4-T2 | Add a service worker for push notifications and basic offline loading | Frontend |
| E0-F4-T3 | Design a step-by-step "Add to Home Screen" guide for iPhone and Android | Design |
| E0-F4-T4 | Build the notification permission request, shown after the user sees value rather than at signup | Frontend |
| E0-F4-T5 | Create the `push_subscriptions` table and save each device's subscription | Database |
| E0-F4-T6 | Build a server function that sends a push notification to a user's devices | Backend |
| E0-F4-T7 | Build an in-app message area as the fallback when notifications are off | Frontend |

## Feature 0.5: Scheduled Jobs and KPI Tracking

**Priority:** Must

**Feature-Level User Story:**

As the product team, we want time-based actions to run automatically and key user actions to be recorded, so that notifications arrive on time and we can measure whether the MVP works.

**Feature-Level Use Case Scenarios:**

- **Main:** Every hour, the scheduler triggers a server function that handles whatever is due, such as Morning Numbers and Park It prompts.
- **Main:** When a user parks an item, an event is recorded for KPI reporting.
- **Edge:** A scheduled job fails; the error is logged and the next hourly run picks up any missed work.

| ID | Task | Type |
| --- | --- | --- |
| E0-F5-T1 | Set up an hourly Supabase scheduled job that calls a secure Vercel server function | Setup |
| E0-F5-T2 | Build the scheduled job handler that routes work to each feature (Morning Number, Park It, bills) | Backend |
| E0-F5-T3 | Add logging for scheduled job runs and failures | Backend |
| E0-F5-T4 | Create the `events` table and a helper to record key actions | Database |
| E0-F5-T5 | Build saved database queries (views) for each MVP KPI: activation, 30- and 90-day retention, comeback rate, Park It skip rate | Database |

---

# Epic 1: Effortless Money Tracking

**Outcome:** Users see what they can spend today with almost no effort.

**Pain points:** P1 Setup overwhelm · P2 Out of sight, out of mind · P6 Abstract budgets

**Use cases:** UC1, UC2, UC3

## Feature 1.1: Quick Onboarding

**Priority:** Must

**Feature-Level User Story:**

As a chronic abandoner, I want setup to take less than five minutes, so that I see value before I lose interest.

**Feature-Level Use Case Scenarios:**

- **Main:** After signup, a user answers three short questions (payday schedule, approximate take-home pay, time zone), connects their bank, and sees Today's Number.
- **Alternate:** A user doesn't know their exact pay; a rough estimate is accepted and can be changed later.
- **Edge:** A user leaves halfway through onboarding; when they return, it resumes where they stopped.

| ID | Task | Type |
| --- | --- | --- |
| E1-F1-T1 | Design the onboarding flow: one question per screen, progress indicator, under 5 minutes total | Design |
| E1-F1-T2 | Build the payday schedule, take-home pay, and time zone screens | Frontend |
| E1-F1-T3 | Save onboarding answers to `profiles`, with progress saved after each step | Backend |
| E1-F1-T4 | Resume unfinished onboarding when the user returns | Frontend |
| E1-F1-T5 | Track the event "onboarding completed" with time taken | Backend |

## Feature 1.2: Bank Connection (Plaid)

**Priority:** Must

**Feature-Level User Story:**

As a user, I want to connect my bank securely, so that my spending is tracked automatically without manual entry.

**Feature-Level Use Case Scenarios:**

- **Main:** A user opens Plaid's secure window, logs in to their bank, and their recent transactions import automatically.
- **Alternate:** The 10-connection beta limit has been reached; the user is offered CSV import instead.
- **Edge:** A bank connection stops working; the user sees a calm message with a one-tap reconnect.
- **Edge:** A user disconnects their bank; their access token is deleted.

| ID | Task | Type |
| --- | --- | --- |
| E1-F2-T1 | Set up Plaid in Sandbox mode and add its keys to Vercel environment variables | Setup |
| E1-F2-T2 | Build a server function that creates a Plaid connection link | Backend |
| E1-F2-T3 | Add Plaid's secure bank login window to onboarding | Frontend |
| E1-F2-T4 | Exchange Plaid's temporary token for an access token and store it encrypted | Backend |
| E1-F2-T5 | Create the `bank_connections`, `accounts`, and `transactions` tables | Database |
| E1-F2-T6 | Build the transaction import, covering the initial import and ongoing updates | Backend |
| E1-F2-T7 | Add a daily sync to the scheduled job handler | Backend |
| E1-F2-T8 | Build reconnect and disconnect flows | Frontend |
| E1-F2-T9 | Track the number of live connections and switch to CSV import when the limit is reached | Backend |

## Feature 1.3: CSV Import

**Priority:** Must (beta fallback)

**Feature-Level User Story:**

As a user who can't or won't link my bank, I want to upload my bank's transaction file, so that I can still use the app.

**Feature-Level Use Case Scenarios:**

- **Main:** A user downloads a CSV file from their bank, uploads it, and the transactions appear sorted into buckets.
- **Alternate:** The file's columns don't match the expected format; the user picks which column is date, amount, and description.
- **Edge:** The user uploads the same file twice; duplicate transactions are skipped.

| ID | Task | Type |
| --- | --- | --- |
| E1-F3-T1 | Design the upload screen with simple instructions for finding a bank's CSV export | Design |
| E1-F3-T2 | Build file upload and parsing | Frontend |
| E1-F3-T3 | Build column matching for files in unfamiliar formats | Frontend |
| E1-F3-T4 | Save imported transactions with source = CSV and skip duplicates | Backend |
| E1-F3-T5 | Add a gentle in-app reminder to upload a new file every week | Backend |

## Feature 1.4: Three Buckets

**Priority:** Must

**Feature-Level User Story:**

As a user, I want my transactions sorted automatically into Bills, Needs, and Wants, so that I never have to categorize anything myself.

**Feature-Level Use Case Scenarios:**

- **Main:** New transactions arrive and are sorted into a bucket automatically.
- **Alternate:** A transaction is in the wrong bucket; the user swipes to move it, and future transactions from that merchant follow the correction.
- **Edge:** A transaction can't be confidently sorted; it defaults to Wants, so Today's Number stays cautious, and it's never flagged as a to-do.

| ID | Task | Type |
| --- | --- | --- |
| E1-F4-T1 | Create a lookup table mapping Plaid spending categories to Bills, Needs, and Wants | Database |
| E1-F4-T2 | Build keyword rules for sorting CSV transactions, which have no Plaid category | Backend |
| E1-F4-T3 | Build the sorting function: user corrections first, then category or keyword rules, then Wants | Backend |
| E1-F4-T4 | Create the `bucket_rules` table for saved merchant corrections | Database |
| E1-F4-T5 | Design and build the transaction list with swipe-to-move | Frontend |
| E1-F4-T6 | Write tests for the sorting rules | Testing |

## Feature 1.5: Today's Number

**Priority:** Must

**Feature-Level User Story:**

As a user with time blindness, I want one daily number that tells me what's safe to spend on wants today, so that I can decide at a glance without thinking about the whole month.

**Feature-Level Use Case Scenarios:**

- **Main:** A user opens the app and sees Today's Number, for example "$28 for today."
- **Alternate:** The user overspent yesterday; today's number is slightly lower, with no warning or red color.
- **Edge:** Money is tight and the number would be negative; the app shows $0 with a supportive message and a suggestion such as parking purchases until payday.

| ID | Task | Type |
| --- | --- | --- |
| E1-F5-T1 | Define the calculation: (expected income − upcoming bills − estimated needs − Wants spent this pay period) ÷ days until payday | Backend |
| E1-F5-T2 | Estimate needs from the user's last 30 days of Needs spending | Backend |
| E1-F5-T3 | Build the calculation as a server function, recalculated each morning and after new transactions | Backend |
| E1-F5-T4 | Write tests for the calculation, including the overspending and $0 cases | Testing |
| E1-F5-T5 | Design the home screen with Today's Number as the main element (calm colors, no red) | Design |
| E1-F5-T6 | Build the home screen | Frontend |

## Feature 1.6: Morning Number Notification

**Priority:** Must

**Feature-Level User Story:**

As a user who forgets to check apps, I want Today's Number sent to me each morning, so that I know my number before I start spending.

**Feature-Level Use Case Scenarios:**

- **Main:** At about 8 a.m. in the user's time zone, a notification arrives: "Today's Number: $28."
- **Alternate:** The user changes the notification time in settings.
- **Edge:** Notifications are off; the number appears at the top of the app when it's opened.

| ID | Task | Type |
| --- | --- | --- |
| E1-F6-T1 | Add Morning Number sending to the hourly job, targeting users whose local time matches their chosen time | Backend |
| E1-F6-T2 | Write friendly notification text with a few rotating variations | Design |
| E1-F6-T3 | Build the notification time setting | Frontend |
| E1-F6-T4 | Track the event "Morning Number sent," and "opened" when the notification is tapped | Backend |

---

# Epic 2: Impulse Pause

**Outcome:** Users pause before impulse buys and feel rewarded for skipping them.

**Pain point:** P3 Impulse purchases

**Use cases:** UC4, UC5

## Feature 2.1: Park It

**Priority:** Must

**Feature-Level User Story:**

As someone who buys on impulse, I want to quickly park something I'm tempted to buy, so that I can delay the decision until the urge passes.

**Feature-Level Use Case Scenarios:**

- **Main:** A user taps Park It from the home screen, enters the item name and price in two taps, and sees a confirmation like "Parked! We'll check in with you in 48 hours."
- **Alternate:** The item costs more than Today's Number; the app gently shows how it compares, without blocking or judging.
- **Edge:** A user parks several items at once; each gets its own 48-hour timer.

| ID | Task | Type |
| --- | --- | --- |
| E2-F1-T1 | Design the Park It flow: one button on the home screen, two fields, two taps to finish | Design |
| E2-F1-T2 | Create the `parked_items` table | Database |
| E2-F1-T3 | Build the Park It form and confirmation | Frontend |
| E2-F1-T4 | Show how the price compares with Today's Number, using supportive wording | Frontend |
| E2-F1-T5 | Build the "Parked" list showing waiting items and time remaining | Frontend |
| E2-F1-T6 | Track the event "item parked" | Backend |

## Feature 2.2: 48-Hour Decision Prompt

**Priority:** Must

**Feature-Level User Story:**

As a user, I want to be asked later whether I still want a parked item, so that I decide when the impulse has passed.

**Feature-Level Use Case Scenarios:**

- **Main:** 48 hours later, a notification asks "Still want the headphones?" The user chooses Skip, Buy, or Park longer.
- **Alternate:** The user chooses Park longer, and the timer resets for another 48 hours.
- **Edge:** The user doesn't respond; the item stays parked with one gentle follow-up reminder, and is never automatically counted as bought or skipped.

| ID | Task | Type |
| --- | --- | --- |
| E2-F2-T1 | Add a 48-hour check to the hourly job and send the decision prompt | Backend |
| E2-F2-T2 | Build the decision screen with Skip, Buy, and Park longer | Frontend |
| E2-F2-T3 | Save the decision and date | Backend |
| E2-F2-T4 | Add one follow-up reminder for unanswered prompts | Backend |
| E2-F2-T5 | Track the events "item skipped," "item bought," and "parked longer" | Backend |

## Feature 2.3: Money Kept Counter

**Priority:** Must

**Feature-Level User Story:**

As someone who needs immediate rewards, I want to see the money I've kept by skipping purchases, so that not spending feels like a win.

**Feature-Level Use Case Scenarios:**

- **Main:** A user skips a $65 item, and a brief celebration shows "Money Kept: $340."
- **Alternate:** The user reaches a milestone such as $100 kept and sees a special celebration.
- **Edge:** A user hasn't skipped anything yet; the counter shows an encouraging empty state rather than $0.

| ID | Task | Type |
| --- | --- | --- |
| E2-F3-T1 | Build the Money Kept total from skipped items (calculated, not stored) | Backend |
| E2-F3-T2 | Design the counter and the celebration animation | Design |
| E2-F3-T3 | Add the counter to the home screen | Frontend |
| E2-F3-T4 | Build milestone celebrations ($50, $100, $250, $500) | Frontend |
| E2-F3-T5 | Design the empty state | Design |

---

# Epic 3: Bill Reminders

**Outcome:** Users never miss a bill.

**Pain point:** P5 Missed bills and late fees

**Use case:** UC7

## Feature 3.1: Bill Detection

**Priority:** Should

**Feature-Level User Story:**

As a newly diagnosed adult, I want my bills found automatically, so that I don't have to remember or list them myself.

**Feature-Level Use Case Scenarios:**

- **Main:** The app finds payments from the same merchant, for a similar amount, about a month apart, and lists them as bills with expected due dates.
- **Alternate:** A detected "bill" isn't really a bill; the user removes it.
- **Edge:** A bill isn't detected; the user adds it manually.

| ID | Task | Type |
| --- | --- | --- |
| E3-F1-T1 | Create the `bills` table | Database |
| E3-F1-T2 | Build recurring payment detection (same merchant, similar amount, monthly interval) | Backend |
| E3-F1-T3 | Build the bills list with remove and manual add | Frontend |
| E3-F1-T4 | Use detected bills in the Today's Number calculation | Backend |
| E3-F1-T5 | Write tests for bill detection | Testing |

## Feature 3.2: Bill Reminders

**Priority:** Should

**Feature-Level User Story:**

As someone who forgets due dates, I want a reminder before each bill is due, so that I avoid late fees on money I already have.

**Feature-Level Use Case Scenarios:**

- **Main:** Three days before a bill is due, a notification arrives: "Electric bill ($85) is due Friday."
- **Alternate:** The user marks the bill as paid, and no further reminders are sent for that month.
- **Edge:** Today's Number is $0 and a bill is coming up; the reminder suggests parking purchases until payday.

| ID | Task | Type |
| --- | --- | --- |
| E3-F2-T1 | Add a three-day bill check to the hourly job and send reminders | Backend |
| E3-F2-T2 | Write calm, specific reminder text | Design |
| E3-F2-T3 | Build "Mark as paid" | Frontend |
| E3-F2-T4 | Track the events "bill reminder sent" and "marked as paid" | Backend |

---

# Epic 4: Guilt-Free Comebacks

**Outcome:** Users return after a lapse without a backlog or shame.

**Pain point:** P4 Shame spiral after falling off

**Use cases:** UC6, UC8

## Feature 4.1: Welcome-Back Summary

**Priority:** Must

**Feature-Level User Story:**

As a chronic abandoner, I want returning after time away to be quick and judgment-free, so that one missed week doesn't make me quit.

**Feature-Level Use Case Scenarios:**

- **Main:** A user returns after 7+ days and sees a short summary of at most three items (what changed, any bill due soon, and Today's Number), then goes straight to the home screen.
- **Alternate:** The user returns after a shorter break (under 7 days); no summary is shown.
- **Edge:** A lot happened while away, such as several bills or many transactions; the summary still shows only three items, with "see more" optional.

| ID | Task | Type |
| --- | --- | --- |
| E4-F1-T1 | Update "last active date" in `profiles` each time the app is opened | Backend |
| E4-F1-T2 | Build the summary generator, which picks the three most useful items | Backend |
| E4-F1-T3 | Design the welcome-back screen: warm wording, no red, no overdue language | Design |
| E4-F1-T4 | Build the welcome-back screen | Frontend |
| E4-F1-T5 | Write welcome-back message variations | Design |
| E4-F1-T6 | Track the event "returned after lapse," used for the comeback rate KPI | Backend |
| E4-F1-T7 | Review all screens to remove streaks, overdue warnings, and guilt-based wording | Testing |

## Feature 4.2: Money Stress Check-In

**Priority:** Should

**Feature-Level User Story:**

As the product team, we want users to rate their money stress at signup and after 30 days, so that we can measure whether the app reduces stress.

**Feature-Level Use Case Scenarios:**

- **Main:** During onboarding, a user rates "How stressed do you feel about money?" from 1 to 5. On day 30, the app asks again.
- **Edge:** A user skips the check-in; it's offered once more, then dropped.

| ID | Task | Type |
| --- | --- | --- |
| E4-F2-T1 | Create the `checkins` table | Database |
| E4-F2-T2 | Build the one-question check-in screen | Frontend |
| E4-F2-T3 | Add the check-in to onboarding | Frontend |
| E4-F2-T4 | Schedule the day-30 check-in through the hourly job | Backend |

## Feature 4.3: Weekly Recap

**Priority:** Could

**Feature-Level User Story:**

As a user, I want a quick weekly summary of my progress, so that I see what's going well without reviewing every transaction.

**Feature-Level Use Case Scenarios:**

- **Main:** Every Sunday, a notification links to a 30-second recap: Money Kept this week, bills paid, and one encouraging note.
- **Edge:** A quiet week with little activity; the recap stays positive and short.

| ID | Task | Type |
| --- | --- | --- |
| E4-F3-T1 | Design the recap screen (three cards, 30 seconds to read) | Design |
| E4-F3-T2 | Build the recap generator | Backend |
| E4-F3-T3 | Add the weekly recap to the hourly job | Backend |
| E4-F3-T4 | Build the recap screen | Frontend |

---

## Summary

| Epic | Features | Tasks | Priority Mix |
| --- | --- | --- | --- |
| Epic 0: Platform Foundation | 5 | 32 | All Must |
| Epic 1: Effortless Money Tracking | 6 | 35 | All Must |
| Epic 2: Impulse Pause | 3 | 16 | All Must |
| Epic 3: Bill Reminders | 2 | 9 | All Should |
| Epic 4: Guilt-Free Comebacks | 3 | 15 | 1 Must, 1 Should, 1 Could |
| **Total** | **19** | **107** |  |

> ➡️ **Next:** These 107 tasks populate the Notion backlog. Each task's ID, type, priority (from its feature), and build phase (from its epic) become backlog fields, so the backlog can be sorted by phase and priority for development.
>