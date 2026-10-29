# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        max_diff = 0

        def dfs(node):
            nonlocal max_diff
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diff = abs(left - right)
            max_diff = max(diff, max_diff)

            return 1 + max(left, right)
        dfs(root)
        return max_diff < 2