"""Pascal triangle"""

"""Problems links"""
# https://leetcode.com/problems/minimum-path-sum

"""Import required"""
from typing import List, Dict


"""Define global variables"""
strs: List[str]

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global strs

        with open('input.txt', 'r') as f:
            """Set variables"""
            #read nums
            strs_data = f.readline()
            """Set variables"""
            strs = [strs_data for strs_data in strs_data.split()]

class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    #TODO: implement innovative way
    def solve(self, strs: List[str])-> List[List[str]]:
        #solve here
        groups: Dict[str, List[str]] = {}
        for str in strs:
            tmp = ''.join(sorted(str))
            if( tmp in groups):
                groups[tmp].append(str)
            else:
                groups[tmp] = [str]
            
        #get result
        res: List[List[str]] = []
        for key in groups:
            res.append(groups[key])
        
        return res
            
def app():
    global strs
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    print(solution.solve(strs))

app()