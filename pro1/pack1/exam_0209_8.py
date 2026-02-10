	
# [문항8] 아래의 코드를 람다 함수를 이용한 소스 코드로 적으시오. (배점:5)
def Hap(m, n):
  return m + n * 5

# def hapFunc(x,y):
#     return x+y
# print(hapFunc(1,2))

# # 람다로 표현
# print((lambda x , y : x+y)(1,2))                               # 람다를 써서 코드 간소화..

print((lambda m, n: m + n * 5)(1,2))