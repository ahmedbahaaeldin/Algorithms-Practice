class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        length = len(string)
        pivot = length/2
        if length == 1:
            return True
        if length == 2:
            if string[0] == string[1]:
                return True
            else:
                return False
        if pivot % 2 !=0:
            pivot = math.floor(pivot)
        int_list = list(string)
        for i in range(int(pivot)):
            unique = set([int_list[i],int_list[length-i-1]])
            if len(unique)>1:
                return False
        return True
