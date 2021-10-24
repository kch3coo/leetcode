class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 0:
            return 0
        l = 0
        r = 0
        ans = 1
        cache = {s[0],}
        while r < len(s) and l < len(s):
            ans = max(ans, len(cache))
            if r + 1 < len(s) and s[r + 1] not in cache:
                cache.add(s[r + 1])
                r += 1
            else:
                cache.remove(s[l])
                l += 1
            # print(l, r, cache)
        return ans