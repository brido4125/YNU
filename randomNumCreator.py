import random

flag = True
while flag:
    num = int(input("몇번의 게임을 진행할까요 ?? - 0이하는 종료"))
    if num <= 0:
        flag = False
    else:
        numList = []
        for i in range(num):
            print(str(i + 1) + "회전 : ", end="")
            for k in range(6):
                numList.append(random.randint(1, 45))
            numList.sort()
            print(numList)
            numList.clear()




