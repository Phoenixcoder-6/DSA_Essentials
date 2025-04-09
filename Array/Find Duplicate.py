def duplicate(arr):
    freq={}
    n= len(arr)
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1


    for i, val in freq.items():
        if val>1:
            print(f"Duplicate present. Duplicate element is {i}")
    
arr=[2,5,4,3,2,1,2,1]
duplicate(arr)
.
.
.
