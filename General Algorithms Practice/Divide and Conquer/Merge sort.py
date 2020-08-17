def mergesort(a):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]
    new_l = mergesort(left)
    new_r = mergesort(right)
    a = merge(new_l,new_r)
    return a
def merge(a,b):
    i = 0
    j = 0
    c = []
    while(i<len(a) and j <len(b)):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
        elif a[i] == b[j]:
            c.append(a[i])
            c.append(b[j])
            i += 1
            j += 1
    if i < len(a):
        while(i < len(a)):
            c.append(a[i])
            i += 1
    if j < len(b):
        while(j < len(b)):
            c.append(b[j])
            j += 1
    return c
mergesort([7,8,6,4,3,2,10,100])
