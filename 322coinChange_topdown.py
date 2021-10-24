class Solution:
    def coinChange_topdown(self, coins: List[int], amount: int) -> int:
        Map = {}
        def opt(A):
            if A < 0:
                return 10 ** 4
            if A == 0:
                return 0
            if A in Map:
                return Map[A]
            for k in coins:
                if k == A:
                    return 1
            min_v = 10 ** 4
            for k in coins:
                n = opt(A - k)
                if min_v > n:
                    min_v = n
            Map[A] = 1 + min_v
            return  Map[A]
        result = opt(amount)
        if result >= 10 ** 4:
            return - 1
        return result
        
    def coinChange_bottomup(self, coins: List[int], amount: int) -> int:
        DP = {}
        for i in range(amount + 1):
            if i == 0:
                DP[0] = 0
                continue
            min_v = 10 **4
            for k in coins:
                if k == i:
                    min_v = 0
                    break
                if i > k and min_v > DP[i - k]:
                    min_v = DP[i - k]
            DP[i] = min_v + 1
            # print(i, DP[i])
        if DP[amount] >= 10 ** 4:
            return -1
        
        return DP[amount]