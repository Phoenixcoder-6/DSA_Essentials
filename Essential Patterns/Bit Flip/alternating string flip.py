def altstr(original):
    n = len(original)
    operations1=0
    operations2=0
    # Creates the first pattern
    pattern1= " ".join(["10"[i%2] for i in range(n)])
    for i,j in zip(original, pattern1):
        if i!=j:
            operations1+=1

    pattern2= " ".join(["01"[i%2] for i in range(n)])
    for i,j in zip(original, pattern2):
        if i!=j:
            operations2+=1
    return min(operations1,operations2)


s="1001"
print("Minimum operations needed:", altstr(s))



