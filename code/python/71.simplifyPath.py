class Solution:
    def simplifyPath(self, path: str) -> str:
        r = []
        for p in path.split('/'):
            r = {'':r, '.':r, '..':r[:-1]}.get(p, r+[p])
        return '/' + '/'.join(r)


if __name__ == "__main__":
    print(Solution().simplifyPath('/a/c/../b'))
