class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 4:
            return max(nums)

        return max(self.rob_line(nums[:-1]), self.rob_line(nums[1:]))

    def rob_line(self, nums: List[int]) -> int:
      
        house1 = nums[0]
        house2 = nums[1]
        house3 = nums[0] + nums[2]

        for i in range(3, len(nums)):
            house4 = nums[i] + max(house2, house1)

            house1, house2 = house2, house3
            house3 = house4

        return max(house3, house2)