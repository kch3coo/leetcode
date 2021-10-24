# Definition for a binary tree node.
from math import comb, log
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + "->" + str(self.next)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    def sort_key (self, v1):
        return v1.val
    def sortedmergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode()
        prev = dummy
        sorted_head = []
        while lists:
            v = lists.pop(0)
            if v:
                sorted_head.append(v)

        sorted_head = sorted(sorted_head, key=self.sort_key)
  
        while sorted_head:
            curr = sorted_head.pop(0)
            prev.next = curr
            tmp = curr.next
     
            i = 0
            while i < len(sorted_head) and tmp:
                
                if not sorted_head[i]:
                    sorted_head.pop(i)
                    continue
     

                if tmp.val < sorted_head[i].val:
                    sorted_head.insert(i, tmp)
            
                    break
                if i + 1 == len(sorted_head):
                    sorted_head.append(tmp)
                    break
                i += 1
            prev = prev.next
   
        return dummy.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return self.dcMerge(lists)

    def dcMerge(self, lists):
        dummy = ListNode()
        if len(lists) == 0:
            return dummy.next
        if len(lists) == 1:
            return lists[0]
        m = int(len(lists) / 2)
        return self.merg2Lists(self.dcMerge(lists[0: m]), self.dcMerge(lists[m: ]))

    def merg2Lists(self, l1, l2):
        dummy = ListNode()
        prev = dummy
        if not l1:
            return l2
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 else l2
        return dummy.next
                


if __name__ == "__main__":
    print("hello")
    result = []
    input = [[],[1], []]
    for k in input:
        prev = None
        if k == []:
            result.append(None)
        for i in range(len(k)):
            if not k[i]:
                result.append(None)
                continue
            node = ListNode(k[i])
            if i == 0:
                result.append(node)
            if prev:
                prev.next = node
            prev = node


    sol = Solution()

    print(sol.dcMerge(result))

    
