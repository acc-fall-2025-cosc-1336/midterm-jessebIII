
import os
import sys
import unittest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from src.question_a.question_a import (
    test_config as test_a_config,
    get_assessment_value,
    get_tax_assessed,
)
from src.question_b.question_b import (
    test_config as test_b_config,
    is_prime,
)


class TestQuestionA(unittest.TestCase):
    def test_question_a_config(self):
        self.assertTrue(test_a_config())

    # get_assessment_value tests
    def test_get_assessment_value_10000(self):
        self.assertEqual(get_assessment_value(10000), 6000)

    def test_get_assessment_value_20000(self):
        self.assertEqual(get_assessment_value(20000), 12000)

    # get_tax_assessed tests
    def test_get_tax_assessed_6000(self):
        self.assertAlmostEqual(get_tax_assessed(6000), 43.2, places=2)

    def test_get_tax_assessed_10000(self):
        self.assertAlmostEqual(get_tax_assessed(10000), 72.0, places=2)


class TestQuestionB(unittest.TestCase):
    def test_question_b_config(self):
        self.assertTrue(test_b_config())

    def test_is_prime_4(self):
        self.assertFalse(is_prime(4))

    def test_is_prime_5(self):
        self.assertTrue(is_prime(5))

    def test_is_prime_11(self):
        self.assertTrue(is_prime(11))



from src.question_c.question_c import test_config as test_c_config, get_random_number
from src.question_d.question_d import test_config as test_d_config, get_day_of_week


class TestQuestionC(unittest.TestCase):
    def test_question_c_config(self):
        self.assertTrue(test_c_config())

    def test_get_random_number_range(self):
        # Non-deterministic: check that the result is an int and in the correct range
        n = get_random_number()
        self.assertIsInstance(n, int)
        self.assertGreaterEqual(n, 1)
        self.assertLessEqual(n, 5)


class TestQuestionD(unittest.TestCase):
    def test_day_0_invalid(self):
        with self.assertRaises(ValueError):
            get_day_of_week(0)

    def test_day_1_monday(self):
        self.assertEqual(get_day_of_week(1), "Monday")

    def test_day_2_tuesday(self):
        self.assertEqual(get_day_of_week(2), "Tuesday")

    def test_day_3_wednesday(self):
        self.assertEqual(get_day_of_week(3), "Wednesday")

    def test_day_8_invalid(self):
        with self.assertRaises(ValueError):
            get_day_of_week(8)


if __name__ == "__main__":
    unittest.main()

