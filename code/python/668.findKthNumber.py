# Tag:二分搜索
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 1, m*n
        while l < r:
            mid = (l + r) // 2
            cnt = 0
            for i in range(1,m+1):
                cnt += min(n, mid//i)
            if cnt >= k:
                r = mid
            else:
                l = mid + 1
        return l