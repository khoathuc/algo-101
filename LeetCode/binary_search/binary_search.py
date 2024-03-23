from typing import List

class BinarySearch():
    """Binary Search Prototype"""

    def __init__(self, arr: List[int], target: int) -> None:
        """_summary_

        Args:
            arr (List[int]): given array
            target (int): target
        """
        self.arr = arr
        self.target = target

    @staticmethod
    def binarySearch(arr: List[int], l:int, r: int, x: int) -> int:
        """
        Based on binary search

        Args:
            arr (List[int]): sorted array
            l (int): left position
            r (int): right position
            x (int): value need to be search

        Returns:
            int: index of value in given array
        """
        if l > r:
            return -1

        mid = l + (r-l) // 2

        if arr[mid] == x:
            return mid
        
        elif arr[mid] > x:
            """if mid value > x, find the left side"""
            return BinarySearch.binarySearch(arr, l, mid - 1, x)
        
        else:
            """if mid value > x, find the right side"""
            return BinarySearch.binarySearch(arr, mid + 1, r, x)


    @staticmethod
    def pivotSearch(arr: List[int]) -> int:
        """Search the pivot"""
        tmp = arr[0]
        start = 0
        end = len(arr) - 1
        l = 0
        r = end
        while l <= r:
            mid = l + (r -  l)//2
        
            if (arr[mid] >= tmp):
                l = mid + 1
            else:
                r = mid - 1
        

        return end if l > end else l
    
