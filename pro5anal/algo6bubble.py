# 이웃한 요소와 비교
# [2 4 5 1 3]
# [2 4 1 5 3]
# [2 4 1 3 5]
# ..
# [1 2 3 4 5]

def bubble_sort(a):
    n = len(a)
    while True:
        change = False      # 자료를 앞뒤 변경 여부 확인용

        for i in range(0,n-1):
            if a[i] > a[i+1]:   # 앞쪽 성분이 더 크면
                print(a)
                a[i], a[i+1] = a[i+1], a[i]
                change = True
        if change == False:
            return


d = [2,4,5,1,3]
bubble_sort(d)
print(d)