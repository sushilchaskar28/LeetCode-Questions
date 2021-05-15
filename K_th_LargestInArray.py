def getPartition(arr,l,h):
    pivot = arr[h]
    ind = l
    for j in range(l,h):
        if arr[j]<=pivot:
            arr[ind],arr[j]=arr[j],arr[ind]
            ind+=1
    arr[ind],arr[h]=arr[h],arr[ind]
    return ind

def Kth_Largest(arr,k):
    target = len(arr)-k
    l,h = 0,len(arr)-1
    while l<=h:
        partition = getPartition(arr,l,h)
        if partition == target: return arr[partition]
        elif partition < target: l=partition+1
        else: h = partition - 1

print(Kth_Largest([7,2,5,9,11,12],4))