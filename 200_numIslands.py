class Solution(object):
    #Runtime:  93.61% Memory: 5.56%
    #use dfs when encountering each island, check all directions and continue until reaching the border.
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        row = len(grid)
        col = len(grid[0])
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            # print(visited)
            r, c = node[0], node[1]
            if c - 1 >= 0 and grid[r][c-1] == "1":
                # print((r, c-1), grid[r][c-1])
                dfs((r, c - 1))
            if c + 1 < col and grid[r][c+1] == "1":
                # print((r, c+1), grid[r][c+1])
                dfs((r, c + 1))
            if r - 1 >= 0 and grid[r-1][c] == "1":
                # print((r - 1, c), grid[r - 1][c])
                dfs((r - 1, c))
            if r + 1 < row and grid[r+1][c] == "1":
                # print((r+1, c), grid[r+1][c])
                dfs((r+1, c))
        
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # print("found")
                    dfs((r, c))
                    count += 1

        return count

    #Runtime:  43.27% Memory: 9.41%
    #Create a 2D disjoint set to map out parents, and a 2D array to store the rank of each node, 0 or 1 by default. for each island encounter, check and union previous (i - 1, j) or (i, j -1). Find positive ranks at the end
    def numIslands_disjointset(self, grid: List[List[str]]) -> int:
        disjoint_set = []
        rank = []
        def find(i, j, disjoint_set):
            if disjoint_set[i][j] == (i, j):
                return (i, j)
            p = disjoint_set[i][j]
            disjoint_set[i][j] = find(p[0], p[1], disjoint_set)
            return disjoint_set[i][j]
        def union(i, j, x, y, disjoint_set, rank):
            p1 = find(i, j, disjoint_set)
            p2 = find(x, y, disjoint_set)
            #print(p1, p2)
            if p1 != p2:
                rank1 = rank[p1[0]][p1[1]]
                rank2 = rank[p2[0]][p2[1]]
                if rank1 >= rank2:
                    disjoint_set[p2[0]][p2[1]] = p1
                    rank[p1[0]][p1[1]] = rank1 + rank2
                    rank[p2[0]][p2[1]] = 0
                else:
                    disjoint_set[p1[0]][p1[1]] = p2
                    rank[p2[0]][p2[1]] = rank1 + rank2
                    rank[p1[0]][p1[1]] = 0
                    
        for i in range(len(grid)):
            disjoint_set.append([])
            rank.append([])
            for j in range(len(grid[i])):
                disjoint_set[i].append((i, j))
                if grid[i][j] == "1":
                    rank[i].append(1)
                else:
                    rank[i].append(0)
        #print(rank)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    if i > 0 and grid[i - 1][j] == "1":
                        union(i, j, i-1, j, disjoint_set, rank)
                    if j > 0 and grid[i][j - 1] == "1":
                        union(i, j, i, j-1, disjoint_set, rank)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if rank[i][j] > 0:
                    result += 1
        return result
if __name__ == "__main__":
    print("hello")
    sol = Solution()