print("Enter the number of the lsit one by one\n")

# Take the size of list from the user
size = int(input("Enter size of list\n"))

# Initialize the blank list
mylist = []

# Take the input from the user one by one
for i in range(size):
	mylist.append(int(input(f"Enter {i+1} list element\n")))

# mylist = [7, 3, 2, 1]
print(f"Your list is {mylist}\n")


new_list = []
for i in range(len(mylist)):
	if mylist[i] <= 10:
		new_list.append(mylist[i])

	else:
		while True:
			n = mylist[i] + 1
			if str(n) == str(n)[::-1]:
				new_list.append(n)
				break

print(f"Your New list is {new_list}\n")





