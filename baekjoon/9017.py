import sys
input = sys.stdin.readline
from collections import defaultdict

T = int(input()) # num of test case
for _ in range(T):
    N = int(input())
    table = list(input().split())
    
    counts = defaultdict(int) # {team: num_player}
    for team in table:
        counts[team] += 1
    
    # 6명이 안되는 팀의 선수 제거
    new_table = [team for team in table if counts[team] == 6]
    scores = defaultdict(list) # {team: [scores]}
    
    for score, team in enumerate(new_table, 1):
        scores[team].append(score)
    
    # top4의 합 -> 5등 순서로 정렬
    result = sorted(scores.items(), key=lambda x:(sum(x[1][:4]), x[1][4]))
    print(result[0][0])