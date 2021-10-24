class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def divide_search(nums, i, j, target):
            if i == j:
                if target == nums[i]:
                    return i
                else:
                    return -1
            if i + 1 == j:
                if target == nums[i]:
                    return i
                return j if target == nums[j] else -1
            m = int((j - i) / 2) + i
            try1 = -1
            if nums[m] == target:
                return m
            elif nums[m] < target:
                try1 = divide_search(nums, m, j, target)
                if try1 == -1:
                    return divide_search(nums, i, m, target)
            elif nums[m] > target:
                try1 = divide_search(nums, i, m, target)
                if try1 == -1:
                    return divide_search(nums, m, j, target)
            return try1
        
        return divide_search(nums, 0, len(nums) - 1, target)