import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
heapq.heapify(heap) # 최소 힙

for _ in range(N):
    x = int(input())
    if x == 0:
        print(0) if not heap else print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
