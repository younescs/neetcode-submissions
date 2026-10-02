class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #l1 is a list containing the products of nums from left to right
        l1 = [0]*len(nums)
        l1[0] = nums[0]
        for i in range(1, len(nums)):
            l1[i] = nums[i]*l1[i-1]
        
        #l2 is a list containing the products of nums from right to left
        l2 = [0]*len(nums)
        l2[len(nums)-1] = nums[len(nums) - 1]
        for i in range(len(nums)-2, -1, -1):
            l2[i] = nums[i]* l2[i+1]

        #l3 is the product of the number at every index except self, we build it using the two previous lists this way:

        l3 = [0]*len(nums)
        l3[0] = l2[1]
        l3[len(nums) - 1] = l1[-2]
        for i in range(1, len(l3)-1):
            l3[i] = l1[i - 1]*l2[i+1]


        return l3

