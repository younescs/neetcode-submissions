class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #half the nums check whether the target is in the left or right array, halve it again, keep going until we find the target
        l,r = 0, len(nums) - 1

        while l<=r:
            mid = l + (r - l)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        
        return -1
