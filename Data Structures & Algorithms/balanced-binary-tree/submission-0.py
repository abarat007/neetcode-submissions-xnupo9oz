# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def calc_height(root):
            if not root:
                return 0
            
            # Recursively calculate heights
            left_height = calc_height(root.left)
            right_height = calc_height(root.right)

            # Check if any side is unbalanced (return -1)
            if (left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1):
                return -1
            
            # If we get all the way here, we return the height
            return 1 + max(left_height, right_height)
        return calc_height(root) >= 0
            




        


        