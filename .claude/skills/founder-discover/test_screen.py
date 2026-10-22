"""Tests for screen.py. Run: python3 -m unittest test_screen (from this folder)."""
import copy
import json
import os
import unittest

import screen

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE, "example-ideas.json"), encoding="utf-8") as fh:
    EXAMPLE = json.load(fh)


class ScreenTest(unittest.TestCase):
    def test_example_ranks_and_kills(self):
        res = screen.evaluate(copy.deepcopy(EXAMPLE))
        self.assertEqual([r["id"] for r in res["alive"]], ["I01"])
        self.assertEqual(res["alive"][0]["score"], 44.9)
        kills = res["killed"][0]["kills"]
        self.assertTrue(any("above the budget" in k for k in kills))
        self.assertTrue(any("monopoly" in k for k in kills))

    def test_losing_unit_is_killed(self):
        data = copy.deepcopy(EXAMPLE)
        data["ideas"][0]["variable_cost"] = 200
        res = screen.evaluate(data)
        self.assertFalse(res["alive"])

    def test_missing_reason_is_refused(self):
        data = copy.deepcopy(EXAMPLE)
        del data["ideas"][0]["reasons"]["gap"]
        with self.assertRaises(screen.ScreenError):
            screen.evaluate(data)

    def test_score_out_of_range_is_refused(self):
        data = copy.deepcopy(EXAMPLE)
        data["ideas"][0]["fit"] = 9
        with self.assertRaises(screen.ScreenError):
            screen.evaluate(data)


if __name__ == "__main__":
    unittest.main()
