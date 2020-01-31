# Tag:Nice
from typing import List
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 可以分别考虑开始结束时间
        # 结束 -> 有空放假
        # 开始 -> 需要空房间 若没有则新建一个房间
        # 对开始和结束时间分别排序
        start_times = sorted([interval[0] for interval in intervals])
        end_times = sorted([interval[1] for interval in intervals])
        room_nums = 0
        last_room_idx = 0
        for st in start_times:
            if st >= end_times[last_room_idx]:
                last_room_idx += 1
            else:
                room_nums += 1
        return room_nums
