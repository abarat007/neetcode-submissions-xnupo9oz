# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        # DFS where for each level, we validate the left and right nodes

        def dfs(node, low, high):
            if not node:
                return True
            if not low < node.val < high:
                return False
            # dfs on left node and dfs on right node
            return (dfs(node.left, low, node.val)) and (dfs(node.right, node.val, high))

            
            
        return dfs(root, float('-inf'), float('inf'))        