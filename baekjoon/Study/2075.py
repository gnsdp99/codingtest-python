# 풀이 1. 메모리 초과
import sys
input = sys.stdin.readline

def find_nth_num(n):
    candidates = [(N-1, x) for x in range(N)]
    while n:
        candidates.sort(key=lambda x:board[x[0]][x[1]])
        y, x = candidates.pop()
        candidates.append((y-1, x))
        n -= 1
    
    return board[y][x]
        
if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(find_nth_num(N))

# 풀이 2.
import sys
import heapq
input = sys.stdin.readline

def find_nth_num(n):
    heap = []
    for _ in range(n):
        # 메모리 제한 때문에 N^2의 숫자를 모두 저장하지 않는다.
        for num in map(int, input().split()):
            # 메모리 제한 때문에 힙의 길이를 n으로 유지한다.
            if len(heap) < n:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
    # 힙에 최종적으로 남은 숫자는 상위 N개의 숫자다.
    return heap[0]
    
if __name__ == "__main__":
    N = int(input())
    print(find_nth_num(N))