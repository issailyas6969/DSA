class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n<=2:
            return n
        l=2
        for right in range(2,n):
            if nums[right]!=nums[l-2]:
                nums[l]=nums[right]
                l+=1
        return l
