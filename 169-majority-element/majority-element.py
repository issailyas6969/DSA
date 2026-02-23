class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        count=defaultdict(int)
        res,maxx=0,0
        for num in nums:
            count[num]+=1
            while count[num]> maxx:
                res=num
                maxx=count[num]
        return res
