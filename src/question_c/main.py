import os
import sys

# Ensure repo root is on sys.path so `src` imports work when running this module
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if ROOT not in sys.path:
	sys.path.insert(0, ROOT)

from src.question_c.question_c import get_random_number


def main():
	print("Guess the number game (1-5). Enter 'q' to quit.")
	number = get_random_number()
	while True:
		s = input("Enter your guess (1-5): ")
		if not s:
			continue
		if s.strip().lower() in ("q", "quit", "exit"):
			print("Goodbye.")
			break

		try:
			guess = int(s)
		except ValueError:
			print("Please enter an integer between 1 and 5, or 'q' to quit.")
			continue

		if guess < 1 or guess > 5:
			print("Please guess a number between 1 and 5.")
			continue

		if guess == number:
			print("Congratulations! You guessed it.")
			number = get_random_number()
			continue
		else:
			print("Sorry, try again.")


if __name__ == "__main__":
	main()