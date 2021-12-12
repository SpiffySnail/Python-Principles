statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
def online_count(param1):
    value = 0
    for a in param1:
        if param1[a] == 'online':
           value += 1
    return value
    
print(online_count(statuses))