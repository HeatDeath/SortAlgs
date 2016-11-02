'''
排序名称： 选择排序（Selection Sort）(直接选择）
基本思想： 每一次从待排序的数据元素中选出最小的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完
特点：    ①运行时间与输入无关（无论是否有序，消耗时间相同）
         ②移动次数最少（线性的）
命题A:    对于长度为n的数组，选择排序大约需要【n^2/2次比较】和【n次交换】
证明：    0-n-1的任意i都会进行【一次交换】和【n-1-i次比较】
性能：    时间复杂度O(n^2),选择排序是不稳定的。
'''
import random
import time

def SelectSort(a):
    for i in range(len(a)):
        min=i#把min标记初始化在元素a[i]处
        for j in range(i+1,len(a)):#向右侧查找
            if a[j]<a[min]:#如果找到a[j]<a[min]（被min标记的元素）
                min=j;#则将min标记移动到a[j]处
                      #min标记在找到a[i]及其右侧最小元素之前将持续右移，若未找到<a[i]的元素，则a[i]与自己交换
        a[i],a[min]=a[min],a[i]

#以下内容为通用模板
def CreatRandArray(n,a):
    ArrayCreatStart = time.clock()
    for i in range(n):
        a.append(random.randint(0,20))
        #a += [random.randint(0,20)]
    print(a)
    ArrayCreatEnd = time.clock()
    print("we has spend %f seconds to creat your array,\nlet's sort it!" % (ArrayCreatEnd - ArrayCreatStart))

a=[]
n=int(input("input the length of array you want:"))
print("let's creat an array as you want...")
CreatRandArray(n,a)

ArraySortStart = time.clock()
SelectSort(a)
ArraySortEnd = time.clock()
print(a)
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))

