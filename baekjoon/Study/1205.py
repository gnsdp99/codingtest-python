import sys
input = sys.stdin.readline

N, myScore, P = map(int, input().rstrip().split())
scores = list(map(int, input().rstrip().split()))

def findRanking(myScore, scores):
    # 예외 처리
    if len(scores) == 0:
        return 1
    elif len(scores) == P and myScore <= scores[-1]:
        return -1
    elif myScore < scores[-1]:
        return len(scores) + 1
        
    for i in range(len(scores)):
        if myScore >= scores[i]:
            return i + 1
        
print(findRanking(myScore, scores))