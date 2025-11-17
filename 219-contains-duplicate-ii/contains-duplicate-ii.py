class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen=set()
        for right in range(len(nums)):
            if nums[right] in seen:
                return True
            seen.add(nums[right])

            if len(seen)>k:
                seen.remove(nums[right-k])
        return False
    
