class Solution:
    #7:15 - 8:32
    #Runtime:  24.74% Memory: 7.48%
    #Let Opt[i] be the # of ways to decode s[i :]. Opt[i] = Opt[i+1], If s[i]s[i+1] <= 26, Opt[i] + Opt[i+2], If s[i+1] = 0, and s[i] > 2, Opt[i] = 0. Watch out all the edge cases
    def numDecodings(self, s: str) -> int:
        Opt = {}
        def dp(i):
            print(s[i:])
            if i >= len(s):
                return 0
            if s[i] == "0":
                return 0
            if i in Opt:
                return Opt[i]
            if i == len(s) - 1:
                return 1
            if i + 1 == len(s) - 1 and s[i+1] != "0":
                if (int(s[i]) * 10 + int(s[i + 1]) <= 26):
                    return 2
                return dp(i + 1)
            if i + 1 == len(s) - 1 and s[i+1] == "0":
                if (int(s[i]) * 10 <= 26):
                    return 1
                return 0
            Opt[i] = 0
            if i + 1 < len(s) and s[i+1] == "0":
                if (int(s[i]) * 10 + int(s[i + 1])) <= 26:
                    Opt[i] = dp(i+2)
                    return Opt[i]
                else:
                    return 0
            elif i + 1 < len(s) and s[i+1] != "0":
                Opt[i] += dp(i + 1)
            if i + 2 < len(s) and (int(s[i]) * 10 + int(s[i + 1])) <= 26:
                Opt[i] += dp(i + 2)
            return Opt[i]
        return dp(0)