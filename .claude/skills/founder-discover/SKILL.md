---
name: founder-discover
description: >-
  The founder pack in reverse: finds a business to launch when the founder does
  not have an idea yet. Takes the founder's constraints (money, time, skills,
  access, interests, place), generates 10 to 15 ideas that fit them, screens each
  with the board's three lenses, a competitor check and a quick margin estimate,
  ranks them with a fixed rule, runs a quick buyer panel on 3 to 5 finalists and
  hands the winner to /founder-board. Use when the user says "find me a business",
  "what could I launch", "I have money but no idea", "give me business ideas",
  "que negócio eu posso abrir", "me ajude a encontrar um produto para lançar",
  "quero empreender mas não sei em quê", or asks to run the founder pack
  backwards.
argument-hint: "<constraints, or leave blank to be asked>"
---

# founder-discover

Every other skill in the pack starts from an idea and tries to break it. This one
starts from the founder and works backwards: what can this person, with this
money and this time, credibly launch? The output is not a list of trendy ideas;
it is one idea that survived the same tests the rest of the pack will run, with
the runners-up and why they lost.

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

Ideas are only as good as the constraints they answer. Write
`founder/discover/constraints.md` from the conversation and ask for what is
missing, at most five questions in one message:

- **Money**: the cash available, and how much the founder can lose without harm.
- **Time**: full time or alongside a job; how soon the first sale must happen.
- **Edge**: profession, skills, industry access, an audience, suppliers, a
  language, anything that makes this founder better placed than a stranger.
- **Wants and won'ts**: sectors they like; things they refuse (stock in the
  house, night shifts, regulated health claims, selling to businesses...).
- **Where**: a city (for a physical business) or a country for online.
- **What they liked before**: if the pack ran on an earlier idea, what attracted
  them (the subscription, the audience, premium) and what wore them down.

The edge matters most. An idea that any reader of the same article could start
has no reason to work for this founder; ideas that use their edge do.

## Step 2: the long list

Generate 10 to 15 ideas that fit the constraints, spread across at least four
shapes so the list is not ten versions of one thing: physical product online,
local service, digital product, subscription, B2B service, marketplace or
community, a physical place. For each, in `founder/discover/ideas.md`:

- a working name and one line: what it is, for whom, at what price;
- why this founder (which part of the edge it uses);
- why now (a change in regulation, habit, price or technology), only if there is
  a real one.

Do not invent market sizes or competitors. Where a fact would decide it, write
it as a question for Step 3.

## Step 3: the screen

For every idea, quickly and in one pass (this is a filter, not the full board):

1. **Three lenses**, scored 1 to 10 each, with the method in
   `${CLAUDE_SKILL_DIR}/../founder-board/lenses.md`. Same rule as the board:
   apply the published frameworks, never speak as their authors.
2. **Competitor check**: two or three public searches the way a buyer would
   search. Name the nearest alternatives with a link and score the gap 1 to 5.
   If nothing can be reached, say so and score the gap 2, not higher.
3. **Unit margin**: price and variable cost per unit, each marked as an estimate
   with its basis, plus a rough startup cost. No quote yet is fine; a made-up
   precise number is not.
4. **Founder fit** 1 to 5 and **regulatory weight** 1 to 5 (5 = heavy:
   licences, health or financial claims, certifications).

Write every score with a one-line reason into `founder/discover/ideas.json`
(shape: `example-ideas.json` in this folder) and run the tool. It applies the
kill rules (a unit that loses money, a startup above the budget, any lens at 3
or less, no founder fit, a deal-breaker you found) and ranks the rest. The
ranking is arithmetic; argue with the scores, never with the order. If fewer
than three ideas survive, go back to Step 2 with what killed the others.

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
   phone call, one quote, one search).

The panel is simulated buyers, so the buy rates rank finalists; they do not
forecast sales. Say that once.

## Step 6: hand off

With the user's go-ahead (and Step 0 respected), write `founder/idea.md` for the
winner in the shape `/founder-board` expects, copy its `customer.json` and
`pitch.md` into `founder/`, and suggest `/founder-board` next. The rest of the
pack then runs on it as usual: board, competitors, consumer, pricing, offer,
cfo, marketing, brand, ops, launch, plan.

## Rules

- Ideas fit the founder, not the headlines. Each one names the edge it uses.
- No made-up facts: competitors, prices and regulations come with links or are
  marked as questions.
- Kill rules are applied by the tool, not softened by hand.
- Steer clear of ideas whose main risk is legal or harmful to others; flag
  regulated sectors (health, finance, food, children) with their regulator.
- Not financial, legal or tax advice.

## Output

`founder/discover/` (constraints, ideas, ideas.json, screen, one panel folder per
finalist, decision) and, after hand-off, `founder/idea.md`. Next:
`/founder-board`.
