#77486
def solution(enroll, referral, seller, amount):
    referral_dict = dict(zip(enroll, referral))
    money_dict = {name: 0 for name in enroll}

    for i, name in enumerate(seller):
        money = amount[i] * 100
        cur_name = name
        while money > 0 and cur_name != '-':
            money_dict[cur_name] += money - (money // 10)
            cur_name = referral_dict[cur_name]
            money //= 10

    return [value for value in money_dict.values()]