# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # We traverse left
            left_max = dfs(node.left)

            # we traverse right
            right_max = dfs(node.right)

            left_max = max(left_max,0)
            right_max = max(right_max,0)

            # set a current path sum
            curr_ps = node.val + left_max + right_max

            # update max_sum
            max_sum = max(max_sum, curr_ps)

            return node.val + max(left_max, right_max)


        
        dfs(root)
        return max_sum
        