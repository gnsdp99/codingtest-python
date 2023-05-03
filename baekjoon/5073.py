import sys
input = sys.stdin.readline

while True:
    s1, s2, s3 = map(int, input().split()) # s: the length of side
    if not all([s1, s2, s3]):
        break
    
    if s1 == s2 == s3:
        print("Equilateral")
    elif (s1 >= s2+s3) or (s2 >= s1+s3) or (s3 >= s1+s2):
        print("Invalid")
    elif s1 == s2 or s2 == s3 or s3 == s1:
        print("Isosceles")
    else:
        print("Scalene")