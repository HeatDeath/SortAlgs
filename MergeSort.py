'''
排序名称： 归并排序（Merge Sort）
基本思想： 将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序
性能：  时间复杂度O(nlog2n) 空间复杂度O(n) 稳定的排序
'''

import time
import random
def MergeSort(a):
    if len(a)<=1:#当传入的数组中只有1个元素的，返回该数组
        return a
    #将未排序的数组递归的分成左右两个子数组，至子数组的长度为1为止
    left=MergeSort(a[:int(len(a)/2)])
    right=MergeSort(a[int(len(a)/2):])
    merged=[]
    while len(left)>0 and len(right)>0:#将左右子数组的元素，按照从大到小的顺序，依次pop后放入merged[]中
                                       #当一个子数组的元素pop尽后，结束循环
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    #将未pop尽的字数组的剩余元素直接extend到merged[]的尾部
    merged.extend(MergeSort(left) if len(left)>0 else MergeSort(right))
    return merged

#以下内容为通用模板
def CreatRandArray(n,a):
    ArrayCreatStart = time.clock()
    for i in range(n):
        a.append(random.randint(0,10000000))
        #a += [random.randint(0,20)]
    print(a)
    ArrayCreatEnd = time.clock()
    print("we has spend %f seconds to creat your array,\nlet's sort it!" % (ArrayCreatEnd - ArrayCreatStart))

a=[]
n=int(input("input the length of array you want:"))
print("let's creat an array as you want...")
CreatRandArray(n,a)

ArraySortStart = time.clock()
MergeSort(a)
ArraySortEnd = time.clock()
print(MergeSort(a))
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))

