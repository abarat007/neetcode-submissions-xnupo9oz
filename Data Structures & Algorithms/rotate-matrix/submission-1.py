class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        res = [[0 for _ in range(cols)] for _ in range(rows)]

        # step 1: For each row, turn it into a column
        for r in range(rows):
            for c in range(cols):
                if r == c:
                    res[r][c] = matrix[r][c]
                else:
                    res[c][r] = matrix[r][c]
        
        # print(f'res: {res}')

        # step 2: for each row in the new matrix, reverse it
        for r in range(rows):
            left = 0
            right = cols - 1
            while left < right:
                res[r][left], res[r][right] = res[r][right], res[r][left]
                left += 1
                right -= 1
        
        matrix[:] = res


        