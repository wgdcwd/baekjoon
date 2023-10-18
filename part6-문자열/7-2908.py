a, b = input().split()
ra = ""
rb = ""
for i in range(len(a)) :
    ra = ra + (a[len(a) - i - 1])
for i in range(len(b)) :
    rb = rb + (b[len(b) - i - 1])
if ra > rb :
    print(ra)
else :
    print(rb)