### List Initialization

from numpy import random

LENGTH = 12

list = []

for num in range(LENGTH):
	list.append(random.randint(100))

	
print("Unsorted List:")
print(list)
print()
### Beginning of Bubble Sort Algorithm
count = 0
for j in range(len(list)-1, 0, -1):
	done = True # Maybe we're done?
	for i in range(0, j):
		if(list[i+1] < list[i]):
			# Swap list elements.
			temp = list[i]
			list[i] = list[i+1]
			list[i+1] = temp
			done = False # I guess we aren't done.
	count += 1
	if(done):
		break
print("Sorted List:")
print(list)
print("Sorted in " + str(count) + " iterations.")
		
		
		
		