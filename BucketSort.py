'''
排序名称： 桶排序（Bucket Sort）
基本思想： 设置一个个的桶，将需要排序的对象列表按顺序放入桶里面。（利用函数的映射关系，减少了几乎所有的比较工作）
总结：    桶排序对于相同对象特别多的列表速度特别快。但是遗憾的是需要排序的对象必须是已知的数值。
性能：时间复杂度O(n)，空间复杂度为O(n+m)  (n位待排序数的个数，m为桶的个数）
     如果输入数据非常庞大，则空间代价是昂贵的。桶排序是稳定的。
'''
import random
import time
def BucketSort(a):
    buckets=[0]*(max(a)-min(a)+1)#初始化一个大小为max(a)-min(a)+1的buckets[]
    for i in range(len(a)):#遍历a[]，将a[]中的元素依次放入相应的桶中
        buckets[a[i] - min(a)] += 1

    Sorted_a = []

    for i in range(len(buckets)):#遍历buckets[]
        if buckets[i] != 0:#排除元素个数为0的桶
            Sorted_a += [i + min(a)] * buckets[i]#将(buckets的下标+min(a))(还原为原来的数字）
                                                 # 依次放入buckets[i]个
    return Sorted_a


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
BucketSort(a)
ArraySortEnd = time.clock()
print(BucketSort(a))
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))