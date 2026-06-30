# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque([root])
        res = []
        
        # Traverse with bfs
        # If node.left and node.right --> add node.right to queue
        # If node.left and not node.right --> add node.left to queue
        def bfs(root):
            while queue:
                level_len = len(queue)
                for i in range(level_len):
                    node = queue.popleft()
                    if i == level_len - 1:
                        res.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        bfs(root)
        return res
        