class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2
            
        dp = [0] * 3

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1, 1):
            temp = dp[2]
            dp[2] += dp[1]
            dp[1] = temp
        return dp[2]
    

        

