
"""Problems links"""
# https://leetcode.com/problems/symmetric-tree

"""Import required"""
import sys
sys.path.append('..')

#pylint: disable=wrong-import-position
from node import Node
#pylint: enable=wrong-import-position
# pylint: disable=E1101

"""Define global variables"""
nodes = []
"""Reader class"""
class Reader():
	"""Reader class"""
	@staticmethod
	def read():
		"""read input"""
		global nodes
		with open('input.txt', 'r') as f:
			nums_data = f.readline()

			"""Set variables"""
			nodes = [int(num_str) for num_str in nums_data.split(',')]


class Solution():
	"""
	Class Solution
	We'll solve problems here
	"""
	def solve(self):
		for i in range(nodes.__len__() - 1):
			if(i == 0):
				root = Node(nodes[i])
				root.insert(nodes[i + 1], 'l')
				root.insert(nodes[i + 2], 'r')

				if root.left:
					root = root.left
				
				if root.right:
					root = root.right
			pass


def app():
	"""Function read input, solve and output"""
	Reader().read()
	
	solution = Solution()
	solution.solve()

app()