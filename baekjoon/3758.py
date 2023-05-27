import sys
input = sys.stdin.readline
T = int(input()) # 테스트 케이스

def find_rank():
    # n: 팀 수 / k: 문제 수 / t: 나의 팀 ID / m: 로그 수
    n, k, t, m = map(int, input().split())
    
    # key는 팀 ID, value는 {각 key가 총 점수, 제출 횟수, 마지막 제출 시간}인 해시
    records = {key: {'score': 0, 'numSubmit': 0, 'lastSubmit': 0} for key in range(1, n+1)}
    # key는 문제 번호, value는 {key가 팀 ID, value가 점수}인 해시
    problems = {key: {} for key in range(1, k+1)}
    
    # i: 팀 ID / j: 문제 번호 / s: 획득 점수
    for submitTime in range(1, m+1):
        i, j, s = map(int, input().split())
        if i not in problems[j]: # 아직 안 푼 문제임
            problems[j][i] = s
            records[i]['score'] += s
        else: # 풀었던 문제임
            if problems[j][i] < s: # 점수가 더 높아짐
                records[i]['score'] += (s - problems[j][i])
                problems[j][i] = s
            else: # 점수가 같거나 더 낮아짐
                pass
        records[i]['numSubmit'] += 1
        records[i]['lastSubmit'] = submitTime
        
    # 기록을 총 점수 높은 순 -> 제출 횟수 적은 순 -> 마지막 제출 시간 뻐른 순으로 정렬
    sorted_records = sorted(records.items(), key=lambda x:(-x[1]['score'], x[1]['numSubmit'], x[1]['lastSubmit']))
    # 기록 중 등수만 추출
    ranks = list(zip(*sorted_records))[0]
    
    # 나의 팀 순위를 반환
    myRank = ranks.index(t) + 1 # 인덱스가 0부터 시작
    return myRank
                
for _ in range(T):
    print(find_rank())