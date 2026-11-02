"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dico = {}

        def dfs(node):
            nonlocal dico
            if not node:
                return
            if node in dico:
                return dico[node]
            
            new_node = Node(node.val, [])
            dico[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node

        return dfs(node)
        
            
        