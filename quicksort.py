def quicksort(my_tuple):
	if len(my_tuple) < 2: # base case
		return my_tuple
	else: 
		pivot = my_tuple[0]
		for i in my_tuple:
			less = [i for i in my_tuple[1:] if i <= pivot]
			greater = [i for i in my_tuple[1:] if i  > pivot]
	return quicksort(less) + [pivot] + quicksort(greater)

my_tuple = tuple(int(x) for x in input().split(","))
print (quicksort(my_tuple))