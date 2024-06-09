def get_longest_seq(list):
    num_dic = {}
    
    for i in list:
        num_dic[i] = 1
        
    result = 0
    for i in list:
        if i-1 not in num_dic:            
            count = 1
            add = 1
            
            while(i + add in num_dic):
                count += 1
                add += 1
            
            if count > result:
                result = count
        
    return result

list = [100, 4, 200, 1, 3, 2]    
print(get_longest_seq(list))