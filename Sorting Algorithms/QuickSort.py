def swap(arr,i,j):
    arr[i],arr[j]= arr[j],arr[i]
    
def partition(arr,low,high):    #Partition algorithm
    pivot= arr[high]            #choose the pivot
    i= low-1

    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            swap(arr,i,j)

    swap(arr,i+1,high)
    return i+1

def quicksort(arr,low,high):
    if low<high:
        pi= partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

arr=[10,8,2,3,4,1,7]
print("Original Array:",arr)
quicksort(arr,0,len(arr)-1)
print(arr)
