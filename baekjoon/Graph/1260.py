import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N, M, V = map(int, input().split())

# 그래프는 {노드: set(연결된 노드들)} 구조의 해시 테이블
graph = defaultdict(set)
for _ in range(M):
    k, v = map(int, input().split())
    graph[k].add(v)
    graph[v].add(k)

for key in graph.keys():
    graph[key] = sorted(graph[key])

# 1. DFS (재귀)
def dfs():
    visited = [0 for _ in range(N+1)] # 1: 방문한 노드, 0: 방문하지 않은 노드
    def recur(curr):
        visited[curr] = 1
        print(curr, end=' ')
        if not graph[curr]: # 방문할 노드가 없다
            return
        
        for node in graph[curr]:
            if not visited[node]:
                recur(node)
                
    recur(V)

dfs()
print()

# 2. BFS (큐)
def bfs():
    visited = [0 for _ in range(N+1)] # 1: 방문한 노드, 0: 방문하지 않은 노드
    
    queue = deque([V])
    visited[V] = 1
    while queue:
        curr = queue.popleft()
        print(curr, end=' ')
        for node in graph[curr]:
            if not visited[node]:
                queue.append(node)
                visited[node] = 1
                
bfs()