class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        minn=float("inf")
        count=0
        for right in range(len(nums)):
            count+=nums[right]
            while count>=target:
                minn=min(minn,right-left+1)
                count-=nums[left]
                left+=1
        return 0 if minn==float("inf") else minn
        