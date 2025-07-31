def foursum(arr,target):
    arr.sort()
    n= len(arr)
    result=[]

    for i in range(n):
        if i>0 and arr[i]== arr[i -1 ]:
            continue

        for j in range(i+1,n):
            if j>i+1 and arr[j]==arr[j-1]:
                continue

            left = j+1
            right= n-1

            while left< right:
                total= arr[i] + arr[j] +arr[left] + arr[right]

                if total == target:
                    result.append((arr[i], arr[j] , arr[left] , arr[right]))

                    # Skip duplicates
                    while left < right and arr[left] == arr[left + 1]:
                        left += 1
                    while left < right and arr[right] == arr[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < target:
                    left +=1

                else:
                    right -= 1


    return result



arr=[2,3,4,5,6,7]
target=14
res= foursum(arr,target)
print(res)