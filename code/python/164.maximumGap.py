# Tag:排序
# 解题思路：
# 桶排序
# 为了使得最后比较次数小，并且额外空间尽可能小 -> 桶只保留最大最小值
# 避免在桶内产生最大的间隔 -> 设置桶的大小为最大间隔最小的情况 -> ceil((max-min)/n-1)
# 比较桶间的最大间隔
from typing import List
import math 
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        minn, maxn = min(nums), max(nums)
        d = math.ceil((maxn-minn)/(len(nums)-1))
        if d == 0:
            return 0
        buckets = [[maxn, minn, 0] for _ in range(math.ceil((maxn-minn+1)/d))] # [最小值， 最大值， 元素个数]
        for n in nums:
            bucket_idx = (n - minn) // d
            buckets[bucket_idx][0] = min(n, buckets[bucket_idx][0])
            buckets[bucket_idx][1] = max(n, buckets[bucket_idx][1])
            buckets[bucket_idx][2] += 1
        pre_max = buckets[0][1]
        max_interval = 0
        for bucket in buckets[1:]:
            if bucket[2] > 0:
                max_interval = max(max_interval, bucket[0]-pre_max)
                pre_max = bucket[1]
        return max_interval