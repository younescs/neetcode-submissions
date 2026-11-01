class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n < 3:
            return n

        ways = [0]*(n + 1)

        step1 = 1
        step2 = 2

        for i in range(3, n + 1):
            step3 = step2 + step1
            step1 = step2
            step2 = step3


        return step3