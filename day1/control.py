# C_1 = [12,49,70,66,85,98,79,101]
#
# for C in C_1:
#     if (C > 0 and C <= 59):
#         print("不及格")
#     elif (C >= 60 and C <= 70):
#         print("及格")
#     elif (C > 70 and C <= 80):
#         print("良好")
#     elif (C > 80 and C <= 100):
#         print("优秀")
#     else:
#         print("请输入正确的成绩")
#
# for i in  range(1,100,2):
#     print(i)
#
# s = 1
# for i in range(10,0,-1):
#     s = s * i
# print(s)
#

# a = 59
#
# while True:
#     b = int(input("请输入数字"))
#     if b > a:
#         print("大了")
#     elif(b < a):
#         print("小了")
#     else:
#         print("猜对了")
#         break

# for i in range(1,100):
#     if (i % 3 != 0):
#         continue
#     print(i)

# def lever(a , b):
#     print(a // b)
#     print(a % b)
# lever(33 , 8)
# lever(20 , 8)
# def shang_yu(a,b):
#     if(b==0):
#         return  None
#     else:
#         return  (a // b,a % b)
#
# res = shang_yu(20,3)
# res = shang_yu(25,b=3)
#
# if res is None:
#     print("参数错误")
# else:
#     print("商为：",res[0],"余数为：",res[1])

# def sm(a,b=2):
#     return (a+b)
# print(sm(3))
#
# def sum1(name,*args,**kwargs):
#     print(kwargs)
#     print(name)
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum1(1,2,3,4,6,1,511,1,1851,55))
# print(1,2,3,4,6,1,511,1,1851,55)
# print(sum1(name="薛潇"))


# a = 10 # 全局变量
# print(a)
#
# def aaa():
#     global a
#     a = 12
#
# aaa()
# print(a)

# 面向对象
# class calc():
#     a = None
#     b = None
#     res = None
#     def input(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def jian(self):
#         self.res = self.a - self.b
#     def cheng(self):
#         self.res = self.a * self.b
#     def get_result(self):
#         print(self.res)
#
#
# c = calc()  # 类的实例化 c对象
#
# c.input(10,20)
# c.sum()
# c.get_result()
# c.div()
# c.get_result()
# c.jian()
# c.get_result()
# c.cheng()
# c.get_result()

# class calc():
#     res = None
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res = self.a + self.b
#     def div(self):
#         self.res = self.a / self.b
#     def jian(self):
#         self.res = self.a - self.b
#     def cheng(self):
#         self.res = self.a * self.b
#     def get_result(self):
#         print(self.res)
#
# c = calc(29,39)  # 类的实例化 c对象
# c.sum()
# c.get_result()
# c.div()
# c.get_result()
# c.jian()
# c.get_result()
# c.cheng()
# c.get_result()

# print("ssss",end="\n")
# print("ssss",end="\t")
# print("ssss")
# # 九九乘法表
# for i in range(9,0,-1):
#      for j in range(1,i+1):
#          print(j,"x",i,"=",i*j,end="\t")
#      print()
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, "x", i, "=", i * j, end="\t")
#     print()
#
# l = [11,13,15,141,18,6695,1,3,9,54,5245,654666,7,75,46,96]
#
# length = len(l)
# print(len(l))
# for i in range(length-1,0,-1):# 外层循环确定排好序的数据下标
#     for j in range(i):# 遍历为排好序的列表
#         if (l[j] > l[j+1]):# 判断相邻两个数据，前边的如果大于后边的，则两个数据的位置互换
#             l[j],l[j + 1] =l[j+1],l[j]
# print(l)
# for i in range(10,0,-1):
#     print(i)

class Parents():
    money = "10亿"
    house = "10套"
    car = "宾利"
    __shoes = "2双"
    _socks = "2双"

    def technique(self):
        print("点石成金")

class Children(Parents):
    hobby = "花钱"

    def technique(self):
        super().technique()
        print("戈师奶大牛")# 方法重写

c = Children()
print(c.car)
print(c.hobby)
print(c.house)
print(c.money)
c.technique()
















