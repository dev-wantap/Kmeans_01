# Kmeans_01
 Kmeans 학습용

# wordlist.py
### MakeWordList_articles(article_list)
article_list의 모든 단어가 있는 리스트를 만들어 반환함. (중복x)

### MakeWordList_text(text)
text의 모든 단어를 리스트 형태로 반환함.(중복o)


# wordtovec.py
### WordToVec(WordSet, article_morp)
WordSet의 단어들을 [단어, 횟수]의 꼴로 리스트를 만들어 반환함.<br>
WordSet에는 없지만 article_morp에 있다면 [단어, 0]꼴

### Standardization(Vec)
정규화 : 문서에서 차지하는 비율로 변환 (0~1)

# dist.py
### euclidean_distance(Vec1, Vec2)
Vec1, Vec2간 유클리디안 거리 계산 후 반환
