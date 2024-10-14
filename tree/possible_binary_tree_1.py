# 프로그래머스 - 표현 가능한 이진트리 (LV3) : https://school.programmers.co.kr/learn/courses/30/lessons/150367
# 사용 알고리즘 : 포화 이진트리
# 필수 선지식 : 포화 이진트리 노드 개수 = 등비수열 합 = 2 ** 높이 - 1
#            포화 이진트리 높이 = 노드 개수 . bit_length()


def solution(numbers):
    def is_valid(tree):
        if len(tree) == 1:
            return True
        mid = len(tree) // 2
        root = tree[mid]
        left = tree[:mid]
        right = tree[mid + 1 :]

        if root == "0":
            return all(node == "0" for node in tree)

        return is_valid(left) and is_valid(right)

    def can_represent(number):
        if number == 1:
            return True

        bin_tree = bin(number)[2:]
        tree_height = len(bin_tree).bit_length()
        full_nodes = 2**tree_height - 1

        bin_tree = "0" * (full_nodes - len(bin_tree)) + bin_tree

        return is_valid(bin_tree)

    return [1 if can_represent(num) else 0 for num in numbers]
