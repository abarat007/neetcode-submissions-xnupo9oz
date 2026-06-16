# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        inserted_node = TreeNode()
        inserted_node.val = val

        if not root:
            return inserted_node
        

        def dfs(node):
            if not node:
                return
            # If val < node.val, dfs to the left

            # If val > node.val, dfs to the right

            if val < node.val:
                if not node.left:
                    node.left = inserted_node
                else:
                    dfs(node.left)
            
            if val > node.val:
                if not node.right:
                    node.right = inserted_node
                else:
                    dfs(node.right)
            


        
        dfs(root)
        return root
        