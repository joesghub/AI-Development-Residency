# User Pain Points and Journeys (v2)

# 🔄 **What changed and why (v1 → v2)**

- **New approach: Patiencents.** v1 designed the product around recovery after a lapse ("Comeback"). A side-by-side journey comparison showed that a planning-focused approach, where users plan purchases ahead with a wishlist and Buy Days, prevents more problems, while keeping recovery as a safety net.
- **Park It and Quick Save removed.** Both depended on users remembering the app at the moment of an impulse and resisting on their own. That relies on the exact skills ADHD makes hardest.
- **Money Kept made real.** v1 counted self-reported "skips" as savings, which can't be verified. v2 counts only unspent money from Today's Number, confirmed by bank data, in a "Patience Pot."
- **Return Rescue moved out of the MVP.** Bank data can't show what was bought or whether it's returnable, and many impulse purchases (takeout, digital items) can't be returned.
- **Buckets renamed.** "Wants" was confusing for purchases that already happened. Past spending is now Bills, Essentials, and **Usuals**; future spending lives on the **wishlist**.
- **Pain points and current journeys unchanged.** The problems are the same; the solution changed.

*Process: Pain points → Current journeys → Approach comparison → Future journey → Differentiators → Feature prioritization*

## Step 1: Pain Points

*Unchanged from v1.*

**How we identified them:** We combined evidence from the market research, competitor analysis, competitor reviews, and published research on ADHD and money. These are evidence-based hypotheses to validate through user interviews.

**Key evidence:**

- Research from The Ohio State University suggests that individuals with ADHD are more likely to incur late fees and overdraw bank accounts.
- Studies show adults with ADHD are more likely to exceed their credit card limits and report more problems with impulse buying.
- Guilt and regret after spending can trigger more emotional spending as a way to find short-term relief, which creates a cycle.
- These extra costs are known as the "ADHD tax": the extra money, time, energy, and stress people pay as a result of having ADHD.
- Non-budgeters' top reason for skipping budgeting is that it's too time-consuming (34.2%, Debt.com).
- YNAB's top user complaints include a steep learning curve and complexity.

| # | Pain Point | When It Happens | ADHD Driver | Severity | Audience |
| --- | --- | --- | --- | --- | --- |
| P1 | **Setup and upkeep overwhelm:** budgeting takes too much time and effort to start and maintain | First days with a new tool, then every week | Overwhelm, task initiation | 🔴 High | 1, 2 |
| P2 | **Out of sight, out of mind:** they forget to check their budget, so it stops guiding decisions | Daily | Working memory, inattention | 🔴 High | 1, 2 |
| P3 | **Impulse purchases:** spending decisions happen in seconds, and the regret comes after | Several times a week | Impulsivity, dopamine-seeking | 🔴 High | 1, 2 |
| P4 | **Shame spiral after falling off:** a missed week creates a backlog and guilt, so they avoid the app, and the guilt can trigger more spending | After any lapse | Emotional regulation, avoidance | 🔴 High | 1 |
| P5 | **Missed bills and late fees:** paying late fees on bills they had money for | Monthly | Time blindness, forgetfulness | 🟠 Medium–High | 2 (and 1) |
| P6 | **Monthly budgets feel abstract:** "$400 for the month" doesn't help decide whether to buy lunch today | Daily | Time blindness | 🟠 Medium | 1, 2 |
| P7 | **Forgotten subscriptions:** paying for services they no longer use | Monthly | Forgetfulness | 🟡 Medium | 1, 2 |

## Step 2: Current User Journeys

*Unchanged from v1.*

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

**Key insight:** Jordan doesn't quit because the method is wrong. Jordan quits at **the lapse and the return attempt**: the first missed week turns into a backlog, and the backlog turns into shame.

**How Audience 2 differs (newly diagnosed adults):** they have no failed tools behind them yet, so setup motivation is higher. But they're more affected by P5 (missed bills) and P6 (abstract budgets), because they have no existing system at all.

## Step 3: Approach Comparison (New in v2)

Two approaches were compared using the same persona and journey stages:

- **Comeback** is *recovery-focused*: slips will happen, so make returning painless. Its key moment is the return after a lapse.
- **Patiencents** is *planning-focused*: help users decide ahead of time, so fewer slips happen. Its key moment is before the purchase.

| Stage | Comeback | Patiencents |
| --- | --- | --- |
| **Tempted by something new** | Resist in the moment (Quick Save) | Add it to the wishlist; it gets a Buy Day |
| **Thinking about a bigger want** | No plan; handled day by day | The wishlist shows when each item fits the budget |
| **Impulse purchase anyway** | After-purchase reflection and return reminders | Shows up in Usuals; the next few days' numbers adjust quietly |
| **The lapse** | Nothing piles up | Nothing piles up; missed Buy Days become "Kept your patience" |
| **How Jordan feels** | "Messing up isn't the end" | "I get the things I want, just on purpose" |

**What the review found:**

| Issue Found | Why It Mattered | Resolution |
| --- | --- | --- |
| Quick Save's "Skip it" counted self-reported savings | Not verifiable; easy to inflate; users stop trusting the reward | Money Kept now comes only from bank-confirmed leftovers of Today's Number |
| Return Rescue can't tell what's returnable | Bank data shows merchant and amount, not items or return policies | Removed from the MVP; possible MMP feature |
| Resisting in the moment relies on memory and willpower | Those are the skills ADHD makes hardest | Replaced with planning: "Not no, just later" |
| Patiencents alone could turn missed Buy Days into a backlog | Would recreate the shame spiral (P4) | Missed Buy Days automatically become "Kept your patience" |

**Decision:** Patiencents as the approach and brand, with Comeback's ideas (welcome-back summary, no backlog, no streaks) built in as the safety net.

## Step 4: Future Journey (Patiencents)

*Replaces the v1 future journey. See the Core Experience page for the full model.*

| Stage | What Jordan Does | Thinks / Feels | Pain Point Solved |
| --- | --- | --- | --- |
| **Setup** | Links a bank account and sees spending split into Bills, Essentials, and Usuals: "Most of your Usuals go to takeout, Amazon, and games." Sees Today's Number. Adds headphones to the wishlist and taps "Why this?" → *Excited about it.* | "That took five minutes" | P1, P2 |
| **Morning** | Notification: "Today's Number: $28. Headphones Buy Day: 12 days 🎧" | Clear and motivating | P2, P6 |
| **During the day** | Spends $19 on Usuals | Glanced at the number once | P6 |
| **Next day** | "Yesterday you kept $9." Once transactions post: "Confirmed! Your Buy Day moved 1 day closer." | A real win, backed by real money | P3 |
| **Tempted by something new** | Adds a jacket to the wishlist by sharing the link; it gets a Buy Day three weeks out | "I'm not saying no, I'm saying later" | P3 |
| **Impulse purchase anyway** | Buys concert tickets. The next few days' numbers drop slightly. No red, no warning. | "I'm still on track" | P4 |
| **Buy Day** | "It's Buy Day! 🎉 Still excited about the headphones?" Buys them; swipes to confirm the matched transaction. | Proud: "I bought this on purpose" | P3 |
| **The lapse** | A week passes without opening the app; the jacket's Buy Day passes after its reminder | Doesn't notice | — |
| **While away** | The jacket moves to "Kept your patience." No matching purchase appears in the bank data, so it's confirmed. | — | P4 |
| **Return** | Welcome-back summary: "Your Pot grew $46 while you were away. Phone bill due Friday. Today's Number: $31." | Back in 10 seconds | P4 |
| **End of month** | Recap: "Total Kept: $212. Bought on purpose: headphones. Kept your patience: jacket." | "This works with my brain" | P1–P6 |

## Step 5: Differentiators

| Pain Point | Journey Moment | Patiencents Mechanic | How Competitors Handle It |
| --- | --- | --- | --- |
| P1 Setup overwhelm | Setup | **Three buckets** (Bills, Essentials, Usuals) sorted automatically; swipe to fix | YNAB requires manual category setup and daily approvals |
| P2 Out of sight | Morning | **Morning notification** with Today's Number and the next Buy Day countdown | Most apps wait for the user to open them |
| P6 Abstract budgets | Daily spending | **Today's Number:** one daily amount for Usuals | PocketGuard shows a safe-to-spend amount based on the month |
| P3 Impulse purchases | Tempted | **Wishlist and Buy Days:** wants are scheduled for when the budget can cover them | YNAB suggests a manual wish list category; no competitor schedules purchase dates automatically |
| P3 No reward for patience | Next day | **The Patience Pot:** bank-confirmed leftovers fund wishlist items and bring Buy Days closer | No major U.S. competitor links daily restraint to a visible future reward |
| P4 Shame spiral | Lapse and return | **Kept your patience, welcome-back summary, no streaks;** overspending never reduces the Pot | YNAB returns users to a backlog; streak-based apps "break" |
| P5 Missed bills | Bill due | **Bill reminders** | Common across competitors (table stakes) |

## Step 6: Feature Prioritization

*Scored 1–3 on pain severity, differentiation, ease of building (3 = easy), and MVP learning value.*

| Feature | Pain Points | Severity | Differentiation | Ease | MVP Learning | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Automatic import and three buckets | P1 | 3 | 2 | 1 | 3 | **9** |
| Usuals insights | P2 | 2 | 2 | 3 | 2 | **9** |
| Today's Number | P2, P6 | 3 | 3 | 2 | 3 | **11** |
| Morning notification (number and Buy Day countdown) | P2 | 3 | 3 | 2 | 3 | **11** |
| Patience Pot (bank-confirmed leftovers) | P3, P4 | 3 | 3 | 2 | 3 | **11** |
| Wishlist (add by link, one-tap "Why this?") | P3 | 3 | 3 | 2 | 3 | **11** |
| Buy Day scheduling and countdown | P3, P6 | 3 | 3 | 2 | 3 | **11** |
| Buy Day check-in and transaction matching | P3 | 3 | 3 | 1 | 3 | **10** |
| Kept your patience (missed Buy Days) | P4 | 3 | 3 | 2 | 3 | **11** |
| Welcome-back summary | P4 | 3 | 3 | 2 | 3 | **11** |
| Bill detection and reminders | P5 | 2 | 1 | 2 | 2 | **7** |
| Money stress check-in | Measurement | 1 | 1 | 3 | 3 | **8** |
| Monthly recap | P2 | 2 | 2 | 2 | 2 | **8** |
| Spending Rhythm (steady weekly amounts) | P3, P6 | 2 | 2 | 2 | 1 | **7** |
| Price drop alerts | P3 | 2 | 3 | 1 | 1 | **7** |
| Return Rescue | P3 | 2 | 2 | 1 | 1 | **6** |
| Save-from-cart browser extension | P3 | 2 | 3 | 1 | 1 | **7** |
| Support partner sharing | P4 | 2 | 3 | 1 | 1 | **7** |

**MoSCoW for MVP #1**

- **Must have:** automatic import and three buckets, Today's Number, morning notification, Patience Pot, wishlist, Buy Day scheduling, Buy Day check-in and matching, Kept your patience, welcome-back summary.
- **Should have:** Usuals insights, bill detection and reminders, money stress check-in.
- **Could have:** monthly recap.
- **Won't have (this release):** Spending Rhythm, price drop alerts, Return Rescue, save-from-cart extension, support partner sharing.

*Note: Usuals insights moved to Should because Today's Number and the Pot deliver the core value without it; it's the first addition if time allows. Bill reminders stay a Should, since they solve a costly pain point even though they don't differentiate.*