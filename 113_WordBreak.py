class Solution:
    #Runtime: 72.89% Memory: 70.51%
    #Let Opt[i] represent if s[0:i] can be word break. If s[ : i] in wordDict, Opt[i] = True. Elif any Opt[j] and s[ j : i ] in wordDict where 0 <= j < i
    def wordBreak_bottomup(self, s: str, wordDict: List[str]) -> bool:
        Opt = [False] * (len(s) + 1)
        for i in range(len(s) + 1):
            if s[:i] in wordDict:
                Opt[i] = True
            else:
                for j in range(0, i):
                    if s[j : i] in wordDict and Opt[j]:
                        Opt[i] = True
                        break
        return Opt[len(s)]