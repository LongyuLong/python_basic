# BeautifulSoup 객체 메서드 활용

from bs4 import BeautifulSoup

html_page = """
<html><body>
<h1>제목 태그</h1>
<p>웹 문서 연습</p>
<p>원하는 자료 확인</p>
</body></html>
"""
print(type(html_page))          # str

soup = BeautifulSoup(html_page, 'html.parser')
print(type(soup))
print()

h1 = soup.html.body.h1
print("h1: ",h1.string)

p1 = soup.html.body.p               # 최초의 p태그를 만남
print("p1: ", p1.string)

p2 = p1.next_sibling.next_sibling   # DOM을 이용한 자료 접근. 약간의 문제가 있다.
print("p2: ", p2.string)

print('\n---- find() method 사용 ----')

html_page2 = """
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹 문서 연습</p>
<p id="my" class="our">원하는 자료 확인</p>
</body></html>
"""

soup2 = BeautifulSoup(html_page2, 'html.parser')

# find(tag명, attrs, recursive, string)
print(soup2.p, ' ', soup2.p.string)
print(soup2.find('p').string)           # 처음만나는 p태그 하나만 가져온다.
                                        # find['p','h1'] 와 같이 표현하면 복수 선택가능
print(soup2.find('p',id="my").string)
print(soup2.find(id="title").string)
print(soup2.find(id="my").string)
print(soup2.find(class_="our").string)  # class뒤에 _ 는 왜 붙어야하는지.
print(soup2.find(attrs={"class":"our"}).string)
print(soup2.find(attrs={"id":"my"}).string)
print()

print('\n---- find_all() method 사용 ----')
html_page3 = """
<html><body>
<h1 id="title">제목 태그</h1>
<p>웹 문서 연습</p>
<p id="my" class="our">원하는 자료 확인</p>
<div>
    <a href="https://www.naver.com">naver</a></br>
    <a href="https://www.daum.net">daum</a></br>
</div>
</body></html>
"""
soup3 = BeautifulSoup(html_page3, 'html.parser')
print(soup3.find_all(['a']))
print(soup3.find_all(['a','p']))
print(soup3.find_all(['a','p']))
print()

links = soup3.find_all('a')
# print(links)
for i in links:
    href = i.attrs['href']
    text = i.text
    print(href, " ", text)

print('\n---- 정규 표현식 사용 ----')

import re
links2 = soup3.find_all(href=re.compile(r'^https')) # https로 시작하는
print(links2)
for k in links2:
    print(k.attrs['href'])

print('\n-----------bugs 사이트 음악 순위 읽기------------')

import requests
url = "https://music.bugs.co.kr/chart"
response = requests.get(url)
# print(response.text)
bsoup = BeautifulSoup(response.text, 'html.parser')
musics = bsoup.find_all("td", class_="check")
for idx, music in enumerate(musics):
    print(f"{idx + 1}위) {music.input['title']} ")



