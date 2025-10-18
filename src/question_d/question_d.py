def get_day_of_week(day: int) -> str:
	"""Return the weekday name for a number in 1..7.

	1 -> Monday
	2 -> Tuesday
	3 -> Wednesday
	4 -> Thursday
	5 -> Friday
	6 -> Saturday
	7 -> Sunday

	Raises ValueError if day is not in 1..7.
	"""
	days = {
		1: "Monday",
		2: "Tuesday",
		3: "Wednesday",
		4: "Thursday",
		5: "Friday",
		6: "Saturday",
		7: "Sunday",
	}
	try:
		return days[int(day)]
	except (KeyError, ValueError, TypeError):
		raise ValueError("Day must be an integer in the range 1..7")


def test_config():
	return True
