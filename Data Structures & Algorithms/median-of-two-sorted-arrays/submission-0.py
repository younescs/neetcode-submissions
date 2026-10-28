class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)
        half = len(nums1)//2
        if len(nums1) % 2:
            return nums1[half]
        
        return (nums1[half-1] + nums1[half])/2

