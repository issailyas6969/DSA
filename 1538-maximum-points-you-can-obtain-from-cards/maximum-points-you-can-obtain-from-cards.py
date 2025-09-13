class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(cardPoints)
        total=sum(cardPoints)
        if k==n:
            return total
        left=0
        win_sum=0
        min_len=float("inf")
        for right in range(n):
            win_sum+=cardPoints[right]
            if right-left+1>n-k:
                win_sum-=cardPoints[left]
                left+=1
            if right-left+1 ==n-k:
                min_len=min(min_len,win_sum)
        return total-min_len