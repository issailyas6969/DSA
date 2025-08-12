class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=0
        maxx=0
        for i in range(len(nums)):
            if nums[i]==1:
                max_count+=1
                maxx=max(maxx,max_count)
            else:
                max_count=0
        return maxx
        