# TAG:动态规划
class Solution:
    def encode(self, s: str) -> str:
        dp = [['' for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
                dp[i][j] = s[i:j+1]
        for width in range(2, len(s)+1):
            for start in range(len(s)-width+1):
                end = start + width - 1
                for k in range(start, end):
                    if width % (k-start+1) == 0 and (width // (k-start+1)) * s[start:k+1] == s[start:end+1]:
                        new_s = f'{width // (k-start+1)}[{dp[start][k]}]'
                        if len(new_s) < len(dp[start][end]):
                            dp[start][end] = new_s
                            break
                    l = len(dp[start][k]) + len(dp[k+1][end])
                    if l < len(dp[start][end]):
                        dp[start][end] = dp[start][k] + dp[k+1][end]
        print(dp)
        return dp[0][len(s)-1]

