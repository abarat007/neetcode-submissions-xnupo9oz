class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        low = 0
        high = (rows * cols) - 1 # should be 11

        while low <= high:
            mid = (low + high) // 2
            r = mid // cols
            c = mid % cols
            if matrix[r][c] < target:
                low = mid + 1
            elif matrix[r][c] > target:
                high = mid - 1
            else:
                return True
        
        return False
            
        
        