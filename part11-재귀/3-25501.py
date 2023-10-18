def recursion(s, l, r, c):
    if l >= r: return 1,c+1
    elif s[l] != s[r]: return 0,c+1
    else: return recursion(s, l+1, r-1, c+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

n = int(input())
for i in range(n) :
    temp = isPalindrome(input())
    print(temp[0], temp[1])