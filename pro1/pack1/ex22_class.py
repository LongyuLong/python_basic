# 클래스는 새로운 타입을 만들어 자원을 공유 가능

# class Singer:
#     title_song = "빛나라 대한민국"

#     def sing(self):
#         msg = "노래는 "
#         print(msg,self.title_song)

# import ex22_singer
from ex22_singer import Singer              # 이렇게 import 하는게 코드 쓰는데 편하긴 함. 이렇게 안하면 ex22_singer.Singer 이런식으로 써줘야됨
bts = Singer()                              #생성자 호출해 객체 생성 후 주소를 bts라는 변수에 치환 // ()의 역할이 생성자 호출
bts.sing()

print(type(bts))
bts.title_song = "Permission to Dance"
bts.sing()
bts.co = "빅히트"
print("소속사 : ", bts.co)

print()

ive = Singer()
ive.sing()
print(type(ive))
# print('소속사 : ',ive.co)
Singer.title_song =  "아 대한민국"          # 원형 클래스의 변수 값을 변경, bts에는 영향없고 ive에게만 나타난다.

bts.sing()
ive.sing()

niceGroup = ive
niceGroup.sing()


