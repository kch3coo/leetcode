class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        temp_stack = []
        result = {}
        for i in range(len(temperatures) - 1, -1 , -1):
            curr_temp = temperatures[i]
            while temp_stack:
                if curr_temp >= temperatures[temp_stack[-1]]:
                    temp_stack.pop(-1)
                else:
                    result[i] = temp_stack[-1]
                    temp_stack.append(i)
                    break
            
            if not temp_stack:
                temp_stack.append(i)
                result[i] = i
        return [0 if i == result[i] else result[i] - i for i in range(len(temperatures))]