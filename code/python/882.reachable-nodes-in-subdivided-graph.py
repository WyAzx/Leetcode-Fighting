# TAG: 图
from typing import List
import heapq
class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        # 1.计算到达节点最短距离
        # 2.边上可到达节点=min(边上节点数， 2*M-d_A-d_B)
        dis = [float('inf') for _ in range(N)]
        heap = [(0, 0)]
        graph = [{} for _ in range(N)]
        for s, e, l in edges:
            graph[s][e] = l+1
            graph[e][s] = l+1
        while heap:
            min_l, min_v = heapq.heappop(heap)
            if dis[min_v] <= min_l:
                continue
            dis[min_v] = min_l
            for k, l in graph[min_v].items():
                if dis[min_v] + l < dis[k]:
                    heapq.heappush(heap, (dis[min_v]+l, k))
        res = sum([d<=M for d in dis])
        for s, e, l in edges:
            res += min(l, 2*M-min(M, dis[s])-min(M, dis[e]))
        return res
