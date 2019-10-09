class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        int_string = ""
        for i in digits:
            int_string+=str(i)
        
        to_int = int(int_string) + 1
        return [int(i) for i in str(to_int)]
