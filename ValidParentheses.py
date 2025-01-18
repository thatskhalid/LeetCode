class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        '''        
        first_spot = s[0]
        second_spot = s[-1]
        
        for x in s:
            
            if first_spot == "(" and second_spot == ")":
                return True
            elif first_spot == "{" and second_spot == "}":
                return True
            elif first_spot == "[" and second_spot == "]":
                return True
            else:
                return False
        '''
        p = {')': '(', '}': '{', ']': '['}
        
        for x in s: 
        
            if x in p:
                if stack and stack[-1] == p[x]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
                
        return not stack