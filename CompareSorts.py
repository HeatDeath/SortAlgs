#import sys
#sys.path.append(r'C:\Users\Administrator\AppData\Local\Programs\Python\Python35')
import MySort
import random
import time

def CreatRandArray(n,a):
    for i in range(n):
        a.append(random.randint(0,100000))
    print(a)
a=[]
n=int(input("input the length of array you want:"))
CreatRandArray(n,a)
print("---------let's sort it!---------")
print("################################")
b=a[:]
c=a[:]
d=a[:]
e=a[:]
f=a[:]
g=a[:]
h=a[:]

print("------BucketSort------")
ArraySortStart=time.clock()
MySort.BucketSort(a)
ArraySortEnd=time.clock()
print(MySort.BucketSort(a))
print("%f seconds"%(ArraySortEnd-ArraySortStart))
print('--------------------------------------------------------------')

print("------BubbleSort------")
ArraySortStart=time.clock()
MySort.BubbleSort(b)
ArraySortEnd=time.clock()
print(MySort.BubbleSort(b))
print("%f seconds"%(ArraySortEnd-ArraySortStart))
print('--------------------------------------------------------------')

print("------SelectSort------")
ArraySortStart=time.clock()
MySort.SelcetSort(c)
ArraySortEnd=time.clock()
print(MySort.SelcetSort(c))
print("%f seconds"%(ArraySortEnd-ArraySortStart))
print('--------------------------------------------------------------')

print("------InsertSort------")
ArraySortStart=time.clock()
MySort.InsertSort(d)
ArraySortEnd=time.clock()
print(MySort.InsertSort(d))
print("%f seconds"%(ArraySortEnd-ArraySortStart))
print('--------------------------------------------------------------')

print("------ShellSort------")
ArraySortStart=time.clock()
MySort.ShellSort(e)
ArraySortEnd=time.clock()
print(MySort.ShellSort(e))
print("%f seconds"%(ArraySortEnd-ArraySortStart))
print('--------------------------------------------------------------')

print("------MergeSort------")
ArraySortStart=time.clock()
MySort.MergeSort(f)
ArraySortEnd=time.clock()
print(MySort.MergeSort(f))
print("%f seconds"%(ArraySortEnd-ArraySortStart))
print('--------------------------------------------------------------')

print("------QuickSort------")
ArraySortStart=time.clock()
MySort.QuickSort(g)
ArraySortEnd=time.clock()
print(MySort.QuickSort(g))
print("%f seconds"%(ArraySortEnd-ArraySortStart))
print('--------------------------------------------------------------')

print("------HeapSort------")
ArraySortStart=time.clock()
MySort.HeapSort(h)
ArraySortEnd=time.clock()
print(MySort.HeapSort(h))
print("%f seconds"%(ArraySortEnd-ArraySortStart))
print('--------------------------------------------------------------')




'''
ArraySortStart=time.clock()
BubbleSort(a)
ArraySortEnd=time.clock()
print(a)
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))
print('--------------------------------------------------------------')



'''