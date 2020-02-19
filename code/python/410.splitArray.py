# Tag:二分搜索
from typing import List
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l+r)//2
            cnt, s = 1, 0
            for n in nums:
                if s + n <= mid:
                    s += n
                else:
                    cnt += 1
                    s = n
            if cnt > m:
                l = mid + 1
            else:
                r = mid
        return l