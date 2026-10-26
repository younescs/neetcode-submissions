class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        differences = dict()

        for i, num in enumerate(numbers):
            diff = target - num

            if diff in differences:
                return sorted([i + 1, differences[diff] + 1])
            
            differences[num] = i