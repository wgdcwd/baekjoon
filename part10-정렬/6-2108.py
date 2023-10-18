import sys
from collections import Counter
n = int(sys.stdin.readline().strip())
arr = []
for i in range(n) :
    arr.append(int(sys.stdin.readline().strip()))
arr = sorted(arr)

print(round(sum(arr)/n))

print(arr[(n-1)//2])

#최빈값
cnt = Counter(arr)
cnt = cnt.most_common()
if len(cnt) == 1 :
    print(cnt[0][0])
elif cnt[0][1] == cnt[1][1] :
    print(cnt[1][0])
else :
    print(cnt[0][0])



print(arr[n-1] - arr[0])