'''

Take an n X m matrix. We need to find the fastest route from the top left corner to the top
right. However, each step has a cost, and we can only go down and to the right. What is the
minimal-cost to navigate the matrix?

| 1  6  0 |
| 3  4  1 |
| 5  7  2 |

Answer: 1 + 6 + 0 + 1 + 2 = 10

'''

def solution(matrix: list) -> int:
	# n: number of rows
	# m: number of columns
	# r: row index
	# c: column index
	n = len(matrix)
	m = len(matrix[0])

	# Greedy first column
	for r in range(1, n):
		matrix[r][0] += matrix[r-1][0]

	# Greedy first row
	for c in range(1, m):
		matrix[0][c] += matrix[0][c-1]
	# Row number
	for r in range(1, n):
		# Column number
		for c in range(1, m):
			matrix[r][c] += min(matrix[r][c-1], matrix[r-1][c])
	return matrix

test = [
[5,4,3,2],
[9,9,9,9],
[1,1,1,1]
]

answer = solution(test)
print(answer[-1][-1])

