# a = 123
# b = "456"
# print(int(b)+a)
# print(str(a)+b)
#
# c = [1,2,3,4,5]
# d = (1,2,5,6,9)
# e = {3,4,5,6,7}
# print(set(c))
# print(tuple(c))
# print(list(d))
# print(set(d))
# print(tuple(e))
# print(list(e))

# 打开模式：r 读取 w清空写入 a追加写入
# f = open ("hqb2.py",'a')
# f.write(",nice to meet you\n"",hqb\n")
# print(f.writable())
# f.close()
# g = open("aaa.txt",'w')
# g.write("hello kitty")
# g.close()
# h = open("hqb2.py",'r')
# print(h.read())
# print(h.read(20))
# print(h.readable())r
# print(h.readline())
# print(h.readlines())

# a = "abcdefghijklmnopqrstuvwxyz"
# print(a[0])
# print(a[-1])
# print(a[1:-2])
# print(a[1:-2:2])
# print(a[-1:0:-1])
# print(a[::-1])
# print(a[2:])
# print(a[:-2])
# print(a[::-2])

# z = "    sddsds     "
# print(z.strip())
# print(z.lstrip())
# print(z.rstrip())
#
# l = "ujwdbk,bdwbd,beuao"
# print(l.split(","))
#
# with open("aaa.txt",'r') as f:
#     lines = f.readlines()
#     print(lines)
#     for i in lines:
#         print(i.replace("\n",""),end="")

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{} x {} = {}".format(j,i,j*i),end="\t")
#     print()
#
# for i in range(9,0,-1):
#     for j in range(1,i+1):
#         print("%d x %d = %d"%(j,i,j*i),end="\t")
#     print()

# l = [1,23,55,88,165,555]
#
# l[0] = 20
# print(l)
# l[1:3] =20,30
# print(l)

# l = [2,3,4,5]
# l.append("王大锤一")
# l.extend({"王大锤二",1234})
# l.insert(0,"王大锤三")
# print(l)

# l = [True,1,2,515,16,35,484,36] # python Trun 1 false 0
#
# print(l.pop())
# print(l)
# print(l.pop(3))
# print(l)
# l.remove(2)
# print(l)
# l.remove(1)
# print(l)
# l.clear()
# print(l)

# a = [5,2,3,9,8797,5498,554,74,66,4152]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)


# d = {"name":"小明","age":18,"sex":"男"}
#
# d.update({"addr":"上海闵行","学历":"本科"})
# print(d)
# d['name']="小虎"
# print(d)
# d['moeny']="100000000000"
# print(d)

# d = {"name":"小明","age":18,"sex":"男"}
# s = {}
# for key in d:
#     if key.startswith("a"):
#           continue
#     s[key]=d[key]
# print(s)

# try:
#     f = open("bbbb.txt",'r')
#     print(f.read())
#     f.close()
# except:
#     print("文件不存在")
#
# print("操作完文件")
#
# def div(a,b):
#     try:
#         return a / b
#     except:
#         return
#
# print(div(10,0))
# print(div(10,30))

# class CustomException(Exception ):
#     def __init__(self,value="值不能为0"):
#         self.value = value
#
#     def __str__(self):
#         return self.value
#
# a = 2
# try:
#     if a == 0 :
#         print("a = {} 触发异常".format(a))
#         raise CustomException
#     print("a = {} 未触发异常".format(a))
# except CustomException as e:
#     print(e)



















