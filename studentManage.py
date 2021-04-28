flag = True
student_info = {}
while flag:
    num = int(input("1.입력 2.요약보기 3.학번검색 4.종료 : "))
    if num == 1:
        stdNum = int(input("학번 입력 : "))
        if stdNum not in student_info:
            stdName = input("이름 입력")
            stdKor = int(input("국어 성적 입력 : "))
            stdEng = int(input("영어 성적 입력 : "))
            stdMath = int(input("수학 성적 입력 : "))
            stdAvg = (stdKor + stdEng + stdMath) / 3
            if stdAvg >= 90:
                stdGrade = 'A'
            elif stdAvg >= 80:
                stdGrade = 'B'
            elif stdAvg >= 70:
                stdGrade = 'C'
            elif stdAvg >= 60:
                stdGrade = 'D'
            else:
                stdGrade = 'A'
            student_info[stdNum] = stdName, stdKor, stdEng, stdMath, round(stdAvg, 2), stdGrade
            print("입력완료")
        else:
            print("이미 존재하는 학번입니다.")
    elif num == 2:
        print("학번       평균      등급    ")
        print("===========================")
        for k in student_info.keys():
            print(k, end="\t")
            print((student_info.get(k))[4], end="\t")
            print((student_info.get(k))[5])
    elif num == 3:
        stdNum_ = int(input("검색할 학번 : "))
        if stdNum_ not in student_info:
            print("존재하지 않는 학번입니다.")
        else:
            print("학번       이름      국어      영어      수학      평균      등급")
            print("============================================================")
            print(stdNum_, end="\t")
            for i in range(6):
                print((student_info.get(stdNum_))[i], end="\t\t")
            print()
    elif num == 4:
        print("종료합니다.")
        flag = False
    else:
        print("잘못된 입력입니다.")
