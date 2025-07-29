class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        overall_max,curr_max=nums[0],nums[0]

        for i in range(1,len(nums)):
            curr_max=max(nums[i],nums[i]+curr_max)
            overall_max=max(overall_max,curr_max)
        return overall_max
        