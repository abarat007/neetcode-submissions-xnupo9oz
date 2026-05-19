class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = (rows * cols) - 1

        # binary search on compressed matrix
        while left <= right:
            middle = (left + right) // 2
            r = middle // cols
            c = middle % cols
            if target > matrix[r][c]:
                left = middle + 1
            elif target < matrix[r][c]:
                right = middle - 1
            else:
                return True
        
        return False




        
                
        