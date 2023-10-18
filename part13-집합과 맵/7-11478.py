inp = input()
s = set()
l = len(inp)
for i in range(1, l + 1) :
    for j in range(0, l - i + 1) :
        s.add(inp[j:j+i])
print(len(s))