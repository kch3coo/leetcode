# Definition for a binary tree node.
from math import log

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        M = {}
        for i in nums:
            if i not in M:
                M[i] = 1
            else:
                M[i] += 1
        major = int(len(nums) / 2) + 1
 
        for key in M:
            if M[key] >= major:
                return key

if __name__ == "__main__":
    print("hello")
    sol = Solution()
    
