import re                                           # 정규표현식 지원 모듈

ss = "1234 abc가나다abcABC_123s555집에가나78요_6'Python is fun'"
print(ss)
print(re.findall(r'123', ss))                       # 반환할 때 list로 가져옴. 그래서 ['123', '123'] 반환
print(re.findall(r'가나', ss))
print(re.findall(r'[0-9]', ss))
print(re.findall(r'[0-9]+', ss))
print()
print(re.findall(r'[0-9]{2}', ss))                  # 2개 연속된거?
print(re.findall(r'[0-9]{2,3}', ss))                # 연속된 2개 혹은 3개
print()
print(re.findall(r'[a-zA-Z]', ss))
print(re.findall(r'[a-zA-Z]+', ss))
print(re.findall(r'[가-힣]+', ss))
print(re.findall(r'\d+', ss))