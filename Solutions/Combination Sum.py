import numpy as np
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        Tracker = [[[] for i in range(target+1)] for j in range(len(candidates))]
        candidates = sorted(candidates)
        if len(candidates) == 1 and candidates[0] - target == 0:
            col = []
            col.append([1])
            return col
        if len(candidates) == 2 and candidates[0] - target == 0:
            col = []
            col.append([1])
            return col
        if len(candidates) == 1 and candidates[0] > target:
            return []
        for i in range(len(candidates)):
            for j in range(1,target+1):
                if candidates[i] > j:
                    Tracker[i][j].extend(Tracker[i-1][j])
                elif j == candidates[i]:
                    if Tracker[i-1][j] != []:
                        Tracker[i][j].extend(Tracker[i-1][j]) 
                        Tracker[i][j].append([candidates[i]])  
                    else:
                        Tracker[i][j].extend([candidates[i]])
                elif j > candidates[i]:
                    difference = j - candidates[i]
                    if Tracker[i][difference] == []:
                        Tracker[i][j] = Tracker[i-1][j]
                    elif isinstance(Tracker[i][difference][0],int):
                        Tracker[i][j].extend(Tracker[i-1][j])
                        Tracker[i][j].append(Tracker[i][difference]+[candidates[i]])
                    elif isinstance(Tracker[i][difference][0],list):
                        Tracker[i][j].extend(Tracker[i-1][j])
                        for row in Tracker[i][difference]:
                            Tracker[i][j].append(row+[candidates[i]])
        k = np.array(Tracker[-1][-1])
        if len(k.shape) > 1 or k.shape[0] > 1:
            if k.shape[0] == 1 and k.shape[1] >=1:
                return Tracker[-1][-1]
            elif k.shape[0] > 1:
                k = np.squeeze(k)
                return k
        elif len(k.shape) == 1 and Tracker[-1][-1] != []:
            return [Tracker[-1][-1]]
        elif len(k.shape) == 1 and Tracker[-1][-1] == []:
            return []
        
