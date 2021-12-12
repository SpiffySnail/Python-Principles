def consecutive_zeros(param1):
    total = []
    count = 0
    for a in param1:
        if a == '0':
            count += 1
            total.append(count)
        elif a == '1':
            count = 0
    big = 0
    for b in total:
        if b >= big:
            big = b
    return big
    
print(consecutive_zeros("101"))