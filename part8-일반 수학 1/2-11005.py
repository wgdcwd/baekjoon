dic = {}
for i in range(0, 10):
    dic[i] = str(i)
for i in range(26):
    dic[10 + i] = chr(ord("A") + i)

N, B = map(int, input().split(" "))

ans = ""

while N != 0:
    ans = dic[N % B] + ans
    N = N // B
print(ans)
