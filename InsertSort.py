'''
排序名称： 插入排序（Insertion Sort）(直接插入）
基本思想： 为了给要插入的元素腾出空间，将其余所有在合适的插入位之后的元素依次右移一位
时间：    所需时间取决于输入中元素的初始顺序
命题B:    对于随机排列的长度为n且主键不重复的数组，平均情况下插入排序需要【~n^2/4次比较】和【~n^2/4次交换】
                                           最坏情况下插入排序需要【~n^2/2次比较】和【~n^2/2次交换】
                                           最好情况下插入排序需要【n-1次比较】和【0次交换】
命题C:    插入排序需要的【交换次数】和数组中倒置的数量相同，倒置的数量<=【比较次数】<=倒置的数量+len(a)-1
性能：    时间复杂度O(n^2),插入排序是稳定的。
'''
import random
import time


def InsertSort(a):
    for i in range(1,len(a)):
        for j in range(1,i+1)[::-1]:#从当前位置a[i]开始向左遍历到a[1]
            if a[j]<a[j-1]:#若<左侧元素，则交换位置
                a[j],a[j-1]=a[j-1],a[j]


#Improved，较大元素直接右移，不用交换位置
#经测试，该方法可以小幅度缩短对相同数组的运行时间
def InsertSortX(a):
    for i in range(1,len(a)):
        tmp=a[i]#利用tmp储存a[i]当前的值
        position=i#位置标记初始化为当前位置
        #for j in range(0,i)[::-1]:#从位置a[i-1]开始向左遍历到a[1]
        for j in range(i-1,-1,-1):
            if tmp<a[j]:#若遇到大于a[i]的元素，将其右移(此时a[i]"悬空")
                a[j+1]=a[j]
                position-=1#位置标记左移一位
        a[position]=tmp#将tmp存入到正确的位置

'''把a[]中的最小值放在a[0]当做哨兵似乎并不能优化运行时间
#算法第四版中说：在插入排序的实现中先找出最小的元素并将其置于数组的最左边，这样就能去掉内循环的判断条件j>0
def InsertSortX(a):
    a.insert(0,min(a))
    for i in range(1,len(a)):
        tmp=a[i]#利用tmp储存a[i]当前的值
        position=i#位置标记初始化为当前位置
        for j in range(i)[::-1]:#从位置a[i-1]开始向左遍历到a[1]
            if tmp<a[j]:#若遇到大于a[i]的元素，将其右移(此时a[i]"悬空")
                a[j+1]=a[j]
                position-=1#位置标记左移一位
        a[position]=tmp#将tmp存入到正确的位置
    a.pop()
'''

'''
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
'''
a=[45476, 31269, 88106, 67693, 33589, 81322, 83327, 60884, 92223, 75413, 83455, 82790, 92192, 71210, 28467, 22797, 57780, 45902, 21124, 7047, 59337, 62798, 18833, 26824, 71973, 40233, 33090, 68259, 12988, 13697, 19059, 82975, 99525, 37660, 69485, 97008, 41806, 58097, 39840, 43930, 71076, 99200, 28796, 55418, 54326, 3130, 12465, 7206, 93529, 98033, 48415, 28223, 90018, 73405, 61659, 61703, 97561, 77814, 82035, 72514, 94623, 90843, 52610, 82107, 12414, 83934, 32207, 37879, 70322, 88019, 84338, 62014, 51696, 16817, 83626, 17015, 42377, 41370, 40890, 41788, 15906, 71108, 64368, 9165, 35868, 7810, 95550, 99910, 80314, 78661, 22163, 9413, 6432, 59063, 69636, 10192, 47132, 35238, 86626, 37547, 74607, 44215, 17171, 46507, 22847, 42814, 20605, 37623, 8983, 11118, 52748, 5114, 20978, 52688, 72590, 12449, 73232, 17348, 78455, 10201, 87214, 18373, 53508, 41000, 47471, 28956, 83459, 12320, 14571, 97169, 70731, 45744, 79297, 68071, 26118, 18273, 65032, 83405, 47677, 49342, 37321, 90817, 30324, 72312, 94267, 91030, 55091, 7208, 11224, 19536, 43086, 60544, 69203, 34784, 70100, 22836, 29184, 81341, 36531, 51572, 32697, 89278, 20316, 96354, 55456, 69808, 54898, 20487, 3368, 12894, 25567, 30720, 27422, 71970, 38267, 53172, 35281, 84658, 46200, 83806, 50133, 53443, 87126, 80096, 22262, 60724, 54229, 22018, 36534, 12471, 68404, 21733, 84116, 30401, 1053, 10481, 78477, 25548, 68073, 92940, 798, 30153, 6597, 23113, 90254, 96253, 28427, 72106, 11306, 15666, 29637, 17406, 81068, 60657, 40215, 9020, 32229, 74201, 31601, 53267, 79819, 88134, 23621, 8239, 4465, 65099, 42528, 45503, 15425, 13193, 90232, 30868, 59730, 71656, 17068, 1542, 22473, 32328, 82396, 25783, 5875, 13209, 46793, 46072, 31359, 70281, 22263, 75560, 11895, 87657, 72643, 68771, 45523, 95667, 51928, 70085, 87529, 10787, 90797, 86888, 24564, 37065, 39078, 67521, 54545, 32138, 47425, 68775, 5535, 59135, 95483, 13783, 10193, 69874, 75692, 69023, 61914, 53477, 62129, 98520, 59428, 20164, 74358, 27408, 85267, 73257, 22324, 57552, 81412, 30249, 78739, 71025, 47330, 83705, 49894, 76198, 99043, 69577, 68579, 34629, 88298, 64464, 92409, 96237, 20562, 80001, 3869, 55263, 79835, 88434, 42274, 43243, 63603, 76740, 98570, 48785, 62727, 25855, 25253, 80106, 60118, 1636, 66463, 55698, 48781, 88122, 49897, 95385, 94929, 30095, 32807, 35586, 13712, 76640, 41824, 85984, 75110, 44600, 28652, 80814, 481, 92817, 85976, 28788, 28724, 81241, 44685, 60576, 76719, 32328, 10553, 17227, 90676, 87949, 71056, 47899, 59864, 54979, 62923, 31426, 2973, 68540, 68379, 85465, 739, 4206, 81930, 94755, 92293, 57726, 14996, 30610, 22152, 93949, 5051, 54452, 41866, 10601, 2773, 14154, 37143, 33477, 52615, 97369, 56429, 10303, 6070, 39849, 72696, 17065, 58012, 32561, 60039, 48222, 8819, 29902, 11046, 15323, 58878, 89758, 28033, 75328, 50617, 32398, 90326, 19484, 40016, 62295, 44565, 18130, 31089, 92045, 76414, 4213, 60508, 1478, 50144, 68527, 18838, 25422, 95090, 66788, 46210, 41623, 57812, 63491, 49805, 87593, 62042, 65961, 90031, 45039, 19199, 70921, 13373, 5795, 93644, 52494, 47383, 15789, 89959, 80473, 59830, 97422, 7711, 47964, 99364, 46024, 26861, 57022, 96315, 76337, 9814, 16338, 94655, 14478, 53973, 57477, 37008, 82973, 31685, 39499, 73161, 34697, 78270, 43494, 85304, 69951, 4354, 45569, 47353, 15184, 60399, 79287, 61133, 30019, 88732, 50908, 27806, 55533, 89357, 28995, 40802, 63738, 42031, 61692, 11811, 80303, 46704, 45195, 66021, 35633, 4572, 33294, 54761, 5251, 65315, 74094, 98376, 79384, 12835, 47942, 63832, 67656, 27498, 94221, 62106, 16700, 92834, 14926, 23774, 90787, 14388, 14458, 31935, 29928, 60230, 61027, 14025, 96530, 86481, 73664, 79242, 1146, 64009, 23191, 95082, 24581, 3105, 9971, 95713, 54702, 2658, 82942, 54515, 42442, 89090, 86238, 22411, 66166, 32151, 59134, 95127, 36444, 26932, 47232, 35350, 75408, 90523, 48972, 70755, 54022, 33823, 67135, 11542, 72802, 56321, 45889, 88959, 56473, 10431, 97487, 9629, 77540, 79279, 94553, 9682, 71651, 63924, 63315, 28427, 80463, 91729, 43437, 40388, 40826, 96387, 37510, 25582, 21932, 76252, 86126, 97480, 78952, 99466, 15536, 47556, 38364, 41989, 50449, 13556, 60198, 50317, 36901, 64789, 42853, 13522, 20334, 93143, 78010, 46797, 20837, 66858, 6064, 13993, 81283, 7734, 49839, 24900, 96386, 61608, 4715, 53736, 11609, 61356, 34878, 17577, 98661, 19815, 54144, 35055, 38114, 52386, 16912, 64138, 52559, 94252, 97587, 80735, 5875, 61975, 16402, 99504, 77889, 80268, 51291, 79668, 54985, 76013, 31847, 48735, 27578, 92067, 50737, 94459, 21477, 27830, 33781, 15568, 25622, 8628, 65953, 16950, 2775, 92447, 7869, 3231, 50527, 95530, 49060, 33607, 44720, 85299, 29038, 45979, 85920, 78639, 22881, 8520, 18353, 96832, 2000, 28399, 22892, 31231, 73134, 96244, 69952, 60256, 88577, 32125, 62150, 50961, 57343, 95648, 7391, 39223, 60228, 54806, 3643, 86160, 95235, 67156, 11231, 15290, 80366, 2133, 17760, 90469, 7746, 74252, 21968, 26013, 54765, 25407, 32761, 45775, 10944, 66306, 95430, 35838, 50738, 43001, 16378, 5148, 87372, 37462, 52528, 99084, 37831, 89473, 97441, 92143, 85295, 69575, 45628, 49188, 75802, 33618, 20270, 90467, 21546, 55368, 94248, 63097, 50769, 85221, 81822, 33738, 38207, 23722, 36219, 87673, 65411, 74665, 75754, 98058, 97385, 17382, 57641, 73274, 12009, 29992, 19397, 51602, 66995, 68928, 64527, 57006, 17306, 73088, 71204, 85744, 67437, 84344, 75016, 43474, 94844, 12878, 75603, 40053, 37210, 1087, 40116, 52140, 52279, 91215, 40363, 26623, 72247, 54857, 61025, 62928, 67699, 39158, 43129, 4965, 27550, 55753, 16643, 25173, 47080, 99039, 43013, 38599, 59083, 77325, 11092, 84698, 61513, 25419, 23235, 48782, 16006, 23629, 74954, 29611, 82740, 21569, 4905, 83179, 41098, 71406, 69583, 52620, 51059, 16362, 65682, 86978, 85728, 35060, 84192, 30893, 46964, 5015, 1549, 69747, 92795, 88913, 45775, 55394, 72791, 21928, 83528, 15125, 85033, 1699, 30215, 97003, 62548, 51345, 99587, 50230, 47141, 70160, 14619, 62932, 54060, 19889, 93025, 1473, 18032, 81582, 80747, 28012, 14716, 50760, 87577, 13639, 10289, 50024, 84305, 48115, 44431, 83672, 78813, 44148, 61270, 36419, 41188, 44232, 51077, 96168, 29779, 28421, 62538, 5300, 95170, 40858, 55242, 9527, 67313, 58684, 38452, 13402, 11308, 51018, 22686, 40478, 42201, 43691, 372, 40053, 46562, 12368, 24391, 20270, 63230, 50033, 68470, 3521, 1322, 64154, 97540, 47717, 59679, 82305, 58152, 67794, 96513, 85591, 58279, 24625, 72945, 80091, 82737, 53231, 57680, 23329, 9985, 60044, 47010, 93135, 9509, 14181, 44374, 33784, 86120, 60938, 56324, 44628, 43594, 90256, 80221, 17368, 49858, 27464, 40749, 22284, 10678, 12525, 39391, 91310, 97916, 66097, 96889, 21002, 3202, 24215, 51403, 90351, 46561, 47336, 70639, 70881, 80159, 50646, 81003, 15808, 92381, 34636, 56187, 32205, 54321, 22489, 5340, 53595, 12562, 95887, 60206, 27512, 59570, 11896, 20146, 78291, 70167, 32019, 84113, 56057, 42549, 50532, 18620, 13495, 10415, 52216, 10335, 32649, 75560, 25934, 40906, 30110, 33972, 89217, 64043, 8477, 98944, 78223, 78097, 14327, 63527]
b=a[:]

print(a)
ArraySortStart = time.clock()
InsertSort(a)
ArraySortEnd = time.clock()
print(a)
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))


print(b)
ArraySortStart = time.clock()
InsertSortX(b)
ArraySortEnd = time.clock()
print(b)
print("we has spend %f seconds to sort your array,\nwe have finished it!"%(ArraySortEnd-ArraySortStart))


