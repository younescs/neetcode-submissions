# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        value = root.val
        counter = 0

        #2
    #         #4
         #10.    #8
               #4

        def dfs(root, maximum):
            nonlocal value
            nonlocal counter
            if not root:
                return
            
            maximum = max(maximum, root.val)
            if value <= root.val and maximum <= root.val:
                counter +=1
            
            dfs(root.left, maximum)
            dfs(root.right, maximum)

            return counter

        
        return dfs(root, float('-inf'))