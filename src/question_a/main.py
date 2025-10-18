"""Interactive program for question A.

Prompts the user for the actual property value repeatedly and displays
the assessment value and property tax until the user decides to quit.
"""

import os
import sys

# Ensure the repository root is on sys.path so `src` is importable when running this module directly
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
	sys.path.insert(0, ROOT)

from src.question_a.question_a import get_assessment_value, get_tax_assessed


def main():
	print("Property tax calculator. Enter 'q' to quit.")
	while True:
		user = input("Enter the actual value of the property: $")
		if not user:
			continue
		if user.strip().lower() in ("q", "quit", "exit"):
			print("Goodbye.")
			break

		try:
			actual_value = float(user)
		except ValueError:
			print("Please enter a numeric value or 'q' to quit.")
			continue

		assessment = get_assessment_value(actual_value)
		tax = get_tax_assessed(assessment)

		print(f"assessment value:  ${assessment:.2f}")
		print(f"property tax: ${tax:.2f}")


if __name__ == "__main__":
	main()