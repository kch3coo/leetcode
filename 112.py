# Definition for a binary tree node.
from math import log

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val) + ", " + str(self.left)+  ", " +str(self.right)


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        #must be leaf
        if root.val == targetSum and root.left == None and root.right == None:
            return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
        

if __name__ == "__main__":
    print("hello")
    sol = Solution()
    root = [4,8,11,None,13,4,7,2,None,None,None,1]
    # rt = TreeNode(5)
    # prev = [rt]
    # while root:
    #     for r in prev:
    #         prev.pop(0)
    #         if len(root) > 0:
    #             r.left = TreeNode(root.pop(0))
    #             prev.append(r.left)
    #         if len(root) > 0:
    #             r.right = TreeNode(root.pop(0))
    # print(rt)

    Ex = TreeNode(1)
    Ex.left = TreeNode(2)
    print(sol.hasPathSum(Ex, 1))
    
