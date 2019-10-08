class Solution:
    def isValid(self, s: str) -> bool:
        listed = list(s)
        stack = []
        if len(listed) == 0:
            return True
        if len(listed) == 1:
            return False
        for letter in listed:
            if letter == "(" or letter == "[" or letter == "{":
                stack.append(letter)
            else:
                if letter == ")" and len(stack)>0:
                    if stack[-1] == "(":
                        stack.pop()
                    elif stack[-1]!="(":
                        return False
                elif letter == "]" and len(stack)>0:
                    if stack[-1] == "[":
                        stack.pop()
                    elif stack[-1]!="[":
                        return False
                elif letter == "}" and len(stack)>0:
                    if stack[-1] == "{":
                        stack.pop()
                    elif stack[-1]!="{":
                        return False
                elif letter ==")" or letter == "]" or letter == "}" and len(stack) == 0:
                    return False
        if len(stack) == 0:
            return True
