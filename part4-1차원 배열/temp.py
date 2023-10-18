def isHan(n) :
    if (n//100) - ((n//10)%10) == ((n//10)%10) - n%10 :
        return True
    return False

print(isHan(122))