# l = [11,13,15,141,18,6695,1,3,9,54,5245,654666,7,75,46,96]
# length = len(l)
# print(len(l))
# for i in range(length-1,0,-1):
#     for j in range(i):
#         if l[j] > l[j+1]:
#             l[j], l[j+1]= l[j+1],l[j]
# print(l)
# #
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j, "x", i, "=", i * j, end="\t")# print("%dx%d=%d"%(j,i,i*j),end="\t")
#     print()


# l = [11,13,15,141,18,6695,1,3,9,54,5245,654666,7,75,46,96]
# length = len(l)
# print(len(l))
# for i in range(0,length):
#     for j in range(0,(length-1)-i):
#         if l[j] < l[j+1]:
#             l[j + 1], l[j] =  l[j], l[j+1]
# print(l)

# s = 100
# if (s>=0 and s<=59):
#     print("不及格")
# elif (s>=60 and s<=70):
#     print("及格")
# elif (s>=71 and s<=80):
#     print("良好")
# elif (s>=81 and s<=100):
#     print("优秀")
# else:
#     print("输入正确的成绩")


# l = [11,13,15,141,18,6695,1,3,9,54,5245,654666,7,75,46,96]
#
# length=len(l)
# print(len(l))
# for i in range(length-1,0,-1):
#     for j in range (i):
#         if (l[j]>l[j+1]):
#             l[j],l[j+1]=l[j+1],l[j]
# print(l)

for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,i*j),end="\t")
    print()






















