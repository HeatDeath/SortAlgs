'''
排序名称： 冒泡排序（Bubble Sort）（交换排序）
基本思想： 每次比较两个相邻的元素，如果顺序错误，则交换两元素的位置
总结：    如果有n个元素进行排序，只需要将n-1个元素归位，也就是说要进行n-1趟操作。
         而“每一趟”都需要从第一个位置开始进行相邻两个的比较，将比较大的元素放在后边，
         比较完毕后，向后移动一位，继续比较下面两个相邻元素的大小，重复此步骤
         直到最后一个尚未归位的元素，已归位的元素无需再次进行比较
性能：  时间复杂度O(n^2) 双重嵌套循环，稳定的排序
'''
import random
import time
def BubbleSort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:#如果一个元素>它之后的元素，则后移一位
                a[j],a[j+1]=a[j+1],a[j]

#以下内容为通用模板
def CreatRandArray(n,a):
    for i in range(n):
        a.append(random.randint(0,20))
    print(a)
a=[]
n=int(input("input the length of array you want:"))
print("let's creat an array as you want...")
ArrayCreatStart=time.clock()
CreatRandArray(n,a)
ArrayCreatEnd=time.clock()
print("we has spend %f seconds to creat your array,\nlet's sort it!"%(ArrayCreatEnd-ArrayCreatStart))
ArraySortStart=time.clock()
BubbleSort(a)
ArraySortEnd=time.clock()
print(a)
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))


