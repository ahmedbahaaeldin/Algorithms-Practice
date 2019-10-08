class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==None:
            return ""
        if len(strs)==1:
            return strs[0]
        min_len = 1000
        shortest = ""
        for w in strs:
            if len(w)<min_len:
                min_len = len(w)
                shortest = w

        longest_common = ""
        flag = True
        for i,letter in enumerate(shortest):
            if(flag==True):
                for word in strs:
                    if letter == word[i]:
                        flag=True
                    else:
                        flag=False
                        break
                if(flag==True):
                    longest_common+=letter
            else:
                break
        return longest_common
                
                
            
        
