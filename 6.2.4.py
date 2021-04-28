import random

base = "abcdefghijklmnopqustuvwxyz0123456789"


def createPW():
    passwordList = [0, 0, 0, 0, 0, 0]
    for i in range(len(passwordList)):
        passwordList[i] = random.choice(base)
    print(''.join(passwordList))


for i in range(3):
    createPW()

