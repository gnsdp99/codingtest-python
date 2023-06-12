import sys
from collections import deque
input = sys.stdin.readline
p, m = map(int, input().split())
players = {}
for i in range(p):
    lv, nick = input().rstrip().split()
    players[nick] = int(lv)

rooms = []
for nick in players: # O(n^2)
    is_entered = 0
    for room in rooms: # 먼저 생성된 방부터 탐색
        if len(room) < m and players[room[0]] - 10 <= players[nick] <= players[room[0]] + 10: # 입장
            room.append(nick)
            is_entered = 1
            break
        
    if not is_entered: # 참가하지 못헸으면 새로운 방 개설
        rooms.append([nick])
    
for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
        
    # 닉네임 사전순으로 출력
    for nick in sorted(room):
        print(players[nick], nick)