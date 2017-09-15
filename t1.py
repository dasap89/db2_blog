# Example:
# number1 = 1
# number2 = 10
# number3 = 2
# 
# Result: 
# 5, because 2, 4, 6, 8, 10 are divisible by 2

def handle_numbers(number1, number2, number3):
	result = [x for x in range(number1, number2 + 1) if x % number3 == 0]
	return len(result)

number1 = 1
number2 = 10
number3 = 2

if __name__ == '__main__':
	print(handle_numbers(number1, number2, number3))
