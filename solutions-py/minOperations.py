'''
Problem:
Given an integer array 'arr', find the minimum number of integer divisions by 'd' such that there are
'threshold' number of identical elements.

Example:
arr = [1,2,3,4,5], threshold = 3, d = 2

2 // 2 = 1
3 // 2 = 1

newarray = [1,1,1,4,5]
There are 3 values of 2 after doing 2 integer divisions. Return the number of integer divisions 
performed (2)


Solution:

Use dictionaries to keep track of two factors:
1) The quotients and the number of processes to get to it
2) The quotients and the number of integer divisions to get to it


I define a process as a sequence of divions that reduces a number to another number
e.g.
arr=[2, 8, 17], threshold=3, d=2

There is one process that can take 8 to 2: 
8 // 2 = 4
4 // 2 = 2
There were two divisions done to get here.

There is another that can take 16 to 2:
17 // 2 = 8
8 // 2 = 4
4 // 2 = 2
There were three divisions done to get here.

There are two processes that reduce us to 2
The total number of steps across the processes = 5
Return the value 5
'''

def minOperations(arr, threshold, d):
	n = len(arr)

	# Create unique quotients
	unique = {x: 0 for x in set(arr)}

	# Initialize steps to quotient
	to_reduced_form = dict(unique)

	# Load starting count for each value
	for x in arr:
		unique[x] += 1

	i = 0
	while threshold not in unique.values():
		# Reset if we reach end of list
		if i == n:
			i = 0

		# Find the quotient
		div = arr[i] // d

		if div in unique.keys():
			# If the quotient is a pre-existing value, include that there is one more process that integer
			# divides into the value 'div'
			unique[div] += 1
			# Include the number of steps in that process to reach the value
			to_reduced_form[div] += 1 + to_reduced_form[arr[i]]
		else:
			# If the quotient is not seen before, create a new key: value and note that there is one process
			# that reaches it
			unique[div] = 1
			# Include the number of steps in that process to reach 'div'
			to_reduced_form[div] = 1 + to_reduced_form[arr[i]]

		# Update the array value to reflect that it has been divided
		arr[i] = div
		i += 1

	# 'unique' and 'to_reduced_form' grew together, so we can restrict our search to the pertinent dict.values()
	# arrays because their indexes are aligned

	# Get the index of the value that equals threshold
	k = list(unique.values()).index(threshold)
	to_reduced_form = list(to_reduced_form.values())

	# Return the number of steps to get to the threshold
	return to_reduced_form[k]

