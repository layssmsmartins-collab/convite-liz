---
name: founder-discover
description: >-
  The founder pack in reverse: finds a business to launch when the founder does
  not have an idea yet. Takes the founder's constraints (money, reserve, time,
  skills, interests, regulation they accept), looks for products and brands that
  grew steadily in the US (not one viral spike) and match Brazil, screens each
  for sustained demand, virality and community, the board's three lenses, Brazil
  fit, repeat purchase and margin, ranks them with a fixed rule, runs a quick
  buyer panel on 3 to 5 finalists and hands the winner to /founder-board. Use
  when the user says "find me a business", "what could I launch", "I have money
  but no idea", "give me business ideas", "find a viral product to model",
  "que negócio eu posso abrir", "me ajude a encontrar um produto para lançar",
  "produto viral nos EUA para trazer ao Brasil", "quero empreender mas não sei
  em quê", or asks to run the founder pack backwards.
argument-hint: "<constraints, or leave blank to be asked>"
---

# founder-discover

Every other skill in the pack starts from an idea and tries to break it. This one
starts from the market and the founder and works backwards: what is already
selling, growing for years rather than spiking, and could be launched by this
person, with this money and this time, as a premium brand of their own? The
output is one idea that survived the same tests the rest of the pack will run,
with the runners-up and why they lost.

What the user typed after `/founder-discover`: `$ARGUMENTS`.

Tool in this folder:

```bash
python3 "${CLAUDE_SKILL_DIR}/screen.py" founder/discover/ideas.json --out founder/discover/screen.md
```

(If `${CLAUDE_SKILL_DIR}` is not expanded, use the base directory Claude Code
printed for this skill.) State lives in `founder/discover/`.

## Step 0: do not overwrite a live project

If `founder/idea.md` already exists, another idea is being worked on. Before
writing anything outside `founder/discover/`, ask whether to archive it (move
`founder/` contents except `discover/` to `founder-archive/<working-name>/`) or
to keep discovering without handing off. Never delete a previous project.

## Step 1: the founder's constraints

Write `founder/discover/constraints.md` from the conversation and ask for what
is missing, at most five questions in one message:

- **Money and reserve**: the cash available and how much must stay untouched as
  a reserve. The screen's `budget` is cash minus reserve: the most the startup
  can cost. If this is all the founder's money, say so and keep the reserve.
- **Time**: full time or alongside a job; working windows; how soon the first
  sale must happen.
- **Edge**: profession, skills, access, an audience, suppliers. Here it decides
  what the founder can *run*, not what they should *sell*: market evidence
  chooses the product, the edge only rules out what they cannot operate.
- **Wants and won'ts**: own brand or not, premium or not, physical store or
  online only, stock at home, B2B selling, a personal brand (if the business
  must not depend on the founder's face, community has to be brand-led: creators,
  customers' own content, a ritual, not the founder on camera).
- **Regulation accepted**: none, or regulated categories only when a contract
  manufacturer holds the licence or notification (for example a grade 1
  cosmetic notified by the manufacturer). Record which.
- **Where**: a country or city.

## Step 2: the long list (modelling, by default)

Start from evidence, not imagination. Look for products and brands that grew
in the US over the last two to five years and could be modelled for Brazil
(a new brand of your own built on the same insight, never a copy of a name,
look or formula):

1. **Where to look**: fast-growing DTC brands in the news (revenue, funding,
   acquisitions, retail launches), TikTok Shop and Amazon best-seller and
   movers lists, Kickstarter and Product Hunt hits that became companies,
   consumer trend reports. Two to four searches per category the founder accepts.
2. **Keep only sustained growth**: several years of growth, repeat customers, a
   category that keeps getting new brands. One viral video, a holiday peak or a
   celebrity spike is a fad: note it and drop it.
3. **Check the Brazil match**: is anyone searching for it here, is it on
   Brazilian marketplaces, is there already a strong premium local brand, can it
   be made or imported at a price Brazilian premium buyers pay, and can the
   regulation sit with a contract manufacturer.

Write 10 to 15 ideas in `founder/discover/ideas.md`, each with: a working name
and one line (what, for whom, at what price); **the model** (the US brand or
product, with a link); the evidence of sustained demand (links); the Brazil
signal; how it spreads without paid media (the video it makes, the community or
ritual around it); and why this founder can run it. Give a Google Trends link
for the US and for Brazil so the founder can check the curve; this environment
cannot read Trends itself, so never claim a curve you have not seen.

If the founder asks for ideas from their own edge instead, generate those the
same way, but still screen them on demand evidence.

## Step 3: the screen

For every idea, in one pass (a filter, not the full board):

1. **Sustained demand** 1 to 5. Above 2 only with a linked source (revenue
   growth over years, repeat purchase data, a steadily growing category). Mark
   `spike: true` if it rose and already fell.
2. **Virality and community** 1 to 5: does it show itself in a few seconds of
   video, do customers make their own content, does it carry an identity, a
   hobby or a daily ritual people talk about? Mark `needs_paid_ads: true` if it
   only sells through paid media.
3. **Who decides the purchase**: mark `gatekeeper: true` when the buyer will
   not buy without someone else's approval (a paediatrician for children's
   supplements, a nutritionist, a school, an employer). Winning those people
   is medical or institutional marketing: sales teams, samples, studies, years.
   A small budget cannot pay for it, so the tool kills the idea.
4. **Three lenses** 1 to 10 each, with the method in
   `${CLAUDE_SKILL_DIR}/../founder-board/lenses.md`. Apply the published
   frameworks, never speak as their authors.
5. **Brazil fit** 1 to 5: local demand signals and room for a premium brand.
   Name the nearest local alternatives with links. If nothing could be reached,
   say so and score 2, not higher.
6. **Repeat purchase** 1 to 5: consumables, refills and collections compound;
   one-off purchases have to win a new customer every time.
7. **Unit margin**: price and variable cost, each marked as an estimate with its
   basis, plus a rough startup cost (first batch, development, brand, launch).
8. **Founder fit** 1 to 5 (kill rule only) and **regulatory weight** 1 to 5,
   with `regulatory_outsourced: true` when a contract manufacturer holds the
   licence or notification.

Write every score with a one-line reason into `founder/discover/ideas.json`
(shape: `example-ideas.json` in this folder) and run the tool. It kills ideas
that lose money per unit, cost more than the budget, score 3 or less on a lens,
cannot be run by the founder, are fads, sell only through paid media, need a
third party's approval to be bought, or need a
licence that cannot sit with a manufacturer. It ranks the rest with fixed
weights: sustained demand 25%, virality and community 20%, lenses 20%, Brazil
fit 15%, repeat 10%, margin 5%, light regulation 5%. The ranking is arithmetic;
argue with the scores, never with the order. If fewer than three survive, go
back to Step 2 with what killed the others.

## Step 4: quick panels on the finalists

Show the user the screen (the top 5 and why the others died) and let them strike
or add finalists before spending sub-agents. Then, for 3 to 5 finalists, run the
consumer panel exactly as `/founder-consumer --quick` does, each in its own
folder so nothing collides:

```bash
python3 "${CLAUDE_SKILL_DIR}/../founder-consumer/panel.py" --dir founder/discover/<id>/panel init \
  --customer founder/discover/<id>/customer.json --pitch founder/discover/<id>/pitch.md --n 20 --seed <same seed for all>
```

then `prompts`, the waves, `check` and `tally`, following that skill's rules (one
sub-agent per buyer, never answer for a buyer). Use the same seed and the same
pitch length for every finalist so the comparison is fair. Tell the user first
that this is 20 sub-agent calls per finalist, and suggest three finalists if
cost matters.

## Step 5: pick one

Write `founder/discover/decision.md`:

1. A table of the finalists: screen score, panel buy rate, the top reason buyers
   pass, the price buyers called "getting expensive", unit margin, startup.
2. **The pick**, and why: the panel result first, then the screen. If the best
   panel buy rate is under 15%, say plainly that no finalist convinced simulated
   buyers and recommend widening the list or changing a constraint rather than
   forcing a pick.
3. **The runner-up** and what would have to be true for it to win.
4. What the founder should check this week that would change the pick (one
   phone call, one quote, one look at the Trends curve).

The panel is simulated buyers, so the buy rates rank finalists; they do not
forecast sales. Say that once.

## Step 6: hand off

With the user's go-ahead (and Step 0 respected), write `founder/idea.md` for the
winner in the shape `/founder-board` expects, copy its `customer.json` and
`pitch.md` into `founder/`, and suggest `/founder-board` next. The rest of the
pack then runs on it as usual: board, competitors, consumer, pricing, offer,
cfo, marketing, brand, ops, launch, plan.

## Rules

- Evidence picks the product; the founder's edge only rules out what they
  cannot run.
- Model the insight, never the brand: no copied names, logos, packaging,
  formulas or claims.
- No made-up facts: growth numbers, competitors, prices and regulations come
  with links or are marked as questions.
- Kill rules are applied by the tool, not softened by hand.
- Steer clear of ideas whose main risk is legal or harmful to others; flag
  regulated sectors (health, cosmetics, food, children) with their regulator.
- Not financial, legal or tax advice.

## Output

`founder/discover/` (constraints, ideas, ideas.json, screen, one panel folder per
finalist, decision) and, after hand-off, `founder/idea.md`. Next:
`/founder-board`.
