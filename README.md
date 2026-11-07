# Gap Finder

**Lane 3: Fund it.** Does it pencil, and who closes the gap?

**In one line:** For one affordable ownership home, derive the family's income-capped price from the state formula, show which income table it used and when, and show how a rate change or a gift moves the gap.

## Real user
> TODO before submitting: replace with one real person from your room (a nonprofit finance lead, development director or donor). Add what they do today and what changes.
>
> Test persona from the lab repo (made up, not a real person): a finance lead who says "I'm $95k short per home. Rates went up. How much bigger is the gap now?" **Before:** rebuild a spreadsheet by hand for each rate or table change. **After:** change one number and see the family price, the gap and the dollar change at once.

## Run it
Open `index.html` in a browser. No install, no keys, no personal data. Optional Claude memo: use "Download scenario," then `pip install anthropic`, set `ANTHROPIC_API_KEY` (never commit it) and run `python memo.py scenario.json`.

## How it works
Family price + public subsidies + rent earned + stacked sources + fundraising gap = cost to create.
1. Max monthly housing cost = income percentage x area median income x household-size factor / 12 (Health and Safety Code 50052.5: very low 30% x 50%; lower 30% x 70%; moderate 35% x 110%).
2. Subtract insurance and HOA. Solve the price whose mortgage payment plus property tax fits what is left, at the chosen rate and down payment.
3. Gap = cost minus family price, subsidies, rent earned and any sources entered.
4. A rate table recomputes steps 1 to 3 at other rates, including the 7.40% (2026-10-08) rate.
5. The income-table selector warns when a replaced table is chosen, and when the separate HOME table is chosen.
6. The donor panel shows what share of the gap a gift covers.
7. "Homes in project" scales the gap to a 4 to 12 home project, and a chart shows the gap per home at each rate.
8. In the live demo link, "Ask Claude" writes a funder memo or donor note from the scenario, using only its numbers.

## Honesty rules
- Funding sources start at $0. Anything entered is flagged until the funds are confirmed. Forgivable Equity Builder is not modeled (unverified, reported winding down). Dream For All is marked unconfirmed.
- The default deal is the lab's synthetic example. It is not a real project. Cost, subsidy and rent lines are assumptions.

## Sources
- Health and Safety Code 50052.5 (formula) and the lab data-sources file (checked Nov 6, 2026).
- Freddie Mac 30-year rate: 7.18% on 2026-11-05 and 7.40% on 2026-10-08 (FRED MORTGAGE30US, as listed in the lab data sources).
- HCD 2026 State Income Limits (revised June 23, 2026) and State HOME limits (effective June 1, 2026), as listed in the lab data sources.
- 4-person AMI $138,600: derived from the Irvine Company's published 2026 Orange County 120% limit ($166,300) / 1.2. Not read from the HCD PDF. Confirm.
- Program pages: HCD CalHome and HOSN, FHLBank SF AHP and WISH, CalHFA, Santa Ana (statuses from the lab data sources).

## Assumptions
Down payment 5%, property tax 1.1%, insurance $2,400/yr, HOA $200/mo, 30-year term, no mortgage insurance. The affordable-price calculation uses the target income, not the buyer's own income, and does not apply the 28%-of-gross-income floor.

## Next 100 projects
The same inputs describe any project. Next steps: load a CSV of projects to rank them by gap per home, add real program amounts and round dates once confirmed, and connect to the Freddie Mac rate file for automatic updates.

## License
MIT
