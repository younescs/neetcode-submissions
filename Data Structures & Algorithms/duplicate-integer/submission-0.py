class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aset = set()

        for num in nums:
            if num in aset:
                return True
            aset.add(num)
        return False
        