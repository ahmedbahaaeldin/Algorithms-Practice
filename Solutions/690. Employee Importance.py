class Solution:
    def getImportance(self, employees, id):
        dic = {}
        queue = collections.deque()
        for emp in employees:
            dic[emp.id] = emp
        
        queue.append(dic[id])
        total = 0
        while queue:
            a = queue.popleft()
            total += a.importance
            for e in a.subordinates:
                queue.append(dic[e])
        return total
