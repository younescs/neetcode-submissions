class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #first we create a helper function that's going to help us computer how much time it'll
        #take us to go through the piles of banana given an eating rate

        def how_long(rate):
            counter = 0
            for pile in piles:
                counter += math.ceil(pile/rate)
            return counter

        lo, hi = 1, max(piles)

        output = float('inf')
        while lo <= hi:
            mid = (lo + hi)//2
            time = how_long(mid)
            if time > h:
                lo = mid + 1
            
            else:
                output = min(output, mid)
                hi = mid - 1
        
        return output
