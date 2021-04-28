from google_trans_new import google_translator

translator = google_translator()
flag = True
while flag:
    print("1.한국어 , 2.일본어, 3.중국어, 4.영어 ,5.프랑스어, 0. 종료")
    langNum = int(input("어떤 나라언어로 번역할까요?"))
    if langNum == 1:
        text = input("번역하고 싶은 문장을 입력하세요 : ")
        text = translator.translate(text, lang_tgt='ko', pronounce=True)
        print("번역 : " + text[0])
        print("발음 : " + text[2])
    elif langNum == 2:
        text = input("번역하고 싶은 문장을 입력하세요 : ")
        text = translator.translate(text, lang_tgt='ja', pronounce=True)
        print("번역 : " + text[0])
        print("발음 : " + text[2])
    elif langNum == 3:
        text = input("번역하고 싶은 문장을 입력하세요 : ")
        text = translator.translate(text, lang_tgt='zh-cn', pronounce=True)
        print("번역 : " + text[0])
        print("발음 : " + text[2])
    elif langNum == 4:
        text = input("번역하고 싶은 문장을 입력하세요 : ")
        text = translator.translate(text, lang_tgt='en', pronounce=True)
        print("번역 : " + text[0])
        print("발음 : " + text[1])
    elif langNum == 5:
        text = input("번역하고 싶은 문장을 입력하세요 : ")
        text = translator.translate(text, lang_tgt='fr', pronounce=True)
        print("번역 : " + text[0])
        print("발음 : " + text[1])
    else:
        print("종료합니다.")
        flag = False
