# 340210
# 내 풀이
def solution(expressions):
    def decimal_to_base(n, base):
        if n == 0:
            return 0
        result = []
        while n:
            result.append(str(n % base))
            n //= base
        return int(''.join(result[::-1]))

    def calculate_X(expression:str, base: int):
        exp = expression.split()
        a, b, op = int(exp[0], base), int(exp[2], base), exp[1]
        return decimal_to_base(a+b, base) if op == '+' else decimal_to_base(a-b, base)

    def valid_base_expression(expression: str, base: int):
        exp = expression.split()
        a, b, c = int(exp[0], base), int(exp[2], base), int(exp[4], base)
        return (a + b == c) if exp[1] == '+' else (a - b == c)

    def find_base(expression: str):
        base = [i for i in range(2, 10)]
        exp = expression.split()
        min_base = 2
        for comp in [exp[0], exp[2], exp[4]]:
            if comp != 'X':
                for i in range(len(comp)):
                    min_base = max(min_base, int(comp[i]) + 1)
        base = list(filter(lambda x: x >= min_base, base))

        result = base[:]
        if exp[4] != 'X':
            for num in base:
                if not valid_base_expression(expression, num):
                    result.remove(num)

        return result

    candidates = set([i for i in range(2, 10)])
    unknown = []
    for expression in expressions:
        exp = expression.split()
        tmp_base = find_base(expression)
        candidates.intersection_update(tmp_base)
        if exp[4] == 'X':
            unknown.append(expression)

    answer = []
    for expression in unknown:
        temp_val = set()
        for base in candidates:
            temp_val.add(calculate_X(expression, base))
        answer.append(expression[:-1] + (str(temp_val.pop()) if len(temp_val) == 1 else '?'))

    return answer

print(solution(expressions=["2 - 1 = 1", "2 + 2 = X", "7 + 4 = X", "5 - 5 = X"]))