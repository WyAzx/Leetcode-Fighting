# 解题思路
# dp
# dp[k][i][j] i：有i个A，j：有连续j个L
# dp[k+1][0][0] = dp[k][0][1] + dp[k][0][0] + dp[k][0][2]
# dp[k+1][1][0] = dp[k][1][1] + dp[k][1][0] + dp[k][0][0] + dp[k][0][1] + dp[k][0][2] + dp[k][1][2]
# dp[k+1][0][2] = dp[k][0][1]
# dp[k+1][1][2] = dp[k][1][1]
# dp[k+1][0][1] = dp[k][0][0]
# dp[k+1][1][1] = dp[k][1][0]
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9+7 #写成1e9+7会变成float类型
        # (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)
        dp = [1, 1, 0, 1, 0, 0]
        for _ in range(n-1):
            dp = [(dp[0]+dp[1]+dp[2])%MOD,
                  dp[0],
                  dp[1],
                  sum(dp)%MOD,
                  dp[3],
                  dp[4]]
        return sum(dp) % MOD