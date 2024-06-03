"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/edit-distance

"""Import required"""
from typing import List


"""Define global variables"""
word1: str
word2: str

"""Reader class"""


class Reader:
    """Reader class"""

    @staticmethod
    def read():
        """read input"""
        global word1, word2

        with open("input.txt", "r") as f:
            """Set variables"""
            word1 = f.readline().strip()
            word2 = f.readline().strip()


class Solution:
    """
    Class Solution
    We'll solve problems here
    """

    def solve(self, word1: str, word2: str):
        dist: List[int][int] = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            dist[i][0] = i

        for j in range(len(word2) + 1):
            dist[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                char1 = word1[i - 1]
                char2 = word2[j - 1]

                if char1 == char2:
                    dist[i][j] = dist[i - 1][j - 1]
                else:
                    dist[i][j] = min(
                        dist[i][j - 1] + 1,  # insert
                        dist[i - 1][j] + 1,  # delete
                        dist[i - 1][j - 1] + 1,  # replace
                    )

        return dist[-1][-1]


def app():
    global word1, word2
    """Function read input, solve and output"""
    Reader().read()

    solution = Solution()
    print(solution.solve(word1, word2))


app()
