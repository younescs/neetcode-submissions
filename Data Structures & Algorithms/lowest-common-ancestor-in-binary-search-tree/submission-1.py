# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        smaller, larger = min(p.val, q.val), max(p.val, q.val)

        
        def dfs(root):
            
            
            if smaller <= root.val <= larger:
                return root

            if p.val < root.val:
                return dfs(root.left)
            
            if q.val > root.val:
                return dfs(root.right)

        return dfs(root)