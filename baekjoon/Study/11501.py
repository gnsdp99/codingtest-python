import sys
input = sys.stdin.readline
T = int(input())

def find_max_profit(stocks):
    # 뒤에서부터 탐색
    max_stock = stocks[-1]
    max_profit = 0 # 리턴값
    for i in range(len(stocks), 0, -1):
        max_profit += (max_stock - stocks[i-1]) if max_stock > stocks[i-1] else 0
        max_stock = stocks[i-1] if stocks[i-1] > max_stock else max_stock
    
    return max_profit

for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    print(find_max_profit(stocks))