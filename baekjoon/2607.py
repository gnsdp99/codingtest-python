# 풀이 1.
def is_similar(long_word, short_word):
    long_arr = list(long_word)
    short_arr = list(short_word)

    while short_arr:
        ch = short_arr.pop()
        if ch in long_arr:
            long_arr.remove(ch)

    # long_arr의 남은 길이가 1 이하면 비슷한 단어다.
    if len(long_arr) <= 1:
        return True
    else:
        return False

def main():
    N = int(input()) # 단어의 개수
    word = input()
    
    ans = 0 # 비슷한 단어 개수
    for _ in range(N-1): # word 제외
        other = input()
        if len(word) >= len(other):
            ans += is_similar(word, other)
        else:
            ans += is_similar(other, word)
    
    print(ans)
main()

# 풀이 2.
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
