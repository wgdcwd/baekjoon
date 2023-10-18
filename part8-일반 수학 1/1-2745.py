dic = {}
for i in range(0, 10):
    dic[str(i)] = i
for i in range(26):
    dic[chr(ord("A") + i)] = 10 + i

N, B = input().split(" ")
B = int(B)

ans = 0
for i in range(len(N)):
    ans += dic[N[i]] * (B ** (len(N) - i - 1))
print(ans)
