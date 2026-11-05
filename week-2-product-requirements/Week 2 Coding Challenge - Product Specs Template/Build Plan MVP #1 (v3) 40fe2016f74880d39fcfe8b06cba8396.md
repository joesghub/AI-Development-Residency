# Build Plan: MVP #1 (v3)

> 🔄 **What changed and why (v2 → v3)**
> 
> - **Platform changed from a web app to a cross-platform native app.** The product's core is reaching the user through notifications, and on iOS a web app can only send push notifications if the user manually adds it to the home screen, which fails our "the app comes to you" principle for an ADHD audience. A native app sends notifications reliably from install.
> - **Built with React Native and Expo,** one codebase for iOS and Android.
> - **Vercel moves from hosting the app to hosting the backend.** The app no longer "lives" on Vercel; the app lives on the user's phone, and Vercel runs the API behind it. Supabase and GitHub are unchanged.
> - **Notifications are now the MVP's engagement model,** not a convenience. The app is intentionally low-interaction (mostly read), so the daily notifications are what create engagement. Their open and opt-out rates become a core KPI.
> - **New feature: the Budget Breakdown screen** and its early-afternoon notification, which teach how Today's Budget is calculated from recent settled transactions. This replaced the same-day nudge idea, which relied on data Plaid can't deliver fast enough.
> - **Buy Day reminder reworked into Patience Pot milestone notifications** (25/50/75%, with Buy Day at 100%).
> - **Bill reminders removed from the MVP.** Bill *detection* stays, but only to keep Today's Budget honest, not to notify anyone. (Epic 3 is removed in the scope and epics documents.)
> - **Unchanged:** the whole Patiencents core experience, the money rules, Today's Budget, the Patience Pot, the wishlist and Buy Days, matching, Kept Your Patience, and the welcome-back design.

> 🏗️ **Purpose:** Define *how* MVP #1 will be built: a cross-platform native app with a backend API on Vercel, data in Supabase, code in GitHub, and secure user accounts.
> 

## Required Technology

| Requirement | Tool | Role | Change |
| --- | --- | --- | --- |
| The app | **React Native + Expo** | One codebase for iOS and Android; installs from a test link or the app stores | 🆕 New |
| Backend / API | **Vercel** | Runs business logic, talks to Plaid, triggers notifications | Role changed |
| Database and auth | **Supabase** | Accounts, data, row-level security, scheduler | Unchanged |
| Code repository | **GitHub** | Repo, reviews, deploys the backend to Vercel | Unchanged |
| Bank data | **Plaid** | Bank connections | Unchanged |
| Notifications | **Apple APNs + Google FCM, via Expo Push** | Delivers notifications to phones | 🆕 New |

## Three-Tier Architecture

The three tiers are unchanged in concept; only the presentation tier moves from a web page to a native app.

| Tier | What It Does | Technology | What Lives Here |
| --- | --- | --- | --- |
| **1. Presentation** | What the user sees and taps | **React Native + Expo app** on the user's phone | Home (Today's Budget), Budget Breakdown, Patience Pot, wishlist and Buy Days, welcome-back, settings |
| **2. Application** | Business logic and secure connections | Next.js server functions on **Vercel** | Today's Budget, daily close, breakdown data, Buy Day scheduling, matching, Plaid connection, sending notifications |
| **3. Data** | Stores everything securely | **Supabase** (PostgreSQL, Auth, scheduler) | Accounts, transactions, daily results, Pot ledger, wishlist, matches |

**External services:** **Plaid** for bank connections (application tier only, never the app directly) and **Expo Push → APNs/FCM** for notifications.

**How a request flows:** the user opens the app on their phone (presentation) → the app calls the Vercel API with the user's login token (application) → the server checks identity and queries only that user's data (data) → row-level security enforces the same rule in the database → the server returns results to the app.

## Why Native: the Notification Argument

The app is deliberately **low-interaction**. A user connects their bank, adds a few wishlist items, and then mostly reads: their budget, their Pot, their breakdown. That calm design is the point for an ADHD audience, but it means the app would sit idle without a way to reach people. **Notifications are how the product stays alive in a user's life.** That only works reliably on a native app:

|  | Mobile web app | Native app |
| --- | --- | --- |
| **iOS notifications** | Only if the user manually adds the app to their home screen; less reliable | Work from install |
| **Android notifications** | Fairly reliable | Reliable |
| **The risk for our audience** | "Out of sight, out of mind" users won't do the setup step | Nothing to set up |

Because notifications carry engagement, the MVP measures whether users keep them on and tap them (see KPIs).

## How Notifications Work (Plain Version)

A phone only shows a notification if it comes through the platform's official service: **Apple's APNs** for iPhones, **Google's FCM** for Android. An app can't bypass these. Since we're building with Expo, the backend sends one request to **Expo Push**, which forwards it to APNs or FCM as needed. This saves us from integrating with Apple and Google separately, and it's free. The app can send normal lock-screen notifications; Expo Push is just the bridge to the two services that deliver them.

## The Notification Plan

Notifications are the engagement model, so they're designed as a small, deliberate set. At most 2 on a normal day, 3–4 on a day when an occasional one lands.

| Notification | When | Opens | Frequency | Default |
| --- | --- | --- | --- | --- |
| **Morning budget** | Morning (user's time) | Home screen | Daily | On |
| **Budget breakdown** | ~2pm, after the daily sync | Breakdown screen | Daily | On (user can turn off) |
| **Patience Pot milestone** | At 25%, 50%, 75% toward the next wishlist item | Pot / wishlist | Occasional | On |
| **Buy Day** | At 100% (item is affordable) | Buy Day screen | Occasional | On |

**Rules:** track the daily count per user and never send more than 3–4; milestones track the top wishlist item only and fire once each per item; all wording is supportive, never a warning.

## Resolved Decisions (carried from v2, still valid)

| Decision | Resolution |
| --- | --- |
| How transactions get into the app | Plaid live sync (Sandbox for development, Trial plan for ~10 beta users), with CSV import as a fallback |
| How transactions are sorted | Rules: Plaid category → Bills, Essentials, Usuals; user corrections override |
| How scheduled jobs run | Supabase's scheduler runs hourly and calls secure Vercel functions |
| Today's Budget and the Pot | Leftovers move into the Pot instead of raising future daily numbers; the Pot is never reduced by overspending; Total Kept never goes down |
| When leftovers are confirmed | Pending the next morning, confirmed three days later |
| How Buy Days are calculated | A projection from the Pot balance and recent confirmed leftovers |
| How items match transactions | Score on merchant, amount, and date; the user confirms uncertain matches |
| How product details are read from links | The server reads them from the page where possible, with manual entry as a fallback |

## New Decisions (v3)

### Decision A: The Budget Breakdown screen and notification

**Decision:** A screen, always available, that explains how **today's budget was calculated from recent settled transactions.** A notification around 2pm points the user to it.

**Why it works from day one:** the breakdown explains the *inputs* to today's number, not today's fresh purchases. Plaid delivers 30–90 days of history the moment the account connects, so the app has everything it needs immediately. It doesn't wait for today's transactions to post.

**Why 2pm and settled data:** today's purchases often haven't posted by afternoon, and pending amounts change. So the breakdown uses the most recent *settled* transactions, and every number in it is confirmed, not pending. This matches the "every number is real" principle.

**What the screen shows:**

- Income this pay period
- − Bills set aside (from detected recurring payments)
- − Essentials set aside (estimated from recent spending)
- − Usuals already spent this pay period
- ÷ days until payday
- = **Today's Budget**

### Decision B: Patience Pot milestone notifications

**Decision:** Notifications fire when the Pot crosses 25%, 50%, and 75% of the next wishlist item's cost. Buy Day (100%) is handled by its own notification.

**Rules:** track the top wishlist item only; each milestone fires once per item; if an item is added when the Pot is already past a milestone, the passed ones don't fire; money moving in and out doesn't re-trigger a crossed milestone.

### Decision C: Bill detection without reminders

**Decision:** The app still detects recurring bills, but only to subtract them in the Today's Budget math. No bill reminder notifications in the MVP.

**Why:** reminders were cut from the MVP, but the budget would be wrong if it didn't set money aside for bills. So detection stays, quietly, as an input to the number. Bill reminders can return as an MMP feature.

## Data Model (v3)

Unchanged from v2, with one note: the `bills` table stays (detection feeds Today's Budget), and a small `notification_log` is added to enforce the daily cap and record milestones already sent.

| Table | Change from v2 |
| --- | --- |
| profiles, bank_connections, accounts, transactions, bucket_rules, daily_results, pot_ledger, wishlist_items, transaction_matches, checkins, events | Unchanged |
| **bills** | Kept, but used only for the budget calculation, not reminders |
| **device_tokens** 🆕 | Each device's Expo push token, replacing the web `push_subscriptions` table |
| **notification_log** 🆕 | What was sent to whom and when: enforces the daily cap and records which Pot milestones already fired |

## Scheduled Jobs (v3)

The Supabase scheduler still runs hourly and calls Vercel functions. Changes from v2: the breakdown notification is added, bill reminders are removed, and the Buy Day reminder becomes milestone checks.

| Job | When | Change |
| --- | --- | --- |
| Morning budget notification | User's chosen time | Unchanged |
| **Budget breakdown notification** 🆕 | ~2pm, after the daily sync | New |
| Daily close | Midnight, user's time zone | Unchanged |
| Leftover confirmation | Three days later | Unchanged |
| Buy Day recalculation | After confirmations | Unchanged |
| **Patience Pot milestone check** 🆕 | After confirmations and Pot changes | Replaces the plain Buy Day reminder |
| Buy Day notification | When an item reaches 100% | Unchanged in purpose |
| Transaction sync | Daily, plus Plaid updates | Unchanged |
| ~~Bill reminders~~ | — | ❌ Removed |
| Day-30 check-in | 30 days after signup | Unchanged |
| Monthly recap | First of the month | Unchanged |

## Security Plan (v3)

Unchanged from v2, with native-specific additions:

| Area | Approach |
| --- | --- |
| Authentication, data isolation, Pot integrity, server-only secrets, bank connections, encrypted Plaid tokens, scheduled-job secrets, minimal data, user control | Same as v2 |
| **Secure token storage on device** 🆕 | The user's login token is kept in the phone's secure storage (Keychain on iOS, Keystore on Android), not in plain storage |
| **App transport security** 🆕 | The app only talks to the Vercel backend over HTTPS |

## GitHub Workflow

Unchanged in principle. `main` is protected; changes merge through reviewed pull requests; merging deploys the **backend** to Vercel; Supabase migrations live in the repo. New: the app is built and shared to testers through Expo's build service (see Environments).

## Environments

| Environment | The app | Backend | Plaid | Database |
| --- | --- | --- | --- | --- |
| **Local** | Expo on a developer's phone (Expo Go or a dev build) | Local or preview | Sandbox | Local Supabase |
| **Preview** | A build shared via Expo | Vercel preview | Sandbox | Test Supabase |
| **Production (beta)** | Distributed to testers through **Expo / TestFlight**, no app store review needed yet | Vercel production | Trial plan (~10 users) + CSV | Production Supabase |

**Key point for the MVP:** Expo lets beta testers install the app from a link or TestFlight **without full App Store review.** So the beta avoids the app store process entirely; store submission becomes an MMP task.

## MVP Cost Estimate (v3)

| Service | Plan | Cost |
| --- | --- | --- |
| Expo | Free tier (builds, push) | $0, with limited free build minutes |
| Vercel | Hobby | $0 |
| Supabase | Free | $0 |
| Plaid | Sandbox + Trial | $0 |
| GitHub | Free | $0 |
| Apple Developer account | Needed for TestFlight and the App Store | **$99/year** |
| Google Play Developer account | Needed for Play Store (MMP) | **$25 once** |

**MVP cost:** close to $0 for software. The Apple Developer account ($99/year) is the one likely cost, needed if you distribute the iOS beta through TestFlight. Expo's own test distribution can avoid even that for early testing.

## Build Phases (v3)

| Phase | Focus | Change |
| --- | --- | --- |
| **Phase 0: Foundation** | Expo app, Vercel backend, Supabase, auth, row-level security, push notification setup, the scheduler | Now sets up the native app + push instead of a web app |
| **Phase 1: Effortless Money Tracking** | Plaid + CSV, three buckets, Today's Budget, daily close, morning notification, **Budget Breakdown screen + 2pm notification** | Breakdown added |
| **Phase 2: Patience Pot and Wishlist** | Pot, wishlist, Buy Days, matching, Kept Your Patience, **milestone notifications** | Milestones added |
| **Phase 3: Guilt-Free Comebacks** | Welcome-back, check-in, monthly recap | Unchanged |
| ~~Phase 4: Bill Reminders~~ | — | ❌ Removed |
| **Phase 4: Beta Readiness** | KPI tracking, security review, privacy policy, Expo/TestFlight distribution | Renumbered; distribution added |

> ➡️ **Next:** MVP Scope (v3) applies the native platform, the new breakdown feature and notification model, the removal of bill reminders, and the revised KPIs.
> 

---

That's the Build Plan v3. The biggest structural change is Vercel moving to the backend role and Epic 3 (Bill Reminders) being removed. Next is **MVP Scope (v3)**. Want me to continue?