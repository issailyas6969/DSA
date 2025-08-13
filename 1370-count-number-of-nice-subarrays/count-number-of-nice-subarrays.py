class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmost(k):
            left=0
            count_odd=0
            total=0
            for right in range(len(nums)):
                if nums[right]%2:
                    count_odd+=1
                while count_odd>k:
                    if nums[left]%2:
                        count_odd-=1
                    left+=1
                total+=(right-left+1)
            return total
        return atmost(k) - atmost(k - 1)
