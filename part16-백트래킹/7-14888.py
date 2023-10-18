def cal(operand, operator) :
    result = operand[0]
    for i in range(len(operator)) :
        if operator[i] == 0 :
            result += operand[i+1]
        elif operator[i] == 1 :
            result -= operand[i+1]
        elif operator[i] == 2 :
            result *= operand[i+1]
        else :
            if result < 0 :
                result = -((-result) // operand[i+1])
            else :
                result //= operand[i+1]
    if result > ans[0] :
        ans[0] = result
    if result < ans[1] :
        ans[1] = result

def insert_oerator(k, n) :
    if k == n :
        cal(operand, operator)
        return
    
    for i in range(4) :
        if count[i] == 0 :
            continue
        operator.append(i)
        count[i] -= 1
        insert_oerator(k+1, n)
        operator.pop()
        count[i] += 1
    
#------------------------------
n = int(input())
operand = list(map(int, input().split()))
count = list(map(int, input().split()))

operator = []
#ans[0] = max ans[1] = min
ans = [-1000000000, 1000000000]

insert_oerator(0, n-1)
print(ans[0])
print(ans[1])