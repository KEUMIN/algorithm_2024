def solution(numbers):
    def validate_bin_tree(binary):
        if len(binary) == 1:
            return True

        mid = len(binary) // 2
        root = binary[mid]
        left = binary[:mid]
        right = binary[mid + 1 :]

        if root == "0":
            return "1" not in binary

        return validate_bin_tree(left) and validate_bin_tree(right)

    def convert_and_validate_num(num):
        binary = bin(num)[2:]
        h = len(binary).bit_length()
        N = 2**h - 1
        perfect_binary = "0" * (N - len(binary)) + binary

        return validate_bin_tree(perfect_binary)

    return [1 if convert_and_validate_num(n) else 0 for n in numbers]
