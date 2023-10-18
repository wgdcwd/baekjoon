s = input()
s = s.upper()
arr = []
for i in range(26) :
    arr.append(0)

for i in s :
    arr[ord(i) - ord('A')] += 1
temp = max(arr)
if arr.count(temp) != 1 :
    print("?")
else :
    print(chr(arr.index(temp) + ord("A")))