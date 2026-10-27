# Product Release Vision and Scope

# MVP #1 Vision and Scope

> 🧪 **MVP goal:** Test our riskiest assumption: *if budgeting takes very little effort, steps in before impulse buys, and makes it easy to come back, adults with ADHD will keep using it.* The MVP exists to learn, not to earn revenue.
> 

## How We Identified Our Audiences

An audience is a group within the target segment whose **needs, motivations, or behavior are different enough to change what we build for them**. Our target segment, adults with ADHD aged 50 and under who use or want to try a budgeting app, is one market. But not everyone in it arrives with the same history or goals.

**Step 1: Start from the target segment.** Audiences are subgroups of the segment chosen in the Competitive Analysis, not new markets.

**Step 2: Brainstorm ways to split the segment.** Look for differences that change the product, not just demographics:

- **Past behavior:** Have they tried budgeting apps before?
- **Life stage or trigger:** What prompted them to look for help now?
- **Role:** Are they the person budgeting, or someone helping that person?
- **Demographics:** Age, income, student status.

**Step 3: Test each candidate audience.** A good audience passes four tests:

| Test | Question |
| --- | --- |
| **Distinct needs** | Does this group need something different from the product? |
| **Distinct motivation** | Do they come to the product for a different reason? |
| **Reachable** | Can we find and talk to them, through Reddit, ADHD communities, or app stores? |
| **Release fit** | Does serving them help test this release's riskiest assumption? |

**Step 4: Evaluate the candidates.**

| Candidate Audience | Distinct Needs | Distinct Motivation | Reachable | MVP Fit | Decision |
| --- | --- | --- | --- | --- | --- |
| **Chronic abandoners** (tried budgeting apps and quit) | ✅ Need low effort and easy restarts | ✅ Want something that finally sticks | ✅ Vocal in ADHD communities | ✅ Directly tests the riskiest assumption | **MVP Audience 1** |
| **Newly diagnosed adults** (recently diagnosed, building systems for the first time) | ✅ Need simple structure and guidance | ✅ Motivated by fresh self-understanding | ✅ Active in ADHD communities and searching for tools | ✅ Tests whether the product works without past budgeting habits | **MVP Audience 2** |
| **Support partners** (partner, family member, or coach helping someone with ADHD) | ✅ Need visibility without control | ✅ Want to help without nagging | ⚠️ Reached through the primary user | 🚫 Doesn't test the core assumption | **MMP Audience 3** |
| Age-based groups (for example, 18–29 vs. 30–50) | 🚫 Needs largely the same | 🚫 | ✅ | 🚫 | Rejected: age alone doesn't change the product |
| College students with ADHD | ⚠️ Some differences (irregular income) | ⚠️ | ✅ | 🚫 | Possible future audience; too narrow for the MVP |
| Employers | 🚫 They're buyers, not users | — | ⚠️ Long sales cycles | 🚫 | Business channel after the MMP, not an audience |

*Key lesson: demographics like age rarely make good audiences on their own. Behavior and motivation do, because they change what the product needs to do.*

# Audiences

**Audience 1: Chronic abandoners**

Adults with ADHD who have downloaded budgeting apps or built spreadsheets before, used them briefly, and quit.

- **Motivation:** They want control over their money and are frustrated that nothing has stuck. Many feel shame about it.
- **Goals:** Find a system they can keep using, stop impulse overspending, and stop paying late fees.
- **Why they matter:** If the product works for people who have already failed with other tools, it validates the core assumption.

**Audience 2: Newly diagnosed adults**

Adults recently diagnosed with ADHD who are learning how it affects their daily life, including money. About half of U.S. adults with ADHD were diagnosed in adulthood, so many people are building these systems for the first time.

- **Motivation:** Their diagnosis explains past money struggles, and they're actively looking for tools designed for how their brain works.
- **Goals:** Understand their spending patterns, build a simple routine, and avoid repeating past money mistakes.
- **Why they matter:** They test whether the product works for people without established budgeting habits, and they're highly motivated early adopters.

**Audience 3: Support partners (deferred to MMP)**

Partners, family members, or coaches who help someone with ADHD manage money. Deferred because this audience doesn't test the MVP's core assumption.

# Problems To Solve Per Audience

## Pain Points

**How we identified them:** We combined evidence from the market research, competitor analysis, competitor reviews, and published research on ADHD and money. These are evidence-based hypotheses to validate through user interviews.

**Key evidence:**

- Research from The Ohio State University suggests that individuals with ADHD are more likely to incur late fees and overdraw bank accounts.
- Studies show adults with ADHD are more likely to exceed their credit card limits and report more problems with impulse buying.
- Guilt and regret after spending can trigger more emotional spending as a way to find short-term relief, which creates a cycle.
- The extra costs have a name: the "ADHD tax," a casual term for the extra money, time, energy, and stress people pay as a result of having ADHD.
- Non-budgeters' top reason for skipping budgeting is that it's too time-consuming (34.2%, Debt.com).
- YNAB's top user complaints include a steep learning curve and complexity.

**Pain point inventory**

*Severity = how often it happens × how much it costs the user (money or emotional toll).*

| # | Pain Point | When It Happens | ADHD Driver | Severity | Audience |
| --- | --- | --- | --- | --- | --- |
| P1 | **Setup and upkeep overwhelm:** budgeting takes too much time and effort to start and maintain | First days with a new tool, then every week | Overwhelm, task initiation | 🔴 High | 1, 2 |
| P2 | **Out of sight, out of mind:** they forget to check their budget, so it stops guiding decisions | Daily | Working memory, inattention | 🔴 High | 1, 2 |
| P3 | **Impulse purchases:** spending decisions happen in seconds, and the regret comes after | Several times a week | Impulsivity, dopamine-seeking | 🔴 High | 1, 2 |
| P4 | **Shame spiral after falling off:** a missed week creates a backlog and guilt, so they avoid the app, and the guilt can trigger more spending | After any lapse | Emotional regulation, avoidance | 🔴 High | 1 |
| P5 | **Missed bills and late fees:** paying late fees on bills they had money for | Monthly | Time blindness, forgetfulness | 🟠 Medium–High | 2 (and 1) |
| P6 | **Monthly budgets feel abstract:** "$400 for the month" doesn't help decide whether to buy lunch today | Daily | Time blindness | 🟠 Medium | 1, 2 |
| P7 | **Forgotten subscriptions:** paying for services they no longer use | Monthly | Forgetfulness | 🟡 Medium | 1, 2 |

**Top pain points:** P1–P4 are rated high severity. P4 is the most important for Audience 1, since it explains why every previous tool failed them.

# Business Goals

*How we got here: an MVP's business goals are about learning and validating, not revenue.*

1. **Validate the core assumption:** show that adults with ADHD stay engaged with the product longer than they did with past budgeting tools.
2. **Learn which features drive engagement:** find out whether the safe-to-spend view, impulse pauses, or easy restarts matter most, to guide MMP priorities.
3. **Build an early community:** recruit early users who can give feedback and become advocates at public launch.
4. **Establish a secure foundation:** prove we can handle bank connections and financial data safely, since trust is a prerequisite for the MMP.

# Value

*How we got here: value describes what users get from this specific release.*

The MVP lets adults with ADHD:

- **Budget with almost no effort:** spending is tracked and categorized automatically.
- **Know what's safe to spend:** one clear number, always up to date.
- **Pause before impulse buys:** a quick check and cooling-off option before spending.
- **Never miss a bill:** reminders before due dates.
- **Come back anytime without guilt:** returning after time away is instant, with no backlog to clear.

# Unique Value Proposition

*How we got here: the UVP was developed in Product Positioning; this is the one-sentence version.*

[Product Name] is the budgeting app that does the remembering for you: it combines low-effort automation, in-the-moment impulse support, and shame-free restarts in one product built for ADHD brains.

# Barriers to Success

*How we got here: barriers are risks that could stop the MVP from succeeding, drawn from the competitor research and the nature of the audience.*

| Barrier | Why It's a Risk | How We'll Address It |
| --- | --- | --- |
| **ADHD abandonment patterns** | Our audience is known for dropping apps, the very behavior we're trying to change. | Design for comebacks, and measure return rates, not just daily use. |
| **Trust and data security** | Users must link bank accounts, which feels risky with a new, unknown app. | Use an established bank data provider, explain security clearly, and keep data collection minimal. |
| **Bank connection reliability** | Syncing issues are a top complaint about competitors like YNAB. | Choose a reliable provider and offer a clear fallback when a connection breaks. |
| **Technical limits on "in-the-moment" help** | We can't see a purchase before it happens at a store or checkout. | The MVP uses a user-triggered "Should I buy this?" check and a cooling-off wishlist. Automatic interventions are explored later. |
| **Notification fatigue** | Too many alerts lead users to turn them off or delete the app. | Keep alerts few, useful, and adjustable. |
| **Gamification that backfires** | Streaks punish breaks, creating the shame we want to avoid. | Reward progress without streaks, so missed days never "break" anything. |
| **Established competitors** | YNAB already markets to ADHD users and has a loyal community. | Compete on effort and comebacks, YNAB's weakest areas. |

# Release-Level Costs

*How we got here: at this stage, costs are estimated by category, not exact budgets. These are assumptions to refine with a development team.*

| Cost Category | What It Covers | Relative Cost |
| --- | --- | --- |
| **Development** | Building one mobile platform (iOS first), backend, and bank sync integration | High |
| **Design and user research** | ADHD-friendly interface, usability testing with target users | Medium |
| **Bank data provider fees** | Per-user fees for connecting bank accounts | Medium (grows with users) |
| **Security and compliance** | Encryption, data privacy practices, security review | Medium |
| **Infrastructure** | Hosting, databases, notifications | Low |
| **User recruitment** | Recruiting beta users through ADHD communities | Low |

*Why iOS first: building for one platform cuts MVP cost. iOS held the largest revenue share of the ADHD apps market in 2025, according to the market research.*

# Key Performance Indicators

*How we got here: Product Positioning defined success as "users still engaged months later." These KPIs measure that. Targets are hypotheses to adjust once we have baseline data.*

| KPI | What It Measures | Why It Matters |
| --- | --- | --- |
| **Activation rate** | % of new users who link a bank account and see their safe-to-spend number in their first session | Tests whether setup is truly low-effort |
| **30-day and 90-day retention** | % of users still active after 30 and 90 days | Directly tests the core assumption |
| **Comeback rate** | % of users inactive for 7+ days who return | Measures whether shame-free restarts work |
| **Impulse pause usage** | How often users use the "Should I buy this?" check, and how often they decide to skip or wait | Tests whether in-the-moment support is valued |
| **Bills paid on time** | Self-reported missed bills before vs. after using the app | Measures real-world money impact |
| **User-reported money stress** | Short in-app check-in at signup and after 30 days | Measures whether the product reduces anxiety, not just tracks money |

# Use Cases to Support

*How we got here: each use case comes from a problem above and is tagged with the audience it serves. These feed directly into the backlog.*

| # | Use Case | Audience |
| --- | --- | --- |
| 1 | User signs up, links a bank account, and sees Today's Number in under 5 minutes | 1, 2 |
| 2 | Transactions sort automatically into Bills, Needs, and Wants; the user swipes to fix one that's wrong | 1, 2 |
| 3 | User receives a morning notification with Today's Number | 1, 2 |
| 4 | User parks a tempting purchase instead of buying it | 1, 2 |
| 5 | After 48 hours, the user decides whether to buy the parked item; skipped items add to Money Kept | 1, 2 |
| 6 | User returns after a lapse and sees a welcome-back summary with no backlog | 1 |
| 7 | User gets a reminder 3 days before a bill is due | 2 |
| 8 | User completes a money stress check-in at signup and after 30 days | 1, 2 |

# Release-Level Scope

*How we got here: this table pulls together the sections above, connecting the value we deliver to the problem it solves and the outcome we expect.*

| Value | Problem | Scope of Outcomes |
| --- | --- | --- |
| **Budget with almost no effort** | P1: Setup and upkeep overwhelm | Automatic import and Three Buckets; users see Today's Number within 5 minutes of signup |
| **Know what you can spend today, without remembering to check** | P2: Out of sight, out of mind; P6: Abstract budgets | Today's Number delivered by morning notification; users can answer "Can I afford this?" at a glance |
| **Pause before impulse buys, and feel rewarded for it** | P3: Impulse purchases | Park It with a 48-hour decision prompt; Money Kept grows with each skipped purchase |
| **Come back anytime without guilt** | P4: Shame spiral | Welcome-back summary, no backlog, no streaks; a higher share of lapsed users return |
| **Never miss a bill** | P5: Missed bills and late fees | Reminders 3 days before detected bills are due; fewer self-reported late fees |

**Out of scope for the MVP** (planned for the MMP or later):

- **Support partner features:** Audience 3.
- **Paid subscriptions and payments:** the MVP is free for beta users.
- **ADHD money education and coaching content.**
- **Android version.**
- **Automatic purchase interventions:** for example, alerts triggered by card activity.
- **Employer and workplace partnerships.**

> 📝 **Note:** The KPI targets, costs, and features above are assumptions based on the market and competitive research. MVP testing with real users is how we'll confirm or adjust them.
> 

# MMP Vision and Scope

> 🚀 **MMP goal:** Launch publicly and earn revenue. Everything in this section is a **hypothesis**, confirmed or changed by MVP #1 results through the decision gates below.
> 

*How to read this section: the MMP builds on the MVP. Unchanged items say "Same as MVP," and new items are marked **(New)**.*

## Decision Gates: How MVP Results Shape the MMP

*Thresholds are assumptions to refine once baseline data exists.*

| If the MVP Shows… | Then the MMP Will… |
| --- | --- |
| 90-day retention of at least 25% and a comeback rate of at least 40% | ✅ Proceed with the MMP as planned |
| Retention is low, but the comeback rate is high | Invest in the daily loop (notifications, recap) before launch |
| The comeback rate is low | Pause the MMP and redesign the welcome-back experience; consider an MVP #2 |
| Activation is low because users won't link a bank account | Add a manual or CSV import option and stronger trust signals |
| Park It skip rate is high and users value Money Kept | Make Park It and Money Kept the center of marketing |
| Users rarely use Park It | Test automatic purchase interventions in an MVP #2 |
| Bill reminders are the most-used feature | Expand bill features, such as subscription detection |

## Audiences

- **Audience 1: Chronic abandoners** (same as MVP)
- **Audience 2: Newly diagnosed adults** (same as MVP)
- **Audience 3: Support partners (New):** partners, family members, or coaches who help someone with ADHD manage money.
    - **Motivation:** they want to help without nagging or taking control.
    - **Goals:** see progress the user chooses to share, celebrate wins, and avoid money arguments.

## Problems To Solve Per Audience

### Audience 1: Chronic abandoners

Same as MVP (P1–P4, P6), plus **P7: forgotten subscriptions (New)**.

### Audience 2: Newly diagnosed adults

Same as MVP (P1–P3, P5, P6), plus **(New) lack of ADHD-specific money knowledge:** they don't yet understand how ADHD affects their spending.

### Audience 3: Support partners (New)

- **Lack of visibility:** they can't tell whether their partner is doing okay without asking, which can feel like nagging.
- **Conflict over money:** money conversations turn into arguments or shame.

## Business Goals

1. **Launch publicly** in the U.S. as a mobile-friendly web app.
2. **Convert users to paid subscriptions** and validate pricing.
3. **Retain paying users,** keeping retention at or above MVP levels as the user base grows.
4. **Build credibility** through reviews, ADHD community partnerships, and creators.
5. **Lay groundwork for the employer channel:** prepare a pilot pitch for workplace financial wellness programs (post-MMP).

## Value

Same as MVP, plus:

- **(New) Share progress with someone who supports you,** on your terms.
- **(New) Catch forgotten subscriptions** before they drain your money.
- **(New) Learn how ADHD affects money** through bite-sized lessons in the app.

## Unique Value Proposition

Same as MVP: [Product Name] is the budgeting app that does the remembering for you. It combines low-effort automation, in-the-moment impulse support, and shame-free restarts in one product built for ADHD brains.

## Barriers to Success

Same as MVP, plus:

| Barrier | Why It's a Risk | How We'll Address It |
| --- | --- | --- |
| **Converting free users to paid** | Our audience is sensitive to the "ADHD tax" and wary of subscriptions they forget about | Clear trial reminders before charging, a free core tier, and a low-income discount |
| **Pricing** | Competitors charge about $75–$109 a year | Test price points; consider pricing below YNAB |
| **Customer acquisition** | Reaching ADHD adults costs money and needs trust | Partner with ADHD creators, communities, and coaches |
| **Competitor response** | YNAB could copy features like Park It | Move fast and own the "comeback" position in the ADHD community |
| **Support at scale** | More users means more bank connection issues and questions | Help center and in-app support |
| **Privacy with sharing** | Support partner features could feel controlling | Users choose exactly what is shared, and can revoke access anytime |

## Release-Level Costs

Same categories as MVP, plus:

| Cost Category | What It Covers | Relative Cost |
| --- | --- | --- |
| **Marketing (New)** | Launch, creator partnerships, app store and web presence | High |
| **Payments (New)** | Subscription billing and processing fees | Low–Medium |
| **Customer support (New)** | Help center and support staff | Medium |
| **Bank data provider fees** | Grows with the larger user base | Medium–High |
| **Content (New)** | ADHD money lessons, ideally reviewed by an ADHD clinician or financial therapist | Medium |

## Key Performance Indicators

Same as MVP, plus:

| KPI | What It Measures |
| --- | --- |
| **Trial-to-paid conversion (New)** | % of trial users who subscribe |
| **Monthly churn (New)** | % of paying users who cancel each month |
| **Customer acquisition cost (New)** | Marketing spend per new paying user |
| **Support partner adoption (New)** | % of users who invite a support partner |
| **Lifetime value (New)** | Average revenue per user over their time as a customer |

## Use Cases to Support

Same as MVP (use cases 1–8), plus:

| # | Use Case | Audience |
| --- | --- | --- |
| 9 | User starts a free trial and gets a reminder before being charged | 1, 2 |
| 10 | User subscribes and manages billing in the app | 1, 2 |
| 11 | User invites a support partner and chooses what they can see | 1, 2 |
| 12 | Support partner sees shared progress and sends encouragement | 3 |
| 13 | User is alerted to a recurring subscription they haven't used | 1, 2 |
| 14 | User completes a short lesson on ADHD and money | 2 |

## Release-Level Scope

Same as MVP, plus:

| Value | Problem | Scope of Outcomes |
| --- | --- | --- |
| **Share progress on your terms (New)** | Support partners lack visibility; money causes conflict | Invite flow with user-controlled sharing; partners can view progress and send encouragement |
| **Catch forgotten subscriptions (New)** | P7: Forgotten subscriptions | Alerts for recurring charges; users cancel unused subscriptions |
| **Learn how ADHD affects money (New)** | Lack of ADHD-specific money knowledge | Short in-app lessons; newly diagnosed users complete at least one |
| **A product worth paying for (New)** | Users must trust and value the app enough to pay | Free trial with reminders, subscription billing, help center |

> 📝 **Note:** The pain points, journeys, and MMP plans are evidence-based hypotheses. User interviews, ideally with 5–8 adults with ADHD, would strengthen this section before development begins.
> 

# Handoff to Build Plan

> 🔧 **Purpose:** This section turns the MVP scope into requirements the build plan must support. The build plan decides *how* to build; this section defines *what* it must deliver.
> 

*How the next steps connect:*

| Step | Input | Output |
| --- | --- | --- |
| **Build Plan** | This handoff section | Architecture, technology decisions, security approach |
| **Epics, Features, and Tasks** | MVP scope and build plan | Buildable work broken into tasks |
| **Notion Backlog** | Task list | Prioritized tasks ready for development |

### Features the Build Must Support

| Priority | Feature | Epic |
| --- | --- | --- |
| Must | Automatic transaction import and Three Buckets | Epic 1: Effortless Money Tracking |
| Must | Today’s Number | Epic 1: Effortless Money Tracking |
| Must | Morning Number notification | Epic 1: Effortless Money Tracking |
| Must | Park It (48-hour cooling-off) | Epic 2: Impulse Pause |
| Must | Money Kept counter | Epic2: Impulse Pause |
| Should | Bill detection and reminders | Epic 3: Bill Reminders |
| Must | Welcome-back summary (no backlog) | Epic 4: Guilt-Free Comebacks |
| Should | Money stress check-in | Epic 4: Guilt-Free Comebacks |
| Could | Weekly 30-second recap | Epic 4: Guilt-Free Comebacks |

### Platform Requirements

- **Mobile-friendly web app** (progressive web app) that users add to their home screen
- **Hosted on Vercel**, with code in **GitHub** and data in **Supabase** (required)
- **Push notifications** for the Morning Number, Park It decisions, and bill reminders
- **Fast to load and use:** the core loop must fit within two minutes a day

### Data the App Must Store

| Data | Why It’s Needed |
| --- | --- |
| **User accounts** | Sign-up, login, and personal settings |
| **Linked accounts and transactions** | Powers Three Buckets and Today’s Number |
| **Bucket assignments** | Bills, Needs, Wants, plus user corrections |
| **Parked items** | Item, price, date parked, and decision (bought or skipped) |
| **Money Kept total** | Running total of skipped purchases |
| **Detected bills** | Name, amount, and due date for reminders |
| **Check-in responses** | Money stress scores at signup and day 30 |
| **Activity data** | Last active date, to trigger the welcome-back summary and measure KPIs |

### Security Requirements

*User accounts hold financial data, so security is a requirement, not an add-on.*

- **Secure authentication:** users sign up and log in safely.
- **Data isolation:** users can only ever see their own data.
- **No stored bank passwords:** bank connections go through an established provider, never through credentials stored by our app.
- **Encrypted data** in storage and in transit.
- **Minimal data collection:** store only what features and KPIs need.

### Open Decisions for the Build Plan

| Decision | Options | Trade-off |
| --- | --- | --- |
| **How transactions get into the app** | Live bank sync through a provider such as Plaid, or CSV import from the user’s bank | Live sync fits the low-effort promise but adds cost and security responsibility. CSV is cheaper and safer, but adds user effort. |
| **How transactions are sorted into buckets** | Simple rules (for example, recurring charges = Bills), or AI-based categorization | Rules are cheaper and predictable; AI is more accurate but adds cost and complexity |
| **How notifications are sent** | Web push notifications, email, or both | Push is immediate but requires adding the app to the home screen on iPhone; email is a reliable fallback |

> ➡️ **Next:** The Build Plan resolves the open decisions above and defines the three-tier architecture: presentation (the web app on Vercel), application (server logic on Vercel), and data (Supabase).
>