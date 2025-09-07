class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        win=0
        n=len(nums)
        for i in range(k):
            win+=nums[i]
            
        max_sum=win

        for i in range(k,n):
            win+=nums[i]-nums[i-k]
            if win>max_sum:
                max_sum=win
        return max_sum/float(k)