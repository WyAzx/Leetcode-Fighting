class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        # 效率 替换 > 插入 > 删除
        # 当小于6只需要做插入
        # 当小于等于20只需要替换
        # 当大于20需要删除+替换
        missing = 3
        if any(c.isdigit() for c in s):
            missing -= 1
        if any(c.isupper() for c in s):
            missing -= 1
        if any(c.islower() for c in s):
            missing -= 1
        need_replace = 0
        p = 2
        one, two = 0, 0
        while p < len(s):
            if s[p] == s[p-1] == s[p-2]:
                repeat = 2
                while p < len(s) and s[p] == s[p-1]:
                    p += 1
                    repeat += 1
                need_replace += repeat // 3
                if repeat % 3 == 0:
                    # 此时一个del操作可以替换一个replace操作
                    one += 1
                elif repeat % 3 == 1:
                    # 此时两个个del操作可以替换一个replace操作
                    two += 1
                # 其他情况三个del操作可以替换一个replace
            else:
                p += 1
        if len(s) < 6:
            return max(missing, 6 - len(s))
        elif len(s) <= 20:
            return max(missing, need_replace)
        else:
            need_del = remain_del = len(s) - 20
            # 此时尽量有所有的del操作替换replace
            if remain_del:
                need_replace -= min(one, remain_del)
                remain_del -= min(one, remain_del)
            if remain_del:
                need_replace -= min(two, remain_del // 2)
                remain_del -= min(two, remain_del // 2) * 2
            if remain_del:
                need_replace -= min(need_replace, remain_del // 3)
                remain_del -= min(need_replace, remain_del // 3) * 3
            return need_del + max(missing, need_replace)

                