import random

r = random.randint(1,100)
while True:
    num = input('请输入数字')
    num = int(num)
    if num == r:
        print('终于猜对啦')
        break
    elif num > r:
        print('比答案大')
    else:
        print('比答案小')
