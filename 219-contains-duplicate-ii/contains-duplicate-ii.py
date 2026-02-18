class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sett=set()
        for i in range(len(nums)):
            if nums[i] in sett:
                return True
            sett.add(nums[i])
            if i>=k:
                sett.remove(nums[i-k])
        return False       