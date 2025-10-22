def solution(numbers):
    def is_valid_binary_tree(binary):
        if len(binary) == 1:
            return True
        mid = len(binary) // 2
        root = binary[mid]
        left = binary[:mid]
        right = binary[mid + 1 :]

        if root == "0":
            return "1" not in binary

        return is_valid_binary_tree(left) and is_valid_binary_tree(right)

    def can_represent(num):
        if num == 1:
            return True

        binary = bin(num)[2:]
        tree_height = len(binary).bit_length()
        full_tree_size = 2**tree_height - 1

        binary = "0" * (full_tree_size - len(binary)) + binary

        return is_valid_binary_tree(binary)

    return [1 if can_represent(num) else 0 for num in numbers]


solution([63, 111, 95])
