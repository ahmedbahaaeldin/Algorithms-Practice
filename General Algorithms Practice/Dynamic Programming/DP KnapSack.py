def KnapSack(Weights,Values,MaxWeight):
    Tracker = [[0 for i in range(MaxWeight+1)] for j in range(len(Weights))]
    for i in range(len(Weights)):
        for j in range(1,MaxWeight+1):
            if j < Weights[i]:
                Tracker[i][j] = max(Tracker[i-1][j],Tracker[i][j-1])
            else:
                Tracker[i][j] = max(Tracker[i-1][j], Values[i] + Tracker[i-1][j - Weights[i]])    
    return max(max(Tracker))
