# 340210
# 내 풀이
def solution(expressions):
    unsolved_exp = []
    min_base = 2
    for exp in expressions:
        comps = exp.split(" ")
        for i, comp in enumerate(comps):
            if i == 0 or i == 2:
                min_base = max(min_base, int(comp) % 10)
            if i == 4 and comp == "X":
                unsolved_exp.append(exp)
    possible_base = set()
    for i in range(min_base, 10):
        possible = False
        for exp in expressions:
            if exp[len(exp) - 1] == "X":
                continue
            comps = exp.split(" ")
            a = parse_to_base(n=i, target=int(comps[0]))
            b = parse_to_base(n=i, target=int(comps[2]))
            c = parse_to_base(n=i, target=int(comps[4]))
            if comps[1] == "+":
                if a + b == c:
                    possible = True
                else:
                    possible = False
            elif comps[1] == "-":
                if a - b == c:
                    possible = True
                else:
                    possible = False
        if possible:
            possible_base.add(i)
    result = []
    for exp in unsolved_exp:
        comps = exp.split(" ")
        possibles = set()
        for i in possible_base:
            a = parse_to_base(n=i, target=int(comps[0]))
            b = parse_to_base(n=i, target=int(comps[2]))
            if comps[1] == "+":
                possibles.add(a + b)
            elif comps[1] == "-":
                possibles.add(a - b)
        if len(possibles) > 1:
            result.append(exp.replace("X", "?"))
        elif len(possibles) == 1:
            result.append(exp.replace("X", str(possibles.pop())))
    return result
def parse_to_base(n, target):
    if target >= 100:
        return (target // 100) * (n ** 2) + ((target % 100) // 10) * n + (target % 10)
    elif 10 <= target < 100:
        return (target // 10) * n + (target % 10)
    else:
        return target
print(solution(expressions=["10 - 2 = X", "30 + 31 = 101", "3 + 3 = X", "33 + 33 = X"]))
