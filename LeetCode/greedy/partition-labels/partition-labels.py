"""Minimal template"""

"""Problems links"""
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

"""Import required"""
from typing import List


"""Define global variables"""
s: str


"""Reader class"""
class Reader():
    """Reader class"""
    @staticmethod
    def read():
        """read input"""
        global s

        with open('input.txt', 'r') as f:
            s = f.readline()


class Solution():
    """
    Class Solution
    We'll solve problems here
    """
    def solve(self, s: str):
        last: dict = dict()
        parts: List[str] = []

        # use visited to check if char is visited or not
        visited: dict = dict()

        # mark all visited char as false initially
        # store last index of that char in s
        for i in range (len(s)):
            last[s[i]] = i
            visited[s[i]] = False
        
        #start from first letter, find minimal partition contain first letter
        #update the partition
        part: str = ""
        end_part: int = 0
        start_part: int = 0

        index = 0
        while index <= len(s):
            if(index == len(s)):
                parts.append(len(part))
                break

            if(visited[s[index]]):
                index+=1
                continue
            else:
                visited[s[index]] = True
                
            last_char_index = last[s[index]]
            #if last char index < end_part, do not need to update the part
            if(last_char_index < end_part):
                index+=1
                continue
            
            if(index > end_part):
                #push part in parts
                parts.append(len(part))

                #init new part, start from index => last_index
                start_part = index
                part = s[start_part:last_char_index + 1]
                end_part = last_char_index
            else:
                #compare end_part with last_index of s[i]
                if(end_part <= last_char_index):
                    part = s[start_part:last_char_index + 1]
                    end_part = last_char_index
            
            index+=1
        return parts


def app():
    """Function read input, solve and output"""
    Reader().read()
    global s

    solution = Solution()
    print(solution.solve(s))

app()