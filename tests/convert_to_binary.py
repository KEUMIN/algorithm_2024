#70129
def solution(s):
    cnt_of_loop = 0
    num_of_rm_zero = 0
    while s != "1":
        cnt_of_loop += 1
        num_of_rm_zero += s.count("0")
        s = bin(s.count("1"))[2:]
    return [cnt_of_loop, num_of_rm_zero]