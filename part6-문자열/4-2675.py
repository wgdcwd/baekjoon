n = int(input())
for i in range(n) :
    k, s = input().split()
    k = int(k)
    for j in range(len(s)) :
        print(s[j] * k, end="")
    print()