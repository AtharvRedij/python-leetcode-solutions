from heapq import heappush, heappop

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        for i in range(len(mat)):
            heappush(heap, (mat[i].count(1), i))

        return [heappop(heap)[1] for _ in range(k)]
