class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        presum = {}
        result = 0
        hmap = {}
        for i in range(len(nums)):
            if i == 0:
                presum[0] = 0
            else:
                presum[i] = nums[i - 1] + presum[i - 1]
        for i in range(len(nums)):
            if presum[i] not in hmap:
                hmap[presum[i]] = 1
            else:
                hmap[presum[i]] += 1
 
            target_sum = presum[i] + nums[i] - k
            if target_sum in hmap:
                result += hmap[target_sum]
        return result