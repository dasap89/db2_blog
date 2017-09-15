# Result:
# Letters -  10
# Digits -  3

def handle_string(value):
	digits = [x for x in value if x.isdigit()]
	letters = [x for x in value if x.isalpha()]

	return "Letters - {}\nDigits - {}".format(len(letters), len(digits))

value = "Hello world! 123!"


if __name__ == '__main__':
	print(handle_string(value))
