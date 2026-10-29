# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root, maxi, mini):
            if not root:
                return True
            if not (mini < root.val < maxi):
                return False

            left = dfs(root.left, root.val, mini)
            right = dfs(root.right, maxi, root.val)
           
            return right and left

        
        return dfs(root, float('inf'), float('-inf'))

       