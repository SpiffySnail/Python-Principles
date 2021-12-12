def mid(str):
    charNum = len(str)
    if charNum % 2 == 0:
        print('can only find middle char of odd number')
        return('')
    elif charNum == 1:
        return(str)
    else:
        charMidNum = round(charNum / 2)
        i = 0
        for a in str:
            i += 1
            if i == charMidNum:
                return(a)

print(mid('a'))
