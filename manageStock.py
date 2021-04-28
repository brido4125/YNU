flag = True
my_dic = {
}
while flag:
    num = int(input("1.입고 2.출고 3.현황 4.종료 : "))
    if num == 1:
        name = input("제품명 : ")
        cnt = int(input("수량 : "))
        if name not in my_dic:
            my_dic[name] = cnt
        else:
            # dic.update()로 대체가능!
            my_dic[name] = my_dic.get(name) + cnt
        print("입고되었습니다.")
    elif num == 2:
        name = input("제품명 : ")
        cnt = int(input("수량 : "))
        if name not in my_dic:
            print("존재하지 않는 제품입니다.")
        else:
            # dic.update()로 대체가능!
            if my_dic.get(name) < cnt:
                print("출고하려는 제품 수가 더 많습니다.")
            else:
                my_dic[name] = my_dic.get(name) - cnt
                print("출고되었습니다.")
    elif num == 3:
        print(my_dic)
    elif num == 4:
        print("종료합니다.")
        flag = False
    else:
        print("잘못된 입력입니다.")
