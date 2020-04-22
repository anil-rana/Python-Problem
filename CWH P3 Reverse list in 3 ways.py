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

reverse1 = mylist[:]  # [:] is used so that copy of mylist save in reverse1 list. if not use this and we reverse reverse1 list then with this mylist also reverse automatically so for solve this we use [:]
reverse1.reverse()
print(f"My first reversed list of {mylist} is {reverse1}")


# Slicing technique for reverse list.
reverse2 = mylist[::-1]
print(f"My second reversed list of {mylist} is {reverse2}")


# Third reverse technique..........>
reverse3 = mylist[:]
for i in range(len(reverse3)//2): # (// is floor division operator) if we not devide len(reverse3) by 2 then it again reverse the list and give same list as input.
	reverse3[i], reverse3[len(reverse3) -i-1] = reverse3[len(reverse3) -i-1], reverse3[i]
	# print(f"The reverse list at i={i} is {reverse3}")

print(f"My third reversed list of {mylist} is {reverse3}\n")

if reverse1 == reverse2 and reverse2 == reverse3:
	print("All three method give same results")

