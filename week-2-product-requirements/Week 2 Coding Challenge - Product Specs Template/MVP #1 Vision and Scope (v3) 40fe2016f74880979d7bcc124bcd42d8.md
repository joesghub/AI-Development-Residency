# MVP #1 Vision and Scope (v3)

# 🔄 **What changed and why (v2 → v3)**

- **Platform is now a cross-platform native app** (iOS + Android), not a mobile web app. Reason: notifications are the product's engagement model, and native is the only way they work reliably, especially on iOS.
- **Notifications are named as the engagement model.** The app is intentionally low-interaction (mostly read), so the daily notifications are what keep users engaged. Their open and opt-out rates are now core KPIs.
- **New feature: the Budget Breakdown** screen and its ~2pm notification, which teach how Today's Budget is calculated. Replaces the same-day nudge idea.
- **Buy Day reminder became Patience Pot milestone notifications** (25/50/75%, Buy Day at 100%).
- **Bill reminders removed.** Bill detection stays only to keep Today's Budget honest. Epic 3 is gone.
- **KPIs updated** for notifications and the removal of bill-related metrics.
- **Costs updated** for the native build (an Apple Developer account).
- **Unchanged:** the riskiest assumption, the audiences, and the whole Patiencents core experience.

> 🧪 **MVP goal:** Test our riskiest assumption: *if daily patience visibly funds the things people want, and lapses never create a backlog, adults with ADHD will plan purchases instead of buying on impulse, and keep using the app.* The MVP exists to learn, not to earn revenue.
> 

## MVP Selection

*Unchanged from v2. The Patiencents Core Loop remains the chosen MVP; see v2 for the scoring. The platform beneath it changed from web to native, but the loop being tested did not.*

## How We Identified Our Audiences

*Unchanged from v2.* Audiences are behavior-and-motivation subgroups of the target segment, not demographics. The evaluation selected **chronic abandoners** and **newly diagnosed adults** for the MVP, with **support partners** deferred to the MMP.

## Audiences

*Unchanged from v2.*

**Audience 1: Chronic abandoners.** Adults with ADHD who have tried budgeting apps and quit. Motivated to find something that finally sticks; the main test of the core assumption.

**Audience 2: Newly diagnosed adults.** Recently diagnosed adults building money systems for the first time. Highly motivated early adopters.

**Audience 3: Support partners.** Deferred to the MMP.

## Problems To Solve Per Audience

*Unchanged from v2.*

- **Audience 1:** P1 Setup overwhelm, P3 Impulse purchases, P4 Shame spiral, P6 Abstract budgets.
- **Audience 2:** P2 Out of sight, P3 Impulse purchases, P5 Missed bills, P6 Abstract budgets.

*Note on P5:* with bill reminders cut, the MVP addresses P5 only indirectly, by setting bill money aside in Today's Budget so a user doesn't accidentally spend it. Active bill reminders return in the MMP.

## Business Goals

*Updated: goal 6 added.*

1. **Validate the core assumption:** users plan wants through the wishlist and keep using the app longer than past tools.
2. **Learn which parts of the loop drive engagement:** Today's Budget, the Patience Pot, or Buy Days.
3. **Test the reward model:** confirm that bank-confirmed leftovers feel motivating despite the confirmation delay.
4. **Build an early community** of beta users.
5. **Establish a secure foundation** for bank connections and financial data.
6. **Validate notifications as the engagement model (New):** confirm that a low-interaction app can keep people engaged through a small set of daily notifications, by measuring whether users keep them on and tap them.

## Value

*Updated: the Budget Breakdown added; the engagement note added.*

The MVP lets adults with ADHD:

- **Budget with almost no effort:** spending sorts into Bills, Essentials, and Usuals automatically.
- **Know what they can spend today:** one number, delivered every morning.
- **Understand where that number comes from (New):** a breakdown screen, with an afternoon notification, that teaches how recent spending shaped today's budget.
- **See patience pay off:** unspent money goes into the Patience Pot, confirmed by their bank, with milestone notifications as they near a wishlist item.
- **Get what they want, on purpose:** wishlist items get a Buy Day when the budget can cover them.
- **Come back anytime without guilt:** missed Buy Days become "Kept your patience," and nothing piles up.

*The app is calm by design. A user mostly reads, so its two daily notifications are what keep it present in their life.*

## Unique Value Proposition

*Unchanged.* Patiencents is the budgeting app that turns patience into the things you want. *(See Product Positioning v2.)*

## Barriers to Success

*Updated: web/native rows changed; a notification-dependence row added.*

| Barrier | Why It's a Risk | How We'll Address It |
| --- | --- | --- |
| **Engagement depends on notifications (New)** | The app is low-interaction, so a user who turns notifications off may forget it, the exact abandonment we fight | Keep notifications few and genuinely useful; measure open and opt-out rates; make the morning and breakdown pushes carry real value |
| **ADHD abandonment patterns** | Our audience drops apps | No-backlog design; measure the comeback rate |
| **Wishlist adoption** | If users don't add items, the loop loses its reward | Prompt one item during onboarding; suggest ideas from Usuals |
| **Delayed rewards** | Transactions take 1–2 days to post | Show pending amounts, then celebrate on confirmation |
| **Trust and data security** | Users link a bank to a new app | Established provider, clear explanations, minimal data |
| **Native build and distribution (New)** | A native app adds app store accounts and a build process | Use Expo and TestFlight for the beta, avoiding store review until the MMP |
| **Bank connection limits** | The free Plaid Trial allows ~10 live connections | CSV import for additional testers |
| **Matching accuracy** | Messy merchant names and combined orders | Confirm medium-confidence matches; allow manual linking |
| **Irregular income** | Today's Budget assumes a predictable payday | Manual income and payday settings; gather feedback |

## Release-Level Costs

*Updated for the native build.*

| Cost Category | What It Covers | Relative Cost |
| --- | --- | --- |
| **Development** | The React Native/Expo app, the Vercel backend, bank integration, Today's Budget and breakdown, matching | High |
| **Design and user research** | ADHD-friendly interface, usability testing | Medium |
| **Apple Developer account** | TestFlight beta distribution | $99/year |
| **Bank data provider** | Plaid Sandbox and Trial | Free for the MVP |
| **Infrastructure** | Vercel, Supabase, Expo, GitHub | Free tiers |
| **User recruitment** | Recruiting beta testers | Low |

## Key Performance Indicators

*Updated: notification metrics added; bill metric removed.*

| KPI | What It Measures | Why It Matters |
| --- | --- | --- |
| **Activation rate** | % of new users who connect a bank (or import CSV), see Today's Budget, and add one wishlist item in the first session | Tests low-effort setup |
| **Notification open rate (New)** | % of morning and breakdown notifications that are tapped | Tests whether the engagement model works |
| **Notification opt-out rate (New)** | % of users who turn notifications off | A high rate warns that the quiet-app model is failing |
| **Breakdown screen views (New)** | % of users who open the breakdown, by notification or directly | Tests whether the teaching feature is valued |
| **30-day and 90-day retention** | % still active later | Tests the core assumption |
| **Comeback rate** | % of users away 7+ days who return | Tests the no-backlog design |
| **Days under Today's Budget** | % of days users spend under their number | Measures steadier spending |
| **Patience Pot growth** | Bank-confirmed leftover added per user per week | Measures real savings |
| **Wishlist adoption** | % of active users with at least one item | Tests whether users plan wants |
| **Buy Day outcomes** | Bought on purpose / bought early / kept your patience | Tests the loop |
| **Money stress** | Check-in at signup and day 30 | Measures whether stress drops |

## Use Cases to Support

*Updated: breakdown and milestone use cases added; bill reminder use case removed.*

| # | Use Case | Audience |
| --- | --- | --- |
| 1 | User signs up, connects a bank (or imports a CSV), and sees Today's Budget in under 5 minutes | 1, 2 |
| 2 | Transactions sort automatically into Bills, Essentials, and Usuals; the user swipes to fix one | 1, 2 |
| 3 | User receives a morning notification with Today's Budget and their next Buy Day countdown | 1, 2 |
| 4 | User opens the Budget Breakdown screen and sees how recent spending shaped today's number (New) | 1, 2 |
| 5 | User receives a ~2pm notification pointing to the Budget Breakdown (New) | 1, 2 |
| 6 | User adds an item to the wishlist by link or by hand, and taps a reason | 1, 2 |
| 7 | User sees a Buy Day calculated for each wishlist item | 1, 2 |
| 8 | Yesterday's leftover appears as pending in the Patience Pot, then is confirmed | 1, 2 |
| 9 | User gets a milestone notification at 25/50/75% toward their next item (New) | 1, 2 |
| 10 | On Buy Day, the user buys the item and confirms the match, or keeps their patience | 1, 2 |
| 11 | A Buy Day passes with no response; the item becomes "Kept your patience" | 1 |
| 12 | User returns after 7+ days and sees a welcome-back summary with no backlog | 1 |
| 13 | User completes a money stress check-in at signup and day 30 | 1, 2 |

## Release-Level Scope

*Updated: breakdown row added; milestone added to the patience row; bill row removed.*

| Value | Problem | Scope of Outcomes |
| --- | --- | --- |
| **Budget with almost no effort** | P1 | Automatic import and three buckets; Today's Budget within 5 minutes of signup |
| **Know what you can spend today** | P2, P6 | Today's Budget delivered each morning; users spend under it on more days over time |
| **Understand your number (New)** | P2, P6 | A breakdown screen plus a ~2pm notification; users who view it understand how spending shapes their budget |
| **See patience pay off** | P3 | Bank-confirmed leftovers fill the Pot; milestone notifications at 25/50/75%; Pot growth rises over time |
| **Get what you want, on purpose** | P3 | Wishlist with automatic Buy Days; more items bought on Buy Day or kept than bought early |
| **Come back anytime without guilt** | P4 | Kept your patience, welcome-back summary, no streaks; higher comeback rate |

**Out of scope for the MVP** (planned for the MMP or later):

- Bill reminders (bill detection stays, only to keep Today's Budget honest)
- Support partner features (Audience 3)
- Paid subscriptions and payments
- ADHD money education content
- The anytime "what shapes my budget" trend view and gentle pattern observations (the MVP breakdown shows the current day's calculation)
- Spending Rhythm, price drop alerts, Return Rescue
- Save-from-cart and store integrations
- Automatic transfers to savings
- App store distribution (the beta uses Expo/TestFlight)

---

# Handoff to Build Plan (v3)

*The Build Plan (v3) is already written and resolves everything below. This section is kept as the bridge.*

## Features the Build Must Support

| Priority | Feature | Epic |
| --- | --- | --- |
| Must | Native app install + push notifications | Epic 0 |
| Must | Automatic import (Plaid + CSV) and three buckets | Epic 1 |
| Must | Today's Budget | Epic 1 |
| Must | Morning notification | Epic 1 |
| Must | Budget Breakdown screen + ~2pm notification (New) | Epic 1 |
| Should | Usuals insights | Epic 1 |
| Must | Patience Pot (pending + confirmed leftovers) | Epic 2 |
| Must | Wishlist | Epic 2 |
| Must | Buy Day scheduling | Epic 2 |
| Must | Buy Day check-in and matching | Epic 2 |
| Must | Patience Pot milestone notifications (New) | Epic 2 |
| Must | Kept your patience | Epic 2 |
| Must | Welcome-back summary | Epic 4 |
| Should | Money stress check-in | Epic 4 |
| Could | Monthly recap | Epic 4 |

## Platform Requirements

- **Cross-platform native app** (React Native + Expo) for iOS and Android
- **Backend API on Vercel**, data in **Supabase**, code in **GitHub**
- **Push notifications** via Expo Push to APNs and FCM
- **At most 2 notifications on a normal day, 3–4 when an occasional one lands**
- **The core loop fits within two minutes a day**

## Security Requirements

*Unchanged from v2, plus device-side secure token storage and HTTPS-only app traffic (see Build Plan v3).*

> ➡️ **Next:** Epic 0 (v3) replaces "Add to Home Screen" with native app install and push setup.
> 

---

That's MVP Scope v3. The Budget Breakdown is now a first-class feature, notifications are an explicit part of the model with their own KPIs, and Epic 3 is gone. Next is **Epic 0 (v3)**. Continue?