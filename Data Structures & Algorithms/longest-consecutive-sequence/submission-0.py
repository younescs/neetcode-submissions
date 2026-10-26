class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        max_count = 0
        for num in num_set:
            if num -1 in num_set:
                continue
            else:
                counter = 1
                potential_candidate = num
                while potential_candidate + 1 in num_set:
                    counter +=1
                    potential_candidate += 1
                max_count = max(max_count, counter)
        
        return max_count





        