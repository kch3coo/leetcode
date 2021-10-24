class Solution(object):
    map = {}
    map[1] = 1
    map[2] = 2
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n in self.map:
            return self.map[n]
    
        if n == 1:
     
            return 1
        elif n == 2:
     
            return 2
        sol = 0
        if n - 1 > 0:
            sol += self.climbStairs(n - 1)
        if n - 2 > 0:
            sol += self.climbStairs(n - 2)
        self.map[n] = sol
        return sol

    def climbStairs_bottomup(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        prev_1 = 1
        prev_2 = 1
        for i in range(2, n):
            curr = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = curr
        return prev_1 + prev_2
            