
f = open('test.txt', 'r')
x = f.readlines()
f.close()
x = list(map(str.strip,x))
x = [int(l) for l in x]

def count(x):
    if len(x) == 1:
        return 0,x
    else:
        n = len(x)
        left = x[:n//2]
        right = x[n//2:]
        A,left_arr = count(left)
        B,right_arr = count(right)
        C,sorted_arr = countandmerge(left_arr,right_arr)
        return A+B+C,sorted_arr

def countandmerge(A,B):
    i = j = 0
    k = []
    count = 0
    n = len(A)
    while i != len(A) and j != len(B):
        if A[i] <= B[j]:
            k.append(A[i])
            i+=1
        elif B[j] < A[i]:
            count += n - i
            k.append(B[j])
            j+=1
    if i == len(A) and j == len(B):
        return count,k
    while j != len(B):
        k.append(B[j])
        j+=1
    while i != len(A): 
        k.append(A[i])
        i+=1
    return count,k

count_ , _ = count(x)
print(count_)
    
    
