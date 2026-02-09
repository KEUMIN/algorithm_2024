def solution(numbers):
    def is_valid_tree(binary):
        if len(binary) == 1:
            return True

        mid = len(binary) // 2
        root = binary[mid]
        left = binary[:mid]
        right = binary[mid + 1 :]

        if root == "0":
            return "1" not in binary

        return is_valid_tree(left) and is_valid_tree(right)

    def convert_and_valid(num):
        binary = bin(num)[2:]
        height = len(binary).bit_length()
        N = 2**height - 1
        full_binary = "0" * (N - len(binary)) + binary

        return is_valid_tree(full_binary)

    return [1 if convert_and_valid(n) else 0 for n in numbers]
