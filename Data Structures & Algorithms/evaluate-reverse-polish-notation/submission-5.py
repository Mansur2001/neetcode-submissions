class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": "+",
            "-": "-",
            "*": "*",
            "/": "/"
        }

        stack = []

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()

                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                elif t == "/":
                    stack.append(int(float(a / b))) 
        return stack[0]
        
        