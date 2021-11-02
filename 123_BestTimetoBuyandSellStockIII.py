class Solution:
    #Runtime: 49.27% Memory: 82.85%
    #Loop prices 2 times to get Opt_left and Opt_right. Opt_left represents the max profit get by completing at most 1 transaction from prices[0:i]. Opt_right represents the max profit from prices[j:]. Get the at most two transaction by finding Max[Opt_left(k), Opt_right(k+1)] for k in range(len(prices)).
    def maxProfit(self, prices) -> int:
        #plus 1 to prevent Opt_right[k+1] index error
        Opt_left = [0] * (len(prices) + 1)
        Opt_right = [0] * (len(prices) + 1)
        min_i = 10 ** 5
        for i in range(len(prices)):
            min_i = min(min_i, prices[i])
            if i > 0:
                Opt_left[i] = max(prices[i] - min_i, Opt_left[i - 1])
        max_j = 0
        for j in range(len(prices)-1, -1, -1):
            max_j = max(max_j, prices[j])
            if j < len(prices) - 1:
                Opt_right[j] = max(max_j - prices[j], Opt_right[j + 1])
                
        max_profit = 0
        for k in range(len(prices)):
            max_profit = max(max_profit, Opt_left[k] + Opt_right[k+1])
        return max_profit
    #202 / 214 Time Limit Exceed
    def maxProfit_dp(self, prices) -> int:
        Opt = {}
        for i in range(len(prices)):
            min_v = prices[i]
            for j in range(i + 1, len(prices)):
                if j > 0 and i != j -1:
                    Opt[(i, j)] = max(0, Opt[(i, j-1)], prices[j] - min_v)
                else:
                    Opt[(i, j)] = max(0, prices[j] - min_v)
                min_v = min(prices[j], min_v)
        # return Opt
        max_profit = 0
        for k in range(len(prices)):
            left = 0 if (0, k) not in Opt else Opt[(0, k)]
            right = 0 if (k+1, len(prices) -1) not in Opt else Opt[(k+1, len(prices) -1)]
            max_profit = max(max_profit, left + right)
        return max_profit
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([2, 3, 1, 4]))



