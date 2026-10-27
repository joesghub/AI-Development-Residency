# MMP Vision and Scope (v2)

> 🔄 **What changed and why (v1 → v2)**
> 
> - **Built on the Patiencents MVP.** v1 extended the Comeback MVP; v2 extends the Patience Pot, wishlist, and Buy Days.
> - **Decision gates rewritten** around the new MVP KPIs: wishlist adoption, Buy Day outcomes, Pot growth, and matching accuracy.
> - **New MMP candidates** came out of the v2 feature prioritization: Spending Rhythm, price drop alerts, a save-from-cart browser extension, and guided savings transfers. Each is tied to a decision gate rather than committed up front.
> - **Return Rescue** is now a conditional candidate, since bank data can't confirm what's returnable.
> - **Costs updated** with the paid plans identified in the Build Plan (Vercel, Supabase, Plaid).
> - **Pricing hypothesis refined,** including a "we'll remind you before we charge you" promise that fits the brand.
> - **Unchanged:** Audience 3 (support partners), ADHD education, subscriptions, and the MMP goal.

> 🚀 **MMP goal:** Launch Patiencents publicly and earn revenue. Everything in this section is a **hypothesis**, confirmed or changed by MVP #1 results through the decision gates below.
> 

*How to read this section: the MMP builds on the MVP. Unchanged items say "Same as MVP," and new items are marked **(New)**.*

## Decision Gates: How MVP Results Shape the MMP

*Thresholds are assumptions to refine once baseline data exists.*

| If the MVP Shows… | Then the MMP Will… |
| --- | --- |
| 90-day retention of at least 25% and a comeback rate of at least 40% | ✅ Proceed with the MMP as planned |
| Retention is low, but the comeback rate is high | Strengthen the daily loop (morning notification, Pot celebrations) before launch |
| The comeback rate is low | Pause the MMP and redesign the welcome-back experience; consider an MVP #2 |
| **Wishlist adoption is low** (under 40% of active users have an item) | Make adding items easier: test the save-from-cart browser extension in an MVP #2 |
| **Many items are bought before their Buy Day** | Add more reasons to wait: price drop alerts ("Waiting saved you $12") and stronger countdowns |
| **Engagement drops while leftovers are pending** | Celebrate pending amounts more visibly, and look for faster transaction updates |
| **Matching needs frequent manual fixes** | Improve matching accuracy before scaling to more users |
| **Users won't link a bank account** | Improve the CSV and manual paths, and add stronger trust signals |
| **Pot growth is strong and users ask to set the money aside** | Explore guided savings transfers |
| **Users rely heavily on Usuals insights** | Add Spending Rhythm (steady weekly amounts for top Usuals) |
| **Users report returnable impulse buys in feedback** | Consider Return Rescue, with the user confirming what's returnable |

## Audiences

- **Audience 1: Chronic abandoners** (same as MVP)
- **Audience 2: Newly diagnosed adults** (same as MVP)
- **Audience 3: Support partners (New):** partners, family members, or coaches who help someone with ADHD manage money.
    - **Motivation:** they want to help without nagging or taking control.
    - **Goals:** celebrate progress the user chooses to share, and avoid money arguments.

## Problems To Solve Per Audience

### Audience 1: Chronic abandoners

Same as MVP (P1, P3, P4, P6), plus **(New) P7: forgotten subscriptions.**

### Audience 2: Newly diagnosed adults

Same as MVP (P2, P3, P5, P6), plus **(New) lack of ADHD-specific money knowledge:** they don't yet understand how ADHD affects their spending.

### Audience 3: Support partners (New)

- **Lack of visibility:** they can't tell whether their partner is doing okay without asking, which can feel like nagging.
- **Conflict over money:** money conversations turn into arguments or shame.

## Business Goals

1. **Launch publicly** in the U.S. as a mobile-friendly web app.
2. **Convert users to paid subscriptions** and validate pricing.
3. **Retain paying users** at or above MVP retention levels as the user base grows.
4. **Build credibility** through reviews, ADHD community partnerships, and creators.
5. **Lay groundwork for the employer channel:** prepare a pilot pitch for workplace financial wellness programs (post-MMP).

## Value

Same as MVP, plus:

- **(New) Celebrate progress with someone who supports you,** on your terms.
- **(New) Learn how ADHD affects money** through short lessons in the app.
- **(New) Catch forgotten subscriptions** before they drain your Pot.
- **(Conditional, based on decision gates) More reasons to wait:** price drop alerts, steady weekly amounts for Usuals, and one-click wishlist adding from shopping sites.

## Unique Value Proposition

Same as MVP: Patiencents is the budgeting app that turns patience into the things you want. Daily leftovers, confirmed by your bank, fill your Patience Pot and bring every wishlist item's Buy Day closer, with no backlog if you step away.

## Barriers to Success

Same as MVP, plus:

| Barrier | Why It's a Risk | How We'll Address It |
| --- | --- | --- |
| **Converting free users to paid** | Our audience is wary of subscriptions they forget about, a classic "ADHD tax" | Brand promise: *"We'll remind you before we ever charge you."* Clear trial reminders, easy cancellation, and a low-income discount |
| **Pricing** | Competitors charge about $75–$109 a year | Test prices below YNAB |
| **What to keep free** | Paywalling the core loop could hurt retention and trust | Test which features belong in a free tier, such as Today's Number free and the Pot and Buy Days paid, or a full trial |
| **Customer acquisition** | Reaching ADHD adults costs money and needs trust | Partner with ADHD creators, communities, and coaches |
| **Competitor response** | YNAB could add automatic Buy Days | Move fast and own "patience pays" in the ADHD community |
| **Support at scale** | More users means more bank connection issues and matching questions | Help center and in-app support |
| **Privacy with sharing** | Support partner features could feel controlling | Users choose exactly what's shared and can revoke access anytime |
| **Bank data costs** | Plaid's free plan covers only about 10 live connections | Budget for paid production access; costs grow with users |

## Release-Level Costs

Same categories as MVP, plus:

| Cost Category | What It Covers | Relative Cost |
| --- | --- | --- |
| **Hosting and database upgrades (New)** | Vercel Pro (about $20 per team member per month; Hobby is meant for personal projects) and Supabase Pro (free projects can pause after inactivity) | Low–Medium |
| **Bank data provider (New)** | Plaid full production access, priced by usage per connected account | Medium–High (grows with users) |
| **Marketing (New)** | Launch, creator partnerships, web presence | High |
| **Payments (New)** | Subscription billing and processing fees | Low–Medium |
| **Customer support (New)** | Help center and support staff | Medium |
| **Content (New)** | ADHD money lessons, ideally reviewed by an ADHD clinician or financial therapist | Medium |

## Key Performance Indicators

Same as MVP, plus:

| KPI | What It Measures |
| --- | --- |
| **Trial-to-paid conversion (New)** | % of trial users who subscribe |
| **Monthly churn (New)** | % of paying users who cancel each month |
| **Customer acquisition cost (New)** | Marketing spend per new paying user |
| **Lifetime value (New)** | Average revenue per user over their time as a customer |
| **Support partner adoption (New)** | % of users who invite a support partner |
| **Lesson completion (New)** | % of newly diagnosed users who complete at least one lesson |

## Use Cases to Support

Same as MVP (use cases 1–11), plus:

| # | Use Case | Audience |
| --- | --- | --- |
| 12 | User starts a free trial and gets a reminder before being charged | 1, 2 |
| 13 | User subscribes and manages billing in the app | 1, 2 |
| 14 | User invites a support partner and chooses what they can see | 1, 2 |
| 15 | Support partner sees shared progress, such as Total Kept and Buy Days reached, and sends encouragement | 3 |
| 16 | User is alerted to a recurring subscription they may no longer use | 1, 2 |
| 17 | User completes a short lesson on ADHD and money | 2 |
| 18 *(conditional)* | User sees that a wishlist item's price dropped while they waited | 1, 2 |
| 19 *(conditional)* | User adds an item to the wishlist from a shopping cart with one click | 1, 2 |

## Release-Level Scope

Same as MVP, plus:

| Value | Problem | Scope of Outcomes |
| --- | --- | --- |
| **Celebrate progress with someone who supports you (New)** | Support partners lack visibility; money causes conflict | Invite flow with user-controlled sharing; partners see progress and send encouragement |
| **Learn how ADHD affects money (New)** | Lack of ADHD-specific money knowledge | Short in-app lessons; newly diagnosed users complete at least one |
| **Catch forgotten subscriptions (New)** | P7: Forgotten subscriptions | Alerts for recurring charges; users cancel unused subscriptions |
| **A product worth paying for (New)** | Users must trust and value the app enough to pay | Free trial with a reminder before charging, subscription billing, help center |
| **More reasons to wait (Conditional)** | P3: Items bought before Buy Day | Price drop alerts and Spending Rhythm, if the decision gates support them |

> 📝 **Note:** The MMP is a set of bets, not a commitment. MVP #1 results decide which conditional items make it in.
> 

---

Next is **Build Plan (v2)**, which resolves the four new decisions and updates the data model and scheduled jobs. Continue?