"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/climbing-stairs

"""Import required"""
from typing import List


"""Define global variables"""
n: int = 0

"""Reader class"""
class Reader():
	"""Reader class"""
	@staticmethod
	def read():
		"""read input"""
		global n

		with open('input.txt', 'r') as f:
			inp = f.readline()

			"""Set variables"""
			n = int(inp)

class Solution():
	"""
	Class Solution
	We'll solve problems here
	"""
	def solve(self):
		global n
		res = [0] * (n + 1)

		res[0] = 1
		res[1] = 1
		for i in range (2, n + 1):
			res[i] = res[i - 1] + res[i - 2]

		return res[n]    


def app():
	"""Function read input, solve and output"""
	Reader().read()
	
	solution = Solution()
	print(solution.solve())

app()