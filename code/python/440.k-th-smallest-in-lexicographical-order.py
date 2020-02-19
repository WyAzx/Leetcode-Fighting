class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        def count(prefix):
            next_prefix = prefix + 1
            cur = prefix
            cnt = 0
            while cur <= n:
                cnt += min(n+1, next_prefix) - cur
                cur *= 10
                next_prefix *= 10
            return cnt
        
        prefix = 1
        agg = 0
        while agg < k - 1:
            c = count(prefix)
            if agg + c >= k:
                agg += 1
                prefix *= 10
            elif agg + c < k:
                agg += c
                prefix += 1
        return prefix
