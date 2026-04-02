# 리스트 안에 들어있는 자료를 오름차순 정렬

# 1) 선택(Selection) 정렬
# 방법1 : 이해 위주
print("-------- 이해 위주 풀이 --------")
d = [2, 4, 5, 1, 3]
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    
    return min_idx

print(find_min_idx(d))          # 가장 작은 숫자가 있는 index를 반환한다 -> 이걸 기반으로 정렬 코드 제작하는거
print()

def sel_sort(a):
    result = []
    while a:                    # 입력 리스트의 모든 값이 사라질때까지 반복한다.
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)  # pop?
        result.append(value)

    return result

print(sel_sort(d))
print()

# 방법2 : 재귀 알고리즘
print("-------- 재귀 알고리즘 풀이 --------")   
d = [2, 4, 5, 1, 3]

def sel_sort2(a):
    n = len(a)
    for i in range(0,n-1):      # 0부터 n-2회 반복한다.
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]     # 찾은 최소값을 i번 위치로 이동

sel_sort2(d)
print(d)