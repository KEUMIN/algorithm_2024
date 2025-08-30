def solution(n, times):
    s_times = sorted(times)
    left = 1
    right = (n // len(s_times)) * s_times[-1]

    while left < right:
        mid = (left + right) // 2

        if sum(mid // t for t in times) >= n:
            right = mid

        else:
            left = mid + 1

    return left


solution(6, [7, 10])

# left <= right & right = mid - 1 -> 이 방식은 answer를 따로 두어서 정답을 저장하는 방식이다.
# 하지만 off-by-one 에러를 야기하기 쉽기 때문에, 간결하게 while left < right & right = mid -> left OR right 반환 방식을 사용한다.
# while left < right 방법은 결국 left, right 가 같아져야 루프가 끝나기 때문에 둘 중 아무거나 반환해도 상관 없다.
