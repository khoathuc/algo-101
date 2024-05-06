"""Pascal triangle"""

"""Problems links"""
# https://leetcode.com/problems/minimum-path-sum

"""Import required"""
from typing import List


"""Define global variables"""
nums: List[int]
target: int

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global nums,target

        with open('input.txt', 'r') as f:
            """Set variables"""
            #read nums
            nums_data = f.readline()
            """Set variables"""
            nums = [int(nums_data) for nums_data in nums_data.split()]

            #read target
            target = int(f.readline())

class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, nums: List[int], target: int):
        # dictionary that store index of num in nums
        index_nums: dict = {}

        for i, num in enumerate(nums):
            index_nums[num] = i

        for i,num in enumerate(nums):
            if(target-num) in index_nums:
                if(index_nums[target - num] != i):
                    return [i, index_nums[target - num]]
            
def app():
    global nums, target
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    print(solution.solve(nums, target))

app()