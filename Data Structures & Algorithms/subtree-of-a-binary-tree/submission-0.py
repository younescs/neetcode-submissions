# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(q,p):
            if not q and not p:
                return True
            elif not q or not p:
                return False
            if q.val != p.val:
                return False
            return isSameTree(q.left, p.left) and isSameTree(q.right, p.right)

        if not root and not subRoot:
            return True
        elif not root or not subRoot:
            return False
        if root.val == subRoot.val and isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)




        
        