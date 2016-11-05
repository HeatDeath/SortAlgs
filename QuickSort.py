'''
排序名称： 快速排序（Quick Sort）（交换排序）
基本思想： 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
         然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列
性能：  时间复杂度O(nlog2n) 不稳定的排序
'''
import random
import time

def QuickSort(a,lo,hi):
    if lo>=hi:#如果只有一个数字时，结束递归
        return
    flag=lo
    for i in range(lo+1,hi+1):#以数组的第一个元素作为基准数，从第二个数开始，依次向右比较
        if a[flag]>a[i]:      #若小于a[flag]则插入到a[flag]的左侧；否则继续比较下一个数
            tmp=a[i]
            del a[i]
            a.insert(flag,tmp)
            flag+=1
    QuickSort(a,lo,flag-1)#将基准数前边递归排序
    QuickSort(a,flag+1,hi)#将基准数后边递归排序


#该算法看了visuAlgo之后，自然而然就写出来了：）
def position(a,lo,hi):
    flag=a[lo]
    j=lo
    for i in range(lo+1,hi+1):#从左向右遍历，依次查找小于flag的元素，并将其依次排列在a[lo]的身后
        if a[i]<flag:
            j+=1
            a[j],a[i]=a[i],a[j]
    a[lo],a[j]=a[j],a[lo]     #遍历结束后，交换a[lo]和他身后的最后一个小于他的元素
                              #交换结束后，flag值所在的位置的左侧的元素都小于他，右侧的都大于他
    return j                  #返回flag值现在所处的位置

def QuickSortX(a, lo, hi):
    if lo >= hi:
        return
    mark = position(a, lo, hi)
    QuickSortX(a, lo, mark - 1)#将左侧的部分递归排序
    QuickSortX(a, mark + 1, hi)#将右侧的部分递归排序


#以下内容为通用模板
def CreatRandArray(n,a):
    ArrayCreatStart = time.clock()
    for i in range(n):
        a.append(random.randint(0,10000))
        #a += [random.randint(0,20)]
    print(a)
    ArrayCreatEnd = time.clock()
    print("we has spend %f seconds to creat your array,\nlet's sort it!" % (ArrayCreatEnd - ArrayCreatStart))

a=[]
n=int(input("input the length of array you want:"))
print("let's creat an array as you want...")
CreatRandArray(n,a)
b=a[:]

ArraySortStart = time.clock()
QuickSort(a,0,len(a)-1)
ArraySortEnd = time.clock()
#print(a)
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))

ArraySortStart = time.clock()
QuickSortX(b,0,len(b)-1)
ArraySortEnd = time.clock()
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))
