testCase = int(input())
for i in range(testCase) :
    h, w, n = map(int, input().split())
    front = (n-1) % h + 1
    back = (n-1) // h + 1
    if back <10 :
        print("%d0%d" %(front, back))
    else :
        print("%d%d" %(front, back))