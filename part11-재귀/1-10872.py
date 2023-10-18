def pac(n) :
    if n <= 1 :
        return 1
    return pac(n-1) * n

print(pac(int(input())))