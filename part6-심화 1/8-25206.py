score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
denominator = 0
numerator = 0
for i in range(20):
    temp = input().split(" ")
    if temp[2] == "P":
        continue
    denominator += float(temp[1]) * score[temp[2]]
    numerator += float(temp[1])
print(denominator / numerator)
