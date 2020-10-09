'''
Problem
Your chess teacher wants to know if a bishop can reach a certain spot on the board in the given amount of moves.

Given a starting square (str), ending square (str) and the maximum number of moves allowed (int). Return True if
the ending square can be reached from the starting square within the given amount of moves. Keep in mind the
chessboard goes from a1 to h8 (8x8).

Example:
solution("a1", "b4", 3)
>>> True

Solution

When looking at a chess board, we observe two possible colors. All squares of one color can be accessed by a
diagonal move of no more than 2. We can also convert the alphabetical characters to a number, giving us a
matrix. With an index base of 1, if the horizontals add up to an even and the verticals add up to an even,
then there are purely diagonal moves we can take.

|  ■   ■  | 5
|■   ■   ■| 4
|  ■   ■  | 3
|■   ■   ■| 2
|  ■   ■  | 1
 1 2 3 4 5

If we are at (1, 1) and want to go to (1, 3) we can observe that the sums of the x-values and y-values are both be
even. However, if we start at (2, 1), then the sums are not both even or odd, and we also know this move is not
possible. This works for the sum of x and y for any single point, so we can describe a point as 'even' or 'odd'.

Ex. (3, 2), (2,5)
The two have individual sums of 5 and 7, respectively, and both are light squares on our mini board.

As mentioned before, an even point can reach any other even point in 2 moves or less (same applies to odd) so we
can assume that if it passes our even/odd point test, it can be done in under 2 moves. But if we are told it must
be done in one move, then we need to check if the two points lay on a line with a slope of ±1.

slope = (y_2 - y_1)/(x_2 - x_1)
slope = 1
x_2 - x_1 = y_2 - y_1

If both sides produce m or -m, we know we can make a perfectly diagonal move from one point to another.

If the number of moves is 0, then we simply need to check if they are the same point.

'''

d={char: i+1 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}

def solution(a: str, b: str, n: int) -> bool:
	if n == 0:
		return a == b
	a = ( d[a[0]], int(a[1]) )
	b = ( d[b[0]], int(b[1]) )
	if n == 1:
		return abs(a[0] - b[0]) == abs(a[1] - b[1])
	return (a[0] + b[0])%2 == (a[1] + b[1])%2


def solution(a,b,n):
	if n==0:return a==b
	x,y=abs(ord(a[0])-ord(b[0])),abs(int(a[1])-int(b[1]))
	if n==1:return x==y
	return x%2==y%2

