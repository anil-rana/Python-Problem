def next_palindrome(n):
	n = n + 1
	while not is_palindrome(n): # As is_palindrome(n) function return False so 'while not False' mean True due to which while loop run again and again but
		n += 1                  # as is_palindrome(n) functoin return True so 'while not True' mean False due to next_palindrome(n) function return next palindrome number.
	return n

def is_palindrome(n):
	return str(n) == str(n)[::-1]  # We can't use 'n1 == n1[::-1]' here because int object can't be reverse so 1st it bcame string then revers.
                                   # here 'str(n1) == str(n1)[::-1] return True when both n1 and reverse of n1 is equal.

if __name__ == '__main__':
	n = int(input("Enter the number of test cases:\n"))
	numbers = []

	for i in range(n):
		number = int(input(f"Enter the {i+1} number:\n"))
		numbers.append(number)

	print(numbers)

	for i in range(n):
		print(f"Next Palindrome number for {numbers[i]} is {next_palindrome(numbers[i])}") # call next_palindrome(n) function here.


             ############################## (or) #############################################

# def next_palindrome(n):
# 	while True:
# 		n += 1
# 		if str(n) == str(n)[::-1]:
# 			break
# 	return n
#
#
# if __name__ == '__main__':
# 	n = int(input("Enter the number of test cases:\n"))
# 	numbers = []
#
# 	for i in range(n):
# 		number = int(input(f"Enter the {i+1} number:\n"))
# 		numbers.append(number)
#
# 	print(numbers)
#
# 	for i in range(n):
# 		print(f"Next Palindrome number for {numbers[i]} is {next_palindrome(numbers[i])}") # call next_palindrome(n) function here.


