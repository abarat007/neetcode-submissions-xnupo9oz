# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        res = TreeNode()

        # Do DFS, and recurse until both p and q nodes are identified
        def dfs(node):
            if not node:
                return
            nonlocal res
            # If both values are greater than the node value, then we dfs on the right side
            if p.val > node.val and q.val > node.val:
                dfs(node.right)
            
            # If both values are less than the node value, then we dfs on the left side
            elif p.val < node.val and q.val < node.val:
                dfs(node.left)
            
            # If node value is in between, then this is the splitting point
            else:
                res = node
            
        dfs(root)
        return res

        
        