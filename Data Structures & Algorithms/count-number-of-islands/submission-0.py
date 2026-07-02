from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        r = len(grid)
        c = len(grid[0])
        count = 0
        q = deque()

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    count += 1
                    grid[i][j] = "0"
                    q.append((i, j))

                    while len(q) > 0:
                        curr_r, curr_c = q.popleft()
                        adjpos = [
                            (curr_r - 1, curr_c),
                            (curr_r + 1, curr_c),
                            (curr_r, curr_c - 1),
                            (curr_r, curr_c + 1)
                        ]

                        for nr, nc in adjpos:
                          if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == "1":
                              grid[nr][nc] = "0"
                              q.append((nr, nc))

        return count