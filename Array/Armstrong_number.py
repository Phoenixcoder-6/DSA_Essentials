def armstrong_number(num):
    n=len(str(num))
    total=0
    for i in str(num):
        total += int(i) ** n

    if total == num:
        return True
    return False


num=9474
result= armstrong_number(num)
print(result)
.
.

