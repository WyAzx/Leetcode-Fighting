# 解题思路：
# dp
# dp[i][j][k] 表示 boxs[i,j+1]的盒子且前面有k个与boxs[i]相同数字盒子可以得到的最大分数
# dp[i][j][k] = max(
#                    dp[i+1][j][0] + (k+1)^2
#                    dp[i+1][next[boxs[i]]-1][0] + dp[next[boxs[i]]][j][k+1]     next[dp[i]] -> 下一个与boxs[i]数字相同的位置
#                   )
from collections import defaultdict
from typing import List
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        rec = defaultdict(list)
        for i, box in enumerate(boxes):
            rec[box].append(i)
        next_dict = {}
        for _, idxs in rec.items():
            for i in range(len(idxs)-1):
                next_dict[idxs[i]] = idxs[i+1]
        memo = {}
        def dp(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            if i > j:
                return 0
            if i == j:
                return (k+1)**2
            while i < j and boxes[i] == boxes[i+1]:
                i += 1
                k += 1

            max_score = (k+1)**2 + dp(i+1, j, 0)
            pos = i
            while pos in next_dict:
                next_pos = next_dict[pos]
                if next_pos > j:
                    break
                max_score = max(max_score,  dp(i+1, next_pos-1, 0) + dp(next_pos, j, k+1))
                pos = next_pos
            memo[(i ,j ,k)] = max_score
            return max_score
        res = dp(0, len(boxes)-1, 0)
        return res


