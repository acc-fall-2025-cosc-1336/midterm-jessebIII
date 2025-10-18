def is_prime(n: int) -> bool:
	"""Return True if n is a prime number, False otherwise.

	Handles n < 2 as non-prime. Uses a simple O(sqrt(n)) check.
	"""
	if n < 2:
		return False
	if n in (2, 3):
		return True
	if n % 2 == 0:
		return False
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True


def test_config():
	return True