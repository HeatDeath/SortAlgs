'''
排序名称： 希尔排序（Shell Sort）（最小增量排序）(插入排序）
定义： 交换不相邻的而元素以此对数组进行局部排序，并最终用插入排序将局部有序的数组排序
思想： 使数组中任意间隔为h的元素都是有序的，类似于插入排序，但是使用的增量不同
特点：    排序之初，各个子数组都很短；排序之后数组都是部分有序的
适用：    可以用于大型数组，对任意排序的数组表现也很好
性质E:    使用递增序列1,4,13,40,121......的希尔排序所需的比较次数不会超过n的若干倍乘以递增序列的长度
性能：    使用递增序列1,4,13,40,121......的希尔排序运行时间达不到平方级
         希尔排序的性能分析是一个复杂的问题，因为它的时间是所取“增量”序列的函数，这涉及到一些数学上尚未解决的难题。
         希尔排序是不稳定的。
'''
import time
import random
def ShellSort(a):
    h=1
    while h<len(a)/3:
        h=h*3+1

    while h>=1:
        for i in range(h,len(a)):
            for j in range(i,h-1,-h):
                if a[j]<a[j-h]:
                    a[j],a[j-h]=a[j-h],a[j]
        h=int(h/3)


#以下内容为通用模板
def CreatRandArray(n,a):
    ArrayCreatStart = time.clock()
    for i in range(n):
        a.append(random.randint(0,100000))
        #a += [random.randint(0,20)]
    print(a)
    ArrayCreatEnd = time.clock()
    print("we has spend %f seconds to creat your array,\nlet's sort it!" % (ArrayCreatEnd - ArrayCreatStart))

a=[]
n=int(input("input the length of array you want:"))
print("let's creat an array as you want...")
CreatRandArray(n,a)

ArraySortStart = time.clock()
ShellSort(a)
ArraySortEnd = time.clock()
print(a)
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))

