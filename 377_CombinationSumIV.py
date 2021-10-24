class Solution:
    #Runtime:  91.58% Memory: 89.27%
    #Let Opt[i] be the num of possible comb add up to i. Opt[i] = Sum[Opt[i - k]], where k in nums and i > k
    def combinationSum4(self, nums: List[int], target: int) -> int:
        Opt = [0] * (target + 1)
        for i in range(target + 1):
            if i in nums:
                Opt[i] += 1
            for k in nums:
                if i > k:
                    Opt[i] += Opt[i - k]
        return Opt[target]
        