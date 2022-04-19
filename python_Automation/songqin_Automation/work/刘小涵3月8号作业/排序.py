
def mySort(alist,blist):
    for i in range(0,len(alist)-1):
        for j in range(0,len(alist)-1-i):  #依次找出最大值，并
            if alist[j]<alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
        blist.append(alist[len(alist)-1-i])  #把最大值添加到b列表的末尾
    blist.append(alist[0])#把a列表剩余的最小的元素添加到b列表的开始
    print(blist)

mySort(alist=[1,3,5,7,34,23,55,56,2,3,4],blist=[])
