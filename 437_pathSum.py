# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        mem = {}
        mem[0] = 1
        def reFindSum(root, currSum):
            if root == None:
                return 0

            currSum += root.val
            count = 0
            if currSum - targetSum in mem:
                count += mem[currSum - targetSum]
            if currSum in mem:
                mem[currSum] += 1
            else:
                mem[currSum] = 1
            # if count > 0:
            #     print(root.val, currSum, mem, targetSum)
            count += reFindSum(root.left, currSum)
            count += reFindSum(root.right, currSum)
            
            #remove current sum from the tree to seperate path between left and right
            if mem[currSum] > 0:
                mem[currSum] -= 1
            else:
                mem.remove(currSum)
            return count
        
        return reFindSum(root, 0)