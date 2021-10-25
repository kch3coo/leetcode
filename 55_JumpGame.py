from typing import List
class Solution:
    #12:52 - 1:02 75 / 166, Time Limit Exceed
    def canJump_topdown(self, nums: List[int]) -> bool:
        Opt = {}
        def dp(i):
            if i in Opt:
                return Opt[i]
            if i == len(nums) - 1 or nums[i] >= len(nums) - 1:
                return True
            if nums[i] == 0:
                return False
            for k in range(1, nums[i] + 1):
                if dp(i + k):
                    Opt[i] = True
                    return Opt[i]
            Opt[i] = False
            return Opt[i]
        return dp(0)

    #12:52 - 1:13 
    #Runtime:  10.17% Memory: 36.87%
    #Let Opt[i] be true iff can jump to index nums[:i]. If i == 0, Opt[i] = True. Else, Opt[i] = Any(Opt[j] where 0 <= j < i and nums[j] >= i - j)
    def canJump_bottomup(self, nums: List[int]) -> bool:
        Opt = [False] * len(nums)
        Opt[0] = True
        for i in range(1, len(nums)):
            for j in range(i, -1, -1):
                if nums[j] >= i - j and Opt[j]:
                    Opt[i] = True
                    break
        # print(Opt)
        return Opt[len(nums) - 1]
        