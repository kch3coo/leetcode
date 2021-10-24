class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        presum = 0
        total_sum = sum(nums)
        for i, n in enumerate(nums):
            if i != 0:
                presum += nums[i - 1]
            if total_sum- (presum + n) == presum:
                return i
            
        return -1