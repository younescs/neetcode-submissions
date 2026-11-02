# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        queue = deque([[root, 0]])
        col_map = {}
        mini = 0
        maxi = 0

        while queue:
            curr = queue.popleft()
            mini = min(curr[1], mini)
            maxi = max(curr[1], maxi)
            if curr[1] in col_map:
                col_map[curr[1]].append(curr[0].val)
            else:
                col_map[curr[1]] = [curr[0].val]
            if curr[0].left:
                queue.append([curr[0].left, curr[1] - 1])
            if curr[0].right:
                queue.append([curr[0].right, curr[1] + 1])

        res = []
        for i in range(mini, maxi+ 1, + 1):
            res.append(col_map[i])

        return res


        