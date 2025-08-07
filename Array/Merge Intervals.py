def merge_intervals(arr):
    if not arr:
        return []
    arr.sort(key=lambda x: x[0])
    merged= [arr[0]]
    for current in arr[1:]:
        last= merged[-1]

        if current[0] <= last[1]:
            last[1] = max(last[1],current[1])
        else:
            merged.append(current)

    return merged


arr=[[1,3],[2,4],[10,12]]
result= merge_intervals(arr)
print(result)
    



        