n = int(input())
l = 1
sum = 0

while sum < n :
    sum += l
    l += 1

if l % 2 == 0 :
    print("%d/%d" %((sum - n + 1), (l - sum + n - 1)))
else :
    print("%d/%d" %((l - sum + n - 1), (sum - n + 1)))