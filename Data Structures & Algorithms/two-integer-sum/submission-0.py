class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dico = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dico:
                return [dico[diff], i]
            dico[nums[i]] = i

