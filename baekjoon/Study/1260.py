import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def dfs(start_node):
    visited = [0] * (num_node+1)
    def recur(curr_node):
        visited[curr_node] = 1
        print(curr_node, end=' ')
        for node in sorted(edges[curr_node]):
            if not visited[node]:
                recur(node)
    recur(start_node)

def bfs(start_node):
    visited = [0] * (num_node+1)
    queue = deque([start_node])
    visited[start_node] = 1
    while queue:
        curr_node = queue.popleft()
        print(curr_node, end=' ')
        for node in sorted(edges[curr_node]):
            if not visited[node]:
                queue.append(node)
                visited[node] = 1
    
if __name__ == "__main__":
    num_node, num_edge, start_node = map(int, input().split())
    edges = defaultdict(list)
    for _ in range(num_edge):
        node1, node2 = map(int, input().split())
        edges[node1].append(node2)
        edges[node2].append(node1)
    dfs(start_node)
    print()
    bfs(start_node)