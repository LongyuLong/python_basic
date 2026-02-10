# 재귀문제: 리스트 자료 v = [7, 9, 15, 43, 32, 21] 에서 최대값 구하기 - 재귀
# print()


def find_max(v,n):
    if n==1:
        return v[0] # 리스트의 첫번째 값을 반환하고 재귀 종료
    #재귀 호출
    prev_max = find_max(v,n-1)
    # 앞의 n-1개 원소 중 최대값을 구함. 이 호출이 끝나야 아래 코드로 내려옴

    # 마지막 값과 비교
    if v[n-1] > prev_max:
        #현재 단계에서 마지막 원소 v[n-1]과 이전 단계에서 구한 최대값 prev_max
        return v[n-1] #마지막 값이 더 크면 그 값을 최대값으로 반환
    else:
        return prev_max
    

v = [7, 9, 15, 43, 32, 21]
print(find_max(v,len(v)))

####### 간결하게 간다면 ########

def find_max(v,n):
    if n==1:
        return v[0]
    
    return max(v[n-1],              #현재단계의 마지막 ?_?
            find_max(v,n-1))