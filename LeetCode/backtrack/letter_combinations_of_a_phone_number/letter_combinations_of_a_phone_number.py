"""Letter Combinations of a Phone Number"""

"""Problems links"""
# https://leetcode.com/problems/letter-combinations-of-a-phone-number

"""Import required"""
from typing import List


"""Define global variables"""
digits: str

"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global digits

        with open('input.txt', 'r') as f:
            """Set variables"""
            digits = f.readline()

class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, digits:str):
        #solve here
        map_digits: dict[int, List[str]] = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
        }

        res = []

        def backtrack(index: int, combination: str):
                #check if reach limit
                if(index == len(digits)):
                    res.append(combination)
                    return
                
                #check condition
                list_chars: List[str] = map_digits[int(digits[index])]
                for char in list_chars:
                    #append UCV and continue backtrack
                    backtrack(index + 1, combination+char)
                #try backtrack
        
        if(len(digits) > 0):
            backtrack(0, "")
            
        return res
        pass


def app():
    global digits
    """Function read input, solve and output"""
    Reader().read()
    
    solution = Solution()
    solution.solve(digits)

app()