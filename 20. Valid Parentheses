class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1
        
        for letter in s:
            if letter == '(' or letter == '[' or letter == '{':
                stack.append(letter)
                top += 1
                
            if letter == ')':
                if top >= 0:
                    if stack[top] == '(':
                        stack.pop()
                        top -= 1
                    else:
                        return False
                else:
                    return False
                        
            if letter == ']':
                if top >= 0:
                    if stack[top] == '[':
                        stack.pop()
                        top -= 1
                    else:
                        return False
                else:
                    return False
                        
            if letter == '}':
                if top >= 0:
                    if stack[top] == '{':
                        stack.pop()
                        top -= 1
                    else:
                        return False
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False
