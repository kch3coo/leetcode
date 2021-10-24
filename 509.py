# Definition for a binary tree node.
from math import log
class Solution(object):
    def __init__(self):
        self.M = {}
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.M:
            return self.M[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        self.M[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.M[n]

if __name__ == "__main__":
    print("hello")
    sol = Solution()
    print(sol.fib(4))

    
