def format_number(param1):
    count = 1
    totalCount = 1
    groupDigitCountTable = (1,2)
    groupDigits = []
    digits = []
    revParam1 = str(param1)[::-1]
    print(revParam1)
    for a in revParam1:
        if count in groupDigitCountTable:
            digits += a
            count += 1
            totalCount += 1
        elif count == 3:
            digits += a
            groupDigits += [(digits)]
            digits = []
            count = 1
            totalCount += 1
    if digits != []:
            groupDigits += [(digits)]
            digits = []
    count = 1
    groupDigits.reverse()
    result = ""
    for b in groupDigits:
        b.reverse()
        if len(b) != 3:
            for c in b:
                if len (b) == 2:
                    if count == 1:
                        result += str(c)
                    else:
                        result += str(c)
                elif len(b) == 1:
                    result += str(c) 
        if len(b) == 3:
            result += ','
            for d in b:
                result += str(d)

    if result.startswith(","):
        result = result[1:]
    return ''.join(result)
