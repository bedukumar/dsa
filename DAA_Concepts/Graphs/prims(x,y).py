from typing import List
import heapq


class S:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        # adj= {0:[[cost,node],[],[]],1:[cost,node],2:[cost,node],...}  distance between from i to node
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # prim's
        res = 0
        visit = set()
        minH = [[0, 0]]  # [cost,point]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res


s = S()
x = s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
print(x)
# adj = {i: [] for i in range(5)}  # {0:[cost,node],1:[cost,node],...}
# print(adj, type(adj[0]), type(adj))
