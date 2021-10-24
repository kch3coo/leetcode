# Definition for a binary tree node.
from math import comb, log
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + "->" + str(self.next)

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if not l1:
            return l2
        dummy = ListNode()
        prev = dummy
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
                
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        #add the result of the l1 or l2 into the prev
        prev.next = l1 if l1 else l2
        return dummy.next
                


if __name__ == "__main__":

    sol = Solution()

    print("complete")

    
