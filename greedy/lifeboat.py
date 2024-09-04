#42885 구명보트
def solution(people, limit):
    sorted_people = sorted(people)
    i = 0
    j = len(people) - 1
    count = 0
    while i <= j:
        if sorted_people[i] + sorted_people[j] <= limit:
            i += 1
        j -= 1
        count += 1
        
    return count