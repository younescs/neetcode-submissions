class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        max_area = 0
        
        def bfs(i,j):
            nonlocal max_area
            queue = collections.deque([(i,j)])
            seen.add((i, j))
            directions = ([1, 0], [0, 1], [-1, 0], [0, -1])
            area = 1
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in seen and grid[nr][nc] == 1:
                        area += 1
                        seen.add((nr, nc))
                        queue.append((nr, nc))

            max_area = max(area, max_area)
          
          
        for i in range(rows):
            for j in range(cols):
            	if (i,j) not in seen and grid[i][j] == 1:
              	    bfs(i,j)
                
        return max_area