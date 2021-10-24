class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_price = 0
        l, r = 0, 1
        while r < len(prices):
            # print(l, r)
            if prices[r] > prices[l]:
                max_price = max(prices[r] - prices[l], max_price)
            else:
                l = r
            r += 1
        return max_price

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        profit = 0
        l, r = 0, 0
        for i in range(len(prices)):

            if prices[i] > prices[r]:
                r = i
                profit = max(profit, prices[r] - prices[l])
            if prices[i] < prices[l]:
                l = i
                r = i

        return max(profit, prices[r] - prices[l])