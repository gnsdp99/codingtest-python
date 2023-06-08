import sys
input = sys.stdin.readline

def find_longest_seq(sequence):
    longest_len = 0
    left, right = 0, 0
    while right < num_int:
        if available[sequence[right]]:
            available[sequence[right]] -= 1
            right += 1
        else:
            available[sequence[left]] += 1
            left += 1
        longest_len = max(longest_len, right - left)
        
    return longest_len
            
if __name__ == "__main__":
    num_int, num_same = map(int, input().split())
    sequence = list(map(int, input().split()))
    available = [num_same] * (max(sequence) + 1)
    
    print(find_longest_seq(sequence))