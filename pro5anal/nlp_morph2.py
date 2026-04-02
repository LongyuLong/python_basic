# 웹 문서를 읽어 형태소 분석: 위키백과에서 단어 검색결과
# 단어 출현 횟수 DataFrame으로 저장

import requests
from bs4 import BeautifulSoup
from konlpy.tag import Okt
import pandas as pd
from urllib import parse    # 한글 인코딩

okt = Okt()
# url = "https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0"
# para = "이순신" -> https://ko.wikipedia.org/wiki/이순신 출력됨
para = parse.quote("이순신")
url = "https://ko.wikipedia.org/wiki/" + para
# print(url)

headers = {"User-Agent":"Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    page = response.text
    # print(page, type(page)) # <class 'str'>
    soup = BeautifulSoup(page, 'lxml')
    wordlist = []                                   # 형태소 분석으로 명사를 추출해 기억할 리스트
    for item in soup.select("#mw-content-text p"):  # #mw .. 로 #붙이는거 까먹으면 안된다. 
        if item.string != None:
            wordlist += okt.nouns(item.string)

    print('wordlist: ', wordlist)
    print("단어 수: ", len(wordlist))
    print("중복 제거 후 단어 수: ", len(set(wordlist)))
    print()
    word_dict = {}          # 단어의 발생 횟수를 dict로 저장, 근데 dict 동작 이해가 잘 안된다.
    for i in wordlist:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    
    print('word_dict: ', word_dict)

    print("--------Series로 출력---------")
    series_list = pd.Series(wordlist)       # list 자료형으로 Series 만들고
    print(series_list[:3])                  # 시리즈 3개?
    print(series_list.value_counts()[:5])   # 시리즈_list에서 5개 보기
    print()
    series_dict = pd.Series(word_dict)
    print(series_dict[:3])
    print(series_dict.value_counts()[:5])   # 시리즈_dict에서 5개 보기

    print("--------DataFrame으로 출력---------")
    df1 = pd.DataFrame(wordlist, columns=['단어'])
    print("df1.head(3)")
    print(df1.head(3))
    print()
    df2 = pd.DataFrame([word_dict.keys(), word_dict.values()])
    df2 = df2.T
    df2.columns = ['단어', '빈도수']
    print("df2.head(3)")
    print(df2.head(3))

    df2.to_csv('nlp_morph2.csv', index=False)
    df3 = pd.read_csv('nlp_morph2.csv')
    print(df3.head())

    



