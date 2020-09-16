import math
P = [(1,1),(2,2),(4,4),(5,4),(3,3),(6,7),(8,9),(9,11)]
def mergesort(Array,Coordinate):
    if len(Array) == 1:
        return Array
    mid_point = len(Array) // 2
    left_part = Array[:mid_point]
    right_part = Array[mid_point:]

    left_sorted = mergesort(left_part,Coordinate)
    right_sorted = mergesort(right_part,Coordinate)
    combined_array = merge(left_sorted,right_sorted,Coordinate)
    return combined_array

def merge(A,B,Coordinate):
    i = j = 0
    C = []
    if Coordinate == 'x':
        Coordinate = 0
    elif Coordinate == 'y':
        Coordinate = 1

    while i < len(A) and j < len(B):
        if A[i][Coordinate] <= B[j][Coordinate]:
            C.append(A[i])
            i += 1
        elif B[j][Coordinate] < A[i][Coordinate]:
            C.append(B[j])
            j += 1
    while i < len(A) and j == len(B):
        C.append(A[i])
        i += 1
    while j < len(B) and i == len(A):
        C.append(B[j])
        j += 1
    return C

def Initial_Sort(P):
    Px = mergesort(P,'x')
    Py = mergesort(P,'y')
    return Px,Py

Px, Py = Initial_Sort(P)

def Euclidean_Distance(P1,P2):
    return math.sqrt((P1[0] - P2[0])**2 + (P1[1] - P2[1])**2)

def BruteForceClosestPair(Array):
    size = len(Array)
    minimum_distance = Euclidean_Distance(Array[0],Array[1])
    Target_Pair = (Array[0],Array[1])
    if len(Array) == 2:
        return Euclidean_Distance(Array[0],Array[1]),Array[0],Array[1]
    for i in range(0,size):
        for j in range(i+1,size):
            distance = Euclidean_Distance(Array[i],Array[j])
            if distance < minimum_distance:
                minimum_distance = distance
                Target_Pair = (Array[i],Array[j])
    return minimum_distance,Target_Pair
    
def Closest_Pair(Px,Py):
    if len(Px) <= 3:
        return BruteForceClosestPair(Px)

    midpoint_x = len(Px) // 2
    Qx = Px[:midpoint_x]
    Rx = Px[midpoint_x:]
    median_x = Px[midpoint_x]
    Qy,Ry = [], []
    for point in Py:
        if point[0] < int(median_x[0]):
            Qy.append(point)
        else:
            Ry.append(point)

    min_distance_Left = Closest_Pair(Qx,Qy)
    min_distance_Right = Closest_Pair(Rx,Ry)
    min_distance = min(min_distance_Left,min_distance_Right)
    x_bar = Qx[-1][0]
    Sy = []
    for y in Py:
        if x_bar - min_distance[0] < y[0] < x_bar + min_distance[0]:
            Sy.append(y)
    
    Best_pair = (0,0)
    for i in range(len(Sy) - 1):
        for j in range(i+1, min(i + 7, len(Sy))):
            P = Sy[i]
            Q = Sy[j]
            dist = Euclidean_Distance(P,Q)
            if dist < min_distance[0]:
                min_distance = (dist,P,Q)
    return min_distance
    
Closest_Pair(Px,Py)
