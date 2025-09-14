class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        win=0
        n=len(nums)
        max_sum=0
        for i in range(k):
            win+=nums[i]
        max_sum=win

        for i in range(k,n):
            win+=nums[i]-nums[i-k]
            max_sum=max(max_sum,win)
        return max_sum/float(k) 