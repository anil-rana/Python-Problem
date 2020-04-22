
def matchingWrods(sentence1, sentence2):
	words1 = sentence1.split(" ")
	words2 = sentence2.split(" ")
	score = 0

	for word1 in words1:
		for word2 in words2:
			if word1.lower() == word2.lower():
				score += 1
	return score


if __name__ == '__main__':
	# mathingWords("This is good", "python is good")  # call the function.

	sentences = ["python is a good", "this is snake", "anil is a good boy", "Subscribe to code with anil"]

	query = input("Please enter the query string:\n")
	scores = [matchingWrods(query, sentence) for sentence in sentences]
	# print(scores)
	sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse= True)]  # here reverse = True short the list in reverse order.
	# print(sortedSentScore)  # O/P is ---> [(2, 'python is a good'), (1, 'anil is a good boy'), (0, 'this is snake'), (0, 'Subscribe to code with anil')]


	print(f"{len(sortedSentScore)} results found!\n")

	for score, item in sortedSentScore:
		print(f" \"{item}\": with a score of {score}")


	# print(sorted(zip(scores, sentences)))
	# a = [1, 2, 3]
	# b = [4, 5, 6]
	# sorted(zip(a, b)) = [(1,4), (2,5), (3,6)]  # by default short from a.
	# print(sorted(zip(a, b)))



