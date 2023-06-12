import sys
from collections import deque
input = sys.stdin.readline
num_pole = int(input())
poles = sorted([tuple(map(int, input().split())) for _ in range(num_pole)]) # (x, y)
highest_idx = poles.index(max(poles, key=lambda x:x[1]))

def get_left_area():
    area = 0
    # 맨 왼쪽부터 가장 높은 기둥까지 높은 기둥만 선택
    curr_pole = poles[0]
    for next_pole in poles[1: highest_idx+1]:
        if curr_pole[1] <= next_pole[1]:
            area += ((next_pole[0] - curr_pole[0]) * curr_pole[1])
            curr_pole = next_pole
    return area

def get_right_area():
    area = 0
    # 맨 오른쪽부터 가장 높은 기둥까지 높은 기둥만 선택
    curr_pole = poles[-1]
    for next_pole in poles[-2:highest_idx-1:-1] if highest_idx > 0 else poles[-2:highest_idx:-1]:
        if curr_pole[1] <= next_pole[1]:
            area += ((curr_pole[0] - next_pole[0]) * curr_pole[1])
            curr_pole = next_pole
    if curr_pole[0] > poles[highest_idx][0]:
        area += ((curr_pole[0] - poles[highest_idx][0]) * poles[highest_idx][1])
    return area

min_area = get_left_area() + poles[highest_idx][1] + get_right_area()
print(min_area)