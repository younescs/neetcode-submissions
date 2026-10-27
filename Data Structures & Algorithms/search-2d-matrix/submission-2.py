class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        def binarySearch(alist):
            l, r = 0, len(alist) - 1

            while l <=r:
                mid = (l+r)//2

                if alist[mid] == target:
                    return True
                
                elif alist[mid] > target:
                    r = mid - 1
                elif alist[mid] < target:
                    l = mid + 1
            return False
        


        for r in range(rows):
            if matrix[r][0] <= target <= matrix[r][cols -1]:
                return binarySearch(matrix[r])
        return False
        