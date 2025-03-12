from collections import defaultdict
def count_distinct(arr,k):
    n= len(arr)
    freq= defaultdict(int)
    res=[]

    print(F"Initial array:{arr}, Window_Size:{k}")

    print("\nInitializing First Window..")
    for right in range(k):
        freq[arr[right]]+=1
        print(f" Adding {arr[right]} -> freq: {dict(freq)}")

    res.append(len(freq))

    print("\n Sliding the window...")
    for right in range(k,n):
        outgoing_element= arr[right-k]
        incoming_element= arr[right]

        if freq[outgoing_element] ==1:
            del freq[outgoing_element]
        else:
            freq[outgoing_element]-=1

        freq[incoming_element] +=1

        res.append(len(freq))

    print("\n Final result:")
    return res

arr=[1,2,1,3,4,2,3]
k=4
print(count_distinct(arr,k))



              


