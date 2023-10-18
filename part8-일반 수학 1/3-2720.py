n = int(input())
qdnp = [25, 10, 5, 1]
for i in range(n):
    C = int(input())
    for i in range(4):
        print(C // qdnp[i], end=" ")
        C = C % qdnp[i]
    print()
