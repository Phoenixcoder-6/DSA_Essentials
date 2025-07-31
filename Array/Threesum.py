#Bruteforce Approach
'''def threesum(arr,target):
    n= len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i] + arr[j] +arr[k] == target:
                    return True
                
    return False
'''

#Optimized one

def threesum(arr, target):
    arr.sort()
    n= len(arr)
    for i in range(n):
        left= i+1
        right=n-1

        while left<right:
            total= arr[i] + arr[left] + arr[right]
            

            if total == target:
                return True
            
            elif total < target:
                left +=1
            
            else:
                right-=1


    return False


arr=[1,2,3,4,5]
target=8
res= threesum(arr,target)
print(res)