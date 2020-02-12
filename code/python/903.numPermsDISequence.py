# 解题思路：
# 由易到难 可以考虑一种简单的状态
# （0，2，1） ： 'ID'
# 下一步需要在序列后面加入一个数字满足‘D’/‘I’并且不改变之前的关系，只需要将前面大于等于这个数字的数+1
# 当此时为‘D’：可以加入小于等于最后一位的数
#        ‘I'：可以加入大于最后一位的数
# dp[i][j] i 序列长度 j 最后末尾数字 j<=i
# dp[i][j]
from collections import defaultdict
class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 1e9 + 7
        rec = {0:1}
        for i, c in enumerate(S):
            new_rec = defaultdict(int)
            for k, v in rec.items():
                cand = range(k+1) if c == 'D' else range(k+1,i+2)
                for n in cand:
                    new_rec[n] = (new_rec[n] + v) % MOD
            rec = new_rec
        res = 0
        for v in rec.values():
            res = (res + v) % MOD
        return int(res)

# 题解：https://www.cnblogs.com/grandyang/p/11094525.html
class Solution2:
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [1] * (len(S) + 1)
        for c in S:
            if c == "I":
                dp = dp[:-1]
                for i in range(1, len(dp)):
                    dp[i] += dp[i - 1]
            else:
                dp = dp[1:]
                for i in range(len(dp) - 1)[::-1]:
                    dp[i] += dp[i + 1]
        return dp[0] % (10**9 + 7)

