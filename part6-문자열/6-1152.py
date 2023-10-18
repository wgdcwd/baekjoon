s = input()
s = s.strip()

if s == "" :
    print(0)
else :
    print(s.count(" ") + 1)