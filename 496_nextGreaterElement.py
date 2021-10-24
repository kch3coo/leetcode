class Solution(object):
    def nextGreaterElement_naive(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        for n in nums1:
            nge = -1
            start_i = nums2.index(n)
            for i in range(start_i, len(nums2)):
                if n < nums2[i]:
                    nge = nums2[i]
                    break
            result.append(nge)
        return result

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        curr_stack = []
        nge_Map = {}
        for n in nums1:
            nge_Map[n] = -1
        for i in range(len(nums2) - 1, -1, -1):

            while curr_stack:
                if curr_stack[-1] > nums2[i]:
                    if nums2[i] in nge_Map:
                        nge_Map[nums2[i]] = curr_stack[-1]
                    curr_stack.append(nums2[i])
                    break
                else:
                    curr_stack.pop(-1)
            if len(curr_stack) == 0:
                #no greater element exist in stack
                curr_stack.append(nums2[i])
                if nums2[i] in nge_Map:
                    nge_Map[nums2[i]] = -1
                continue
        return [nge_Map[n] for n in nums1]
           