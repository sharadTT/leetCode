class Solution(object):
    def evalRPN(self, tokens):
        if not tokens:
            return -1
        
        stack = []
        
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                operation = token
                b = stack.pop()
                a = stack.pop()
                
                if operation == '+':
                    stack.append(a+b)
                elif operation == '-':
                    stack.append(a-b)
                elif operation == '*':
                    stack.append(a*b)
                elif operation == '/':
                    stack.append(int(float(a)/b))

        return stack[0]
