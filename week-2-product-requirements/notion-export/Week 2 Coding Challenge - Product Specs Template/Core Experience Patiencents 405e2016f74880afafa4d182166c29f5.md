# Core Experience: Patiencents

> 🌱 **Patience pays.** Patiencents helps adults with ADHD get the things they want, on purpose. Every day you stay under your number, your next Buy Day gets closer. And if you slip or step away, nothing piles up; you just come back.
> 

## Glossary

| Term | Meaning |
| --- | --- |
| **Bills** | Recurring payments (rent, phone, utilities) |
| **Essentials** | Necessary spending (groceries, gas, medicine) |
| **Usuals** | The things you regularly buy beyond essentials (takeout, games, online orders) |
| **Today's Number** | What's safe to spend on Usuals today |
| **The Patience Pot** | Where unspent money from Today's Number goes; funds wishlist items |
| **Total Kept** | Everything ever added to the Pot; only goes up |
| **Pot Balance** | What's currently in the Pot and available for wishlist items |
| **Wishlist** | Things you want to buy in the future |
| **Buy Day** | The date a wishlist item fits your budget |
| **Kept your patience** | A wishlist item you decided against or let pass; its money stays in the Pot |

## How the Money Works

*Every number in Patiencents is backed by bank data.*

| Step | What Happens | Confirmed By |
| --- | --- | --- |
| **1. Today's Number** | (Income − Bills − estimated Essentials) ÷ days until payday | Bank data |
| **2. Daily leftover** | Unspent money from Today's Number goes into the Pot as *pending* | Becomes *confirmed* once the day's transactions post (usually 1–2 days) |
| **3. Buy Days** | The app schedules each wishlist item for the date the Pot can cover it, based on recent daily leftovers | Recalculated as the Pot grows |
| **4. Buy Day purchase** | Celebrated as "bought on purpose"; the price leaves the Pot Balance, and Total Kept stays the same | Matched to the bank transaction |
| **5. Deciding against an item** | The money stays in the Pot | No matching bank transaction |
| **Overspending** | Spending more than Today's Number lowers the next few days' numbers slightly. The Pot and Total Kept are never reduced, and there's no warning message. | Bank data |

The Pot is tracked in the app; the money stays in the user's bank account. The MVP doesn't move money.

## Patiencents User Journey

**Persona:** Jordan, 29, has ADHD and is a chronic abandoner of budgeting apps.

| Stage | What Jordan Does | Thinks / Feels | Pain Point Solved |
| --- | --- | --- | --- |
| **Setup** | Links a bank account and sees their spending split into Bills, Essentials, and Usuals: "Most of your Usuals go to takeout, Amazon, and games." Sees Today's Number. Adds headphones to the wishlist with a link and taps "Why this?" → *Excited about it.* | "That took five minutes, and it actually shows me where my money goes" | P1, P2 |
| **Morning** | Notification: "Today's Number: $28. Headphones Buy Day: 12 days 🎧" | Clear and motivating | P2, P6 |
| **During the day** | Spends $19 on lunch and a game | No checking needed; glanced at the number once | P6 |
| **Next day** | "Yesterday you kept $9 (pending)." When transactions post: "Confirmed! Your Buy Day moved 1 day closer." | A real win, backed by real money | P3 |
| **Tempted by something new** | Sees a jacket online, adds it to the wishlist by sharing the link, and gets a Buy Day three weeks out | "I'm not saying no, I'm saying later" | P3 |
| **Impulse purchase anyway** | Buys concert tickets on a whim. They show up in Usuals; the next few days' numbers drop slightly. No red, no warning. | "Okay, that happened. I'm still on track." | P4 |
| **Buy Day** | "It's Buy Day! 🎉 Still excited about the headphones?" Jordan buys them; the app suggests a match: "Was this your headphones?" Swipe to confirm. | Proud: "I bought this on purpose" | P3 |
| **The lapse** | A busy week passes without opening the app. The jacket's Buy Day passes after its reminder. | Doesn't even notice | — |
| **While away** | The jacket moves to "Kept your patience." No matching purchase appears in the bank data, so it's confirmed, and the money stays in the Pot. Nothing piles up. | — | P4 |
| **Return** | Welcome-back summary: "Your Pot grew $46 while you were away. Phone bill due Friday. Today's Number: $31." Jordan can bring the jacket back in one tap. | "Okay, I'm back." Back in 10 seconds | P4 |
| **End of month** | Recap: "Total Kept: $212. Bought on purpose: headphones. Kept your patience: jacket." | "I got what I wanted and still saved. This works with my brain." | P1–P6 |

**The moments that matter most:**

- **The next-morning confirmation:** real money, a real reward, and visible progress toward something the user wants.
- **Buy Day:** buying becomes a celebration of patience instead of a source of guilt.
- **The return:** a lapse makes the Pot grow instead of creating a backlog.

## How Patiencents Solves Each Pain Point

| Pain Point | Mechanic |
| --- | --- |
| **P1 Setup overwhelm** | Automatic sorting into Bills, Essentials, and Usuals; wishlist items are optional and take one link |
| **P2 Out of sight, out of mind** | Morning notification with Today's Number and the next Buy Day countdown |
| **P3 Impulse purchases** | New wants go to the wishlist with a Buy Day; the Pot rewards every day of patience with real money |
| **P4 Shame after falling off** | Overspending never reduces the Pot; missed Buy Days become "Kept your patience"; welcome-back summary instead of a backlog |
| **P5 Missed bills** | Bill reminders three days before the due date |
| **P6 Abstract budgets** | Today's Number makes the budget daily; Buy Days turn savings into a concrete date |

## Core Loop

1. **Morning:** notification shows Today's Number and the next Buy Day countdown.
2. **During the day:** spend on Usuals; add new wants to the wishlist instead of buying.
3. **Next day:** yesterday's leftover is confirmed and goes into the Pot; the next Buy Day moves closer.
4. **Buy Day:** buy it on purpose, or keep your patience.
5. **After a lapse:** the welcome-back summary, then straight back into the loop.

## Design Principles

1. **The app comes to the user.** Never rely on the user remembering to open it.
2. **Every number is real.** Rewards are backed by bank data, never self-reported.
3. **No backlog, ever.** Missed Buy Days and time away never pile up.
4. **No streaks, no losses.** Total Kept only goes up, and overspending is absorbed quietly.
5. **Not "no," just "later."** Wants are planned, not denied.
6. **Two minutes a day, maximum.** Any feature that needs more effort must justify it.

---

**What this changes in the other documents**

| Document | Change |
| --- | --- |
| **Pain Points and Journeys** | Replace the Future Journey with the one above |
| **Positioning** | New statement built around "patience pays" |
| **MVP scope** | Epic 2 becomes **Patience Pot and Wishlist**; buckets renamed to Bills, Essentials, and Usuals; Park It, Quick Save, and Return Rescue removed (Return Rescue moves to the MMP as a maybe) |
| **KPIs** | Replace Park It skip rate with **Pot growth per user**, **wishlist items added**, and **Buy Day outcomes** (bought on purpose vs. kept your patience) |
| **Epics, Features, and Tasks** | Rewrite Epic 2; update bucket tasks in Epic 1 |
| **Backlog CSV** | Regenerate with the new Epic 2 tasks |

The next step is to update the documents and regenerate the backlog CSV, then build the Patiencents pitch deck.