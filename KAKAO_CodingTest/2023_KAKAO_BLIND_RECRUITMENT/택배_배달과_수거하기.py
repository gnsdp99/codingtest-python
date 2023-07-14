# 2023 KAKAO BLIND RECRUITMENT 택배 배달과 수거하기 (Lv.2)
def deliver_or_pickup(cap, houses):
    num_loaded = 0
    max_dist = 0
    while houses:
        if houses[-1] != 0 and max_dist == 0:
            max_dist = len(houses)
        if num_loaded + houses[-1] > cap:
            houses[-1] -= (cap - num_loaded)
            break
        num_loaded += houses.pop()
    return max_dist

def solution(cap, n, deliveries, pickups):
    total_distance = 0
    
    while deliveries or pickups:
        dist_deliver = deliver_or_pickup(cap, deliveries) if deliveries else 0
        dist_pickup = deliver_or_pickup(cap, pickups) if pickups else 0
        total_distance += 2 * max(dist_deliver, dist_pickup)

    return total_distance