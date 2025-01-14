import random
rand=random.randint(1,100)
count = 1
while count <= 10:
    number = eval(input('在我心中有个数，请你猜一猜：'))
    if number > rand:
        print('大了')
    elif number < rand:
        print('小了')
    elif number == rand:
        if count <= 3:
            print('真聪明，一共猜了',count,'次')
        elif count <= 6: 
            print('还可以，一共猜了',count,'次')
        else:
            print('猜的次数有点多，一共猜了',count,'次')
        break
    count += 1 
else:
    print('您没有猜中，我心中的数字是：',rand)
