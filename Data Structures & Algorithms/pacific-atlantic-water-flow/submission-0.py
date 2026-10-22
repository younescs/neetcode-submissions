class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        directions = ([1, 0], [0, 1], [-1, 0], [0, -1])


        def dfs(r, c, visited, prevHeight):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or heights[r][c] < prevHeight:
                return

            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visited, heights[r][c])
            

        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i,cols-1, atlantic, heights[i][cols-1])

        for j in range(cols):
            dfs(0, j, pacific, heights[0][j])
            dfs(rows -1, j, atlantic, heights[rows-1][j])


        return [[i, j] for (i,j) in pacific & atlantic]
        