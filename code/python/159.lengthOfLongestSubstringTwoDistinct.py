from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        rec = defaultdict(int)
        cs = set()
        start = 0
        maxl = 0
        for end, c in enumerate(s):
            rec[c] += 1
            cs.add(c)
            while len(cs) > 2:
                rec[s[start]] -= 1
                if rec[s[start]] == 0:
                    cs.remove(s[start])
                start += 1
            maxl = max(maxl, end-start+1)
        return maxl