#MySort.py
def BucketSort(a):
    buckets=[0]*(max(a)-min(a)+1)
    for i in range(len(a)):
        buckets[a[i]-min(a)]+=1
    sorted=[]
    for i in range(len(buckets)):
        sorted+=[i+min(a)]*buckets[i]
    return sorted

def BubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

def SelcetSort(a):
    for i in range(len(a)):
        min=i
        for j in range(i+1,len(a)):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
    return a

def InsertSort(a):
    for i in range(1,len(a)):
        tmp=a[i]
        position=i
        for j in range(i-1,-1,-1):
            if tmp<a[j]:
                a[j+1]=a[j]
                position-=1
        a[position]=tmp
    return a

def ShellSort(a):
    h=1
    while h<len(a)/3:
        h=h*3+1
    while h>=1:
        for i in range(h,len(a)):
            for j in range(i,h-1,-1):
                if a[j]<a[j-h]:
                    a[j],a[j-h]=a[j-h],a[j]
        h=h//3
    return a

def MergeSort(a):
    if len(a)<=1:
        return a
    left=MergeSort(a[:int(len(a)/2)])
    right=MergeSort(a[int(len(a)/2):])
    merged=[]
    while len(left)>0 and len(right)>0:
        merged.append(left.pop(0) if left[0]<=right[0] else right.pop(0))
    merged.extend(MergeSort(left) if len(left)>0 else MergeSort(right))
    return merged

def QuickSort(a):
    def position(a,lo,hi):
        flag=a[lo]
        j=lo
        for i in range(lo+1,hi+1):
            if a[i]<flag:
                j+=1
                a[i],a[j]=a[j],a[i]
        a[lo],a[j]=a[j],a[lo]
        return j
    def QuickSortX(a,lo,hi):
        if lo>=hi:
            return
        mark=position(a,lo,hi)
        QuickSortX(a,lo,mark-1)
        QuickSortX(a,mark+1,hi)
    lo = 0
    hi = len(a) - 1
    QuickSortX(a, lo, hi)
    return a

def HeapSort(a):
    def BuildHeap(a):
        for i in range(len(a)//2-1,-1,-1):
            AdjustHeap(a,i,len(a))
    def AdjustHeap(a,i,n):
        j=i*2+1
        while j<n:
            if j+1<n and a[j]<a[j+1]:
                j+=1
            if a[i]>a[j]:
                break
            a[i],a[j]=a[j],a[i]
            i=j
            j=2*i+1
    BuildHeap(a)
    for i in range(len(a) - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        AdjustHeap(a, 0, i)
    return a



