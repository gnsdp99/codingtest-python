import sys
input = sys.stdin.readline

num_switch = int(input())
switch_states = [-1] + list(map(int, input().split()))
num_student = int(input())

def switch(num):
    switch_states[num] = 0 if switch_states[num] else 1

def male(num):
    for i in range(num, len(switch_states), num):
        switch(i)

def female(num):
    switch(num)
    if num == 1 or num == len(switch_states): return
        
    left, right = num-1, num+1
    while left >= 1 and right < len(switch_states) and switch_states[left] == switch_states[right]:
        switch(left)
        switch(right)
        left, right = left-1, right+1
    
for _ in range(num_student):
    gender, number = map(int, input().split())
    if gender == 1:
        male(number)
    else:
        female(number)
        
for i in range(1, len(switch_states)):
    print(switch_states[i], end=' ') if i % 20 != 0 else print(switch_states[i])