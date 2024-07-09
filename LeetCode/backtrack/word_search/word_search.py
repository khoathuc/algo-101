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
            word = f.readline()

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
        #m is number of rows
        m:int = len(board)
        #n is number of columns
        n:int = len(board[0])

        def backtrack(index, i, j, visited):
            # check if index is greater than length of word
            if(index > len(word)):
                return False
            
            # check if i, j out of range
            if(i >= m or j >= n or i < 0 or j < 0):
                return False
            
            # check if visited
            if(visited[i][j]):
                return False
            
            # check if board[i][j] is the same at the word's index
            if(board[i][j] != word[index]):
                return False
            
            if(index == len(word)):
                return True
            
            visited[i][j] = True
            return (
                backtrack(index + 1, i + 1, j, visited) or 
                backtrack(index + 1, i, j + 1, visited) or 
                backtrack(index + 1, i + 1, j + 1, visited) or 
                backtrack(index + 1, i - 1, j, visited) or 
                backtrack(index + 1, i, j - 1, visited) or 
                backtrack(index + 1, i - 1, j - 1, visited) or
                backtrack(index + 1, i + 1, j - 1, visited) or
                backtrack(index + 1, i - 1, j + 1, visited)
            )
            # mark as visited
            # backtrack the adjacent
            
        res = False
        for i in range(m):
            for j in range(n):
                    visited = [[False]*n for i in range(m)]
                    res = res or backtrack(0, i, j, visited)
                    
                    if(res):
                        return True
        pass


def app():
    global board, word
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(board, word)

app()