class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 1 and len(board[0]) == 1:
            return board
        #find islands
        def dfs(i, j, visited, island):
            if (i, j) not in visited:
                island.append((i, j))
                visited.add((i, j))
                if i - 1 >= 0 and board[i - 1][j] == "O":
                    dfs(i-1, j, visited, island)
                if i + 1 < len(board) and board[i + 1][j] == "O":
                    dfs(i + 1, j, visited, island)
                if j - 1 >= 0 and board[i][j - 1] == "O":
                    dfs(i, j - 1, visited, island)
                if j + 1 < len(board[0]) and board[i][j + 1] == "O":
                    dfs(i, j + 1, visited, island)
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                island = []
                if board[i][j] == "O" and (i, j) not in visited:
                    dfs(i, j, visited, island)
                    border = False
                    for p in island:
                        if p[0] == 0 or p[0] == len(board) - 1 or p[1] == 0 or p[1] == len(board[0]) - 1:
                            border = True
                    if not border:
                        for p in island:
                            x, y = p[0], p[1]
                            board[x][y] = "X"
        return board

    def solve2(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 1 and len(board[0]) == 1:
            return board
        #find islands
        def dfs(i, j, visited, island):
            if (i, j) not in visited:
                island.append((i, j))
                visited.add((i, j))
                if i - 1 >= 0 and board[i - 1][j] == "O":
                    dfs(i-1, j, visited, island)
                if i + 1 < len(board) and board[i + 1][j] == "O":
                    dfs(i + 1, j, visited, island)
                if j - 1 >= 0 and board[i][j - 1] == "O":
                    dfs(i, j - 1, visited, island)
                if j + 1 < len(board[0]) and board[i][j + 1] == "O":
                    dfs(i, j + 1, visited, island)
        visited = set()
        #visite all the baorder O first
        for j in range(len(board[0])):
            island = []
            if board[0][j] == "O" and (0, j) not in visited:
                dfs(0, j, visited, island)
            if board[len(board) - 1][j] == "O" and (len(board) - 1, j) not in visited:
                dfs(len(board) - 1, j, visited, island)
        for i in range(len(board)):
            island = []
            if board[i][0] == "O" and (i, 0) not in visited:
                dfs(i, 0, visited, island)
            if board[i][len(board[i]) - 1] == "O" and (i, len(board[i]) - 1) not in visited:
                dfs(i, len(board[i]) - 1, visited, island)
                
        for i in range(len(board)):
            for j in range(len(board[i])):
                island = []
                if board[i][j] == "O" and (i, j) not in visited:
                    dfs(i, j, visited, island)
                    for p in island:
                        x, y = p[0], p[1]
                        board[x][y] = "X"
        return board