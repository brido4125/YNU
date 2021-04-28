sentence = input("문장을 입력하세요 : ")
sentenceSet = set(sentence)
alpha = list(sentenceSet)
alpha.sort()
countNumList = []
sentenceDic = {}

for i in range(len(alpha)):
    countNumList.append(sentence.count(alpha[i]))
    sentenceDic[alpha[i]] = countNumList[i]

print(sentenceDic)
print("가장 높은 빈도수 : ", end="")
print(max(sentenceDic.values()))
