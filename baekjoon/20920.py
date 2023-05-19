# 풀이 1
import sys
from collections import defaultdict
input = sys.stdin.readline
N, M = map(int, input().split())

words = defaultdict(int)
for i in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words[word] += 1

words = sorted(words.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
for word, _ in words:
    print(word)
    
# 풀이 2
import sys
from collections import Counter
input = sys.stdin.readline
N, M = map(int, input().split())
words = [input().rstrip() for _ in range(N)]

counter = Counter([word for word in words if len(word) >= M])
words_note = sorted(counter.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))
words_note = list(zip(*words_note))[0]

print('\n'.join(words_note))