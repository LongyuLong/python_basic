var1 = "안녕 파이썬"
print(var1)  # 주석
'''여러줄 주석'''
var1 = 5; var2 = var1
print(var1,var2)
var3 = 7
print(id(var1), var2, var3)

Var3 =8
print(var3, Var3)

a = 5
b = a
c = 5

print(a,b,c)
print(a is b, a==b)
print(b is c, b==c) # is: 주소 비교 연산, ==:값 비교 연산

aa=[5]
bb=[5]
print(aa,bb)

print(aa is bb, aa==bb)
# print('-----') 
print("------------")

import keyword
print('예약어 목록:', keyword.kwlist)

print('type(자료형) 확인')
kbs = 9
print(isinstance(kbs,int))
print(isinstance(kbs,float))
print(5,type(5)) # 5 <class 'int'>
print(5.3,type(5.3)) # 5.3 <class 'float'>
print(5+4j,type(5+4j)) # 5+4j <class 'complex'>
print(True,type(True))
print('good', type('good'))
print((1,), type((1,)))
print([1], type([1]))
print({1},type({1}))
print({'k':1}, type({'k':1}))


