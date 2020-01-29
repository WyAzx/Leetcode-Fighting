class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # 前向后向匹配，比较第一个不相同位置
        if s == t:
            return False  
        if len(t) > len(s):
            s, t = t, s
        fori = 0
        while fori < len(t) and s[fori] == t[fori]:
            fori += 1
        baci, bacj = len(s)-1, len(t)-1
        while bacj >= 0 and s[baci] == t[bacj]:
            baci -= 1
            bacj -= 1
        return fori == baci or fori == len(s) or baci == 0