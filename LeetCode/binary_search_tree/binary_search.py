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
    

    @staticmethod
    def findFirst(arr: List[int],l: int, r: int, target: int) -> int:
        if l > r:
            if(l <= len(arr) - 1) and (arr[l] == target):
                return l
            else: 
                return -1
        
        mid = l + (r-l)//2
        if(arr[mid] >= target):
            r = mid - 1
            return BinarySearch.findFirst(arr, l, r, target)
        
        elif arr[mid] < target:
            l = mid + 1
            return BinarySearch.findFirst(arr, l, r, target)

    @staticmethod
    def findLast(arr: List[int], l: int, r: int,  target: int) -> int:
        if l > r:
            if(r >= 0) and (arr[r] == target):
                return r
            else: 
                return -1
        
        mid = l + (r-l)//2
        if(arr[mid] > target):
            r = mid - 1
            return BinarySearch.findLast(arr, l, r, target)
        
        elif arr[mid] <= target:
            l = mid + 1
            return BinarySearch.findLast(arr, l, r, target)
    

    @staticmethod
    def matrixSearch(matrix: List[List[int]], target: int) -> int:
        start, end = 0, len(matrix) - 1


        def findIndexRange(matrix: List[List[int]], target: int) -> int:
            l, r = start, end
            while (l <= r):
                mid = l + (r - l)//2

                row_mid = matrix[mid]

                min_row_mid = row_mid[0]
                max_row_mid = row_mid[-1]

                if (target >= min_row_mid) and (target <= max_row_mid):
                    return mid
                
                if(target < min_row_mid):
                    r = mid - 1

                else:
                    l = mid + 1
            
            return l
        
        index_range = findIndexRange(matrix, target)
        if (index_range < 0) or (index_range > end):
            return False
        
        row_contain = matrix[index_range]
        print(row_contain)
        print(BinarySearch.binarySearch(row_contain, 0, len(row_contain) - 1, target))
        return True if BinarySearch.binarySearch(row_contain, 0, len(row_contain) - 1, target) != -1 else False
    
    @staticmethod
    def matrixSearch2(matrix: List[List[int]], target):
        m = len(matrix)
        n = len(matrix[0])

        l,r = 0, m*n -1

        while(l <= r):
            mid = l + (r - l) // 2
            row, col = divmod(mid, n)

            if(matrix[row][col] == target):
                return (row, col)
            
            if(matrix[row][col] < target):
                l = mid + 1
            else:
                r = mid - 1
        
        if(l >= m*n) or (r < 0):
            return -1
