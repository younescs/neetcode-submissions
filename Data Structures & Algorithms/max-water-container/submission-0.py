class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        max_surface = 0
        while l < r:
            surface = (r - l) * min(heights[l], heights[r])
            max_surface = max(surface, max_surface)

            if heights[l] <= heights[r]:
                l +=1
            else:
                r -=1

        return max_surface
