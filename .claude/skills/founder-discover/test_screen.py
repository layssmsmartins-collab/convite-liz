"""Tests for screen.py. Run: python3 -m unittest test_screen (from this folder)."""
import copy
import json
import os
import unittest

import screen

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "example-ideas.json"), encoding="utf-8") as fh:
    EXAMPLE = json.load(fh)


def first(data):
    return data["ideas"][0]


class ScreenTest(unittest.TestCase):
    def test_example_ranks_and_kills(self):
        res = screen.evaluate(copy.deepcopy(EXAMPLE))
        self.assertEqual([r["id"] for r in res["alive"]], ["I01"])
        kills = res["killed"][0]["kills"]
        self.assertTrue(any("fad" in k for k in kills))
        self.assertTrue(any("monopoly" in k for k in kills))

    def test_losing_unit_is_killed(self):
        data = copy.deepcopy(EXAMPLE)
        first(data)["variable_cost"] = 200
        self.assertFalse(screen.evaluate(data)["alive"])

    def test_regulated_without_contract_manufacturer_is_killed(self):
        data = copy.deepcopy(EXAMPLE)
        first(data)["regulatory_outsourced"] = False
        res = screen.evaluate(data)
        self.assertTrue(any("contract manufacturer" in k for k in res["killed"][0]["kills"]))

    def test_paid_ads_only_is_killed(self):
        data = copy.deepcopy(EXAMPLE)
        first(data)["needs_paid_ads"] = True
        self.assertFalse(screen.evaluate(data)["alive"])

    def test_gatekeeper_is_killed(self):
        data = copy.deepcopy(EXAMPLE)
        first(data)["gatekeeper"] = True
        res = screen.evaluate(data)
        self.assertTrue(any("third party" in k for k in res["killed"][0]["kills"]))

    def test_demand_above_2_needs_a_link(self):
        data = copy.deepcopy(EXAMPLE)
        first(data)["reasons"]["demand"] = "It is growing a lot"
        with self.assertRaises(screen.ScreenError):
            screen.evaluate(data)

    def test_missing_reason_is_refused(self):
        data = copy.deepcopy(EXAMPLE)
        del first(data)["reasons"]["virality"]
        with self.assertRaises(screen.ScreenError):
            screen.evaluate(data)

    def test_score_out_of_range_is_refused(self):
        data = copy.deepcopy(EXAMPLE)
        first(data)["repeat"] = 9
        with self.assertRaises(screen.ScreenError):
            screen.evaluate(data)

    def test_demand_weighs_most(self):
        data = copy.deepcopy(EXAMPLE)
        base = screen.evaluate(copy.deepcopy(data))["alive"][0]["score"]
        first(data)["demand"] = 5
        first(data)["reasons"]["demand"] += " https://example.com/more"
        self.assertGreater(screen.evaluate(data)["alive"][0]["score"], base)


if __name__ == "__main__":
    unittest.main()
