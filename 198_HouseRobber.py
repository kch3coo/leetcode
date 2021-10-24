class Solution:
    #3:04 - 3:12
    #Runtime:   29.58% Memory: 92.90%
    #Let Opt[i] be the max amount selected from nums[ i : ] with no two adjacent element being selected. Opt[i] = Max[ Opt(i - 1), Opt(i - 2) + nums[i] ]
    def rob(self, nums: List[int]) -> int:
        Opt = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in Opt:
                return Opt[i]
            Opt[i] = max(dp(i + 1), dp(i + 2) + nums[i])
            return Opt[i]
        return dp(0)

    #3:04 - 3:17
    #Runtime:  19.71% Memory: 19.59%
    def rob_bottomup(self, nums: List[int]) -> int:
        Opt = {}
        Opt[-2] = 0
        Opt[-1] = 0
        for i in range(len(nums)):
            Opt[i] = max(Opt[i - 1], Opt[i - 2] + nums[i])
        return Opt[len(nums) - 1]
    #3:04 - 3:20
    #Runtime:  36.29% Memory: 77.46%
    def rob_bottomup_reduce_memory(self, nums: List[int]) -> int:
        prev = 0
        prev2 = 0
        for i in range(len(nums)):
            curr = max(prev, prev2 + nums[i])
            prev2 = prev
            prev = curr
        return prev