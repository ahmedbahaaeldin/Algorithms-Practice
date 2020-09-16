class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        tracker = [["()"],["()()","(())"]]
        if n == 0:
            return [""]
        elif n == 1:
            return tracker[0]
        elif n == 2:
            return tracker[1]
        i = 1
        while(i <= n):
            temp = []
            for bracket in tracker[i]:
                for loc,paren in enumerate(bracket):
                    if loc < len(bracket) - 1:
                        temp.append(bracket[:loc]+"()"+bracket[loc:])
            temp = set(temp)
            tracker.append(temp)
            i += 1
        
        return tracker[n-1]
