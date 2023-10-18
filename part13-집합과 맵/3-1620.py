import sys
n, m = map(int, input().split())
dic1 = {}
dic2 = {}
for i in range(n) :
    temp = sys.stdin.readline().strip()
    dic1[i+1] = temp
    dic2[temp] = i+1
for i in range(m) :
    temp = sys.stdin.readline().strip()
    if temp.isdecimal() :
        sys.stdout.write(str(dic1[int(temp)]) + "\n")
    else :
        sys.stdout.write(str(dic2[temp]) + "\n")