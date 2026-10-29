class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}

        def dfs(pos):

            if pos < 2:
                return 0
            if pos in cache:
                return cache[pos]
            
            cache[pos] = min(dfs(pos - 1) + cost[pos - 1],
                             dfs(pos - 2) + cost[pos - 2])
            return cache[pos]

        return dfs(len(cost))
        