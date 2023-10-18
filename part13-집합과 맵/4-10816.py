n = int(input())
arr = list(map(int, input().split()))
dic = {}
for i in range(n) :
    if arr[i] in dic :
        dic[arr[i]] += 1
    else :
        dic[arr[i]] = 1
m = int(input())
arr = list(map(int, input().split()))
for i in range(m) :
    if arr[i] in dic :
        print(dic[arr[i]], end=" ")
    else :
        print(0, end=" ")