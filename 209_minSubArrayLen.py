class Solution(object):
    def minSubArrayLen_bruteforce(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        for w in range(1, len(nums) + 1):
            i = 0
            # print("current window: ", w)
            while i < len(nums):
                # print(nums[i : i + w])
                if sum(nums[i : i + w]) >= target:
                    return w
                i += 1
        return 0
    def minSubArrayLen_windows(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        result = 0
        curr_sum = nums[0]
        while r < len(nums):
            if curr_sum >= target:
                if result == 0:
                    result = r - l + 1
                else:
                    result = min(result, r - l + 1)
            if (result == 0 or curr_sum < target):
                if r + 1 >= len(nums):
                    return result
                #move right pointer
                r += 1
                curr_sum += nums[r]
            elif curr_sum >= target:
                #move left pointer
                curr_sum -= nums[l]
                l += 1
            # print(l, r, curr_sum)

        # print(curr_sum)
        return result