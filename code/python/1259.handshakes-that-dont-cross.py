class Solution:
    def numberOfWays(self, num_people: int) -> int:
        if not num_people:
            return 0
        MOD = 10**9 + 7
        dp = [1 if i in [0,1] else 0 for i in range(num_people//2+1)]
        for i in range(2, num_people//2+1):
            for j in range(i):
                dp[i] += (dp[j] * dp[i-j-1])%MOD
        return dp[-1]%MOD