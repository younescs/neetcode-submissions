# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0 
        def solution(root):
            if not root:
                return 0
            left = maxdepth(root.left)
            right = maxdepth(root.right)
            self.best = max(self.best, left + right)
            solution(root.left)
            solution(root.right)
        

        def maxdepth(node):

            if not node:
                return 0
            return 1 + max(maxdepth(node.left), maxdepth(node.right))

        solution(root)
        return self.best

