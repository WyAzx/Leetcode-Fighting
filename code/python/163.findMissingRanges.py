from typing import List
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        pre = lower-1
        res = []
        for n in nums + [upper+1]:
            if n - pre == 2:
                res.append(str(n-1))
            elif n - pre > 2:
                res.append(f'{pre+1}->{n-1}')
            pre = n
        return res
    