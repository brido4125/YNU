NumDic = {"zero": "영",
          "one": "일",
          "two": "이",
          "three": "삼",
          "four": "사",
          "five": "오",
          "six": "육",
          "seven": "칠",
          "eight": "팔",
          "nine": "구",
          "ten": "십",
          }

word = ""
while word != 'q':
    word = input("영어를 입력(종료는 q) : ")
    if word == 'q':
        print("종료합니다.")
    else:
        print(NumDic.get(word))
