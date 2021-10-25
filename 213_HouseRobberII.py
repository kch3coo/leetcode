from typing import List
class Solution:
    #3:35 - 3:54
    #Runtime 5.49% Memory: 5.68%
    #Let Opt[i, j] be the max amount selected from nums[i : j], Opt[i, j] = Max[Opt[i + 1, j], Opt[i + 2, j] + nums[i]]. Create a special case when i == 0 and j == len(nums) - 1.
    def rob(self, nums: List[int]) -> int:
        Opt = {}
        def dp(i, j):
            if (i, j) in Opt:
                return Opt[(i, j)]
            if i > j:
                return 0
            if i == j:
                return nums[i]
            if i == 0 and j == len(nums) - 1:
                Opt[(i, j)] = max(dp(i + 1, j), dp(i + 2, j), dp(i + 2, j - 1) + nums[i])
            else:
                Opt[(i, j)] = max(dp(i + 1, j), dp(i + 2, j) + nums[i])
            return Opt[(i, j)]
        return dp(0, len(nums) - 1)

    #Runtime 15.84% Memory: 24.20%
    #Let Opt[i] = max amount selected from nums[i:]. Opt[i] = Max[Opt[i + 1], Opt[i + 2] + nums[i]]. Calculate Max[ dp(nums[：-1]), dp(nums[1: ])]
    def rob_bottomup(self, nums: List[int]) -> int:

        def dp(li):
            Opt = {}
            Opt[-1] = 0
            Opt[-2] = 0
            prev = 0
            prev2 = 0
            for i in range(len(li)):
   
                Opt[i] = max(prev, prev2 + li[i])
                prev2 = prev
                prev = Opt[i]

            return prev

        if len(nums) == 1:
            return nums[0]
        return max(dp(nums[1:]), dp(nums[:len(nums) - 1]))