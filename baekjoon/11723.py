import sys
input = sys.stdin.readline

M = int(input()) # num of operations
mySet = []

for _ in range(M):
    op = input().split() # operation
    if len(op) == 2:
        op[1] = int(op[1])
        
    if (op[0] in ('add', 'toggle')) and op[1] not in mySet:
        mySet.append(op[1])
    elif (op[0] in ('remove', 'toggle')) and op[1] in mySet:
        mySet.remove(op[1])
    elif op[0] == 'all':
        mySet = [i for i in range(1, 21)]
    elif op[0] == 'empty':
        mySet = []
    elif op[0] == 'check':
        print(1 if op[1] in mySet else 0)
        # sys.stdout.write('1\n' if op[1] in mySet else '0\n')