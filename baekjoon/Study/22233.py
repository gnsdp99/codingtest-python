import sys
input = sys.stdin.readline
N, M = map(int, input().split())
keywords = set(input().rstrip() for _ in range(N))

def remove_keyword(args):
    for key in args:
        if key in keywords:
            keywords.remove(key)
            
for _ in range(M):
    write = input().rstrip().split(',')
    remove_keyword(write)
    print(len(keywords))