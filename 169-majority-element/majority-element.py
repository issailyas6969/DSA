class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}
        for char in nums:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        return max(count,key=count.get)