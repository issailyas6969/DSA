class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        left=0
        count_z=0
        max_len=0
        for right in range(n):
            if nums[right]==0:
                count_z+=1
            while count_z>1:
                if nums[left]==0:
                    count_z-=1
                left+=1
            max_len=max(max_len,right-left)
        return max_len

        