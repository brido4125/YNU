import random

x = random.randint(1, 100)
cnt = 0
num = 0
while x != num:
    num = int(input("숫자를 입력하세요 : "))
    if num < x:
        cnt += 1
        print("UP!")
    elif num > x:
        cnt += 1
        print("Down!")
    else:
        cnt += 1
        print(str(cnt) + "번만에 맞춤")
        break
