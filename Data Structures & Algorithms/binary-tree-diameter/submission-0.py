# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0
        
        # dfs to traverse and collect left and right heights
        def dfs(node):
            if not node:
                return 0
            nonlocal maxDiameter
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            maxDiameter = max(maxDiameter,left_height + right_height)
            
            return 1 + max(left_height, right_height)
          
        dfs(root)
        return maxDiameter
        
            



        