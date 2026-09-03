class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Assuming the tokens list is always valid
        stack = []
        op_set = {'+', '-', '*', '/'}

        for token in tokens:
            if token in op_set:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                elif token == '/':
                    stack.append(int(a/b))
            else:
                stack.append(int(token))
            # print(stack)

        # Assuming always at the end there would be one value
        return stack[0]