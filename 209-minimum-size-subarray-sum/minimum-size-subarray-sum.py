class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left=0
        minn=float("inf")
        win=0
        for right in range(len(nums)):
            win+=nums[right]
            while win>=target:
                minn=min(minn,right-left+1)
                win-=nums[left]
                left+=1
        return 0 if minn==float("inf") else minn
