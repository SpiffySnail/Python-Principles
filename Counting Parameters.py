def param_count(*params):
    count = 0
    for a in params:
        print(a)
        count += 1
        
    return count
    
param_count(1,2,3)