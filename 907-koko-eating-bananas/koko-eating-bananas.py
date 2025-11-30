class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        import math
        l,r=1,max(piles)
        res=r
        while l<=r:
            mid=(l+r)//2
            hours=0
            for p in piles:
                hours+=math.ceil(float(p)/mid)
            if hours<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        