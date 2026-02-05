def solution(numbers):
    def is_valid_bin_tree(nodes):
        if len(nodes) == 1:
            return True

        mid = len(nodes) // 2
        root = nodes[mid]
        left = nodes[:mid]
        right = nodes[mid + 1 :]

        if root == "0":
            return "1" not in nodes

        return is_valid_bin_tree(left) and is_valid_bin_tree(right)

    def convert_and_validate(num):
        binary = bin(num)[2:]
        h = len(binary).bit_length()
        perfect_num = 2**h - 1

        return is_valid_bin_tree("0" * (perfect_num - len(binary)) + binary)

    return [1 if convert_and_validate(n) else 0 for n in numbers]
