'''
Problem:
A gym manager is trying to pair dumbbells. You are given a frequency array. This array means the index equals
(dumbbell_weight - 1) and the value equals number_of_dumbbells. The manager is okay with mixing weights, so
long as the weight difference is no more than 1 (e.g. a 14lb dumbbell can be matched with a 15lb dumbbell and
a 15lb dumbbell with a 16lb dumbbell). How many of these pairs can you make?

Example:
freq = [3,2,3,2]
1lb: 3
2lb: 2
3lb: 3
4lb: 2

These can be paired as [[1,1], [1,2], [2,3], [3,3], [4,4]], which means we have 5 pairs.


Solution:
Given a continuous array (i.e. there are no 0's for values), the number of pairs is equal to the integer
division of the sum. If there is a discontinuous array, the number of pairs is equal to the integer division
of the sum of all subarrays that are continuous.

e.g. [1,1,1,0,2,3,1]
For weights 1lb through 3lb, we can make only 1 pair: sum([1,1,1]) // 2
For weights 5lb through 7lb, we can make 3 pairs: sum([2,3,1]) // 2

This gives us a total of 4 pairs.
[[1,2], [5,5], [6,6], [6,7]]

'''

def taskOfPairing(freq):
	# Initialize the start of the continuous subarray
	i_0 = 0
	# Initialize the end of the continuous subarray
	i_1 = 1
	n = len(freq)
	total = 0

	while i_1 < n:
		# While not at the end of the subarray, check if the next value is non-zero
		if freq[i_1] == 0:
			# If value is zero, take the sum of the continuous subarray and integer divide by 2. That's the
			# number of pairs in this segment
			total += sum(freq[i_0: i_1]) // 2
			# The new start of the continuous array is here
			i_0 = i_1
		i_1 += 1
	# Upon reaching the end, find the number of pairs of the last subarray
	total += sum(freq[i_0:i_1]) // 2
	return total

