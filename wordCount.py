from collections import Counter
import re

txt = input("영어문장 : ")
separators = ",", " ", ".", "'"


def mySplit(sepr_list, str_to_split):
    regular_exp = '|'.join(map(re.escape, sepr_list))
    return re.split(regular_exp, str_to_split)


wordList = mySplit(separators, txt)
print(wordList)
countList = Counter(wordList)
print(countList)
