# pandas14json.py

# JSON 자료: XML에 비해 경량. 배열 개념만 있으면 처리가능

import json 
import urllib.request as req
import pandas as pd

dict = {'name':'tom', 'age':25, 'score':['90','80','88']}

print(dict, type(dict))     # 원형 출력

print('----- json 인코딩: dict -> str -----')
str_val = json.dumps(dict)      # dict를 str로 변경
# str_val = json.dumps(dict, indent=4)
print(str_val, type(str_val))
# print(str_val['name'])  # TypeError: string indices must be... 오류 발생
print(str_val[0:20])        # 문자열 관련 함수만 사용 가능
print()
print('---- json 디코딩: dict -> dict ----')
json_val = json.loads(str_val)
print(json_val, type(json_val)) # class 'dict' 확인
print(json_val['name'])         # dict 관련 명령 사용 가능

print('----- key 출력 -----')
for k in json_val.keys():
    print(k)    
print('----- value 출력 -----')
for v in json_val.values():
    print(v)

print("\n----서울시 제공 도서관 정보 json 샘플 자료(5개 읽기)----")

url = "http://openapi.seoul.go.kr:8088/sample/json/SeoulLibraryTimeInfo/1/5"
plainText = req.urlopen(url).read().decode()
print(plainText, type(plainText))

jsonData = json.loads(plainText)
print(jsonData, type(jsonData))     # class 'dict'
print(jsonData["SeoulLibraryTimeInfo"]["row"][0]["LBRRY_NAME"])

# dict의 get()사용

print()
libData = jsonData.get("SeoulLibraryTimeInfo").get("row")
name = libData[0].get('LBRRY_NAME')
print(name)

print()
datas = []
for ele in libData:
    name = ele.get("LBRRY_NAME")
    tel = ele.get('TEL_NO')
    addr = ele.get("ADRES")
    print(name, ' ', tel, ' ', addr)
    datas.append([name, tel, addr])

import pandas as pd
df = pd.DataFrame(datas, columns=['도서관명','전화','주소'])
print(df)



