# Tag:字符串
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        rec = [0]
        lines = input.split('\n')
        maxd = 0
        for line in lines:
            lev = line.count('\t')
            lenl = len(line) - lev
            rec = rec[:lev+1]
            if '.' in line:
                maxd = max(maxd, rec[-1]+lenl+lev)
            rec.append(rec[-1]+lenl)
        return maxd