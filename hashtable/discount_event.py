from collections import Counter

def solution(want, number, discount):
    result = 0
    shop_list = list(zip(want, number))
    
    for i in range(len(discount) - 9):
        dc_cnt = Counter(discount[i:i+10])
        if can_buy_all(shop_list, dc_cnt):
            result += 1
            
    return result

def can_buy_all(shop_list, dc_cnt):
    for prd, num in shop_list:
        if dc_cnt[prd] == None or dc_cnt[prd] < num:
            return False
    return True