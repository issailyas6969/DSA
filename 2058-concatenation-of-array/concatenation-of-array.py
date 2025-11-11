class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in range(len(nums)):
            res.append(nums[i])
        for j in range(len(nums)):
            res.append(nums[j])
        return res
        