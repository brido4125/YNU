from fractions import Fraction


def add(a, b): return a + b;


def subtract(a, b): return a - b;


def multiply(a, b): return a * b;


def divide(a, b): return a / b;


flag = True
while flag:
    calText = input("계산식입력(ex:'1/3+1/2','bye'는 종료) : ")
    if calText == "bye":
        print("종료합니다")
        flag = False
    elif len(calText) != 7:
        print("잘못된 수식입니다.")
    elif int(calText[2]) == 0 or int(calText[6]) == 0:
        print("Divide 0 error")
    else:
        firstFrac = Fraction(int(calText[0]), int(calText[2]))
        secondFrac = Fraction(int(calText[4]), int(calText[6]))
        if calText[3] == '+':
            print(add(firstFrac, secondFrac))
        elif calText[3] == '-':
            print(subtract(firstFrac, secondFrac))
        elif calText[3] == '*':
            print(multiply(firstFrac, secondFrac))
        elif calText[3] == '%':
            print(divide(firstFrac, secondFrac))
        else:
            print("잘못된 연산자입니다.")


