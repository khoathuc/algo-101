"""Pascal triangle"""

"""Problems links"""
# https://leetcode.com/problems/longest-palindromic-substring

"""Import required"""
from typing import List


"""Define global variables"""
s:str

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global s
        
        with open('input.txt', 'r') as f:
            """Set variables"""
            s = f.readline()


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, s:str):
        #DP approach
        arr: List[List[int]] = [[0]*len(s) for i in range(len(s))]
        res:str = ""

        for i in range (len(s)):
            """
            Check all arr[i][i] and arr[i][i + 1]
            because we will check substring arr[i+1][j-1] of arr[i][j] so we do not want arr[l][r] has l > r => i+1 <= j - 1 => j-i > =2
            """

            arr[i][i] = 1
            if(i + 1 < len(s)) and (s[i] == s[i+1]):
                arr[i][i+1] = 1
        
        for i in range (len(s), -1, -1):
            for j in range(i, len(s)):
                if(j > i + 1):
                    if(s[i] == s[j]):
                        arr[i][j] = arr[i + 1][j - 1]
                    else: 
                        arr[i][j] = 0

                #update res if len(dlps) > res    
                if(arr[i][j] == 1):
                    if(j - i + 1) > len(res):
                        res = s[i : j + 1]
                
        return res
        
def app():
    global s
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    print(solution.solve(s))

app()