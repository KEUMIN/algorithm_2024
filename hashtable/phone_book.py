#42577

def solution_1(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True

def solution(phone_book):
    phone_set = set()
    phone_book.sort(key=len)
    for num in phone_book:
        for i in range(1, len(num)):
            if num[:i] in phone_set:
                return False
        phone_set.add(num)
    return True