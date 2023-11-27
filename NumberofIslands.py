class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        def isVal(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == '0':
                return

            grid[row][col] = '0'

            isVal(row - 1, col)
            isVal(row + 1, col)
            isVal(row, col - 1)
            isVal(row, col + 1)

        m, n = len(grid), len(grid[0])
        islands_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands_count += 1
                    isVal(i, j)

        return islands_count
