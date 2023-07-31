# 백준 14889 스타트와 링크 (S2)
def calculate_diff(team1, team2):
    sum_team1 = sum([S_list[i][j] + S_list[j][i] for idx, i in enumerate(team1[:len(team1)-1]) for j in team1[idx+1:]])
    sum_team2 = sum([S_list[i][j] + S_list[j][i] for idx, i in enumerate(team2[:len(team2)-1]) for j in team2[idx+1:]])
    return abs(sum_team1 - sum_team2)

def backtrack(rest, members, num_to_select):
    global min_diff
    if num_to_select == 0:
        others = [i for i in range(N) if i not in members]
        curr_diff = calculate_diff(members, others)
        if min_diff > curr_diff:
            min_diff = curr_diff
        return        
    
    for i, fixed in enumerate(rest):
        backtrack(rest[i+1:], members + [fixed], num_to_select - 1)

if __name__ == "__main__":
    N = int(input().strip())
    S_list = [list(map(int, input().split())) for _ in range(N)]

    min_diff = float('inf')
    backtrack([i for i in range(1, N)], [0], N // 2 - 1)
    print(min_diff)