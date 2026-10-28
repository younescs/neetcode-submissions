class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def memo(n):
            nonlocal cache
            if n == 2:
                return 2
            if n == 1:
                return 1
            if n in cache: return cache[n]

            cache[n] = memo(n-2) + memo(n-1)

            return cache[n]
        return memo(n)
        