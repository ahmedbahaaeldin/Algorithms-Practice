class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I":1,
                     "V":5,
                     "X":10,
                     "L":50,
                     "C":100,
                     "D":500,
                     "M":1000}
        sums = 0
        if s == "":
            return 0
        i = 0
        while(i <= len(s)-1):
            if i + 1 > len(s) -1:
                sums += dictionary[s[i]]
                i += 1
            else:
                if dictionary[s[i]] < dictionary[s[i+1]]:
                    sums = sums - dictionary[s[i]] + dictionary[s[i+1]]
                    i += 2

                elif dictionary[s[i]] >= dictionary[s[i+1]]:
                    sums += dictionary[s[i]]
                    i += 1
        return sums
