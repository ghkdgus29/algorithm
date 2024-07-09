class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j]

        h = len(grid)
        w = len(grid[0])
        s = [[0] * (w + 1) for _ in range(h + 1)]
        cnt = 0
        for y in range(1, h + 1):
            for x in range(1, w + 1):
                s[y][x] = s[y - 1][x] + s[y][x - 1] - s[y - 1][x - 1] + grid[y - 1][x - 1]
                if s[y][x] <= k:
                    cnt += 1

        return cnt
