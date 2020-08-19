def WordToVec(WordSet, article_morp):
    article_vect = []
    for i in WordSet:
        j = 0
        for k in article_morp:
            if i == k:
                j += 1
        article_vect.append([i, j])
    return article_vect


def Standardization(Vec):
    sum_ = 0
    for i in Vec:
        sum_ += i[1]
    for i in Vec:
        i[1] /= sum_
    return Vec
