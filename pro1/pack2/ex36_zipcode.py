# 우편 정보 파일 자료 읽기
# 키보드에서 입력한 동 이름으로 해당 주소 정보 출력

def zipProcess():
    dongIrum = input("동 이름 입력: ")
    
    # print(dongIrum)
    with open(r"zipcode.txt", mode = 'r', encoding='euc-kr') as f:      # 한글 인코딩 utf-8이 안되면 euc-kr로 시도
        line = f.readline()                                             # 한 행 읽기
        # print(line)                                                   # 135-806 서울    강남구  개포1동 경남아파트 << 잘라줘야 쓸 수 있다.
        # lines = line.split("\t")                                      # lines = line.split(chr(9)) : tab 키를 구분자로 자른다., chr(9)는 ASCII 코드
        # print(lines)                                                  # 자주 사용되는 아스키코드값으로는 10, 13번 = (Enter) 입력이 있다
        while line:
            lines = line.split("\t")
            if lines[3].startswith(dongIrum):
                # print(lines)
                print('우편번호: '+ lines[0] + ', ' + ' ' + lines[2] + ' ' + lines[3])

            line = f.readline()

if __name__ == '__main__':  
    zipProcess()

