# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        
        queue = deque([root])

        def bfs(node):
            while queue:
                res = []
                level_size = len(queue)
                for _ in range(level_size):
                    nde = queue.popleft()
                    res.append(nde.val)
                    if nde.left:
                        queue.append(nde.left)
                    if nde.right:
                        queue.append(nde.right)
                result.append(res)
        bfs(root)
        
        return result
                







        bfs(root)

        