class Solution(object):
    def largestRectangleArea_bruteForce(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 1:
            return heights[0]
        elif len(heights) == 0:
            return 0
        m = heights[0]
        for i in range(len(heights)):
            curr_height = heights[i]
            curr_left_suit = []
            curr_right_suit = []
            for l in range(i, -1, -1):
                print(i, l)
                if heights[l] < curr_height:
                    # print("left finished [%d]" %(heights[l]))
                    break
                curr_left_suit.append(heights[l])
            for r in range(i+1, len(heights)):
                if heights[r] < curr_height:
                    # print("right finished [%d]" %(heights[r]))
                    break
                curr_right_suit.append(heights[r])
            width = len(curr_left_suit) + len(curr_right_suit)
            area = width * curr_height
            print(i, curr_height, curr_left_suit, curr_right_suit)
            if area > m:
                m = area
        return m

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 1:
            return heights[0]
        elif len(heights) == 0:
            return 0
        #stores the idex of the element in heights, element store in stack should be in asceding fashion
        left_stack = []
        left_boundary = {}
        for i in range(len(heights)):
            curr_height = heights[i]
            curr_boundary_i = i
            while left_stack:
                stack_idx = left_stack[-1]
                if heights[stack_idx] >= curr_height:
                    
                    curr_boundary_i = left_boundary[stack_idx]
                    left_stack.pop()
                else:
                    #found boundary where stack[-1] < curr_height
                    left_stack.append(i)
                    break
            if not left_stack:
                left_stack.append(i)
            left_boundary[i] = curr_boundary_i
        # print(left_boundary)

        right_stack = []
        right_boundary = {}
        for r in range(len(heights)-1, -1, -1):
            curr_height = heights[r]
            curr_boundary_i = r
            while right_stack:
                stack_idx = right_stack[-1]
                if heights[stack_idx] >= curr_height:
                    
                    curr_boundary_i = right_boundary[stack_idx]
                    right_stack.pop()
                else:
                    #found boundary where stack[-1] < curr_height
                    right_stack.append(r)
                    break
            if not right_stack:
                right_stack.append(r)
            right_boundary[r] = curr_boundary_i
        # print(right_boundary)

        max_area = heights[0]
        for i in range(len(heights)):
            width = right_boundary[i] - left_boundary[i] + 1
            area = width * heights[i]
            if area > max_area:
                max_area = area
        return max_area
if __name__ == "__main__":

    sol = Solution()
    ans = sol.largestRectangleArea([4,2,0,3,2,4,3,4])
    # ans = sol.largestRectangleArea([2, 1, 5, 6, 2, 3, 1])
    print(ans)
