def rangeupdate(n,updates):
    arr= [0] * n
    gradient= [0] * (n+1)

    for l,r,val in updates:
        gradient[l] += val
        if r+1 < len(gradient):
            gradient[r+1] -= val


    #Construct the final array
    arr[0]= gradient[0]
    for i in range(1,n):
        arr[i] = gradient[i]+ arr[i-1]

    return arr

n=5
updates= [(1,3,2),(2,4,3)]
print(rangeupdate(n,updates))