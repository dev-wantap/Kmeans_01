#-*- coding:utf-8 -*-

import urllib3
import json
import math

# 언어 분석 기술(문어)
openApiURL = "http://aiopen.etri.re.kr:8000/WiseNLU"

accessKey = "<accessKey>"
analysisCode = "morp"

def MakeWordList_articles(article_list):
    text = ''
    for i in article_list:
        text += i
    requestJson = {
        "access_key": accessKey,
        "argument": {
            "text": text,
            "analysis_code": analysisCode
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )
    result = ""
    for i in str(response.data, "utf-8"):
        result += i
    wordlist = []
    morps = ['NNG', 'NNP', 'NP', 'NF', 'NV',
             'VV', 'VA', 'VX', 'VCP', 'VCN',
             'MM', 'MAG', 'MAJ',
             'IC',
             'XR',
             'SL', 'SH', 'SN']
    for i in result.split('lemma'):
        for j in morps:
            if j in i:
                k = 3
                while(i[k] != '"'):
                    k += 1
                if i[3:k] in wordlist:
                    pass
                else:
                    wordlist.append(i[3:k])
                continue
    return wordlist


def MakeWordList_text(text):
    requestJson = {
        "access_key": accessKey,
        "argument": {
            "text": text,
            "analysis_code": analysisCode
        }
    }

    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        openApiURL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(requestJson)
    )
    result = ""
    for i in str(response.data, "utf-8"):
        result += i
    wordlist = []
    morps = ['NNG', 'NNP', 'NP', 'NF', 'NV',
             'VV', 'VA', 'VX', 'VCP', 'VCN',
             'MM', 'MAG', 'MAJ',
             'IC',
             'XR',
             'SL', 'SH', 'SN']
    for i in result.split('lemma'):
        for j in morps:
            if j in i:
                k = 3
                while(i[k] != '"'):
                    k += 1
                wordlist.append(i[3:k])
                continue
    return wordlist
