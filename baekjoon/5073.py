import sys
input = sys.stdin.readline

while True:
    s1, s2, s3 = map(int, input().split()) # s: the length of side
    if all(s == 0 for s in [s1, s2, s3]):
        break
     
    if s1 == s2 == s3:
        result = "Equilateral"
    elif (s1 >= s2+s3) or (s2 >= s1+s3) or (s3 >= s1+s2):
        result = "Invalid"
    elif s1 == s2 or s2 == s3 or s3 == s1:
        result = "Isosceles"
    else:
        result = "Scalene"
        
    print(result)