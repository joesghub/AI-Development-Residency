# Pain Points, Journeys, Features

# User Pain Points and Journeys

> 🧭 **Purpose:** Define the audience's real pain points first, map how they experience money today, then design our app's journey and differentiators around those moments, rather than around competitor gaps alone.
> 

*Process: Pain points → Current journeys → Future journey → Differentiators → Feature prioritization → MVP selection → MMP*

## Step 1: Pain Points

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

## Step 2: Current User Journeys

**Persona: Jordan, 29, a chronic abandoner (Audience 1).** Jordan has ADHD, earns a steady salary, and has tried two budgeting apps and a spreadsheet. Jordan wants to stop living paycheck to paycheck and stop paying late fees.

### Journey A: No App (Status Quo)

| Stage | What Jordan Does | Thinks / Feels | Pain Points |
| --- | --- | --- | --- |
| **Payday** | Checks the bank balance and feels flush | "I'm fine this month" | P6 |
| **Daily spending** | Buys coffee, takeout, and online items without checking anything | "It's just small stuff" | P2, P3 |
| **Impulse moment** | Sees a sale and buys immediately | Excited, then regretful | P3 |
| **Bill due** | Forgets the electric bill | Doesn't notice until the late fee arrives | P5 |
| **Mid-month** | Balance is lower than expected | Anxious: "Where did it go?" | P2, P6 |
| **End of month** | Runs short before payday | Shame: "I'm bad with money" | P4 |
| **Next month** | Repeats the cycle | Resigned | P4 |

### Journey B: With YNAB (Biggest Direct Competitor)

| Stage | What Jordan Does | Thinks / Feels | Pain Points | Drop-off Risk |
| --- | --- | --- | --- | --- |
| **Discovery** | Finds YNAB's ADHD guide and starts the free trial | Hopeful: "This one gets me" | None | Low |
| **Setup** | Links accounts, learns the method, creates categories, assigns every dollar | Overwhelmed but motivated; it takes an evening | P1 | Medium |
| **Week 1** | Approves transactions daily and moves money between categories | Proud, engaged (novelty) | P1 | Low |
| **Impulse moment** | Is in a store; YNAB isn't open, so Jordan forgets to check and buys | Regret afterward | P2, P3 | Medium |
| **Weeks 2–3** | Daily approvals get skipped, and unapproved transactions pile up | "I'll catch up this weekend" | P1, P2 | High |
| **The lapse** | A busy week passes without opening the app | Avoids it: "It'll be a mess" | P4 | **🔴 Critical** |
| **Return attempt** | Opens the app to dozens of unapproved transactions and overspent categories in red | Shame: "I failed again" | P4 | **🔴 Critical** |
| **Outcome** | Stops opening the app; the subscription renews or is canceled | "Budgeting doesn't work for me" | P4 | Abandoned |

**Key insight:** Jordan doesn't quit YNAB because the method is wrong. Jordan quits at **the lapse and the return attempt**: the first missed week turns into a backlog, and the backlog turns into shame. Every tool Jordan has tried fails at the same moment.

**How Audience 2 differs (newly diagnosed adults):** they have no failed tools behind them yet, so setup motivation is higher. But they're more affected by P5 (missed bills) and P6 (abstract budgets), because they have no existing system at all. The lapse moment still applies: without a design for it, they'll become chronic abandoners.

## Step 3: Future Journey (Our App)

| Stage | What Jordan Does | Thinks / Feels | Pain Point Solved |
| --- | --- | --- | --- |
| **Setup** | Links a bank account; transactions sort automatically into Bills, Needs, and Wants. Sees Today's Number in under 5 minutes. | "That was easy" | P1 |
| **Morning** | Gets a notification: "Today's Number: $28" | Clear, no effort | P2, P6 |
| **Impulse moment** | Taps **Park It** instead of buying; the item is saved for 48 hours | The urge is acknowledged, not denied | P3 |
| **48 hours later** | The app asks "Still want it?" Jordan skips it, and **Money Kept** grows by $65 | A dopamine hit from *not* spending | P3, P4 |
| **Bill due** | Gets a reminder 3 days before the bill is due | Pays on time, no late fee | P5 |
| **The lapse** | A busy week passes without opening the app; nothing piles up, because sorting is automatic | No dread | P4 |
| **Return** | Opens the app to a welcome-back summary: what changed, one bill due soon, and today's number. No red warnings, no backlog. | "Okay, I'm back" | P4 |
| **Outcome** | Back in the routine within 10 seconds; progress never resets | Confident: "This works with my brain" | P1–P6 |

**The moment that matters most:** the return after a lapse. Where YNAB's journey ends in abandonment, ours resumes. That's the core of our differentiation.

## Step 4: Differentiators and Core Experience

**Differentiators, traced to pain points and journey moments**

| Pain Point | Journey Moment | Our Mechanic | How Competitors Handle It |
| --- | --- | --- | --- |
| P1 Setup overwhelm | Setup, ongoing upkeep | **Three Buckets:** automatic sorting into Bills, Needs, and Wants; users only swipe to fix mistakes | YNAB requires manual category setup and daily approvals |
| P2 Out of sight | Daily spending | **Morning Number notification and home screen icon:** the number comes to the user | Most apps wait for the user to open them |
| P6 Abstract budgets | Daily spending | **Today's Number:** one daily amount safe to spend on wants, recalculated each morning | PocketGuard shows a safe-to-spend amount based on the month as a whole |
| P3 Impulse purchases | Impulse moment | **Park It:** save a tempting purchase for 48 hours, then decide | Rule uses shopping cooldowns, but isn't available in the U.S. or built around a daily number |
| P3/P4 No reward for restraint | 48 hours later | **Money Kept counter:** skipped purchases add to a growing total | No major U.S. competitor rewards money *not* spent |
| P4 Shame spiral | The lapse and return | **Welcome-back summary, with no backlog and no streaks** | YNAB returns users to a backlog; streak-based apps "break" |
| P5 Missed bills | Bill due | **Bill reminders** based on detected recurring payments | Common across competitors: table stakes, not a differentiator |

**Core loop: about 1–2 minutes a day**

1. **Morning:** notification shows Today's Number.
2. **Before buying:** glance at the number, or Park It.
3. **48 hours later:** decide on parked items, and Money Kept grows.
4. **Weekly:** a 30-second recap.
5. **After a lapse:** the welcome-back summary, then straight back into the loop.

**Design principles: rules every feature must follow**

1. **The app comes to the user.** Never rely on the user remembering to open it.
2. **No backlog, ever.** Nothing piles up while the user is away.
3. **No streaks.** Progress only goes up.
4. **Reward restraint.** Make not spending feel like a win.
5. **Two minutes a day, maximum.** Any feature that needs more effort must justify it.

## Step 5: Feature Prioritization

**Method:** Each candidate feature is scored 1–3 on four criteria, then sorted into MoSCoW categories for the MVP.

- **Pain severity:** how severe is the pain point it solves?
- **Differentiation:** does it set us apart from competitors?
- **Ease:** 3 = easy to build, 1 = hard.
- **MVP learning:** does it help test the core assumption?

| Feature | Pain Points | Severity | Differentiation | Ease | MVP Learning | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Automatic transaction import and Three Buckets | P1 | 3 | 2 | 1 | 3 | **9** |
| Today's Number | P2, P6 | 3 | 3 | 2 | 3 | **11** |
| Morning Number notification | P2 | 3 | 3 | 2 | 3 | **11** |
| Park It (48-hour cooling-off) | P3 | 3 | 3 | 3 | 3 | **12** |
| Money Kept counter | P3, P4 | 3 | 3 | 3 | 3 | **12** |
| Welcome-back summary (no backlog) | P4 | 3 | 3 | 2 | 3 | **11** |
| Bill detection and reminders | P5 | 2 | 1 | 2 | 2 | **7** |
| Weekly 30-second recap | P2 | 2 | 2 | 2 | 2 | **8** |
| Money stress check-in | Measurement | 1 | 1 | 3 | 3 | **8** |
| Subscription detection | P7 | 2 | 1 | 2 | 1 | **6** |
| ADHD money education content | P4 | 2 | 2 | 2 | 1 | **7** |
| Support partner sharing | P4 | 2 | 3 | 1 | 1 | **7** |
| Automatic purchase interventions (card-triggered alerts) | P3 | 3 | 3 | 1 | 1 | **8** |

**MoSCoW for MVP #1**

- **Must have:** automatic transaction import and Three Buckets, Today's Number, Morning Number notification, Park It, Money Kept, welcome-back summary.
- **Should have:** bill detection and reminders (table stakes for P5, a high-cost pain), money stress check-in (needed to measure impact).
- **Could have:** weekly recap.
- **Won't have (this release):** subscription detection, ADHD education content, support partner sharing, automatic purchase interventions.

*Note: bill reminders score low on differentiation, but they solve a costly pain point (late fees). Users would also notice their absence, so they're included as a Should.*

## Step 6: MVP Selection

**Candidate MVPs**

| Criterion | A: Single Feature (Park It only) | B: Concierge (manual texts and spreadsheet) | C: Focused Core Loop |
| --- | --- | --- | --- |
| **Pain severity** (addresses the top pains P1–P4) | 1 (P3 only) | 2 | 3 |
| **Riskiest assumption** (tests whether users return after a lapse) | 1 | 1 (no real lapse experience) | 3 |
| **Cost and time** | 3 | 3 | 2 |
| **Learning quality** | 2 | 1 (manual help skews results) | 3 |
| **Risk** (security, technical) | 3 | 3 | 2 (bank data) |
| **Total** | 10 | 10 | **13** |

**Selected: MVP C, the Focused Core Loop.**

**Riskiest assumption:** *If the app comes to users, rewards restraint, and never creates a backlog, adults with ADHD will return after a lapse instead of abandoning it.*

The journey mapping showed that users abandon tools at the lapse and return moment. Only MVP C includes a real core loop that users can lapse from and return to, so only MVP C can test that assumption.

**Updates to the MVP #1 section**

- **Problems to Solve:** replace with pain points P1–P6, assigned by audience as in the inventory above.
- **Platform:** change from "iOS first" to a **mobile-friendly web app (progressive web app)** that users add to their home screen. This matches the required Vercel hosting, works on iPhone and Android, and costs less than a native app. Remove "Android version" from out of scope.
- **Features:** "safe-to-spend number" becomes **Today's Number**; the "Should I buy this?" check and cooling-off wishlist become **Park It**; streak-free rewards become **Money Kept**; add the **Morning Number notification**.
- **KPIs:** add **Park It skip rate** (% of parked items the user decides not to buy) and **Money Kept per user**.

**Updated MVP #1 Release-Level Scope**

| Value | Problem | Scope of Outcomes |
| --- | --- | --- |
| **Budget with almost no effort** | P1: Setup and upkeep overwhelm | Automatic import and Three Buckets; users see Today's Number within 5 minutes of signup |
| **Know what you can spend today, without remembering to check** | P2: Out of sight, out of mind; P6: Abstract budgets | Today's Number delivered by morning notification; users can answer "Can I afford this?" at a glance |
| **Pause before impulse buys, and feel rewarded for it** | P3: Impulse purchases | Park It with a 48-hour decision prompt; Money Kept grows with each skipped purchase |
| **Come back anytime without guilt** | P4: Shame spiral | Welcome-back summary, no backlog, no streaks; a higher share of lapsed users return |
| **Never miss a bill** | P5: Missed bills and late fees | Reminders 3 days before detected bills are due; fewer self-reported late fees |

**Updated MVP #1 Use Cases**

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