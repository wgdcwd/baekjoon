def isGroup(s) :
    i = 0
    s = s + " "
    while True :
        if s[i] == " " :
            break
        if s[i] == s[i+1] :
            s = s.replace(s[i] * 2,s[i], 1)
        else :
            i += 1

    s = s.strip()
    
    for i in range(ord('a'), ord('z') + 1) :
        if s.count(chr(i)) > 1 :
            return False
    return True

n = int(input())
ans = 0
for i in range(n) :
    if isGroup(input()) == True :
        ans += 1
print(ans)