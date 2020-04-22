try:
	apples = int(input("Enter the number of Apples: "))

	min_number = int(input("Enter the minimum number of studnet: "))
	max_number = int(input("Enter the maximum number os student: "))

except ValueError:
	print("Please Enter integer value only")
	exit()

if min_number == max_number:
	print(f"This is not a range as {min_number} is equal to {max_number}")

	if apples % min_number == 0:
		print(f"{min_number} is divisor of {apples}")
	else:
		print(f"{min_number} is not divisor of {apples}")

	exit()

if min_number > max_number:
	print(f"This is not a range as {min_number} is greater than {max_number}")

	if apples % min_number == 0:
		print(f"{min_number} is divisor of {apples}")
	else:
		print(f"{min_number} is not divisor of {apples}")

	exit()


for range_number in range(min_number, max_number+1):
	if apples % range_number == 0:
		print(f"{range_number} is divisor of {apples}")
	# else:
	# 	print(f"{range_number} is not divisor of {apples}")


