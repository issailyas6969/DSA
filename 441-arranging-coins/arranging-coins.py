class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right=1,n
        while left<=right:
            mid=(left+right)//2
            ni=mid*(mid+1)//2
            if ni==n:
                return mid
            elif ni>n:
                right=mid-1
            else:
                left=mid+1
        return right
        