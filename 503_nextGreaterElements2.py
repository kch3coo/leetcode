class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #trying to find left ngn
        stack = []
        result = [-1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[0]] <= nums[i]:
                stack.pop(0)
            if stack:
                result[i] = nums[stack[0]]
            stack.insert(0, i)

        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[0]] <= nums[i]:
                stack.pop(0)

            if stack:
                result[i] = nums[stack[0]]
            stack.insert(0, i)
        return result
if __name__ == "__main__":
    print("hello")
    sol = Solution()
    sol.nextGreaterElements([1, 2, 1])
    #[2,-1,2]
    sol.nextGreaterElements([6,1,2,3,4,2])
    #[-1,2,3,4,6,6]