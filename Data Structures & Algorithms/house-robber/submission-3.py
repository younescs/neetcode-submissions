class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return max(nums)

        house1 = nums[0]
        house2 = nums[1]
        house3 = nums[0] + nums[2]


        for i in range(3, len(nums)):

            house4 = max(nums[i] + house2, nums[i] + house1)

            house1, house2 = house2, house3
            house3 = house4

        return max(house3, house2)
        