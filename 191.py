class Solution:
    #Approach1: Use bin() to convert integer to binary. 
    def hammingWeight_ans1(self, n: int) -> int:
        b = ""
        if n >= 0:
            b = bin(n)[2:]
        else:
            b = bin(n)[3:0]
        acc = 0

        for i in range(len(b)):
            if b[i] == "1":
                acc += 1
        return acc
    #Approach2: use (2**i & n) to find out which index contains 1 faster than 73.32%
    def hammingWeight_ans2(self, n: int) -> int:
        acc = 0
        for i in range(32):
            if 2 ** i & n:
                acc += 1
        return acc
    # Approach3: n % 2 gives whether the last bit is 1, and we can combine this with n >> 1, to check every bit
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            if n % 2 == 1:
                result += 1
            n = n >> 1
        return result
