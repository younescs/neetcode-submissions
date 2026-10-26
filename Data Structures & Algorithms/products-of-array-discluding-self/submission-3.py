class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1]*len(nums)
        prefix[0] = nums[0]

        suffix = [1]*len(nums)
        suffix[-1] = nums[-1]
    
        for i in range(1, len(nums)):
            product = nums[i] * prefix[i-1]
            prefix[i] = product
        
        for i in range(len(nums) - 2, -1, -1):
            product = nums[i]* suffix[i+1]
            suffix[i] = product

        nums[0] = suffix[1]
        nums[-1] = prefix[-2]

        for i in range(1, len(nums) - 1):
            nums[i] = prefix[i-1] * suffix[i+1]
        

        return nums
