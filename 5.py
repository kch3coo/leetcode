class Solution(object):
    def longestPalindrome_timelimit_exceed(self, s):
        """
        :type s: str
        :rtype: str
        """
        Map = {}
        ans = {}
        def dpPalindrome(i, j):
            if (i, j) in Map:
                return Map[(i, j)]
            if i == j:
                Map[(i, j)] = 1
                ans[1] = i, j
                return 1
            elif i + 1 == j and s[i] == s[j]:
                Map[(i, j)] = 2
                ans[2] = i, j
                return 2
            
            if s[i] == s[j]:
                m = dpPalindrome(i + 1, j - 1)
                if m == j - 1 - (i + 1) + 1:
                    ans[m + 2] = (i, j)
                    Map[(i, j)] = m + 2
                    return Map[(i, j)]
            r = dpPalindrome(i, j - 1)
            l = dpPalindrome(i + 1, j)
            longest = max(r, l)
            if r > l:
                Map[(i, j)] = r
                return r
           
            Map[(i, j)] = l
            return l
            
        max_len = dpPalindrome(0, len(s) - 1)
        i, j = ans[max_len]
        return s[i : j + 1]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_len = 0
        result = ""
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:

                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    result = s[l : r + 1]
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    result = s[l : r + 1]
                l -= 1
                r += 1
        
        return result