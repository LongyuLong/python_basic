##opencv(computer vision) 영상 처리, 색상 처리, 필터링 
import cv2

img1 = cv2.imread('ani.jpg', cv2.IMREAD_COLOR)
print(type(img1))               ##배열이다  

cv2.imshow('image', img1)
cv2.waitKey()                   ##대기
cv2.destroyAllWindows()         ##창 닫기



#다른 이름으로 저장
cv2.imwrite('ani2.jpg', img1)
cv2.imwrite('ani3.jpg', img1, [cv2.IMWRITE_JPEG_QUALITY, 10])


#이미지 크기 조정
img2 = cv2.resize(img1,(300,100), interpolation = cv2.INTER_AREA)
cv2.imwrite('ani3.jpg', img2)

#이미지 밝기 조정

#이미지 상하좌우 회전

#특정 영역 자르기

print('end')