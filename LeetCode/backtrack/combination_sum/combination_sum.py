"""Combination Sum"""

"""Problems links"""
# https://leetcode.com/problems/combination-sum

"""Import required"""
from typing import List


"""Define global variables"""
candidates: List[int]
target: int

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global candidates, target

        with open('input.txt', 'r') as f:
            row_data = f.readline()
            """Set variables"""
            candidates = [int(row_data) for row_data in row_data.split()]

            target = int(f.readline())


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, candidates:List[int], target:int):
        #solve here
        res = []

        def backtrack(candidate_list: List[int], sum: int):
            """
            backtrack

            Args:
                candidate_list (List[int]): list of current candidates
                sum (int): cache sum to reduce caculate step
            """
            if(sum == target):
                res.append(candidate_list)
                return
            
            if(sum > target):
                return

            for candidate in candidates:
                #just add candidate that equal or greater than all the candidate in candidate_list
                #this way we will remove the duplicate
                if(len(candidate_list) > 0) and (candidate < candidate_list[-1]):
                    continue

                candidate_list.append(candidate)
                #use copy to prevent reference
                backtrack(candidate_list.copy(), sum+candidate)
                candidate_list.pop()
                            
            pass

        backtrack([], 0)
        return res
        pass


def app():
    global candidates, target
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(candidates, target)

app()