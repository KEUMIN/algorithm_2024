dict = {}

def climb_stairs(n):
    print('climb {} stairs'.format(n))
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if n not in dict:
        dict[n] = climb_stairs(n - 1) + climb_stairs(n - 2)
        
    return dict[n]

print(climb_stairs(7))