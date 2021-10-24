class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = [s[0]]
        for i in range(1, len(s)):
            if len(stack) != 0:
                if stack[-1] == "(" and s[i] == ")":
                    stack.pop()
                elif stack[-1] == "[" and s[i] == "]":
                    stack.pop()
                elif stack[-1]  == "{" and s[i] == "}":
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return len(stack) == 0