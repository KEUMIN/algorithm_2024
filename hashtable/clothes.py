# 1. 딕셔너리를 만든다. 같은 카테고리면 +1
# 2. 딕셔너리의 키의 숫자만큼 순회한다
# 3. 조합을 구해서 순회한다
# 4. 딕셔너리에서 찾아서 곱한다.

from collections import Counter

def solution(clothes):
    categories = Counter([category for _, category in clothes])
    result = 1
    for num_of_clothes in categories.values():
        result *= num_of_clothes + 1
    return result - 1
    
    
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
print(solution(clothes))