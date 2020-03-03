from typing import List

class Solution:
    def intersection(self, start1: List[int], end1: List[int],
                     start2: List[int], end2: List[int]) -> List[float]:
        
        def getLine(start, end):
            x1, y1 = start
            x2, y2 = end
            return (y2 - y1, x1 - x2, x2 * y1 - x1 * y2)

        def inLine(x, y):
            for s, e in ((start1, end1), (start2, end2)):
                mnx = min(s[0], e[0])
                mxx = max(s[0], e[0])
                mny = min(s[1], e[1])
                mxy = max(s[1], e[1])
                if not (mnx <= x <= mxx and mny <= y <= mxy):
                    return False
            return True

        a1, b1, c1 = getLine(start1, end1)
        a2, b2, c2 = getLine(start2, end2)
        if a1 * b2 == a2 * b1:
            # 平行
            if c1 != c2:
                return []
            # 共线, 需要额外判断交点是否在两条线段上
            res = []
            for p in (start1, end1, start2, end2):
                if inLine(p[0], p[1]):
                    if not res or p[0] < res[0] or p[0] == res[
                            0] and p[1] < res[1]:
                        res = p
            return res

        # 不平行, 分母不为0
        # 可以计算交点了
        x = (c2 * b1 - c1 * b2) / (a1 * b2 - a2 * b1)
        y = (c1 * a2 - c2 * a1) / (a1 * b2 - a2 * b1)
        if inLine(x, y):
            return [x, y]
        else:
            return []

#LJ solution
class Solution2:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        start1, end1 = sorted([start1, end1], key=lambda x: [x[0], x[1]])
        start2, end2 = sorted([start2, end2], key=lambda x: [x[0], x[1]])

        def cal_k_b(start, end):
            dely, delx = end[1]-start[1], end[0]-start[0]
            if delx == 0:
                return float("inf"), start1[1]
            k = dely / delx
            b = start[1] - k*start[0]
            return k, b
        k1, b1 = cal_k_b(start1, end1)
        k2, b2 = cal_k_b(start2, end2)

        if k1 < k2:
            k1, b1, k2, b2 = k2, b2, k1, b1
            start1, end1, start2, end2 = start2, end2, start1, end1
        elif k1 == k2:
            if b1 > b2:
                k1, b1, k2, b2 = k2, b2, k1, b1
                start1, end1, start2, end2 = start2, end2, start1, end1
        
        if k1 == float('inf'):
            if k2 == float('inf'):
                if start1[0] == start2[0] and end1[1] > end2[1]:
                    return [start1[0], max(start1[1], start2[1])]
                else:
                    return []
            elif start2[0] <= start1[0] and end2[0] >= start1[0]:
                return [start1[0], start1[0]*k2+b2]
            else:
                return []

        if k1 == k2 and b1 == b2:
            if max(start1[0], start2[0]) <= min(end1[0], end2[0]):
                return [max(start1[0], start2[0]),max(start1[0], start2[0])*k1+b1]
            else:
                return []
        
        l = max(start1[0], start2[0])
        r = min(end1[0], end2[0])
        if k1*l+b1 > k2*l+b2 or k1*r+b1 < k2*r+b2:
            return []
        x = (b2-b1)/(k1-k2)
        y = k1*x+b1
        return [x,y]