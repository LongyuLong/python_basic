# 예외처리: 파일, 네트워크, DB작업, 실행 에러 등의 에러 대처

def divide(a, b):
    return a / b

print('이런 저런 작업 진행...')

# c = divide(5,2)
# print(c)

try:                                                # 실행문(예외 발생 가능 구문)
    c = divide(5,2)
    print(c)

    aa = [1,2]
    print(aa[0])
    # print(aa[3])                                  # 여기서 오류발생하면 그 아래쪽 코드는 실행되지 않음

    open("c:/work/abc_2.txt")

except ZeroDivisionError:                           # 예외 종류 관련 클래스
    print("두번째 값은 0을 주면 안돼요")              # 예외 발생 처리 구문  
except IndexError as err:
    print("참조 범위 오류: ", err)
except Exception as e:
    print("에러: ",e)
finally:
    print("에러 유무에 상관없이 반드시 수행되는 finally")

print('end')

print('종료')





















