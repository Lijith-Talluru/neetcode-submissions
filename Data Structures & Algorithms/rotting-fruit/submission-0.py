from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        r = len(grid)
        c = len(grid[0])
        fresh_oranges = 0

        for i in range(0, r):
            for j in range(0, c):
                if grid[i][j] == 2:
                    q.append((i, j, 0))   
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        time = 0

        while len(q) > 0:
            x = q.popleft()
            curr_r, curr_c, curr_t = x[0], x[1], x[2]
            time = curr_t
            
            adjpos = [
                (curr_r - 1, curr_c, curr_t + 1),
                (curr_r + 1, curr_c, curr_t + 1),
                (curr_r, curr_c - 1, curr_t + 1),
                (curr_r, curr_c + 1, curr_t + 1)
            ]
            
            for neighbours in adjpos:
                nr, nc, nt = neighbours
                if 0 <= nr < r and 0 <= nc < c and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges -= 1
                    q.append((nr, nc, nt))

        if fresh_oranges > 0:
            return -1
        else:
            return time