import sys
input = sys.stdin.readline

N = int(input()) # 단어의 개수
word = input()
ans = 0 # 비슷한 단어 개수

for _ in range(N-1): # word 제외
    other = input()
    word_copy = list(word)
    diff_cnt = 0
    for ch in other:
        if ch in word_copy:
            word_copy.remove(ch)
        else:
            diff_cnt += 1
    
    ans += 1 if len(word_copy) <= 1 and diff_cnt <= 1 else 0

print(ans)