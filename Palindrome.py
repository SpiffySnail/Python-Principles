def palindrome(param1):
    rev = param1 [::-1]
    if param1 == rev:
        return True
    else:
        return False
print(palindrome("bosb"))