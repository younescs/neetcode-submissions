class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        counter = 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]


        def bfs(i,j):
            queue = collections.deque([[i,j]])
            visited.add((i,j))

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr,nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and (nr,nc) not in visited and grid[nr][nc] == "1":
                        queue.append((nr,nc))
                        visited.add((nr,nc))


        


        for i in range(rows):
            for j in range(cols):
            
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs(i,j)
                    counter +=1


        return counter

        