def solution(record):
    uid = {}
    for line in record:
        cmd = line.split(" ")
        if cmd[0] != 'Leave':
            uid[cmd[1]] = cmd[2]
            
    answer = []
    for line in record:
        cmd = line.split(" ")
        if cmd[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' % uid[cmd[1]])
        elif cmd[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' % uid[cmd[1]])
    return answer