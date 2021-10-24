class Solution:
    #6:36 - 7:08 Time limit exceed
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        Opt = []
        for i in range(len(text1)):
            Opt.append([])
            for j in range(len(text2)):
                Opt[i].append(0)
        result = 0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    Opt[i][j] = 1
                    for u in range(0, i):
                        for v in range(0, j):
                            if text1[u] == text2[v]:
                                Opt[i][j] = max(Opt[i][j], Opt[u][v] + 1)
                    result = max(result, Opt[i][j])
                
        return result
    #Runtime: 12.40% Memory: 12.71%
    #Let Opt(i, j) be LCS in text1[ i : ] and text2[ j : ]. If text1[i] == text2[j], Opt(i, j) = Opt(i + 1, j + 1) + 1. Else Opt(i, j) = Max(Opt(i + 1, j ), Opt(i, j + 1)) 
    def longestCommonSubsequence_topdown(self, text1: str, text2: str) -> int:
        Opt = {}
        def dp(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if (i, j) in Opt:
                return Opt[(i, j)]
            if text1[i] == text2[j]:
                Opt[(i, j)] = 1 + dp(i + 1, j + 1)
            elif text1[i] != text2[j]:
                Opt[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))
            return Opt[(i, j)]
        return dp(0, 0)
        
    #Runtime: 35.35% Memory: 55.34%
    #Let Opt(i, j) be LCS in text1[ : i ] and text2[ : j ]. If text1[i] == text2[j], Opt(i, j) = Opt(i - 1, j - 1) + 1. Else Opt(i, j) = Max(Opt(i - 1, j ), Opt(i, j - 1)) 
    def longestCommonSubsequence_bottomup(self, text1: str, text2: str) -> int:
        Opt = []
        for i in range(len(text1)):
            Opt.append([])
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    Opt[i].append(1)
                else:
                    Opt[i].append(0)

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j] and i > 0 and j > 0:
                    Opt[i][j] = Opt[i - 1][j - 1] + 1
                elif text1[i] != text2[j]:
                    l1, l2 = 0, 0
                    if i > 0:
                        l1 = Opt[i - 1][j]
                    if j > 0:
                        l2 = Opt[i][j - 1]
                    Opt[i][j] = max(l1, l2)
                
        return Opt[len(text1) - 1][len(text2) - 1]