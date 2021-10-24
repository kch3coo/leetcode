class Solution:
    #let Opt(i) be the lenth of the longest subsequence such that nums[i] is the min element, Opt(i) is the max(Opt[j]) + 1 in i < j <= len(nums)
    def lengthOfLIS_topdown(self, nums: List[int]) -> int:
        Opt = {}
        def dp(i):
            if i in Opt:
                return Opt[i]
            if i == len(nums) - 1:
                Opt[i] = 1
                return 1
            max_len = 0
            for j in range(i, len(nums)):

                if nums[i] < nums[j]:
                    max_len = max(dp(j), max_len)
            Opt[i] = max_len + 1
            return Opt[i]
        max_len = 0
        min_i = 0
        for i in range(len(nums)):
            dp(i)
            if Opt[i] > max_len:
                
                max_len = Opt[i]
#                 min_i = i
#         result = [nums[min_i]]
        
#         for j in range(min_i, len(nums)):
#             if Opt[j] == (Opt[min_i] - 1) and nums[j] > nums[min_i]:
#                 # print(nums[j])
#                 result.append(nums[j])
#                 min_i = j
#         print(result)
        return max_len

    #Let Opt[i] be the max element in the list, then Opt[i] is the max(Opt[j]) + 1 in all previous 0 <= j < i
    def lengthOfLIS_bottomup(self, nums: List[int]) -> int:
        Opt = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                Opt[0] = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    Opt[i] = max(Opt[i], Opt[j] + 1)
                
        # print(Opt)
        return max(Opt)