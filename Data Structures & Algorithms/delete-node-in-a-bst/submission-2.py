# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(node, key):
            if not node:
                return None

            # Run dfs on left and right side if val not equal to key
            if key > node.val:
                node.right = dfs(node.right, key)
            
            elif key < node.val:
                node.left = dfs(node.left, key)

            else: 
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    # node has two valid children
                    # return smallest node in curr.right
                    curr = node.right
                    while curr.left:
                        curr = curr.left
                    node.val = curr.val
                    node.right = dfs(node.right, curr.val)
                
            return node
        
        

        return dfs(root, key)

        