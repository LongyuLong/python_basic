# # pack1/ex15module - main
# print('사용자 정의 모듈 처리하기')
# s = 20  #뭔가를 하다가..
# print('\n경로 지정 방법 1 : import 모듈명')

# import pack1.mymod1
# print(dir(mymod1))
# print(mymod1.__file__)
# print(mymod1.__name__)

# list1 = [1,2]
# list2 = [3,4,5]
# mymod1.listHap(list1, list2)

# if __name__ == '__main__':print('나는 메인모듈~~~')             ##메인 모듈에서만 찍힘



# print('\n경로 지정 방법 2 : from 모듈명 import 함수명')
# from mymod1 import mbc, tot
# mbc()
# print(tot)

# from mymod1 import *        # '*'을 사용해 mymod1모듈의 모든 메머 로딩(비권장)
# print('tot : ', tot)


# from mymod1 import mbc as 앰비시만새별명
# 앰비시만새별명()


# print('\n경로 지정 방법 3 : import 하위패키지.모듈명')
# import subpack.sbs
# subpack.sbs.sbsMansae()

# import subpack.sbs as nickname
# nickname.sbsMansae()

print('\n경로 지정 방법 4 : 현재 package와 동등한 다른 패키지 모듈 읽기') #python3 -m pack1.ex15module 확장자는 쓰지 말것
# import ../pack1_other.mymod2
from pack1_other import mymod2          ##from 패키지 import 파일명
print(mymod2.hapFunc(4, 3))


import mymod3 
result = mymod3.gopFunc(4,3)
print('path가 설정된 곳의 module 읽기', result)
print('end')
