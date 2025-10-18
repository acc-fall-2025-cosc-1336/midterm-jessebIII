"""Unit tests for question A functions."""
import os
import sys
import unittest


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.question_a.question_a import (
    test_config,
    get_assessment_value,
    get_tax_assessed,
)


class TestQuestionA(unittest.TestCase):
    def test_question_a_config(self):
        self.assertTrue(test_config())

    # get_assessment_value tests
    def test_get_assessment_value_10000(self):
        self.assertEqual(get_assessment_value(10000), 6000)

    def test_get_assessment_value_20000(self):
        self.assertEqual(get_assessment_value(20000), 12000)

    # get_tax_assessed tests
    def test_get_tax_assessed_6000(self):
        # 72 cents per $100 on $6000 -> (6000/100) * 0.72 = 60 * 0.72 = 43.2
        self.assertAlmostEqual(get_tax_assessed(6000), 43.2, places=2)

    def test_get_tax_assessed_10000(self):
        # (10000/100) * 0.72 = 100 * 0.72 = 72.0
        self.assertAlmostEqual(get_tax_assessed(10000), 72.0, places=2)


if __name__ == "__main__":
    unittest.main()


