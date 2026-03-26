# 한글 형태소 분석
# 형태소(Morpheme)는 의미를 갖는 가장 작은 단위
# 실제 사용된 언어를 컴퓨터가 읽을 수 있는 형태로 
# 대규모로 수집, 가공, 저장한 언어 자료의 집합
# 문법 연구, 번역 시스템, 챗봇 등 다양한 언어 데이터 분석의 기초 자료로 활용
# 형태소(Morpheme)는 의미를 가지는 가장 작은 단위를 말함

# 대표적인 한글 형태소 분석 라이브러리
from konlpy.tag import Okt, Kkma, Komoran

text = "나는 오늘 아침에 학교에 갔다. 가는 길에 강아지를 봤는데 귀여웠다"

print("-------- Okt ---------")
okt = Okt()
print("형태소: ",okt.morphs(text))
print("품사 태깅: ",okt.pos(text))
print("품사 태깅(어간 포함): ",okt.pos(text,stem=True))     # 원형을 출력. 봤는데->보다
print("명사 추출: ",okt.nouns(text))
print()

print("-------- Kkma ---------")
kkma = Kkma()
print("형태소: ",kkma.morphs(text))
print("품사 태깅: ",kkma.pos(text))
print("명사 추출: ",kkma.nouns(text))
print()

print("-------- Komoran ---------")
komoran = Komoran()
print("형태소: ",komoran.morphs(text))
print("품사 태깅: ",komoran.pos(text))
print("명사 추출: ",komoran.nouns(text))
print()

