class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #the plan is to go from the treasure chest cells and attempt to reach 

        rows = len(grid)
        cols = len(grid[0])
        queue = collections.deque()
        visited = set()
        directions = ([1,0], [0,1], [-1,0], [0,-1])
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j)) 


        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) not in visited and nr in range(rows) and nc in range(cols) and grid[nr][nc] > 0:
                        grid[nr][nc] = grid[r][c] + 1
                        visited.add((nr, nc))
                        queue.append((nr,nc))
                    