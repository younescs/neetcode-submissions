class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 4:
            return max(nums)

        max_profit = 0

        house1 = nums[0]
        house2 = nums[1]
        house3 = nums[0] + nums[2]

        for i in range(3, len(nums) - 1):
            house4 = nums[i] + max(house2, house1)

            house1, house2 = house2, house3
            house3 = house4

        max_profit = max(house3, house2)
        
        house1 = nums[1]
        house2 = nums[2]
        house3 = nums[3] + nums[1]

        for i in range(4, len(nums)):
            house4 = nums[i] + max(house2, house1)

            house1, house2 = house2, house3
            house3 = house4

         
        max_profit = max(max_profit, house3, house2)

        return max_profit



