def merge(arr,left,mid,right):
    L=arr[left:mid+1]
    R=arr[mid+1: right+1]

    #initial indexes for L and R
    i=j=0
    #initial index for merged array
    k=left

    #merge two arrays
    while i<len(L) and j<len(R):
        if L[i]<R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k]= R[j]
            j+=1

        k+=1

    while i<len(L):
        arr[k]= L[i]
        i+=1
        k+=1
    while j<len(R):
        arr[k]= R[j]
        j+=1
        k+=1

def mergeSort(arr,left,right):
    if left<right:
        mid= (left+right)//2
        mergeSort(arr,left,mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,mid,right)

arr=[5,8,3,1,4]
print("Original array:",arr)
mergeSort(arr,0,len(arr)-1)
print("Sorted array:", arr)

