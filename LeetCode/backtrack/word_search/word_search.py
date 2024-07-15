"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/word-search

"""Import required"""
from typing import List


"""Define global variables"""
board: List[List[str]] = []
word: str

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global board, word

        with open('input.txt', 'r') as f:
            """Set variables"""
            word = f.readline().strip()

            while True:
                r = f.readline().strip().split()
                if not r:
                    break
                board.append(r)


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, board:List[List[str]], word: str):
        #solve here
        #r is number of rows
        r:int = len(board)
        #c is number of columns
        c:int = len(board[0])

        def backtrack(index, i, j):
            # check if index is greater than length of word
            if(index > len(word)):
                return False
            
            # check if i, j out of range
            if(i > r-1 or j > c-1 or i < 0 or j < 0):
                return False
            
            # check if visited
            if(visited[i][j]):
                return False
            
            # check if board[i][j] is the same at the word's index
            if(board[i][j] != word[index]):
                return False
            
            if(index == len(word) - 1):
                return True
            
            # mark as visited
            visited[i][j] = True
            # backtrack the adjacent
            result =  (
                backtrack(index + 1, i + 1, j) or 
                backtrack(index + 1, i, j + 1) or 
                backtrack(index + 1, i - 1, j) or 
                backtrack(index + 1, i, j - 1)
            )

            visited[i][j] = False
            return result
            
        res = False
        
        visited = [[False]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                    res = res or backtrack(0, i, j)
                    if(res):
                        return True

        return False

def app():
    global board, word
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    print(solution.solve(board, word))

app()