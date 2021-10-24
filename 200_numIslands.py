class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        row = len(grid)
        col = len(grid[0])
        def bfs(node):
            if node in visited:
                return
            visited.add(node)
            # print(visited)
            r, c = node[0], node[1]
            if c - 1 >= 0 and grid[r][c-1] == "1":
                # print((r, c-1), grid[r][c-1])
                bfs((r, c - 1))
            if c + 1 < col and grid[r][c+1] == "1":
                # print((r, c+1), grid[r][c+1])
                bfs((r, c + 1))
            if r - 1 >= 0 and grid[r-1][c] == "1":
                # print((r - 1, c), grid[r - 1][c])
                bfs((r - 1, c))
            if r + 1 < row and grid[r+1][c] == "1":
                # print((r+1, c), grid[r+1][c])
                bfs((r+1, c))
        
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # print("found")
                    bfs((r, c))
                    count += 1

        return count

if __name__ == "__main__":
    print("hello")
    sol = Solution()