class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l, r = 0, 0
        result = 0
        curr_lo = 0
        k_count = 0

        while r < len(nums) and l < len(nums):
            # print(l, r)
            if  nums[r] == 1:
                #next is 1, keep going
                r += 1
                curr_lo += 1
                result = max(curr_lo, result)
            elif k_count < k and nums[r] == 0:
                #flip a zero to move on
                k_count += 1
                curr_lo += 1
                r += 1
                result = max(curr_lo, result)
            elif nums[l] == 0:
                # print(l, r, k_count)
                #no more flips, found a flipped position, unflip
                k_count -= 1
                l += 1
                curr_lo -= 1
            else:
                l += 1
                curr_lo -= 1
        return result