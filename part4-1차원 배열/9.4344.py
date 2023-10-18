import math
def cal(arr) :
    avr = sum(arr) / arr[0] - 1
    cnt = 0
    for i in range(arr[0]) :
        if arr[i+1] > avr :
            cnt += 1
    ans = round(cnt / arr[0], 6) * 100
    print("%.3f%%" %ans)

    
n = int(input())
for i in range(n) :
    cal(list(map(int, input().split())))