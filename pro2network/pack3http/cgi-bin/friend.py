import sys
sys.stdout.reconfigure(encoding='utf-8')

import os
import urllib.parse

query = os.environ.get("QUERY_STRING", "")
params = urllib.parse.parse_qs(query)


irum = params.get("name", [""])[0]              # 없으면 빈 리스트 대신 [""] 사용
junhwa = params.get("phone", [""])[0]
gen = params.get("gen", [""])[0]

print("Content-Type: text/html; charset=utf-8")
print()
print("""
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>world</title>
</head> 
<body>
    넘겨 받은 값 : 이름은 {0}, 전화번호는 {1}, 성별은 {2}
</body>
</html>
""".format(irum, junhwa, gen))