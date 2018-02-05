print ("Give numbers seperated by comma")
input_list = sorted(tuple(int(x) for x in input().split(","))) 

def binary_search(input_list, item):
	high = len(input_list) - 1
	low = 0
	steps = 0

	while low <= high:
		middle = (low + high)//2
		guess = input_list[middle]
		if guess < item: 
			low = middle + 1
			steps = steps + 1
		else: 
			high = middle - 1
			steps = steps + 1
		if guess == item:
			return middle
	return "Doesn't exist in the list"

print(binary_search(input_list, int(input("Search for a number: "))))
