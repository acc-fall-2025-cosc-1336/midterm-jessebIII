"""Interactive program for question D: map numbers 1..7 to weekday names.

Prompts the user repeatedly for a number 1..7 and displays the corresponding
weekday. Displays an error message for numbers outside 1..7. Enter 'q' to quit.
"""

import os
import sys

# Ensure repo root is on sys.path so `src` imports work when running this module
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
	sys.path.insert(0, ROOT)

from src.question_d.question_d import get_day_of_week


def main():
	print("Day-of-week lookup. Enter 'q' to quit.")
	while True:
		s = input("Enter a number (1-7): ")
		if not s:
			continue
		if s.strip().lower() in ("q", "quit", "exit"):
			print("Goodbye.")
			break

		try:
			daynum = int(s)
		except ValueError:
			print("Invalid number")
			continue

		try:
			dayname = get_day_of_week(daynum)
		except ValueError:
			print("Invalid number")
			continue

		print(dayname)


if __name__ == "__main__":
	main()