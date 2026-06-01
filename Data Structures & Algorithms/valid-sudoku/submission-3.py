class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We can create 3 sets
        row_set = set()
        col_set = set()
        box_set = set()
        isValid = True

        # To point to the right box, we use r // 3, c // 3

        # Loop through each value
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    row_key = (r, board[r][c])
                    col_key = (c, board[r][c])
                    box_key = (r // 3, c // 3, board[r][c])
                    if (row_key in row_set) or (col_key in col_set) or (box_key in box_set):
                        return False
                
                    row_set.add(row_key)
                    col_set.add(col_key)
                    box_set.add(box_key)
        
        return isValid

                
                
        


        