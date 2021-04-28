file = open("data.txt", "r")
wordSet = set()
countList = []
wordDic = {}
text = file.read().replace("\n"," ")
for word in text.split(" "):
    wordSet.add(word)
wordList = list(wordSet)
wordList.sort()
for i in range(len(wordList)):
    countList.append(text.count(wordList[i]))
    wordDic[wordList[i]] = countList[i]
print(wordDic)
file.close()
