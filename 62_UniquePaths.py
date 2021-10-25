class Solution:
    #12:27 - 12:37
    #Runtime: 48.56% Memory: 8.07%
    def uniquePaths_topdown(self, m: int, n: int) -> int:
        Opt = {}
        def dp(i, j):
            if i <= 0 or j <= 0:
                return 0
            if i == 1 or j == 1:
                return 1
            if (i , j) in Opt:
                return Opt[(i, j)]
            Opt[(i, j)] = dp(i - 1, j) + dp(i, j -1)
            return Opt[(i, j)]
        return dp(m, n)

    #12:38 - 12:45
    #Runtime:  90.76% Memory: 86.48%
    #Let Opt[i, j] be the # of unqiue path in grid i, j. Opt[i, j] = Opt[i-1, j] + Opt[i, j - 1]
    def uniquePaths_bottomup(self, m: int, n: int) -> int:
        Opt = []
        for i in range(m + 1):
            Opt.append([])
            for j in range(n + 1):
                if i == 0 or j == 0:
                    Opt[i].append(0)
                elif i == 1 or j == 1:
                    Opt[i].append(1)
                else:
                    Opt[i].append(0)
        for i in range(m + 1):
            for j in range(n + 1):
                if i > 1 and j > 1:
                    Opt[i][j] = Opt[i - 1][j] + Opt[i][j - 1]
        return Opt[m][n]
        