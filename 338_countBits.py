class Solution:

    def countBits_ans1(self, n: int) -> List[int]:

        def count1s(num):
            res = 0
            while num != 0:
                res += num & 1
                num = num >> 1
            return res
        
        result = []
        for i in range(n + 1):
            result.append(count1s(i))
        return result

    def countBits_ans2(self, n: int) -> List[int]:
        result = [0]
        while(len(result) <= n):
            next_bit = [i + 1 for i in result]
            result += next_bit
        return result[:n + 1]
            