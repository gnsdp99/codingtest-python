# 2023 KAKAO BLIND RECRUITMENT 이모티콘 할인행사 (Lv.2)
def get_dup_permutation(array, num_to_select):
    dup_permutation = []
    if num_to_select == 0:
        return [[]]
    
    for fixed in array:
        for perm in get_dup_permutation(array, num_to_select - 1):
            dup_permutation.append([fixed] + perm)
    return dup_permutation

def solution(users, emoticons):
    percentages = [10, 20, 30, 40]
    dup_permutation = get_dup_permutation(percentages, len(emoticons))
    max_joined, max_bought = 0, 0
    for percentages in dup_permutation:
        num_joined, price_bought = 0, 0
        prices = [price * (1 - percentage * 0.01) for price, percentage in zip(emoticons, percentages)]
        for max_percentage, max_price in users:
            total_price = 0
            for i, percentage in enumerate(percentages):
                if percentage >= max_percentage:
                    total_price += prices[i]
            if total_price >= max_price:
                num_joined += 1
            else:
                price_bought += total_price
                
        if num_joined > max_joined or (num_joined == max_joined and price_bought > max_bought):
            max_joined, max_bought = num_joined, price_bought
            
    return [max_joined, max_bought]