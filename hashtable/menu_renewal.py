from itertools import combinations
from collections import defaultdict

def solution(orders, courses):
    course_dict = defaultdict(int)
    for order in orders:
        for num in courses:
            for combi in combinations(sorted(order), num):
                combi_str = ''.join(combi)
                course_dict[combi_str] += 1
                
    course_list = [(k, v) for k, v in course_dict.items() if v >= 2]
    course_list = sorted(course_list, key= lambda x: (len(x[0]), -x[1]))
    result = []
    max = -1
    num = min(courses)
    for course, cnt in course_list:
        if len(course) > num:
            num = len(course)
            max = -1
        if cnt >= max:
            max = cnt
            result.append(course)
    
    return sorted(result, key= lambda x: (x, len(x)))
    

print(solution(orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], courses=[2,3,4]))