# 리스트 안에 들어있는 자료를 오름차순 정렬
# 1) 병합(merge) 정렬
# List 내에 자료가 1개씩 남을 때 까지 반복해서 List 자료를 반으로 나눈다.
# 분할된 리스트를 정렬하며 하나로 합친다
# 방법1: 이해 위주

def merge_sort(a):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2                    # List의 중간 지점을 찾아서 두 그룹으로 나눈다
    # 함수는 독립적인 공간을 갖는다 -> 아래 group1, group2는 서로 간섭하지않는다.
    group1 = merge_sort(a[:mid])    # 재귀
    group2 = merge_sort(a[mid:])    # 여기까지만 작성하고 결과 출력하면 [6]이 나오는데,
                                    # 제일 앞에 있는 6만 남고 나머지는 다른 메모리에 있다? 설명좀
    # print('group1: ',group1)
    # print('group2: ',group2)
    
    # 두 그룹
    result = []
    while group1 and group2:
        print(group1[0], ' ', group2[0])
        if group1[0] < group2[0]:
            result.append(group1.pop(0))
        else:
            result.append(group2.pop(0))
        print("result: ", result)

    # group1과 group2 중 소진된 것은 스킵
    while group1:
        result.append(group1.pop(0))
    while group2:
        result.append(group2.pop(0))    
    return result

d = [6,8,3,1,2,4,7,5]
print(merge_sort(d))

print()

# 방법2: 일반 알고리즘
# 재귀호출이 정렬된 리스트를 반환
# 병합도 새 리스트를 만들어 반환
# 원본 리스트는 그대로이고 정렬된 결과는 새 리스트에 저장

def merge_sort2(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort2(a[:mid])
    right = merge_sort2(a[mid:])
    result = []
    i = j = 0

    # 병합
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # 남은 요소 추가
    result += left[i:]
    result += right[j:]

    return result



d = [6,8,3,1,2,4,7,5]
sorted_d = merge_sort2(d)
print(sorted_d)












