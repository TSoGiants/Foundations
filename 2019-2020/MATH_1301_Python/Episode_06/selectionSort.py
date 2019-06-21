### List Initialization

from numpy import random

LENGTH = 12

list = []

for num in range(LENGTH):
	list.append(random.randint(100))

print("Unsorted List:")
print(list)
print()
### Beginning of Selection Sort Algorithm

for i in range(0, len(list)-1):
	min = i	# Assume that element i is the smallest.
	for j in range(i+1, len(list)):
		if list[min] > list[j]:
			min = j # We found a smaller element.
	# Swap list elements.
	temp = list[min]
	list[min] = list[i]
	list[i] = temp
	
print("Sorted List:")
print(list)
	
	
	