class Solution(object):
    def findCircleNum_set(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        result = []
        for r in range(len(isConnected)):
            tmp = set()
            for i in range(len(isConnected)):
                if isConnected[r][i] == 1:
                    tmp.add(i)
            unique_province = True
            for i, s in enumerate(result):
                if s.intersection(tmp):
                    result[i] = s.union(tmp)
                    unique_province = False
            if unique_province:
                result.append(tmp)
        ans = []
        while result:
            s1 = result.pop()
            i = 0
            while i < len(result):
                s2 = result[i]
                if s1.intersection(s2):
                    s1 = s1.union(s2)
                    result.pop(i)
                    continue
                i += 1
            ans.append(s1)
        

        return len(ans)
    
    def findCircleNum_dfs(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        N = len(isConnected)
        visited = set()
        def dfs(node):
            visited.add(node)
            for i in range(N):
                if isConnected[i][node] and i not in visited:
                    dfs(i)
        count = 0
        for i in range(N):
            if i not in visited:
                count += 1
                dfs(i)
        return count

if __name__ == "__main__":
    print("hello")
    sol = Solution()
    result = [set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), set([0, 1, 2, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])]

    # print(len(result))
