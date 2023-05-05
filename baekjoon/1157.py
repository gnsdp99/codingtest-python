# 풀이 1
import sys
from collections import Counter
input = sys.stdin.readline

word = input().rstrip().upper() # remove '\n'
numAlpha = sorted(Counter(word).items(), key=lambda x:x[1], reverse=True)

if len(numAlpha) >= 2 and numAlpha[0][1] == numAlpha[1][1]:
    print("?")
else: 
    print(numAlpha[0][0])

# 풀이 2
import sys
from collections import Counter
input = sys.stdin.readline

word = input().rstrip().upper() # remove '\n'
numAlpha = Counter(word)

maxNumAlpha = [k for k, v in numAlpha.items() if max(numAlpha.values()) == v]
print("?") if len(maxNumAlpha) >= 2 else print(maxNumAlpha[0])

# 풀이 3
import sys
from collections import Counter
input = sys.stdin.readline

word = input().rstrip().upper() # remove '\n'
numAlpha = Counter(word).most_common(2)
print("?") if len(numAlpha) >= 2 and numAlpha[0][1] == numAlpha[1][1] else print(numAlpha[0][0])