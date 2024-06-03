"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/edit-distance

"""Import required"""
from typing import List


"""Define global variables"""
word1: str
word2: str

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global word1, word2

        with open('input.txt', 'r') as f:
            """Set variables"""
            word1 = f.readline().strip()
            word2 = f.readline().strip()


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, word1:str, word2:str):
        #solve here
        dist: List[int][int] = [[0] * (len(word2) + 1) for i in range(len(word1) + 1)]

        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        
        # set value for base cases
        for i in range (len(word1)):
            dist[i][len(word2)] = i

        for i in range (len(word2)):
            dist[len(word1)][i] = i
        
        # dynamic 
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if(word1[i] == word2[j]):
                    dist[i][j] = dist[i + 1][j + 1]
                else:
                    dist[i][j] = min(
                        dist[i][j + 1] + 1,
                        dist[i + 1][j] + 1,
                        dist[i + 1][j + 1] + 1
                    )
        
        print(dist)
        return dist[0][0]


def app():
    global word1, word2
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    print(solution.solve(word1, word2))

app()