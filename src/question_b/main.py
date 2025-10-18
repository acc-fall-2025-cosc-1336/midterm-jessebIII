

import os
import sys

# Ensure repo root is on sys.path so `src` imports work when running this module
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
	sys.path.insert(0, ROOT)

from src.question_b.question_b import is_prime


def main():
	print("Prime checker. Enter 'q' to quit.")
	while True:
		s = input("Enter an integer: ")
		if not s:
			continue
		if s.strip().lower() in ("q", "quit", "exit"):
			print("Goodbye.")
			break

		try:
			n = int(s)
		except ValueError:
			print("Please enter a valid integer or 'q' to quit.")
			continue

		result = is_prime(n)
		print(f"{n} is {'a prime' if result else 'not a prime'}.")


if __name__ == "__main__":
	main()