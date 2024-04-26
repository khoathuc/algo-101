"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

"""Import required"""
from typing import List


"""Define global variables"""
prices: List[int] = []

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global prices

        with open('input.txt', 'r') as f:
            nums_data = f.readline()

            """Set variables"""
            prices = [int(num_str) for num_str in nums_data.split()]
            start = f.readline()


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, prices: List[int]):
        max_profit = prices[-1]
        res = 0
        for i in range(len(prices) - 1, -1, -1):
            max_profit = max(max_profit, prices[i])
            res = max(max_profit - prices[i], res)

        return res

def app():
    """Function read input, solve and output"""
    Reader().read()
    global prices

    solution = Solution()
    print(solution.solve(prices))

app()