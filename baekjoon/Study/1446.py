import sys
import heapq
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    # 가중치가 가장 작은 노드부터 방문
    heapq.heappush(queue, (0, start))
    distances[start] = 0
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
        if curr_dist > distances[curr_node]:
            continue
        
        for node, dist in shorts[curr_node]:
            cost = curr_dist + dist
            if distances[node] > cost:
                distances[node] = cost
                heapq.heappush(queue, (cost, node))

if __name__ == "__main__":
    num_short, len_highway = map(int, input().split())
    # 모든 노드는 다음 노드와 연결되어야 함
    shorts = [[(curr_node+1, 1)] if curr_node < len_highway else [] for curr_node in range(len_highway+1)]
    for _ in range(num_short):
        start, end, dist = map(int, input().split())
        if end <= len_highway and (end - start) > dist:
            shorts[start].append((end, dist))

    distances = [float('inf')] * (len_highway + 1)
    dijkstra(0)
    
    print(distances[len_highway])