import sys

#병합정렬
def merge_sort(arr) :
    if len(arr) <= 1 :
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    return merge(sorted_left, sorted_right)

#병합
def merge(left, right) :
    i, j = 0, 0
    sorted_arr = []

    #true면 왼쪽삽입 False면 오른쪽 삽입
    while len(left) > i and len(right) > j :
        if comp(left[i], right[j]) :
            sorted_arr.append(left[i])
            i += 1
        else :
            sorted_arr.append(right[j])
            j += 1

    #남은것 삽입
    while i < len(left) :
        sorted_arr.append(left[i])
        i += 1
    while j < len(right) :
        sorted_arr.append(right[j])
        j += 1
    
    return sorted_arr


# 왼쪽(a)가 작으면 true 반환
def comp(a, b) :
    if a[0] < b[0] :
        return True
    elif a[0] > b[0] :
        return False
    else :
        if a[1] < b[1] :
            return True
        else :
            return False


n = int(sys.stdin.readline().strip())
arr = []
for i in range(n) :
    temp = sys.stdin.readline().strip().split(" ")
    arr.append([int(temp[0]), temp[1]])
ans = merge_sort(arr)
for i in range(n) :
    print(ans[i][0], ans[i][1])