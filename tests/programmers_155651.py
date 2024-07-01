def solution(book_time):
    events = []
    
    for start, end in book_time:
        start_hour, start_minute = map(int, start.split(':'))
        end_hour, end_minute = map(int, end.split(':'))
        
        start_time = start_hour * 60 + start_minute
        end_time = end_hour * 60 + end_minute + 10
        
        events.append((start_time, 'start'))
        events.append((end_time, 'end'))
    
    events.sort(key=lambda x: (x[0], x[1] == 'start'))
    
    current_rooms = 0
    max_rooms = 0
    
    for event in events:
        if event[1] == 'start':
            current_rooms += 1
            max_rooms = max(max_rooms, current_rooms)
        else:
            current_rooms -= 1
    
    return max_rooms
