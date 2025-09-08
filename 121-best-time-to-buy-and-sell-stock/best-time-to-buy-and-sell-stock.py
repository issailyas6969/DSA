class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell=0
        buy=1
        max_p=0
        while buy<len(prices):
            if prices[sell]<prices[buy]:
                p=prices[buy]-prices[sell]
                max_p=max(max_p,p)
            else:
                sell=buy
            buy+=1
        return max_p