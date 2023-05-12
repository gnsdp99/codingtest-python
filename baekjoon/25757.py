import sys
input = sys.stdin.readline

N, game = input().rstrip().split()
names = {input().rstrip() for _ in range(int(N))} # duplicate not allowed

numPlayer = len(names) # number of players

# number of games
ans = numPlayer if game == 'Y' else numPlayer // 2 if game == 'F' else numPlayer // 3

print(ans)