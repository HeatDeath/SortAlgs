'''
排序名称： 堆排序（Bubble Sort）（选择排序）
基本思想： 用大顶堆(小顶堆)堆顶记录的是最大关键字(最小关键字)这一特性，使得每次从无序中选择最大记录(最小记录)变得简单、
命题R:    将n个元素排序，堆排序只需要少于（2nlgn+2n）次比较和一般次数的交换
性能：  时间复杂度O(nlogn) 不稳定的排序
'''
import time
import random
#import heapq #堆数据结构模块


#下沉：将根节点与其左右子节点比较，若小于其子节点，则将根节点下沉
def sink(a,i,n):
    j=i*2+1
    while j<n:
        if j+1<n and a[j]<a[j+1]:#若j+1=n，则说明a[j]是该数组中的最后一个元素
            j+=1                 #根节点a[i]与其子节点(a[j]左节点,a[j+1]右节点)中较大的元素交换位置

        if a[i]>a[j]:#若a[i]大于其子节点中的最大者，则跳出循环
            break

        a[i],a[j]=a[j],a[i]#当a[i]小于其子节点中较大者时，交换两者的位置
        i=j#标记i向下移动一层，到其左子节点处
        j=i*2+1#标记j向下移动一层，到其左子节点处

#构造堆：将原始的random数组安排进堆中，使其成为大根堆（最大堆，大顶堆）
def buildheap(a):
    for i in range(len(a)//2-1,-1,-1):#从倒数第二层开始（自底向上），从右向左，依次遍历根节点
        sink(a,i,len(a))

#大根堆排序
def HeapSort(a):
    buildheap(a)#将无序的数组转化为大根堆
    print("your max_heap is:\n%s"%a)
    #将堆顶元素与最后一个节点交换位置，再调整堆
    for i in range(len(a)-1,0,-1):
        a[0],a[i]=a[i],a[0]
        sink(a,0,i)#将新的堆顶元素下沉到合适的位置，下沉结束后，余下元素依然是大根堆


'''
#使用heapq模块
def HeapqSort(a):
    heapq.heapify(a)
    b=[]
    for i in range(len(a)):
        b+=[heapq.heappop(a)]
    return b
a=HeapqSort(a)
'''

#以下内容为通用模板
def CreatRandArray(n,a):
    ArrayCreatStart = time.clock()
    for i in range(n):
        a.append(random.randint(0,90))
        #a += [random.randint(0,20)]
    print(a)
    ArrayCreatEnd = time.clock()
    print("we has spend %f seconds to creat your array,\nlet's sort it!" % (ArrayCreatEnd - ArrayCreatStart))

a=[]
n=int(input("input the length of array you want:"))
print("let's creat an array as you want...")
CreatRandArray(n,a)

ArraySortStart = time.clock()
HeapSort(a)
ArraySortEnd = time.clock()
print(a)
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))

