# MMP Vision and Scope (v3)

> 🔄 **What changed and why (v2 → v3)**
> 
> - **App store launch is now an explicit MMP milestone.** The MVP beta runs through Expo/TestFlight with no store review; the MMP is where the app goes live on the App Store and Google Play.
> - **Bill reminders moved here.** Cut from the MVP, they become an MMP feature (detection already exists from the MVP, feeding Today's Budget).
> - **New decision gates** for the things the MVP now tests: the notification engagement model and the Budget Breakdown.
> - **The "what shapes my budget" trend view** (the richer, over-time version of the breakdown) is named as an MMP feature.
> - **Costs updated** for app store accounts and the native build.
> - **Unchanged:** Audience 3 (support partners), ADHD education, subscriptions, and the MMP goal.

> 🚀 **MMP goal:** Launch Patiencents publicly on the app stores and earn revenue. Everything here is a **hypothesis**, confirmed or changed by MVP #1 results through the decision gates.
> 

## Decision Gates: How MVP Results Shape the MMP

*Updated: notification and breakdown gates added.*

| If the MVP Shows… | Then the MMP Will… |
| --- | --- |
| 90-day retention ≥ 25% and comeback rate ≥ 40% | ✅ Proceed with the MMP as planned |
| **Notification opt-out is high, or open rates are low (New)** | Rethink the engagement model before scaling: fewer or smarter notifications, or a reason to open the app beyond them |
| **The Budget Breakdown is widely viewed and valued (New)** | Build the richer "what shapes my budget" trend view and gentle pattern observations |
| **The Budget Breakdown is ignored (New)** | Simplify or drop it rather than expanding it |
| Wishlist adoption is low (< 40%) | Make adding items easier: test a save-from-cart extension |
| Many items are bought before their Buy Day | Add more reasons to wait: price drop alerts, stronger countdowns |
| Milestone notifications drive engagement | Expand them: milestones for multiple items, bigger celebrations |
| Users ask about bills they weren't reminded of | Prioritize the bill reminder feature (detection already exists) |
| Matching needs frequent manual fixes | Improve matching before scaling |
| Users won't connect a bank | Improve the CSV and manual paths; add trust signals |
| Pot growth is strong and users want the money set aside | Explore guided savings transfers |

## Audiences

- **Audience 1: Chronic abandoners** (same as MVP)
- **Audience 2: Newly diagnosed adults** (same as MVP)
- **Audience 3: Support partners (New):** partners, family, or coaches who help someone with ADHD manage money. Motivated to help without nagging.

## Problems To Solve Per Audience

- **Audience 1:** same as MVP, plus **P7 forgotten subscriptions (New).**
- **Audience 2:** same as MVP, plus **(New) lack of ADHD-specific money knowledge**, and **P5 missed bills now actively handled** through bill reminders (the MVP only set the money aside).
- **Audience 3 (New):** lack of visibility into a partner's progress; money causing conflict.

## Business Goals

*Updated: goals 1 and 6 reflect the app store and native launch.*

1. **Launch on the App Store and Google Play (New):** pass review and publish on both platforms.
2. **Convert users to paid subscriptions** and validate pricing.
3. **Retain paying users** at or above MVP retention levels.
4. **Build credibility** through reviews, ADHD community partnerships, and creators.
5. **Lay groundwork for the employer channel** (post-MMP).
6. **Prove the native app at scale (New):** reliable notifications, bank syncing, and performance beyond a small beta.

## Value

Same as MVP, plus:

- **(New) Active bill reminders**, so users never miss a due date, not just avoid spending the money.
- **(New) Celebrate progress with someone who supports you**, on your terms.
- **(New) Learn how ADHD affects money** through short lessons.
- **(New) Catch forgotten subscriptions** before they drain your Pot.
- **(New) A richer "what shapes my budget" view**, if the MVP breakdown proves valued.
- **(Conditional) More reasons to wait:** price drop alerts and steady weekly amounts for Usuals.

## Unique Value Proposition

*Unchanged.* Patiencents is the budgeting app that turns patience into the things you want.

## Barriers to Success

Same as MVP, plus:

| Barrier | Why It's a Risk | How We'll Address It |
| --- | --- | --- |
| **App store review (New)** | Apple and Google can reject or delay apps, especially finance apps handling bank data | Follow store guidelines early; budget time for review; have privacy and data handling well documented |
| **Converting free users to paid** | Our audience is wary of forgotten subscriptions | "We'll remind you before we ever charge you," easy cancellation, a low-income discount |
| **Pricing** | Competitors charge ~$75–$109/year | Test prices below YNAB |
| **What to keep free** | Paywalling the core loop could hurt trust | Test a free tier vs. a full trial |
| **Customer acquisition** | Reaching ADHD adults costs money and needs trust | Partner with ADHD creators and communities |
| **Competitor response** | YNAB could copy automatic Buy Days | Move fast; own "patience pays" |
| **Notifications at scale (New)** | More users means more push volume and delivery edge cases | Monitor delivery; keep the gentle daily cap |
| **Support at scale** | More users, more connection and matching issues | Help center and in-app support |
| **Privacy with sharing** | Support partner features could feel controlling | User-controlled sharing, revocable anytime |
| **Bank data costs** | Plaid's free plan covers ~10 connections | Budget for paid production access |

## Release-Level Costs

Same categories as MVP, plus:

| Cost Category | What It Covers | Relative Cost |
| --- | --- | --- |
| **App store accounts (New)** | Apple Developer ($99/year) and Google Play ($25 once) | Low |
| **Hosting and database upgrades (New)** | Vercel Pro (~$20/member/month), Supabase Pro, Expo paid tier for more builds | Low–Medium |
| **Bank data provider (New)** | Plaid production access, by usage | Medium–High |
| **Marketing (New)** | Launch, creator partnerships, app store presence | High |
| **Payments (New)** | Subscription billing and processing fees | Low–Medium |
| **Customer support (New)** | Help center and staff | Medium |
| **Content (New)** | ADHD money lessons, ideally clinician-reviewed | Medium |

## Key Performance Indicators

Same as MVP, plus:

| KPI | What It Measures |
| --- | --- |
| **App store rating (New)** | Public rating on the App Store and Google Play |
| **Trial-to-paid conversion (New)** | % of trial users who subscribe |
| **Monthly churn (New)** | % of paying users who cancel each month |
| **Customer acquisition cost (New)** | Marketing spend per new paying user |
| **Lifetime value (New)** | Average revenue per user |
| **Support partner adoption (New)** | % of users who invite a support partner |
| **Lesson completion (New)** | % of newly diagnosed users completing a lesson |

## Use Cases to Support

Same as MVP, plus:

| # | Use Case | Audience |
| --- | --- | --- |
| 14 | User gets a reminder before a bill is due (New) | 1, 2 |
| 15 | User starts a free trial and gets a reminder before being charged | 1, 2 |
| 16 | User subscribes and manages billing in the app | 1, 2 |
| 17 | User invites a support partner and chooses what they can see | 1, 2 |
| 18 | Support partner sees shared progress and sends encouragement | 3 |
| 19 | User is alerted to a recurring subscription they may not use | 1, 2 |
| 20 | User completes a short lesson on ADHD and money | 2 |
| 21 | User opens a richer "what shapes my budget" trend view (New) | 1, 2 |
| 22 *(conditional)* | User sees that a wishlist item's price dropped while they waited | 1, 2 |

## Release-Level Scope

Same as MVP, plus:

| Value | Problem | Scope of Outcomes |
| --- | --- | --- |
| **Never miss a bill (New)** | P5: Missed bills | Reminders before detected bills are due; fewer self-reported late fees |
| **Celebrate progress with someone (New)** | Support partners lack visibility | Invite flow with user-controlled sharing |
| **Learn how ADHD affects money (New)** | Lack of ADHD money knowledge | Short in-app lessons |
| **Catch forgotten subscriptions (New)** | P7: Forgotten subscriptions | Alerts for recurring charges |
| **Understand your budget over time (New)** | P2, P6 | The richer trend view, if the MVP breakdown proved valued |
| **A product worth paying for (New)** | Users must trust and value it enough to pay | Free trial with a reminder before charging, subscription billing, help center |

> 📝 **Note:** The MMP is a set of bets. MVP #1 results, especially on notifications and the breakdown, decide which make it in.
> 

---

> 🔭 **Future Vision (beyond the MMP): A real, funded Patience Pot**
> 
> 
> Two linked ideas to explore once the core product is proven and profitable:
> 
> 1. **Move real money.** Instead of only tracking the Patience Pot, the app could move a calculated savings amount into a real, separate pot the user can’t easily spend, making patience tangible and putting the money out of impulse’s reach.
> 2. **An outcome-based revenue model.** Rather than (or alongside) a subscription, Patiencents could earn from the value it creates for the user, such as a share of returns, rather than from their income.
> 
> **Why this is parked, not planned:** moving or growing user money turns Patiencents from a budgeting app into a regulated financial service (money transmission, and possibly investment licensing). That’s a major leap in cost, compliance, and risk, and it could complicate the calm, low-risk feeling the brand depends on. It should be a deliberate strategic decision made *after* the MMP proves users will pay for the core experience, not a feature bolted onto this release. Flagged here so the vision isn’t lost.
>