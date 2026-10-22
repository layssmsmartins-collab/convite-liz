#!/usr/bin/env python3
"""Idea screen for founder-discover. Standard library only, no network.

Takes the long list of business ideas, each with the scores the screening step
gave it, and ranks them the same way every time: hard kill rules first, then a
weighted score. The ranking is arithmetic on the inputs; the judgement lives in
the scores, and every score must come with its one-line reason.

    python3 screen.py founder/discover/ideas.json
    python3 screen.py founder/discover/ideas.json --out founder/discover/screen.md
    python3 screen.py founder/discover/ideas.json --top 5 --json

The input (see example-ideas.json in this folder):

    budget              the founder's cash for the venture
    ideas               [ ... ] each with:
      id, name          short id ("I03") and a working name
      one_line          what it is and who it is for
      price             price of one unit, before tax
      variable_cost     estimated cost of that unit (product, shipping, fees)
      startup_cost      estimated one-off spend before the first sale
      lenses            {offers, monopoly, product}: 1-10 each, from lenses.md
      fit               1-5: the founder's skills, access and time match it
      gap               1-5: evidence that competitors leave room (linked)
      regulatory        1-5: how heavy licences, claims and compliance are
                        (5 = very heavy)
      reasons           {field: "one line"} for every score above
      kill              optional, a deal-breaker found while screening
"""

import argparse
import json
import sys

WEIGHTS = {"lenses": 0.40, "fit": 0.20, "gap": 0.20, "margin": 0.10, "regulatory": 0.10}
LENSES = ("offers", "monopoly", "product")


class ScreenError(Exception):
    pass


def _num(idea, key):
    try:
        return float(idea[key])
    except (KeyError, TypeError, ValueError):
        raise ScreenError("idea %s: %r must be a number" % (idea.get("id", "?"), key))


def _score(idea, key, lo, hi):
    v = _num(idea, key) if key in idea else None
    if v is None or not lo <= v <= hi:
        raise ScreenError("idea %s: %r must be between %s and %s" % (idea.get("id", "?"), key, lo, hi))
    return v


def evaluate(data):
    budget = float(data["budget"])
    out = []
    for idea in data["ideas"]:
        iid = idea.get("id") or "?"
        lenses = idea.get("lenses") or {}
        if set(LENSES) - set(lenses):
            raise ScreenError("idea %s: lenses needs %s" % (iid, ", ".join(LENSES)))
        for k in LENSES:
            if not 1 <= float(lenses[k]) <= 10:
                raise ScreenError("idea %s: lens %s must be 1-10" % (iid, k))
        fit = _score(idea, "fit", 1, 5)
        gap = _score(idea, "gap", 1, 5)
        reg = _score(idea, "regulatory", 1, 5)
        price, var, startup = _num(idea, "price"), _num(idea, "variable_cost"), _num(idea, "startup_cost")
        if price <= 0:
            raise ScreenError("idea %s: price must be above zero" % iid)
        reasons = idea.get("reasons") or {}
        missing = [k for k in ("offers", "monopoly", "product", "fit", "gap", "regulatory", "variable_cost")
                   if not str(reasons.get(k, "")).strip()]
        if missing:
            raise ScreenError("idea %s: every score needs a one-line reason; missing %s" % (iid, ", ".join(missing)))

        margin = (price - var) / price
        lens_avg = sum(float(lenses[k]) for k in LENSES) / 3
        kills = []
        if margin <= 0:
            kills.append("each sale loses money (price %.2f, cost %.2f)" % (price, var))
        if startup > budget:
            kills.append("startup %.0f is above the budget %.0f" % (startup, budget))
        low = [k for k in LENSES if float(lenses[k]) <= 3]
        if low:
            kills.append("a lens scores 3 or less: %s" % ", ".join(low))
        if fit <= 1:
            kills.append("no founder fit")
        if idea.get("kill"):
            kills.append(str(idea["kill"]))

        # each part on 0..1, higher is better
        parts = {
            "lenses": (lens_avg - 1) / 9,
            "fit": (fit - 1) / 4,
            "gap": (gap - 1) / 4,
            "margin": max(0.0, min(margin, 0.8)) / 0.8,
            "regulatory": (5 - reg) / 4,
        }
        score = round(100 * sum(WEIGHTS[k] * parts[k] for k in WEIGHTS), 1)
        out.append({
            "id": iid, "name": idea.get("name", iid), "one_line": idea.get("one_line", ""),
            "score": score, "lens_avg": round(lens_avg, 1), "margin": round(margin, 3),
            "startup": startup, "fit": fit, "gap": gap, "regulatory": reg,
            "lenses": {k: float(lenses[k]) for k in LENSES}, "kills": kills,
        })
    alive = sorted([r for r in out if not r["kills"]], key=lambda r: -r["score"])
    dead = sorted([r for r in out if r["kills"]], key=lambda r: -r["score"])
    return {"budget": budget, "alive": alive, "killed": dead, "weights": WEIGHTS}


def render(res, top):
    L = ["# Idea screen", "",
         "Ranked by arithmetic on the screening scores (weights: lenses 40%, founder fit 20%, "
         "competitor gap 20%, unit margin 10%, light regulation 10%). Kill rules come first.", ""]
    L += ["| rank | id | idea | score | lenses O/M/P | fit | gap | reg | unit margin | startup |",
          "| ---: | --- | --- | ---: | --- | ---: | ---: | ---: | ---: | ---: |"]
    for i, r in enumerate(res["alive"], 1):
        mark = " **finalist**" if i <= top else ""
        l = r["lenses"]
        L.append("| %d | %s | %s%s | %.1f | %g/%g/%g | %g | %g | %g | %.0f%% | %s |" % (
            i, r["id"], r["name"], mark, r["score"], l["offers"], l["monopoly"], l["product"],
            r["fit"], r["gap"], r["regulatory"], 100 * r["margin"], "{:,.0f}".format(r["startup"])))
    if res["killed"]:
        L += ["", "## Killed", "", "| id | idea | why |", "| --- | --- | --- |"]
        for r in res["killed"]:
            L.append("| %s | %s | %s |" % (r["id"], r["name"], "; ".join(r["kills"])))
    n = min(top, len(res["alive"]))
    L += ["", "**Finalists for the quick panel: %s.**" % (", ".join(r["id"] for r in res["alive"][:n]) or "none")]
    if len(res["alive"]) < 3:
        L.append("Fewer than 3 ideas survive: widen the long list or revisit the constraints before running panels.")
    return "\n".join(L) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("ideas")
    ap.add_argument("--top", type=int, default=5, help="how many finalists (default 5)")
    ap.add_argument("--out")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        with open(a.ideas, encoding="utf-8") as fh:
            res = evaluate(json.load(fh))
    except (OSError, ValueError, KeyError, ScreenError) as e:
        print("screen.py: %s" % e, file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(res, indent=1, ensure_ascii=False))
        return 0
    text = render(res, a.top)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("wrote %s" % a.out)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
