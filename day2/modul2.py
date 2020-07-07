# from day2.modul1 import a as b,name as c,modul1 as d
#
# a = "modul1"
#
# def name():
#     print("我是连海平")
# class modul1():
#     name="我是共潮生"
#
# print(b)
# c()
# print(d.name)

import random

# 电脑随机出拳


user = int(input('请出拳：1，2/剪刀，3/布'))
computer = random.randint(1, 3)


if user == 1:
    user = '拳头'
elif user == 2:
    user = '剪刀'
else:
    user = '布'

if computer == 1:
    computer = '拳头'
elif computer == 2:
    computer = '剪刀'
else:
    computer = '布'

print('电脑出的是{},沙雕余鹏出的是{}' .format(computer, user))
if ((user == 1 and computer == 2)
        or (user == 2 and computer == 3)
        or (user == 3 and computer == 1)):
    print('沙雕余鹏胜出~_~')
elif user == computer:
    print('好吧，平局@_@')
else:
    print('电脑胜出！')














