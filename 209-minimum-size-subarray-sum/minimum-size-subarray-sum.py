class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        min_l=float("inf")
        left=0
        summ=0
        for right in range(n):
            summ+=nums[right]

            while summ>=target:
                min_l=min(min_l,right-left+1)
                summ-=nums[left]
                left+=1
        return 0 if min_l==float("inf") else min_l