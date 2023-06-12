# 풀이 1
import sys
input = sys.stdin.readline
from collections import deque
N = int(input()) # num of cards
queue = deque([i for i in range(1, N+1)])

should_remove = 1
while len(queue) > 1:
    curr = queue.popleft()
    queue.append(curr) if not should_remove else 0
    should_remove = 0 if should_remove else 1

print(queue[0])

# 풀이 2
import sys
input = sys.stdin.readline
from collections import deque
N = int(input()) # num of cards

def find_card(N):
    if N == 1:
        return 1

    queue = deque([i for i in range(1, N+1)])
    while len(queue) > 2:
        queue.popleft() 
        queue.append(queue.popleft())
        
    return queue[1]
    
print(find_card(N))
