class Solution(object):
    def isValid(self, s):
        stack=[]
        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack or (char == ")" and stack[-1]!="(") or (char == "]" and stack[-1]!="[") or (char == "}" and stack[-1]!="{"):
                    return False
                stack.pop()
        return len(stack) == 0
    
             
    pass







    



  

