class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        e_r = row2
        e_c = col2

        total = 0

        # Constraints
        # horizontally, I cannot go past col2
        # Verticially, I cannot go past row2

        # Double For loop through the defined box
        start_row, end_row = row1, row2+1 # [2,5)
        start_col, end_col = col1, col2+1 # [1,4)
        

        for row in range(start_row, end_row):
            for col in range(start_col, end_col):
                total += self.matrix[row][col]
            
        return total







        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)