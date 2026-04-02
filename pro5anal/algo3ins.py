# 리스트 안에 들어있는 자료를 오름차순 정렬
# 1) 삽입(insertion) 정렬: 앞에서부터 하나씩 꺼내서 적절한 자리에 끼워넣는 정렬

# 방법 1: 이해 위주
print("-------- 이해 위주 풀이 --------")   
d = [2, 4, 5, 1, 3]

def find_ins_idx(r, v):
    for i in range(0, len(r)):
        # vr 값이 i번 위치값보다 작으면
        if v < r[i]:
            return i
    return len(r)               # 적절한 삽입 위치를 못찾은 경우, 맨 뒤로 삽입

# List d에 있는 성분을 하나 하나 대입했을 때 오름차순 정렬 시 적절한 위치를 출력
# print(find_ins_idx(d,2))      # 1
# print(find_ins_idx(d,4))      # 3
# print(find_ins_idx(d,5))      # 4
# print(find_ins_idx(d,1))      # 0
# print(find_ins_idx(d,3))      # 2

def ins_sort(a):
    result = []
    while a:
        value = a.pop(0)
        ins_idx = find_ins_idx(result, value)
        result.insert(ins_idx, value)
        print('a: ',a)
        print('result: ', result)
    return result

print(f"최종 결과: {ins_sort(d)}")
# 출력 결과
# a:  [4, 5, 1, 3]
# result:  [2]
# a:  [5, 1, 3]
# result:  [2, 4]
# a:  [1, 3]
# result:  [2, 4, 5]
# a:  [3]
# result:  [1, 2, 4, 5]
# a:  []
# result:  [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]

# 방법2: 일반 알고리즘
print("-------- 알고리즘 풀이 --------")
d = [2, 4, 5, 1, 3]

def ins_sort2(a):
    n = len(a)
    # 두번째 값(인덱스1)부터 마지막까지 차례대로 '삽입할 대상'을 선택
    for i in range(1,n):
        key = a[i]      # i번 위치에 있는 값을 key에 저장
        j = i-1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]         # 삽입할 공간이 생기도록 값을 우측으로 밀기
            j -= 1                  # 그 다음 왼쪽으로 이동하면서 다시 비교
        a[j + 1] = key              # 찾아낸 삽입 위치에 key를 저장한다

ins_sort2(d)
print(d)
# 인수레시피~
# d = [2, 4, 5, 1, 3]
# d.sort()
# print(d)