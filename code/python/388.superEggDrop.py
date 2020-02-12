# 解题思路
# dp
# K：鸡蛋个数   m：测试次数
# dp[K][m]: K个鸡蛋测试m次最多可以测试楼层数
# base case：k=1 dp=m, m=1 dp=1
# 转移方程 dp[k][m] = dp[k-1][m-1] + dp[k][m-1] + 1
class Solution(object):
    def superEggDrop(self, K: int, N: int) -> int:
            dp = [0] * (K + 1)
            m = 0
            while dp[K] < N:
                m += 1
                for k in range(K, 0, -1):
                    # print(m, k)
                    dp[k] = dp[k - 1] + dp[k] + 1
            return m