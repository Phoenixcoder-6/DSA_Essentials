def count_windows(arr,k):
    n= len(arr)
    if n<k:
        return "Invalid"
    
    total_windows= n-k+1
    print(f"Total number of windows:{total_windows}")

    #print all the windows
    for i in range(total_windows):
        window= arr[i: i+k]
        print(f" window{i+1}: {window}")



arr= [2,3,1,4,5,6,2]
k=3

count_windows(arr,k)


