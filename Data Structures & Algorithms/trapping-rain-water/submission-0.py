class Solution:
    def trap(self, height: List[int]) -> int:

        prefix = [0]*len(height)
        suffix = [0]*len(height)
        minfix = [0]*len(height)
        highest = 0

        for i in range(len(height)):
            prefix[i] = highest
            highest = max(highest, height[i])

        highest = 0 

        for i in range(len(height) -1, -1, -1):
            suffix[i] = highest
            highest = max(highest, height[i])

        for i in range(len(height)):
            minfix[i] = min(prefix[i], suffix[i])

        total_area = 0
        for i in range(len(minfix)):
            area = minfix[i] - height[i]
            if area <=0:
                continue
            total_area += area

        return total_area


        
        