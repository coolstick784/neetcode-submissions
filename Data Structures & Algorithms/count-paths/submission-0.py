class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for _ in range(n)] for _ in range(m)]
        for r in range(m):
            dp[r][0] = 1
        for c in range(n):
            dp[0][c] = 1
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row][col-1] + dp[row-1][col]
        return dp[m-1][n-1]