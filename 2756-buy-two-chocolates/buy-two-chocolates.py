class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices.sort()
        cost=prices[0]+prices[1]
        if cost<=money:
            return money-cost
        return money
        