class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        count = defaultdict(int)
        max_sum=0
        window_sum=0
        left=0
        for right in range(len(nums)):
            count[nums[right]]+=1
            window_sum+=nums[right]

            if right-left+1 >k:
                count[nums[left]]-=1
                window_sum-=nums[left]
                if count[nums[left]]==0:
                    del count[nums[left]]
                left+=1
            if right-left+1==k and len(count)==k:
                max_sum=max(max_sum,window_sum)
        return max_sum