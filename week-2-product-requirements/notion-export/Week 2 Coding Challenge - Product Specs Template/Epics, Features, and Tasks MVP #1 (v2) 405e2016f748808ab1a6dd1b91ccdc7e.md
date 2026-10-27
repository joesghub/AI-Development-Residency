# Epics, Features, and Tasks: MVP #1 (v2)

> 🔄 **What changed and why (v1 → v2)**
> 
> - **Epic 2 rewritten:** "Impulse Pause" (Park It, 48-hour prompt, self-reported Money Kept) becomes **"Patience Pot and Wishlist,"** with five new features: Daily Close and Patience Pot, Wishlist, Buy Day Scheduling, Buy Day Check-In and Matching, and Kept Your Patience. The v1 Epic 2 tasks are retired, and the Epic 2 task IDs now refer to the new tasks.
> - **Epic 1 updated:** buckets renamed to Bills, Essentials, and Usuals; Today's Number uses the new formula; the morning notification adds the Buy Day countdown; **Usuals Insights** added as a new Should-have feature.
> - **Epic 0 updated:** a new security task makes the Pot ledger read-only for users, and the KPI views cover the new KPIs.
> - **Epic 4 updated:** the welcome-back summary shows Pot growth and kept-patience items; the weekly recap is replaced by a **monthly recap**.
> - **Epic 3 unchanged,** apart from one scenario's wording.
> - **Task count:** 107 → 140.

> 🧩 **Purpose:** Break the MVP #1 scope into buildable work. **Epics** are large outcomes, **features** are user-facing capabilities, and **tasks** are individual work items that feed the Notion backlog.
> 

## How This Section Connects to Earlier Work

| Source | What It Provides |
| --- | --- |
| **MVP #1 Vision and Scope (v2)** | One epic per scope area; MoSCoW priorities |
| **Build Plan (v2)** | Epic 0, technical decisions, money rules, and build phase order |
| **User Pain Points and Journeys (v2)** | Each feature traces to a pain point (P1–P6) and a use case (UC1–UC11) |

## Epic Overview

| Epic | Outcome | Pain Points | Build Phase | Features | Tasks |
| --- | --- | --- | --- | --- | --- |
| **Epic 0: Platform Foundation** | A secure, deployed app with accounts, notifications, and scheduled jobs | Supports all | Phase 0 | 5 | 33 |
| **Epic 1: Effortless Money Tracking** | Users see what they can spend today with almost no effort | P1, P2, P6 | Phase 1 | 7 | 39 |
| **Epic 2: Patience Pot and Wishlist** | Daily patience visibly funds the things users want | P3, P4, P6 | Phase 2 | 5 | 44 |
| **Epic 3: Bill Reminders** | Users never miss a bill | P5 | Phase 4 | 2 | 9 |
| **Epic 4: Guilt-Free Comebacks** | Users return after a lapse without backlog or shame | P4 | Phase 3 | 3 | 15 |
| **Total** |  |  |  | **22** | **140** |

**Task types:** Setup · Design · Frontend · Backend · Database · Security · Testing

## Definition of Done

*Updated in v2: adds the money rules check.*

- Code is merged to `main` through a reviewed pull request.
- It works on a phone screen, on both iPhone and Android browsers.
- Any new table has row-level security, verified so one user can't access another user's data.
- No secrets appear in the code or the browser.
- **Any money-related task follows the money rules:** no double counting, the Pot is never reduced by overspending, and Total Kept never goes down.
- It follows the six design principles: the app comes to the user, every number is real, no backlog, no streaks or losses, not no but later, and two minutes a day.
- It's tested in the preview deployment before merging.

---

# Epic 0: Platform Foundation

**Outcome:** A secure, deployed web app with user accounts, data protection, notifications, scheduled jobs, and KPI tracking.

## Feature 0.1: Project Setup and Deployment Pipeline

**Priority:** Must · *Unchanged from v1 (tasks E0-F1-T1 to T7).*

**Feature-Level User Story:** As the product team, we want code changes to deploy automatically and safely, so that features reach beta users quickly without breaking the app.

## Feature 0.2: User Accounts

**Priority:** Must · *Unchanged from v1 (tasks E0-F2-T1 to T7).*

**Feature-Level User Story:** As a user, I want to create an account and log in securely, so that my financial information stays private and available only to me.

## Feature 0.3: Data Security

**Priority:** Must · *Updated: one new task.*

**Feature-Level User Story:** As a user, I want my financial data protected and my progress accurate, so that I can trust the app with my bank information and trust the numbers it shows me.

**Feature-Level Use Case Scenarios:**

- **Main:** A logged-in user requests their data and receives only their own.
- **Edge:** Someone tries to request another user's data and receives nothing.
- **Edge (New):** A user tries to add an entry to their own Pot directly; the request is rejected, because only the server can write Pot entries.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E0-F3-T1 | Write row-level security policies for every table | Security | — |
| E0-F3-T2 | Write automated tests confirming one user can't read or change another user's data | Testing | — |
| E0-F3-T3 | Restrict the Supabase admin key and Plaid secrets to server functions only | Security | — |
| E0-F3-T4 | Set up encrypted storage for Plaid access tokens, readable only by the server | Security | — |
| E0-F3-T5 | Add secret-key validation to all scheduled job endpoints | Security | — |
| E0-F3-T6 | Write the privacy policy page explaining what data is stored and why | Design | — |
| E0-F3-T7 | Make `pot_ledger` and `daily_results` read-only for users, so only server functions can write to them | Security | 🆕 |

## Feature 0.4: Home Screen App and Notifications

**Priority:** Must · *Unchanged from v1 (tasks E0-F4-T1 to T7).*

**Feature-Level User Story:** As a user, I want to add the app to my home screen and receive notifications, so that the app reminds me instead of relying on me to remember it.

## Feature 0.5: Scheduled Jobs and KPI Tracking

**Priority:** Must · *Updated: two tasks revised.*

**Feature-Level User Story:** As the product team, we want time-based actions to run automatically and key actions to be recorded, so that notifications and Pot updates happen on time and we can measure whether the MVP works.

**Feature-Level Use Case Scenarios:**

- **Main:** Every hour, the scheduler triggers a server function that runs whatever is due for each user's time zone: morning notifications, daily close, confirmations, Buy Day reminders, and bill reminders.
- **Edge:** A job fails; the error is logged and the next hourly run picks up any missed work.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E0-F5-T1 | Set up an hourly Supabase scheduled job that calls a secure Vercel server function | Setup | — |
| E0-F5-T2 | Build the scheduled job handler that runs each user's due jobs based on their time zone | Backend | ✏️ Updated |
| E0-F5-T3 | Add logging for scheduled job runs and failures | Backend | — |
| E0-F5-T4 | Create the `events` table and a helper to record key actions | Database | — |
| E0-F5-T5 | Build saved database queries (views) for each MVP KPI: activation, retention, comeback rate, days under Today's Number, Pot growth, wishlist adoption, Buy Day outcomes | Database | ✏️ Updated |

---

# Epic 1: Effortless Money Tracking

**Outcome:** Users see what they can spend today with almost no effort.

**Pain points:** P1, P2, P6 · **Use cases:** UC1, UC2, UC3

## Feature 1.1: Quick Onboarding

**Priority:** Must · *Unchanged from v1 (tasks E1-F1-T1 to T5).* The first wishlist item prompt is added in Feature 2.2.

**Feature-Level User Story:** As a chronic abandoner, I want setup to take less than five minutes, so that I see value before I lose interest.

## Feature 1.2: Bank Connection (Plaid)

**Priority:** Must · *Unchanged from v1 (tasks E1-F2-T1 to T9).* Transaction updates now also trigger wishlist matching (Feature 2.4).

**Feature-Level User Story:** As a user, I want to connect my bank securely, so that my spending is tracked automatically without manual entry.

## Feature 1.3: CSV Import

**Priority:** Must (beta fallback) · *Unchanged from v1 (tasks E1-F3-T1 to T5).*

**Feature-Level User Story:** As a user who can't or won't link my bank, I want to upload my bank's transaction file, so that I can still use the app.

## Feature 1.4: Three Buckets

**Priority:** Must · *Updated: buckets renamed.*

**Feature-Level User Story:** As a user, I want my spending sorted automatically into Bills, Essentials, and Usuals, so that I never have to categorize anything myself.

**Feature-Level Use Case Scenarios:**

- **Main:** New transactions are sorted into Bills, Essentials, or Usuals automatically.
- **Alternate:** A transaction is in the wrong bucket; the user swipes to move it, and future transactions from that merchant follow the correction.
- **Edge:** A transaction can't be confidently sorted; it defaults to Usuals, so Today's Number stays cautious, and it's never flagged as a to-do.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E1-F4-T1 | Create a lookup table mapping Plaid spending categories to Bills, Essentials, and Usuals | Database | ✏️ Updated |
| E1-F4-T2 | Build keyword rules for sorting CSV transactions into Bills, Essentials, and Usuals | Backend | ✏️ Updated |
| E1-F4-T3 | Build the sorting function: user corrections first, then category or keyword rules, then Usuals | Backend | ✏️ Updated |
| E1-F4-T4 | Create the `bucket_rules` table for saved merchant corrections | Database | — |
| E1-F4-T5 | Design and build the transaction list with swipe-to-move | Frontend | — |
| E1-F4-T6 | Write tests for the sorting rules | Testing | — |

## Feature 1.5: Today's Number

**Priority:** Must · *Updated: new formula.*

**Feature-Level User Story:** As a user with time blindness, I want one daily number for my Usuals, so that I can decide at a glance without thinking about the whole month.

**Feature-Level Use Case Scenarios:**

- **Main:** A user opens the app and sees "$28 for today."
- **Alternate:** The user overspent yesterday; today's number is slightly lower, with no warning or red color, and the Pot is untouched.
- **Edge:** Money is tight and the number would be negative; the app shows $0 with a supportive message, and Buy Days show "coming soon."

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E1-F5-T1 | Define the calculation: (income − Bills − estimated Essentials − Usuals spent this period − Pot additions this period) ÷ days until payday | Backend | ✏️ Updated |
| E1-F5-T2 | Estimate Essentials from the user's last 30 days of Essentials spending | Backend | ✏️ Updated |
| E1-F5-T3 | Build the calculation as a server function, recalculated each morning and after new transactions | Backend | — |
| E1-F5-T4 | Write tests for the calculation, including overspending, $0, and Pot additions | Testing | ✏️ Updated |
| E1-F5-T5 | Design the home screen with Today's Number, the Pot, and the next Buy Day (calm colors, no red) | Design | ✏️ Updated |
| E1-F5-T6 | Build the home screen | Frontend | — |

## Feature 1.6: Morning Notification

**Priority:** Must · *Updated: adds the Buy Day countdown.*

**Feature-Level User Story:** As a user who forgets to check apps, I want Today's Number and my next Buy Day sent to me each morning, so that I know my number and stay excited about what's coming.

**Feature-Level Use Case Scenarios:**

- **Main:** At about 8 a.m. in the user's time zone: "Today's Number: $28. Headphones Buy Day: 12 days 🎧"
- **Alternate:** The user has no wishlist items; the notification shows only Today's Number, with an occasional gentle prompt to add one.
- **Edge:** Notifications are off; the same information appears at the top of the app.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E1-F6-T1 | Add the morning notification to the scheduled jobs, including Today's Number and the next Buy Day countdown | Backend | ✏️ Updated |
| E1-F6-T2 | Write friendly notification text with rotating variations, including versions with and without a Buy Day | Design | ✏️ Updated |
| E1-F6-T3 | Build the notification time setting | Frontend | — |
| E1-F6-T4 | Track the events "morning notification sent" and "opened" | Backend | — |

## Feature 1.7: Usuals Insights 🆕

**Priority:** Should

**Feature-Level User Story:** As a newly diagnosed adult, I want to see what I usually spend money on, so that I understand my patterns without reviewing every transaction.

**Feature-Level Use Case Scenarios:**

- **Main:** After the first import, a card shows: "Most of your Usuals go to takeout (40%), Amazon (25%), and games (15%)."
- **Alternate:** The user taps a category to see its top merchants.
- **Edge:** Less than two weeks of history; the card says insights are coming soon.

| ID | Task | Type |
| --- | --- | --- |
| E1-F7-T1 | Build the insights calculation: top Usuals categories and merchants over the last 30–90 days | Backend |
| E1-F7-T2 | Design the insights card (short, visual, no judgment) | Design |
| E1-F7-T3 | Build the insights card and category detail view | Frontend |
| E1-F7-T4 | Track the event "insights viewed" | Backend |

---

# Epic 2: Patience Pot and Wishlist 🆕

**Outcome:** Daily patience visibly funds the things users want.

**Pain points:** P3 Impulse purchases · P4 Shame spiral · P6 Abstract budgets

**Use cases:** UC4, UC5, UC6, UC7, UC8

*Replaces v1's "Impulse Pause" epic. Follows the money rules in Build Plan (v2).*

## Feature 2.1: Daily Close and Patience Pot

**Priority:** Must

**Feature-Level User Story:** As someone who needs to see progress, I want the money I don't spend each day to go into a Pot, confirmed by my bank, so that patience feels real and rewarding.

**Feature-Level Use Case Scenarios:**

- **Main:** Jordan spends $19 of a $28 Today's Number. The next morning: "Yesterday you kept $9 (pending)." Three days later: "Confirmed! Your Buy Day moved 1 day closer."
- **Alternate:** A late transaction changes the day's total before confirmation; the confirmed amount is adjusted quietly.
- **Edge:** A transaction arrives after confirmation; it counts toward upcoming days, and the Pot is never reduced.
- **Edge:** Jordan overspends; the leftover is $0 for that day, nothing is taken from the Pot, and no warning appears.

| ID | Task | Type |
| --- | --- | --- |
| E2-F1-T1 | Create the `daily_results` table | Database |
| E2-F1-T2 | Create the `pot_ledger` table | Database |
| E2-F1-T3 | Build the daily close job: calculate each day's pending leftover at midnight in the user's time zone | Backend |
| E2-F1-T4 | Build the confirmation job: recalculate with posted transactions three days later and write confirmed amounts to the Pot ledger | Backend |
| E2-F1-T5 | Update the Today's Number calculation to exclude Pot additions and apply the wishlist purchase rule | Backend |
| E2-F1-T6 | Design the Pot screen: Total Kept, Pot Balance, and history, with pending and confirmed states | Design |
| E2-F1-T7 | Build the Pot screen | Frontend |
| E2-F1-T8 | Build the "Yesterday you kept" message and the confirmation celebration | Frontend |
| E2-F1-T9 | Write tests for the money rules: no double counting, the Pot never reduced by overspending, late transactions | Testing |
| E2-F1-T10 | Track the events "leftover pending" and "leftover confirmed" | Backend |

## Feature 2.2: Wishlist

**Priority:** Must

**Feature-Level User Story:** As someone who buys on impulse, I want a quick way to save things I want for later, so that I can say "later" instead of "now."

**Feature-Level Use Case Scenarios:**

- **Main:** Jordan shares a product link; the name, price, image, and store fill in automatically. Jordan taps "Why this?" → *Excited about it*, and the item is added.
- **Alternate:** The store blocks the link reader; Jordan types the name and price.
- **Alternate:** Jordan drags an item to the top of the list to prioritize it.
- **Edge:** During onboarding, Jordan is asked to add one thing they want, or can skip it.

| ID | Task | Type |
| --- | --- | --- |
| E2-F2-T1 | Create the `wishlist_items` table | Database |
| E2-F2-T2 | Design the add-item flow: share or paste a link, or enter by hand, in a few taps | Design |
| E2-F2-T3 | Build the link reader server function (name, image, price, and merchant from the website address) | Backend |
| E2-F2-T4 | Add safe link reading protections: public web addresses only, with time and size limits | Security |
| E2-F2-T5 | Build the add-item screen with manual entry as the fallback | Frontend |
| E2-F2-T6 | Build the one-tap "Why this?" reasons (Need it, Excited about it, Saw it online, Gift) | Frontend |
| E2-F2-T7 | Build the wishlist screen with drag-to-reorder, edit, and remove | Frontend |
| E2-F2-T8 | Add an optional first-wishlist-item step to onboarding | Frontend |
| E2-F2-T9 | Track the event "wishlist item added," with the reason | Backend |

## Feature 2.3: Buy Day Scheduling

**Priority:** Must

**Feature-Level User Story:** As someone with time blindness, I want each wishlist item to have a real date when I can afford it, so that waiting feels concrete and exciting instead of endless.

**Feature-Level Use Case Scenarios:**

- **Main:** Jordan adds $120 headphones; with $40 in the Pot and an average leftover of $7 a day, the Buy Day is 12 days away.
- **Alternate:** A strong week of patience moves the Buy Day closer: "Your headphones Buy Day moved 3 days closer!"
- **Alternate:** The Pot already covers the item: "Ready now. It's Buy Day!"
- **Edge:** There's no leftover yet: "Buy Day coming soon. Every dollar you keep gets you closer." No date, no failure.
- **Edge:** A Buy Day moves later; it updates quietly and is mentioned gently in a weekly summary.

| ID | Task | Type |
| --- | --- | --- |
| E2-F3-T1 | Build the projected daily leftover: the 14-day average of confirmed leftovers, or 15% of Today's Number (labeled "estimated") with less than 7 days of history | Backend |
| E2-F3-T2 | Build the Buy Day calculation for the ordered wishlist, based on combined prices and the projected Pot | Backend |
| E2-F3-T3 | Handle the "ready now" and "coming soon" states | Backend |
| E2-F3-T4 | Design and build the Buy Day countdown on the wishlist and home screen | Frontend |
| E2-F3-T5 | Add Buy Day recalculation to the scheduled jobs, announcing Buy Days that moved closer | Backend |
| E2-F3-T6 | Build the gentle weekly summary for Buy Days that moved later | Backend |
| E2-F3-T7 | Write tests for Buy Day calculations | Testing |

## Feature 2.4: Buy Day Check-In and Matching

**Priority:** Must

**Feature-Level User Story:** As a user, I want Buy Day to feel like a celebration and my purchase to be recognized automatically, so that buying on purpose feels like a win, not a slip.

**Feature-Level Use Case Scenarios:**

- **Main:** "It's Buy Day! 🎉 Still excited about the headphones?" Jordan taps "Buying it." When the transaction arrives, it's matched automatically: "Bought on purpose!"
- **Alternate:** A medium-confidence match: "Was this your headphones?" Jordan swipes to confirm.
- **Alternate:** Jordan taps "Keep my patience"; the item moves to Kept Your Patience (Feature 2.5).
- **Alternate:** Jordan taps "Move my Buy Day" to push it later.
- **Edge:** The headphones were part of a combined order; Jordan links the transaction by hand.
- **Edge:** Jordan bought the item before its Buy Day; it's recorded quietly as bought early, with no failure message.

| ID | Task | Type |
| --- | --- | --- |
| E2-F4-T1 | Add the Buy Day reminder to the scheduled jobs (morning of each Buy Day) | Backend |
| E2-F4-T2 | Design the Buy Day screen: celebratory, with "Buying it," "Keep my patience," and "Move my Buy Day" | Design |
| E2-F4-T3 | Build the Buy Day screen | Frontend |
| E2-F4-T4 | Create the `transaction_matches` table | Database |
| E2-F4-T5 | Build the matching score: merchant (2 points), amount within 15% (2), date window (1) | Backend |
| E2-F4-T6 | Run matching after each transaction sync; auto-match high scores with an undo option | Backend |
| E2-F4-T7 | Build the swipe-to-confirm card for medium-confidence matches | Frontend |
| E2-F4-T8 | Build manual linking for combined orders | Frontend |
| E2-F4-T9 | Record wishlist purchases in the Pot ledger, with any remainder counted as Usuals | Backend |
| E2-F4-T10 | Build the "Bought on purpose" celebration; record early purchases quietly | Frontend |
| E2-F4-T11 | Write tests for matching | Testing |
| E2-F4-T12 | Track the events "bought on purpose," "bought early," and "match confirmed" | Backend |

## Feature 2.5: Kept Your Patience

**Priority:** Must

**Feature-Level User Story:** As a chronic abandoner, I want missed Buy Days to count as a win instead of a to-do, so that stepping away never creates a backlog.

**Feature-Level Use Case Scenarios:**

- **Main:** The jacket's Buy Day passes after a reminder with no response. Seven days later, with no matching purchase, it becomes "Kept your patience," and the money stays in the Pot.
- **Alternate:** Jordan taps "Keep my patience" on Buy Day; the item moves there right away and is confirmed after seven days.
- **Alternate:** Jordan still wants the jacket; one tap brings it back to the wishlist with a new Buy Day.
- **Edge:** A matching purchase appears later; the item is quietly reclassified as bought, with no message.

| ID | Task | Type |
| --- | --- | --- |
| E2-F5-T1 | Add the seven-day Kept Your Patience check to the scheduled jobs | Backend |
| E2-F5-T2 | Update item status for missed Buy Days and "Keep my patience" choices | Backend |
| E2-F5-T3 | Design the Kept Your Patience message and list | Design |
| E2-F5-T4 | Build one-tap "bring it back" to the wishlist | Frontend |
| E2-F5-T5 | Quietly reclassify items if a late match appears | Backend |
| E2-F5-T6 | Track the event "kept your patience" | Backend |

---

# Epic 3: Bill Reminders

**Outcome:** Users never miss a bill. **Pain point:** P5 · **Use case:** UC10

*Unchanged from v1, apart from one scenario's wording.*

## Feature 3.1: Bill Detection

**Priority:** Should · *Unchanged (tasks E3-F1-T1 to T5).*

**Feature-Level User Story:** As a newly diagnosed adult, I want my bills found automatically, so that I don't have to remember or list them myself.

## Feature 3.2: Bill Reminders

**Priority:** Should · *Tasks unchanged (E3-F2-T1 to T4).*

**Feature-Level User Story:** As someone who forgets due dates, I want a reminder before each bill is due, so that I avoid late fees on money I already have.

**Updated scenario (Edge):** Today's Number is $0 and a bill is coming up; the reminder reassures the user that the bill is already covered in their plan, and suggests adding any new wants to the wishlist for later.

---

# Epic 4: Guilt-Free Comebacks

**Outcome:** Users return after a lapse without a backlog or shame. **Pain point:** P4 · **Use cases:** UC9, UC11

## Feature 4.1: Welcome-Back Summary

**Priority:** Must · *Updated: summary content.*

**Feature-Level User Story:** As a chronic abandoner, I want returning after time away to be quick and judgment-free, so that one missed week doesn't make me quit.

**Feature-Level Use Case Scenarios:**

- **Main:** Jordan returns after 7+ days: "Your Pot grew $46 while you were away. Phone bill due Friday. Today's Number: $31." Then straight to the home screen.
- **Alternate:** A Buy Day passed while Jordan was away: "You kept your patience on the jacket. Want it back on your wishlist?"
- **Alternate:** A shorter break (under 7 days); no summary is shown.
- **Edge:** A lot happened while away; the summary still shows at most three items.

| ID | Task | Type | Change |
| --- | --- | --- | --- |
| E4-F1-T1 | Update "last active date" in `profiles` each time the app is opened | Backend | — |
| E4-F1-T2 | Build the summary generator, choosing the three most useful items: Pot growth, kept-patience items, upcoming bills, and Today's Number | Backend | ✏️ Updated |
| E4-F1-T3 | Design the welcome-back screen: warm wording, no red, no overdue language | Design | — |
| E4-F1-T4 | Build the welcome-back screen | Frontend | — |
| E4-F1-T5 | Write welcome-back message variations | Design | — |
| E4-F1-T6 | Track the event "returned after lapse" | Backend | — |
| E4-F1-T7 | Review all screens to remove streaks, overdue warnings, and guilt-based wording | Testing | — |

## Feature 4.2: Money Stress Check-In

**Priority:** Should · *Unchanged from v1 (tasks E4-F2-T1 to T4).*

**Feature-Level User Story:** As the product team, we want users to rate their money stress at signup and after 30 days, so that we can measure whether the app reduces stress.

## Feature 4.3: Monthly Recap

**Priority:** Could · *Replaces v1's Weekly Recap; a monthly rhythm suits Buy Days and the Pot better.*

**Feature-Level User Story:** As a user, I want a short monthly summary of my progress, so that I can see how patience paid off.

**Feature-Level Use Case Scenarios:**

- **Main:** On the first of the month: "Total Kept: $212. Bought on purpose: headphones. Kept your patience: jacket."
- **Edge:** A quiet month with little activity; the recap stays positive and short.

| ID | Task | Type |
| --- | --- | --- |
| E4-F3-T1 | Design the recap screen (three cards, 30 seconds to read) | Design |
| E4-F3-T2 | Build the recap generator: Total Kept, items bought on purpose, and kept-patience items | Backend |
| E4-F3-T3 | Add the monthly recap to the scheduled jobs | Backend |
| E4-F3-T4 | Build the recap screen | Frontend |

> ➡️ **Next:** The 140 tasks populate the Notion backlog (v2) via an updated CSV.
> 

---

Next is the **Backlog CSV (v2)**. I'll regenerate it with all 140 tasks and add a **Change** column (New, Updated, or Unchanged), so the backlog shows the progression too. Continue?