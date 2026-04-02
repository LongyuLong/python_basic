# 웹(동아일보)에서 특정 단어 관련 문서들 검색 후 명사만 추출
# 워드클라우드 그리기

# pip install pygame simplejson pytagcloud

from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib.request
from konlpy.tag import Okt
from collections import Counter     # 단어 수 카운팅하는 라이브러리
import pytagcloud
import matplotlib.pyplot as plt
import koreanize_matplotlib
import matplotlib.image as mpimg
import webbrowser

# keyword = input("검색어: ")
# print(quote(keyword))
keyword = "춘분"

target_url = "https://www.donga.com/news/search?query=" + quote(keyword)
source_code =  urllib.request.urlopen(target_url)       # urllib.request 사용
print(source_code)
soup = BeautifulSoup(source_code, 'lxml', from_encoding="utf-8")
# print(soup)

msg = ""

for title in soup.find_all("h4",class_='tit'):  # class_= 의 용도 기억안남, h4태그 찾기
    title_link = title.find("a")                # a태그 찾아서 제목 뽑기
    # print(title_link)     # 제목 가져오는건 확인했고 이제 해당 제목의 기사 내용을 봐야하니까 링크 가져와야함
    article_url = title_link["href"]            # title_link에서 href를 가져온다? 이게 어떻게 동작하는지 궁금함
    # print(article_url)    # https://www.donga.com/news/Society/article/all/20260320/133567679/2 << 예시
    try:
        source_article = urllib.request.urlopen(article_url)
        soup2 = BeautifulSoup(source_article)
        # print(soup2)
        contents = soup2.select("div.article_txt")   # select(클래스) >> div탭의 article_txt라는 class 읽어오기
        # print(contents)
        for imsi in contents:
            item = str(imsi.find_all(string=True))
            msg += item
        # print(msg)

    except Exception as e:
        pass

    okt = Okt()
    nouns = okt.nouns(msg)
    result = []
    
    for imsi in nouns:
        if len(imsi)>1:
            result.append(imsi)
    
# print(result[:20])

count = Counter(result)
# print(count) 

# 워드클라우드 만들기, 상위 50개만
tag = count.most_common(50)
# print(tag)           # // [('기운', 17), ('스포츠동아', 12), ('오늘', 12), ....

taglist = pytagcloud.make_tags(tag,maxsize=100)
# print(taglist)       #[{'color': (42, 124, 146), 'size': 123, 'tag': '기운'}, {'color': (135, 130, 176), 'size': 93, ...

pytagcloud.create_tag_image(
        taglist, 'word.png', size=(1000, 600),
        background=(0,0,0),rectangular=False,
        fontname='korean'
    )

img = mpimg.imread('word.png')
plt.imshow(img)
plt.show()

# webbrowser.open('word.png') << 이건 왜 안되나?